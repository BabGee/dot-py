from django.shortcuts import render, redirect  
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required 
from shopping_cart.models import Order
from .models import Profile


def register(request):
	if request.method == "POST":
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get("username")
			messages.success(request, f"Your account has been created. You can now login")
			return redirect("login")
	else:	
		form = UserRegisterForm()
		
	context = {
		"form":form
	}
	return render(request, "users/register.html", context)
	
@login_required	
def profile(request):
	my_user_profile = Profile.objects.filter(user=request.user).first()
	my_orders = Order.objects.filter(is_ordered=True,owner=my_user_profile)
	context = {
	"my_orders": my_orders
	}
	return render(request, "users/profile.html", context)	








