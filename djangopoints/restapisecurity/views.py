from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet,ReadOnlyModelViewSet,GenericViewSet
from restapisecurity.models import Book
from restapisecurity.book_serializer import  BookSerializer
from rest_framework.mixins import *

class MyCustomViewSet(GenericViewSet,CreateModelMixin,DestroyModelMixin,ListModelMixin):  # Add --> DELETE --> LIST
        pass


from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser

#    A viewset that provides default `create()`, `retrieve()`, `update()`,
#    `partial_update()`, `destroy()` and `list()` actions.
# `create()`, `retrieve()`, `update()`, `partial_update()`, `destroy()` and `list()`

class BookAPIs(ModelViewSet):       # 6
    #
    permission_classes = (AllowAny,)  # AllowANY
    queryset = Book.objects.all()
    serializer_class = BookSerializer


    def get_permissions(self):
         if self.action in ['update','partial_update','destroy']:        # Authentication rkh hai
              self.permission_classes = (IsAuthenticated,)
         elif  self.action in ['destroy']:        # Authentication rkh hai
              self.permission_classes = (IsAdminUser,)
         return super().get_permissions()  # kiska permission  -->  ModelViewSet
