from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *
from rest_framework_simplejwt.views import (TokenObtainPairView , TokenRefreshView)
urlpatterns = [
    path('',TodoView.as_view(),name='todo'),
    path('update/<int:id>/',TodoView.as_view(),name='update'),
    path('register/',Register.as_view(),name='register'),
    path('register/<int:id>/',Register.as_view(),name='register'),
    # path('login/',MyObtainTokenView.as_view(),name='login'),
    path('token/',TokenObtainPairView.as_view(),name='token'),
    path('login/refresh/',TokenRefreshView.as_view(),name='tokenrefresh'),
]
url_patterns=format_suffix_patterns(urlpatterns)