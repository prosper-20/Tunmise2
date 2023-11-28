from django.shortcuts import render, get_object_or_404
from .models import Properties
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PropertySerializer
from rest_framework import status
from rest_framework.generics import ListCreateAPIView


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
from rest_framework.filters import SearchFilter

class NewHomePage(ListCreateAPIView):
    queryset = Properties.objects.all()
    serializer_class = PropertySerializer
    filter_backends = [SearchFilter]
    search_fields = ["address", "type", "status"]

# class NewHomePage(APIView):
#     def get(self, request, *args, **kwargs):
#         all_properties = Properties.objects.all()
#         serialized_properties = PropertySerializer(all_properties, many=True)
#         return Response(serialized_properties.data, status=status.HTTP_200_OK)
    
#     def post(self, request, *args, **kwargs):
#         new_house = PropertySerializer(data=request.data)
#         if new_house.is_valid():
#             new_house.save()
#             return Response({"Success": "House has been added",
#                              "details": new_house.data}, status=status.HTTP_201_CREATED)
#         return Response(new_house.errors, status=status.HTTP_400_BAD_REQUEST)
    

# class PropertyDetailPage(APIView):
#     def get(self, request, id, format=None, *args, **kwargs):
#         # single_property = Properties.objects.get(id=id)
#         single_property = get_object_or_404(Properties, id=id)
#         serialized_property = PropertySerializer(single_property)
#         return Response(serialized_property.data, status=status.HTTP_200_OK)
    
#     def put(self, request, id, format=None, *args, **kwargs):
#         single_property = Properties.objects.get(id=id)
#         serialized_property = PropertySerializer(single_property, data=request.data, partial=True)
#         if serialized_property.is_valid():
#             serialized_property.save()
#             return Response({"Success": "House details updated successfully!"}, status=status.HTTP_202_ACCEPTED)
#         return Response({'Error': 'Something went wrong!!'}, status=status.HTTP_400_BAD_REQUEST)
    
#     def delete(self, request, id, format=None, *args, **kwargs):
#         single_property = Properties.objects.get(id=id)
#         single_property.delete()
#         return Response({"Success": "Property deleted successfully!"}, status=status.HTTP_204_NO_CONTENT)

from rest_framework.generics import RetrieveUpdateDestroyAPIView

class PropertyDetailPage(RetrieveUpdateDestroyAPIView):
    queryset = Properties.objects.all()
    serializer_class = PropertySerializer
    lookup_field = "id"



