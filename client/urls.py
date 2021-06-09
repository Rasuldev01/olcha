from django.urls import path
from .views import ClientRegistration, ClientLogin

app_name = 'client'

urlpatterns = [
    path("registration/", ClientRegistration.as_view(), name='registration'),
    path("login/", ClientLogin.as_view(), name='login')
]