from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, serializers
# from rest_framework.response import Response
# from rest_framework import status
# from rest_framework.decorators import action


from cadastroColetor.models import Coletor
from cadastroColetor.serializers import ColetorSerializer


class ColetorViewSet(viewsets.ModelViewSet):
    queryset = Coletor.objects.all()
    # permission
    # token
    serializer_class = ColetorSerializer

    # @action(detail=False, methods=['POST'])
    # def Login(self, request):
    #     try:
    #         coletor = Coletor.objects.get(email=request.data['email'])

    #         if coletor.senha == request.data['senha']:
    #             return Response({'mensagem': 'Logado'})
    #         else:
    #             return Response({'mensagem': 'Senha incorreta'}, status=status.HTTP_400_BAD_REQUEST)
        
    #     except Coletor.DoesNotExist:
    #         return Response ({'mensagem': 'email nao encontrado'}, status=status.HTTP_400_BAD_REQUEST)