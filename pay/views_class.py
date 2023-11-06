from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import PaysSerializer
from .models import Pay
from rest_framework import permissions
from .permissions import IsOwner


class PayListAPIView(ListCreateAPIView):
    serializer_class = PaysSerializer
    queryset = Pay.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)


class PayDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = PaysSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwner,)
    queryset = Pay.objects.all()
    lookup_field = "id"

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)

