from rest_framework import serializers

from cadastroColetor.models import Coletor

class ColetorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coletor
        fields = ['id','nome','cpf','email','senha']