import re
from validate_docbr import CPF

def cpf_valido(cpf):
    val_cpf = CPF()
    return val_cpf.validate(cpf)

def nome_valido(nome):
    return nome.isalpha()

def celular_valido(celular):
    modelo = '[0-9]{2} [0-9]{5}-[0-9]{4}'
    resultado = re.findall(modelo, celular)
    return len(celular) >= 11 and resultado