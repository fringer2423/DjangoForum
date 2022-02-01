from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Checkbox
from .serializers import CheckboxSerializers, UserSerializers, UserCreateSerializers
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework import authentication, permissions
from rest_framework import generics


# class CheckboxViewset(viewsets.ModelViewSet):
#     queryset = Checkbox.objects.all()
#     serializer_class = CheckboxSerializers


class UserList(generics.ListCreateAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializers

    # def list(self, request, format=None):
    #     users = User.objects.all()
    #     serializer = UserSerializers(users, many=True)
    #     return Response(serializer.data)
    #
    # def create(self, request, format=None):
    #     serializer = UserCreateSerializers(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #     return Response(serializer.data, status=status.HTTP_201_CREATED)


class UserDelete(APIView):
    permission_classes = [permissions.IsAdminUser]

    def delete(self, request, pk, format=None):
        user = User.objects.get(id=pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def checkbox_list(request):
    checkboxes = Checkbox.objects.all()
    serializer = CheckboxSerializers(checkboxes, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def checkbox_detail(request, pk):
    try:
        checkbox = Checkbox.objects.get(id=pk)
        serializer = CheckboxSerializers(checkbox)
    except Checkbox.DoesNotExist as err:
        return Response({"error": f"Checkbox with id={pk} not found"}, status=status.HTTP_404_NOT_FOUND)
    return Response(serializer.data)


@api_view(['POST'])
def checkbox_create(request):
    serializer = CheckboxSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['PUT'])
def checkbox_update(request, pk):
    try:
        checkbox = Checkbox.objects.get(id=pk)
        serializer = CheckboxSerializers(checkbox, data=request.data)
        if serializer.is_valid():
            serializer.save()
    except Checkbox.DoesNotExist as err:
        return Response({"error": f"Checkbox with id={pk} not found"}, status=status.HTTP_404_NOT_FOUND)
    return Response(serializer.data)


@api_view(['DELETE'])
def checkbox_delete(request, pk):
    checkbox = Checkbox.objects.get(id=pk)
    checkbox.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
