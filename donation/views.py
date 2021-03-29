from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from . import models

# Create your views here.

class HomePage(View):
    def get(self,request):
        return render(request,'donation/home.html')
        # render and returning the homepage





class DonorPage(View):
    def get(self,request):
        return render(request,'donation/donarPage.html')
        # get function to render the user input form


    def post(self,request):
        #post to validate the user input data and record it in the table.
        return
