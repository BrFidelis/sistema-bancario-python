from typing import List, Dict, Any
from dataclasses import dataclass

@dataclass
class Endereco:
    #Classe que representa um endereço completo
    logradouro: str
    numero: str
    bairro: str
    cidade: str
    estado: str

    def __str__(self):
        return f"{self.logradouro}, {self.numero} - {self.bairro} - {self.cidade}/{self.estado}"

class Usuario:
    #Classe que representa um usuário (cliente) do banco
    def __init__(self, nome: str, data_nascimento: str, cpf: str, endereco: Endereco):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        self.endereco = endereco

class ContaCorrente:
    #Classe que representa uma conta bancária
    AGENCIA = "0001"
    LIMITE_SAQUES = 3
    LIMITE_VALOR_SAQUE = 500.0
    
    def __init__(self, usuario: Usuario, numero_conta: int):
        self.usuario = usuario
        self.numero = numero_conta
        self._saldo = 0.0
        self._extrato: List[str] = []
        self._saques_realizados = 0
    
    def depositar(self, valor: float, /) -> bool:
        """Realiza um depósito na conta (positional only)
        
        Args:
            valor: Valor a ser depositado (deve ser positivo)"""
        if valor <= 0:
            print("\nErro: O valor do depósito deve ser positivo.")
            return False
            
        self._saldo += valor
        self._extrato.append(f"Depósito: R$ {valor:.2f}")
        print(f"\nDepósito de R$ {valor:.2f} realizado com sucesso!")
        return True
    
    def sacar(self, *, valor: float) -> bool:
        """Realiza um saque na conta (keyword only)
        
        Args:
            valor: Valor a ser sacado"""
        if self._saques_realizados >= self.LIMITE_SAQUES:
            print("\nErro: Você já realizou o limite diário de saques.")
            return False
            
        if valor <= 0:
            print("\nErro: O valor do saque deve ser positivo.")
            return False
            
        if valor > self.LIMITE_VALOR_SAQUE:
            print(f"\nErro: O valor máximo por saque é R$ {self.LIMITE_VALOR_SAQUE:.2f}.")
            return False
            
        if valor > self._saldo:
            print("\nErro: Saldo insuficiente para realizar o saque.")
            return False
            
        self._saldo -= valor
        self._saques_realizados += 1
        self._extrato.append(f"Saque: R$ {valor:.2f}")
        print(f"\nSaque de R$ {valor:.2f} realizado com sucesso!")
        return True
    
    def extrato(self, saldo: float, /, *, extrato: List[str]) -> None:
        """Exibe o extrato da conta (positional and keyword args)
        
        Args:
            saldo: Saldo atual da conta (positional)
            extrato: Lista de operações (keyword)"""
        print("\n=== EXTRATO ===")
        print("\n".join(extrato))
        print(f"\nSaldo atual: R$ {saldo:.2f}")
        print("================")

class Banco:
    #Classe principal que gerencia o sistema bancário"""
    def __init__(self):
        self.usuarios: List[Usuario] = []
        self.contas: List[ContaCorrente] = []
        self._numero_conta = 1
    
    def cadastrar_usuario(self) -> Usuario:
        #Cadastra um novo usuário no sistema
        print("\n=== CADASTRO DE USUÁRIO ===")
        
        cpf = input("Informe o CPF (somente números): ").strip()
        if any(u.cpf == cpf for u in self.usuarios):
            print("\nErro: Já existe um usuário com esse CPF!")
            return None
        
        nome = input("Nome completo: ").strip()
        data_nascimento = input("Data de nascimento (dd/mm/aaaa): ").strip()
        
        print("\nInforme o endereço:")
        logradouro = input("Logradouro: ").strip()
        numero = input("Número: ").strip()
        bairro = input("Bairro: ").strip()
        cidade = input("Cidade: ").strip()
        estado = input("Sigla do estado: ").strip()
        
        endereco = Endereco(logradouro, numero, bairro, cidade, estado)
        usuario = Usuario(nome, data_nascimento, cpf, endereco)
        self.usuarios.append(usuario)
        
        print("\nUsuário cadastrado com sucesso!")
        return usuario
    
    def criar_conta_corrente(self) -> ContaCorrente:
        #Cria uma nova conta corrente
        print("\n=== CRIAR CONTA CORRENTE ===")
        
        cpf = input("Informe o CPF do usuário (somente números): ").strip()
        usuario = next((u for u in self.usuarios if u.cpf == cpf), None)
        
        if not usuario:
            print("\nErro: Usuário não encontrado!")
            return None
        
        conta = ContaCorrente(usuario, self._numero_conta)
        self.contas.append(conta)
        self._numero_conta += 1
        
        print(f"\nConta criada com sucesso! Número: {conta.numero}")
        return conta
    
    def listar_contas(self) -> None:
        #Lista todas as contas cadastradas
        print("\n=== CONTAS CADASTRADAS ===")
        
        if not self.contas:
            print("Nenhuma conta cadastrada.")
            return
        
        for conta in self.contas:
            print(f"""
Agência: {conta.AGENCIA}
C/C: {conta.numero}
Titular: {conta.usuario.nome}
CPF: {conta.usuario.cpf}
""")

