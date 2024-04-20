from rest_framework import serializers
from clientes.models import Cliente
from clientes.validators import *

class ClienteSerializer(serializers.ModelSerializer):
    '''Exibir todos os clientes'''
    class Meta:
        model = Cliente
        fields = '__all__'

    def validate(self, data):
        if not cpf_valido(data['cpf']):
            raise serializers.ValidationError({'cpf':'CPF inválido!'})
        if not nome_valido(data['nome']):
            raise serializers.ValidationError({'nome':'Nome inválido!'})
        if not celular_valido(data['celular']):
            raise serializers.ValidationError({'celular':'Celular inválido!'})
        else:
            return data

    #def validate_field(self, field): [lógica de raise do erro ou return do field]

    