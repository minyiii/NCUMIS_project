from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# develop測試
import cv2

def index(request):
    return HttpResponse("test branch, MIS project, 5PEN!!!!")