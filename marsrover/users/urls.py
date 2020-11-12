from django.urls import path, include
from .views import home_view, register_view, rover_view


urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('home/', home_view, name="home"),
    path('register/', register_view, name="register"),
   path('rovers/', rover_view, name="rover"),
   # path('rovers/<int:pk>', rover_detail, name="rover detail"),
]

