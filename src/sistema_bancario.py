class ContaBancaria:
    #Classe que representa uma conta bancária individual com operações básicas.
    
    def __init__(self):
        # Inicializa uma nova conta bancária
        self._saldo = 0.0
        self._extrato = []
        self._saques_realizados = 0
        self.LIMITE_SAQUES = 3
        self.LIMITE_VALOR_SAQUE = 500.0
    
    def depositar(self, valor: float) -> bool:
        # Realiza um depósito na conta
        if valor <= 0:
            print("Erro: O valor do depósito deve ser positivo.")
            return False
            
        self._saldo += valor
        self._extrato.append(f"Depósito: R$ {valor:.2f}")
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
        return True
    
    def sacar(self, valor: float) -> bool:
        # Realiza um saque da conta.
        match valor:
            case _ if self._saques_realizados >= self.LIMITE_SAQUES:
                print("Erro: Limite diário de saques atingido.")
                return False
                
            case _ if valor <= 0:
                print("Erro: Valor do saque deve ser positivo.")
                return False
                
            case _ if valor > self.LIMITE_VALOR_SAQUE:
                print(f"Erro: Valor máximo por saque é R$ {self.LIMITE_VALOR_SAQUE:.2f}.")
                return False
                
            case _ if valor > self._saldo:
                print("Erro: Saldo insuficiente.")
                return False
                
            case _:  # Caso de sucesso
                self._saldo -= valor
                self._saques_realizados += 1
                self._extrato.append(f"Saque: R$ {valor:.2f}")
                print(f"Saque de R$ {valor:.2f} realizado!")
                return True
    
    def mostrar_extrato(self) -> None:
        # Exibe o histórico de transações
        print("\n=== EXTRATO ===")
        if not self._extrato:
            print("Nenhuma movimentação registrada.")
        else:
            for movimentacao in self._extrato:
                print(movimentacao)
        print(f"\nSaldo atual: R$ {self._saldo:.2f}")
        print("================")


class SistemaBancario:
    # Classe principal do sistema bancário.
    
    def __init__(self):
        self.conta = ContaBancaria()
    
    def executar(self) -> None:
        """Loop principal do sistema"""
        print("Bem-vindo ao Sistema Bancário!")
        
        while True:
            self._exibir_menu()
            opcao = input("Escolha uma opção: ").strip()
            self._processar_opcao(opcao)
    
    def _exibir_menu(self) -> None:
        # Exibe o menu de opções
        print("\n=== MENU ===")
        print("1. Depositar")
        print("2. Sacar")
        print("3. Extrato")
        print("4. Sair")
    
    def _processar_opcao(self, opcao: str) -> None:
        # Processa a opção do usuário.
        match opcao:
            case "1":  # Depósito
                self._processar_deposito()
            
            case "2":  # Saque
                self._processar_saque()
            
            case "3":  # Extrato
                self.conta.mostrar_extrato()
            
            case "4":  # Sair
                print("\nObrigado por usar nosso sistema!")
                exit()
            
            case _:
                print("Opção inválida! Tente novamente.")
    
    def _processar_deposito(self) -> None:
        # Trata a operação de depósito
        try:
            valor = float(input("Valor do depósito: R$ "))
            self.conta.depositar(valor)
        except ValueError:
            print("Erro: Valor inválido. Use números (ex: 100.50)")
    
    def _processar_saque(self) -> None:
        # Trata a operação de saque
        try:
            valor = float(input("Valor do saque: R$ "))
            self.conta.sacar(valor)
        except ValueError:
            print("Erro: Valor inválido. Use números (ex: 100.50)")


if __name__ == "__main__":
    sistema = SistemaBancario()
    sistema.executar()