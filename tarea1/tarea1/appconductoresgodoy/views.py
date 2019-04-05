from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request, 'appconductoresgodoy/index.html')

def pagina2(request):
	return render(request, 'appconductoresgodoy/pagina2.html')

def pagina3(request):
	return render(request, 'appconductoresgodoy/pagina3.html')

def pagina4(request):
	return render(request, 'appconductoresgodoy/pagina4.html')

def pagina5(request):
	return render(request, 'appconductoresgodoy/pagina5.html')
