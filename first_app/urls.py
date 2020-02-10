from django.urls import path
from first_app.views import HelloWorld


urlpatterns = [
  path('', HelloWorld.as_view(), name = 'helloworld')
]