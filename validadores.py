class Validador():
    def validaLogin(login):
        if len(login) >= 5:
            return True
        else:
            return {'codigo': 400, 'mensagem':'O login deve ter no mínimo 5 caracteres'}
    def validaSenha(login, senha):
        if len(senha) >= 6 and len(senha) <= 8:
            retorno = {}
            for x in senha:
                if x.isdigit():
                    retorno = {'codigo': 400, 'mensagem':'A senha não pode conter numeros'}
                elif login == senha:
                    retorno = {'codigo': 400, 'mensagem':'A senha não pode ser igual o login'}
                else:
                    retorno = True
            return retorno

        elif len(senha) < 6 or len(senha) > 8:
            return {'codigo': 400, 'mensagem':'A senha deve ter de 6 a 8 caracteres'}

    def validaNome(nome):
        if len(nome) > 5:
            retorno = {}
            for x in nome:
                if x.isdigit():
                    retorno = {'codigo': 400, 'mensagem':'O nome não pode conter numeros'}
                else:
                    retorno = True
        else:
            retorno = {'codigo': 400, 'mensagem':'O nome deve conter mais de 5 caracteres'}
        return retorno

    def validaIdade(idade):
        if idade >= 0 and idade <= 100:
            return True
        else:
            return {'codigo': 400, 'mensagem':'A idade deve ser de 0 a 100 anos'}

    def validaRg(rg): 
        if len(rg) >= 8 or len(rg) <= 12:
            return True
        else:
            return {'codigo': 400, 'mensagem':'O RG deve ter de 8 a 12 digitos'}

    def validaCpf(cpf):
        if len(cpf) == 11:
            return True
        else:
            return {'codigo': 400, 'mensagem':'O CPF deve ter 11 digitos'}

    def validaSalario(salario):
        if salario > 0:
            return True
        else:
            return {'codigo': 400, 'mensagem':'O salário não pode ser 0'}
    
    def validaSexo(sexo):
        if sexo == 'F' or sexo == 'M' or sexo == 'O':
            return True
        else:
            return {'codigo': 400, 'mensagem':'Sexo deve ser F, M ou O'}

    def validaEstadoCivil(estadoCivil):
        if estadoCivil == 'solteiro' or estadoCivil == 'casado' or estadoCivil == 'divorciado':
            return True
        else:
            return {'codigo': 400, 'mensagem':'Estado Civil deve ser solteiro, casado ou divorciado'}