from django.urls import path
from . import views


# urlpatterns = [
    # path('', views.PayListAPIView.as_view(), name="pays"),
    # path('<int:id>', views.PayDetailAPIView.as_view(), name="pay"),
# ]

urlpatterns = [
    path('pays/', views.pay_list, name='pay_list'),
    path('pays/<int:id>/', views.pay_detail, name='pay_detail'),
]

