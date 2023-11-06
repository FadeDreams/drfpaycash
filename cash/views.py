from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import CashSerializer
from .models import Cash
from rest_framework import permissions
from .permissions import IsOwner


class CashListAPIView(ListCreateAPIView):
    serializer_class = CashSerializer
    queryset = Cash.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)


class CashDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = CashSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwner,)
    queryset = Cash.objects.all()
    lookup_field = "id"

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)

