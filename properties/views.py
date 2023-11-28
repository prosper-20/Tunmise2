from django.shortcuts import render
from .models import Properties
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PropertySerializer
from rest_framework import status


# @api_view(["GET", "POST"])
# def home_page(request):
#     if request.method == "GET":
#         all_properties = Properties.objects.all()
#         serialized_properties = PropertySerializer(all_properties, many=True)
#         return Response(serialized_properties.data, status=status.HTTP_200_OK)
#     else:
#         new_house = PropertySerializer(data=request.data)
#         if new_house.is_valid():
#             new_house.save()
#             return Response({"Success": "House has been added",
#                              "details": new_house.data}, status=status.HTTP_201_CREATED)
#         return Response(new_house.errors, status=status.HTTP_400_BAD_REQUEST)


from rest_framework.views import APIView

class NewHomePage(APIView):
    def get(self, request, *args, **kwargs):
        all_properties = Properties.objects.all()
        serialized_properties = PropertySerializer(all_properties, many=True)
        return Response(serialized_properties.data, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        new_house = PropertySerializer(data=request.data)
        if new_house.is_valid():
            new_house.save()
            return Response({"Success": "House has been added",
                             "details": new_house.data}, status=status.HTTP_201_CREATED)
        return Response(new_house.errors, status=status.HTTP_400_BAD_REQUEST)