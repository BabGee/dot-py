from . import views
from django.urls import path

urlpatterns = [
	path("", views.Home, name="foodcart-home"),
	path("about", views.about, name="foodcart-about"),
	path("ourgallery", views.gallery, name="foodcart-gallery"),
	path("menu", views.viewMenu, name="view_menu"),
	path("retailers", views.retailers, name="view_retailers"),
	# path("login", views.login_user, name="foodcart-login"),
	# path("logout", views.logout_user, name="foodcart-logout")
	]