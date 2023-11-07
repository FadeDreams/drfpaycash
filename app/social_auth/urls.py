from django.urls import path

from .views import GoogleSocialAuthView
from . import views

urlpatterns = [
    path('google/', GoogleSocialAuthView.as_view()),
    path('index/', views.index_view, name='index'),

]

