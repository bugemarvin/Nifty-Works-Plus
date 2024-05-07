from blog.actions.create_views import CreateBlogView
from blog.actions.read_views import BlogListView, BlogDetailView
from blog.actions.update_views import UpdateBlogView
from blog.actions.delete_views import DeleteBlogView

def create(request):
    return CreateBlogView(request)

def list(request):
    return BlogDetailView(request)

def detail(request):
    return BlogListView(request)

def update(request):
    return UpdateBlogView(request)

def delete(request):
    return DeleteBlogView(request)