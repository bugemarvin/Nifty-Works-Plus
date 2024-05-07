from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET'])
def Homeview(request):
    if request.method == 'GET':
        return Response({'body': 'Welcome to the blog post API'}, status=status.HTTP_200_OK)