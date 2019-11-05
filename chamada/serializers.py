from rest_framework import serializers

from chamada.models import Chamada

class ChamadaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chamada
        fields = ['id','nome','CEP','bairro','endereco','numero','complemento','telefone','descricao']