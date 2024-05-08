from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from blog.models import Blog

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def DeleteBlogView(request):
        if request.method == 'DELETE':
            try:
                data = request.data
                if 'title' in data:
                        blog = Blog.objects.get(title=data['title'])
                else:
                        return Response({'error': 'Please provide a title to delete a blog post.'}, status=status.HTTP_400_BAD_REQUEST)
                blog.delete()
                return Response({'message': 'Blog deleted successfully.'}, status=status.HTTP_200_OK)
            except Exception as e:
                    return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)