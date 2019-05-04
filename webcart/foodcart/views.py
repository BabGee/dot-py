from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
# Create your views here.
	
		
def Home(request):
	return render(request, "foodcart/home.html")
	
def about(request):
	return render(request, "foodcart/about.html")

def gallery(request):
	return render(request, "foodcart/gallery.html")
	
def viewMenu(request):	
	return render(request, "foodcart/menu.html")
	
def retailers(request):
	return render(request, "foodcart/retailers.html")
	
	
	
	
	
	
# def login_user(request):
	# username = request.POST["username"] 
	# password = request.POST["password"]
	# user = authenticate(request, username=username, password=password)
	# if user is not None:
		# login(request, user)
		# return HttpResponseRedirect(reverse("foodcart-home"))
	# else:
		# return render(request, "foodcart/login.html", {"message":"invalid credentials"})

# def logout_user(request):
	# logout(request)
	# return render(request, "foodcart/login.html", {"message":"Logged out"})
		