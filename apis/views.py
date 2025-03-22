from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
# Create your views here.

# Available API list
api_list = [
    'read-data',
    'save-data',
    'update-data',
    'delete-data',
    'create-data',
    'read-data-by-id',
    'read-data-by-id',
]


def index(request):
    return HttpResponse()

def call_api_by_number(request, api_id):
  if(api_id > len(api_list)):
    return HttpResponseNotFound("API not found!")
  
  api_name = api_list[api_id - 1]
  # return HttpResponse("Current API number: " + str(api_id) + " and API name: " + api_name)
  return HttpResponseRedirect(reverse('api-name', args=[api_name]))

def call_api_by_name(request, api_name):
    if api_name in api_list:
        return HttpResponse("Calling API: " + api_name)
    else:
        return HttpResponseNotFound("API not found!")


def save_data_to_db(data):
    return HttpResponse("Saving data to DB: " + data)
