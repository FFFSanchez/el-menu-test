from django.urls import path, re_path
import menu.views as menu

urlpatterns = [
    path('', menu.home, name='home'),
    re_path(r'^(\d+)', menu.home, name='home')
]