class SistemaBancario:
    #Classe que controla a interface do sistema
    def __init__(self):
        self.banco = Banco()
        self.conta_atual = None
    
    def executar(self):
        #Método principal que inicia o sistema
        print("\n=== SISTEMA BANCÁRIO ===")
        
        while True:
            if not self.conta_atual:
                self._menu_principal()
            else:
                self._menu_conta()
    
    def _menu_principal(self):
        #Exibe o menu principal
        print("\n=== MENU PRINCIPAL ===")
        print("1. Criar usuário")
        print("2. Criar conta corrente")
        print("3. Listar contas")
        print("4. Acessar conta")
        print("5. Sair")
        
        opcao = input("\nEscolha uma opção: ").strip()
        
        match opcao:
            case "1":
                self.banco.cadastrar_usuario()
            case "2":
                self.banco.criar_conta_corrente()
            case "3":
                self.banco.listar_contas()
            case "4":
                self._acessar_conta()
            case "5":
                print("\nObrigado por usar nosso sistema!")
                exit()
            case _:
                print("\nOpção inválida!")
    
    def _menu_conta(self):
        #Exibe o menu da conta
        print(f"\n=== CONTA {self.conta_atual.numero} ===")
        print("1. Depositar")
        print("2. Sacar")
        print("3. Extrato")
        print("4. Voltar")
        
        opcao = input("\nEscolha uma opção: ").strip()
        
        match opcao:
            case "1":
                self._operacao_deposito()
            case "2":
                self._operacao_saque()
            case "3":
                self._mostrar_extrato()
            case "4":
                self.conta_atual = None
            case _:
                print("\nOpção inválida!")
    
    def _acessar_conta(self):
        #Permite acessar uma conta existente
        numero_conta = input("\nInforme o número da conta: ").strip()
        
        try:
            numero_conta = int(numero_conta)
            conta = next((c for c in self.banco.contas if c.numero == numero_conta), None)
            
            if conta:
                self.conta_atual = conta
                print(f"\nBem-vindo, {conta.usuario.nome}!")
            else:
                print("\nConta não encontrada!")
        except ValueError:
            print("\nNúmero de conta inválido!")
    
    def _operacao_deposito(self):
        #Realiza uma operação de depósito
        try:
            valor = float(input("\nValor do depósito: R$ "))
            self.conta_atual.depositar(valor)
        except ValueError:
            print("\nValor inválido!")
    
    def _operacao_saque(self):
        #Realiza uma operação de saque
        try:
            valor = float(input("\nValor do saque: R$ "))
            self.conta_atual.sacar(valor=valor)
        except ValueError:
            print("\nValor inválido!")
    
    def _mostrar_extrato(self):
        #Exibe o extrato da conta
        self.conta_atual.extrato(self.conta_atual._saldo, extrato=self.conta_atual._extrato)

if __name__ == "__main__":
    sistema = SistemaBancario()
    sistema.executar()