from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser, AllowAny
from .models import Category, MenuItem
from .serializers import CategorySerializer, MenuItemSerializer
from rest_framework.response import Response


class CategoryView(APIView):
    
    def get_permissions(self):
        if self.request.method == 'POST':
            return [IsAdminUser()]
        elif self.request.method == 'GET':
            return [AllowAny()]
        return super().get_permissions()


    def post(self, request, *args, **kwargs):
        serializer = CategorySerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
    def get(self, request, *args, **kwargs):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        
        return Response(serializer.data)
    
    
class MenuItemView(APIView):
    
    def get_permissions(self):
        if self.request.method == 'POST':
            return [IsAdminUser()]
        elif self.request.method == 'GET':
            return [AllowAny()]
        return super().get_permissions()
    
    def post(self, request, *args, **kwargs):
        serializer = MenuItemSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
    def get(self, request, *args, **kwargs):
        categories = MenuItem.objects.all()
        serializer = MenuItemSerializer(categories, many=True)
        
        return Response(serializer.data)