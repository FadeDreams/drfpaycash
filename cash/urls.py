
from django.urls import path
from . import views


urlpatterns = [
    path('', views.CashListAPIView.as_view(), name="cashs"),
    path('<int:id>', views.CashDetailAPIView.as_view(), name="cash"),
]
