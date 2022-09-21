from dis import code_info
from validadores import Validador

class Cadastro():

    def usuario():
        print("Cadastro de usuário\n"
          "============================\n")
        login = input("Novo login: ")
        validaLogin = Validador.validaLogin(login)
        if validaLogin == True:
            senha = input("Nova senha: ")
            validaSenha = Validador.validaSenha(login, senha)
            if validaSenha == True:
                return {'codigo':0, 'login':login, 'senha':senha}
            else:
                return validaSenha
        else:
            return validaLogin  

    def pessoa():
        nome = input("Nome: ")
        validaNome = Validador.validaNome(nome)
        if validaNome == True:
            idade = int(input("Idade: "))
            validaIdade = Validador.validaIdade(idade)
            if validaIdade == True:
                rg = input("rg: ")
                validaRg = Validador.validaRg(rg)
                if validaRg == True:
                    cpf = input("CPF (apenas número): ")
                    validaCpf =  Validador.validaCpf(cpf)
                    if validaCpf == True:
                        salario = float(input("Salario: "))
                        validaSalario = Validador.validaSalario(salario)
                        if validaSalario == True:
                            sexo = (input("sexo(M, F ou O): "))
                            validaSexo = Validador.validaSexo(sexo)
                            if validaSexo == True:
                                estadoCivil = (input("Estado Civil(solteiro, casado ou divorcidado): "))
                                validaEstadoCivil = Validador.validaEstadoCivil(estadoCivil)
                                if validaEstadoCivil == True:
                                    pessoa = {'nome':nome,
                                              'idade':idade,
                                              'rg':rg,
                                              'cpf':cpf,
                                              'salario':salario,
                                              'sexo':sexo,
                                              'estadoCivil':estadoCivil}
                                    
                                    possuiDependente = int(input("Possui dependente?(1 - SIM, 2 - NÃO): "))
                                    
                                    if possuiDependente == 1:
                                        dependente = Cadastro.dependete()
                                        pessoa.update(dependente)
                                        return pessoa
                                    elif possuiDependente == 2:
                                        return pessoa
                            else:
                                return validaEstadoCivil
                        else:
                            return validaSalario
                    else:
                        return validaCpf
                else:
                    return validaRg
            else:
                return validaIdade
        else:
            return validaNome
    
    def dependete():
        nome = input("Nome dependente: ")
        validaNome = Validador.validaNome(nome)
        if validaNome == True:
            idade = int(input("Idade dependente: "))
            validaIdade = Validador.validaIdade(idade)
            if validaIdade == True:
                cpf = input("CPF dependente (apenas número): ")
                validaCpf = Validador.validaCpf(cpf)
                if validaCpf == True:
                    sexo = (input("sexo dependente (M, F ou O): "))
                    validaSexo = Validador.validaSexo(sexo)
                    if validaSexo == True:
                        dependente = {'dependente':{'nome':nome,
                                      'idade':idade,
                                      'cpf':cpf,
                                      'sexo':sexo}}
                        return dependente
                    else:
                        return validaSexo
                else:
                    return validaCpf
            else:
                return validaIdade    
        else:
            return validaNome