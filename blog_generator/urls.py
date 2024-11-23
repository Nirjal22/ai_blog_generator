from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('signout/', views.signout, name='signout'),
    path('generate-blog/', views.generate_blog, name='generate-blog'),
]
