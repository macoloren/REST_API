

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api.models import UserProfile


from profiles_api import serializers



class HelloApiView(APIView):
    """API View de prueba"""
    serializer_class = serializers.HelloSerializer #cofigura el API view que creamos en el serializers
    

    def get(self, request, format=None):
        #Rerotnar lista de caracteristicas del APIView
        an_apiview = [
            'Usamos metodos HTTP como funciones (get, post, patch, put, delete)',
            'Es similar a una vista tradicional de Dejango',
            'Nos da el mayor control sobre la logica de nuestra aplicacion',
            'Esta mapeado manuelmente a los URLs',
        ]
                                                                        #////////////////////////
        return Response({'message': 'Hello', 'an_apiview': an_apiview}, status=status.HTTP_200_OK) #comvierte a formato json

    def post(self, request):
        """crea un mensaje con nuestro nombre"""
        serializer = self.serializer_class(data=request.data) #obtener el serializador de la view basado en clases

        if serializer.is_valid():
            name = serializer.validated_data.get('name') #valida el campo 'name' que esta en es serializer
            message = f'hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )    

    def put(self, request, pk=None):
    # """Maneja actualiza un objeto"""
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
    # """Maneja actualiza parcial de un objeto (un unico atributo(campo) de un objeto)"""
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
    # """Elimina un objeto"""
        return Response({'method': 'DELETE'})


class UserAPIView(APIView):

    def get (self,request):
        users = UserProfile.objects.all()  
        users_serializer = serializers.UserSerializer(users,many=True) #lo despliega en fotmato de lista con el atributo many=true   
        return Response(users_serializer.data, status=status.HTTP_200_OK)