# Sistema Bancário em Python

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green)](https://opensource.org/licenses/MIT)

Sistema bancário completo com cadastro de usuários, contas correntes e operações financeiras, desenvolvido em Python seguindo princípios de orientação a objetos.

## Funcionalidades

- **Depósito**: Valores positivos na conta (argumentos por posição)
- **Saque**: Até 3 saques diários (limite de R$ 500,00 cada); Argumentos por nome (keyword only)
- **Extrato**: Histórico completo de transações; Argumentos mistos (saldo por posição, extrato por nome)
- **Interface**: Menu interativo com tratamento de erros

Cadastro de Usuários
- Armazena: nome, data de nascimento, CPF e endereço completo
- Valida CPF único

Listagem
- Visualização de todas as contas cadastradas
- Detalhes: agência, número da conta e titular

## Tecnologias Utilizadas
- Python
