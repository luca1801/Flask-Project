"""
Implementação de classe Funcionarios
"""
# pylint: disable=C0116,C0303,C0301,C0103, C0116, R0902


class Funcionario():
    """implementação de classe Funcionarios"""

    def __init__(self, empresa):
        self.__empresa = empresa
        self.__nome = None
        self.__email = None
        self.__data_nasc = None
        self.__sexo = None
        self.__cargo = None
        self.__cpf = None
        self.id = 0
        self.func_cadastrados = {}
        self.cpf_funcionarios = []

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

    # __metodo torna a funcao privada podendo ser usada somente pela classe
    def __func_cadastrados(self):
        """ metodo para coletar cadastrados"""
        print(self.func_cadastrados)

    def cria_func(self):

        if self.__cpf in self.cpf_funcionarios:
            print('Usuario ja cadastrado no sistema da empresa')
        else:
            self.func_cadastrados.update(
                {self.id: {'nome': self.__nome, 'cpf': self.__cpf, 'empresa': self.__empresa}})
            self.cpf_funcionarios.append(self.__cpf)
            print('Usuario cadastrado com sucesso: ' + self.__cpf)
            self.id += 1
        # print(self.func_cadastrados)

    def exibir_func(self):
        """ metodo para exibir funcionarios"""
        self.__func_cadastrados()

    def envia_func(self):
        func = {'nome': self.get_nome(), 'sexo': self.get_sexo(), 'data_nasc': self.get_data_nasc(),
                'cpf': self.get_cpf(), 'empresa': self.get_empresa(), 'cargo': self.get_cargo(),
                'email': self.get_email()}
        return func

    def __str__(self):
        return f'nome= {self.get_nome()}, sex= {self.get_sexo()}'

    # def __str__(self):
    #   return f'Funcionarios cadastrados na empresa: {self.__empresa} : {self.cpf_funcionarios}'
