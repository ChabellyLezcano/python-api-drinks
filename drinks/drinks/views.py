from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Drink
from .serializers import DrinkSerializer
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

@api_view(['GET', 'POST'])
def drink_list(request, format=None):
    if request.method == 'GET':
        drinks = Drink.objects.all()
        serializer = DrinkSerializer(drinks, many=True)
        response_data = {
            "message": "List of drinks retrieved successfully",
            "drinks": serializer.data
        }
        return JsonResponse(response_data)

    elif request.method == 'POST':
        serializer = DrinkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response_data = {
                "message": "Drink created successfully",
                "drink": serializer.data
            }
            return Response(response_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def drink_detail(request, id,  format = None):
    drink = get_object_or_404(Drink, id=id)

    if request.method == 'GET':
        serializer = DrinkSerializer(drink)
        response_data = {
            "message": "Drink details retrieved successfully",
            "drink": serializer.data
        }
        return JsonResponse(response_data)

    elif request.method == 'PUT':
        serializer = DrinkSerializer(drink, data=request.data)
        if serializer.is_valid():
            serializer.save()
            response_data = {
                "message": "Drink updated successfully",
                "drink": serializer.data
            }
            return Response(response_data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        drink.delete()
        response_data = {
            "message": "Drink deleted successfully"
        }
        return Response(response_data, status=status.HTTP_204_NO_CONTENT)
