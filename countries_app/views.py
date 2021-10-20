from django.shortcuts import render


# imports needed to work with api's

from django.http.response import JsonResponse
# from rest_framework.parsers import JsonParser
from rest_framework.parsers import JSONParser
from rest_framework import status

from countries_app.models import Countries
from countries_app.serializers import CountriesSerializer

from rest_framework.decorators import api_view
# api_view is a wrapper from rest_framework
# used to work with function based views
# provides functionalities to enable django to receive request instance in views.
#  can also restric access to certain views

# Create your views here.

@api_view(['GET', 'POST']) # decorator

def countries_list(request):
    # the incoming request can be get/post

    if request.method == 'GET':
        countries_var = Countries.objects.all()
        # retrieving all the objects

        name = request.GET.get('name', None)
        if name is not None:
            coutries_var = countries_var.filter(name__icontains=name)
            # filter
            # name__icontains  checks if either name or description field 
            # contains the value of search items
        
        countries_serializer_var = CountriesSerializer(countries_var, many=True)
        #   many=True  serialize each if queryset contains multiple items

        return JsonResponse(countries_serializer_var.data, safe=False )
        # safe=False  any object can be passed for serialization as of now  

    
    elif request.method == 'POST':
        countries_data = JSONParser().parse(request)
        countries_serializer_var = CountriesSerializer(data=countries_data)

        if(countries_serializer_var.is_valid()):
            countries_serializer_var.save()
            return JsonResponse(countries_serializer_var.data, status = status.HTTP_201_CREATED)
    
        return JsonResponse(countries_serializer_var.errors, status = HTTP_400_BAD_REQUEST)



# others
# decorator
# put-update
@api_view(['GET', 'PUT', 'DELETE'])

def countries_detail(request, pk):
    #  here this pk is the id columkn primary key

    # we will request everything as per the primary key
    #  so we want to make sure that the key is legit

    try: # to check
        countries_var = Countries.objects.get(pk=pk)

    except Countries.DoesNotExist: # to handle
        return JsonResponse({'message': 'The country does not exist'}, status = status.HTTP_400_NOT_FOUND)


    if request.method == 'GET':
        countries_serializer_var = CountriesSerializer(countries_var)
        # everything is linked so be carefull while doing stuff
        return JsonResponse(countries_serializer_var.data)

    elif(request.method == 'PUT'):
        countries_data = JSONParser().parse(request)
        countries_serializer_var = CountriesSerializer(countries_var, data=countries_data)

        if countries_serializer_var.is_valid():
            countries_serializer_var.save()
            return JsonResponse(countries_serializer_var.data)

        return JsonResponse(countries_serializer_var.errors, status=status.HTTP_400_BAD_REQUEST)


    elif request.method == 'DELETE':
        countries_var.delete()

        return JsonResponse({'message': 'country was deleted successfully'}, status=status.HTTP_204_NO_CONTENT)


        