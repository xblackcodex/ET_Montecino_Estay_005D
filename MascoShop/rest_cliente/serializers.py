from rest_framework import serializers
from MascoApp.models import Cliente

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['run','genero','nombrecliente','edad','estado','ocupacion']