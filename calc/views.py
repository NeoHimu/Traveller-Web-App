from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
	return render(request, 'home.html', {'name':'whatsup'})


def add(request):
	num1 = request.POST['num1']
	num2 = request.POST['num2']
	return render(request, 'result.html', {'result': int(num1)+int(num2)})
