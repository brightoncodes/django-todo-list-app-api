from django.urls import path
from .views import UserFormView, logout_route
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('signup',UserFormView.as_view(), name='sign-up'),
    path('login',auth_views.LoginView.as_view(template_name='login_form.html'), name='login'),
    path('logout',logout_route, name='logout')
]
