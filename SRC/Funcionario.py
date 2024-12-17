"""
Implementação de classe Funcionarios
"""
# pylint: disable=C0116,C0303,C0301,C0103


class Funcionario():
    """implementação de classe Funcionarios"""

    def __init__(self, empresa):
        self.empresa = empresa
        self.__nome = None
        self.__cpf = None
        self.id = 0
        self.func_cadastrados = {}
        self.cpf_funcionarios = []

    def set_nome(self, nome: str) -> None:  # typing
        self.__nome = nome

    def get_nome(self) -> str:
        return self.__nome

    def set_cpf(self, cpf: str) -> None:
        self.__cpf = cpf

    def get_cpf(self) -> str:
        return self.__cpf

    # __metodo torna a funcao privada podendo ser usada somente pela classe
    def __func_cadastrados(self):
        """ metodo para coletar cadastrados"""
        print(self.func_cadastrados)

    def cria_func(self):

        if self.__cpf in self.cpf_funcionarios:
            print('Usuario ja cadastrado no sistema da empresa')
        else:
            self.func_cadastrados.update(
                {self.id: {'nome': self.__nome, 'cpf': self.__cpf, 'empresa': self.empresa}})
            self.cpf_funcionarios.append(self.__cpf)
            print('Usuario cadastrado com sucesso: ' + self.__cpf)
            self.id += 1
        # print(self.func_cadastrados)

    def exibir_func(self):
        """ metodo para exibir funcionarios"""
        self.__func_cadastrados()

    def __str__(self):
        return f'Funcionarios cadastrados na empresa: {self.empresa} : {self.cpf_funcionarios}'
