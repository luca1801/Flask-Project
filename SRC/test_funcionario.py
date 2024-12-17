"""testing class methods"""

import Funcionario


tecal_func = Funcionario.Funcionario('Tecal automacao')
tecal_func.set_nome('lucas soares')
tecal_func.set_cpf('41065063938')
tecal_func.cria_func()
tecal_func.set_nome('Nathan')
tecal_func.set_cpf('31065063938')
tecal_func.cria_func()
tecal_func.set_nome('lucas soares')
tecal_func.set_cpf('41065063938')
tecal_func.cria_func()
tecal_func.exibir_func()

araujo_func = Funcionario.Funcionario('Araujo Abreu')
araujo_func.set_nome('Marcos Palmeiras')
araujo_func.set_cpf('41065063937')
araujo_func.cria_func()
araujo_func.set_nome('Bruno Souza')
araujo_func.set_cpf('41065063356')
araujo_func.cria_func()
araujo_func.cria_func()
araujo_func.set_nome('Nathan')
araujo_func.set_cpf('31065063938')
araujo_func.cria_func()
araujo_func.exibir_func()

print(araujo_func)
print(tecal_func)
