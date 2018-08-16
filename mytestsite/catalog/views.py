from django.shortcuts import render

def index(request):
	"""View function for home page of site."""

  
    

	return render(request, 'index.html')
	
def find_us(request):
	"""View function for find_us of site."""

  
    

	return render(request, 'findus.html')
	
def food(request):
	"""View function for home page of site."""

  
    

	return render(request, 'Food.html')
def icecream(request):
	return render(request, 'icecream.html')