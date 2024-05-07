from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from blog.serializers import BlogSerializer

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def UpdateBlogView(request):
        if request.method == 'PUT':
            try:
                data = request.data
                Serializer = BlogSerializer(data=data)
                if not Serializer.is_valid():
                    return Response(Serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                return Response({'message': 'Blog updated successfully.'}, status=status.HTTP_200_OK)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)