from accounts.auth.register_views import register_user
from accounts.auth.login_views import user_login
from accounts.auth.logout_views import user_logout

def register(request):
    return register_user(request)

def login(request):
    return user_login(request)

def logout(request):
        return user_logout(request)


