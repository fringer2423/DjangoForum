from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Checkbox
from .serializers import CheckboxSerializers


# class CheckboxViewset(viewsets.ModelViewSet):
#     queryset = Checkbox.objects.all()
#     serializer_class = CheckboxSerializers

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
