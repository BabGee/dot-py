from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from products.models import Product

def Home(request):
	return render(request, "foodcart/home.html")

def about(request):
	return render(request, "foodcart/about.html")

def team(request):
	return render(request, "foodcart/team.html")	

def gallery(request):
	return render(request, "foodcart/gallery.html")

def viewMenu(request):
	context = {
		"object_list": Product.objects.all()
	}
	return render(request, "foodcart/menu.html", context)
	return redirect("login")

def retailers(request):
	return render(request, "foodcart/retailers.html")
