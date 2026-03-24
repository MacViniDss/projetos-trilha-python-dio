from abc import ABC, abstractmethod
from datetime import date

class Transacao(ABC):
    @abstractmethod
    def registrar(self, conta):
        pass

class Deposito(Transacao):
    def __init__(self, valor: float):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)
        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)

class Saque(Transacao):
    def __init__(self, valor: float):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)
        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)


class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self, transacao):
        self._transacoes.append(transacao)

class Conta:
    def __init__(self, numero: int, cliente):
        self._saldo = 0.0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()

    @classmethod
    def nova_conta(cls, cliente, numero: int):
        return cls(numero, cliente)

    @property
    def saldo(self):
        return self._saldo

    @property
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self._agencia

    @property
    def cliente(self):
        return self._cliente

    @property
    def historico(self):
        return self._historico

    def sacar(self, valor: float):
        saldo = self.saldo
        if valor <= self._saldo and valor > 0:
            self._saldo -= valor
            print("\n=== Saque realizado com sucesso! ===")
            return True
        else:
            print("Operação falhou!")
            return False

    def depositar(self, valor: float):
        if valor > 0:
            self._saldo += valor
            print("\n=== Depósito realizado com sucesso! ===")
            return True
        else:
            print("Operação falhou! O valor informado é inválido.")
            return False


class ContaCorrente(Conta):
    def __init__(self, numero: int, cliente, limite: 500, limite_saques: 3):
        super().__init__(numero, cliente)
        self._limite = limite
        self._limite_saques = limite_saques
        self._saques_realizados = 0

    def sacar(self, valor: float):
        excedeu_saldo = valor > self._limite
        excedeu_saques = self._saques_realizados >= self._limite_saques

        if excedeu_saldo or excedeu_saques:
            print("Operação falhou!")
            return False

       
        sucesso = super().sacar(valor)
        if sucesso:
            self._saques_realizados += 1
        return sucesso
    

class Cliente:
    def __init__(self, endereco: str):
        self._endereco = endereco
        self._contas = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self._contas.append(conta)


class PessoaFisica(Cliente):
    def __init__(self, cpf: str, nome: str, data_nascimento: date, endereco: str):
        super().__init__(endereco)
        self._cpf = cpf
        self._nome = nome
        self._data_nascimento = data_nascimento
