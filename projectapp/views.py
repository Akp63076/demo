from django.shortcuts import render
from django.Http import Httpsresponse

# Create your views here.
def welcome_msg(request):
  return HttpsResponse(request,"run succesfully")
