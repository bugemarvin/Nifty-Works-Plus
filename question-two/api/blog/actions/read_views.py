from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from blog.serializers import BlogSerializer
from blog.models import Blog

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def BlogListView(request):
    if request.query_params.get('title'):
        data = Blog.objects.filter(title=request.query_params.get('title'))
        if not data:
            return Response({'error': 'No blog post found with the given title.'}, status=status.HTTP_404_NOT_FOUND)
    else:
        data = Blog.objects.all()

    try:
        serializer = BlogSerializer(data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)