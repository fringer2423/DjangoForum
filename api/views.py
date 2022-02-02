import logging

from rest_framework import viewsets, status, permissions, generics
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from .serializers import CheckboxSerializers, UserSerializers, DataSerializers
from .utils import Sum
from .models import Checkbox

logger = logging.getLogger('django')


class CheckboxViewset(viewsets.ModelViewSet):
    queryset = Checkbox.objects.all()
    serializer_class = CheckboxSerializers

    @action(detail=False, methods=["get"])
    def limit(self, request, pk=None):
        try:
            params = request.query_params
        except Exception as error:
            logger.error('error :%s', error)
        return Response({"result": params})


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


class DataView(APIView):
    @staticmethod
    def get(request):
        serializer = DataSerializers(data=request.query_params)
        serializer.is_valid(raise_exception=True)
        result = Sum(serializer.validated_data).call()

        return Response(result, status=status.HTTP_200_OK)
