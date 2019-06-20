from . import views
from django.urls import path

urlpatterns = [
	path("", views.Home, name="foodcart-home"),
	path("about_us", views.about, name="foodcart-about"),
	path("our_team", views.team, name="foodcart-team"),
	path("our_gallery", views.gallery, name="foodcart-gallery"),
	path("menu", views.viewMenu, name="view_menu"),
	path("retailers", views.retailers, name="view_retailers"),
	]
