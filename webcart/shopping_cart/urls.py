from . import views
from django.urls import path

app_name = "shopping_cart"

urlpatterns = [
	path("add-to-cart/(<item_id>[-\w]+)", views.add_to_cart, name="add_to_cart"),
	path("order-summary", views.order_details, name="order_summary"),
	path("success", views.success, name="success"),
	path("item/delete", views.delete_from_cart, name="view_menu"),
	path("checkout", views.checkout, name="checkout"),
	path("payment(<item_id>[-\w]+)", views.process_payment, name="process_payment"),
	path("update-transaction", views.update_transaction_records, name="update_transaction")
	]
