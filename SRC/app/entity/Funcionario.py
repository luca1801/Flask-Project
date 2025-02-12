"""
Implementação de classe Funcionarios
"""
# pylint: disable=C0116,C0303,C0301,C0103, C0116, R0902, R0913, R0917

class Funcionario():
    """implementação de classe Funcionarios"""

    def __init__(self, empresa: str, nome: str, email: str, data_nasc: str,
                 sexo: str, cargo: str, cpf: str) -> None:
        self.__empresa = empresa
        self.__nome = nome
        self.__email = email
        self.__data_nasc = data_nasc
        self.__sexo = sexo
        self.__cargo = cargo
        self.__cpf = cpf

    # get and set empresa
    def set_empresa(self, empresa: str) -> None:  # typing
        self.__empresa = empresa

    def get_empresa(self) -> str:
        return self.__empresa

    # get and set nome
    def set_nome(self, nome: str) -> None:  # typing
        self.__nome = nome

    def get_nome(self) -> str:
        return self.__nome

    # get and set cpf
    def set_cpf(self, cpf: str) -> None:
        self.__cpf = cpf

    def get_cpf(self) -> str:
        return self.__cpf

    # get and set data_nasc
    def set_data_nasc(self, data_nasc: str) -> None:
        self.__data_nasc = data_nasc

    def get_data_nasc(self) -> str:
        return self.__data_nasc

    # get and set sexo
    def set_sexo(self, sexo: str) -> None:
        self.__sexo = sexo

    def get_sexo(self) -> str:
        return self.__sexo

    # get and set empresa
    def set_email(self, email: str) -> None:
        self.__email = email

    def get_email(self) -> str:
        return self.__email

    # get and set cargo
    def set_cargo(self, cargo: str) -> None:
        self.__cargo = cargo

    def get_cargo(self) -> str:
        return self.__cargo

    def envia_func(self) -> dict:
        func = {'nome': self.get_nome(), 'sexo': self.get_sexo(), 'data_nasc': self.get_data_nasc(),
                'cpf': self.get_cpf(), 'empresa': self.get_empresa(), 'cargo': self.get_cargo(),
                'email': self.get_email()}
        return func

    def __str__(self):
        return f'nome= {self.get_nome()}, sexo= {self.get_sexo()}'
