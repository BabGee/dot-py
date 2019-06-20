from django.shortcuts import render
from products.models import Product
from users.models import Profile
from django.contrib.auth.decorators import login_required
from shopping_cart.models import OrderItem, Order
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from shopping_cart.extras import generate_order_id
# from carts.helpers import get_reference_code
from django.urls import reverse


def get_user_pending_order(request):
	user_profile = get_object_or_404(Profile, user=request.user)
	order = Order.objects.filter(owner=user_profile, is_ordered=False)
	if order.exists():
		return order[0]
	return 0	

@login_required
def add_to_cart(request, **kwargs):
	user_profile = get_object_or_404(Profile, user=request.user)
	product = Order.objects.filter(owner=user_profile, is_ordered=False)
	if product in request.user.profile.food_orders.all():
		messages.info(request, "In Cart")
		return redirect(reverse("view_menu")) #MENU.HTML NAME
		
	order_item, status = OrderItem.objects.get_or_create(product=product)
	order_order, status = Order.objects.get_or_create(owner=user_profile, is_ordered=True)
	user_order.items.add(order_item)
	
	if status:
		user_order.ref_code = generate_order_id()
		user_order.save()
		
	messages.info(request, "Item added to Cart")
	return redirect(reverse("view_menu"))#MENU.HTML NAME

@login_required
def delete_from_cart(request, item_id):
	item_to_delete = OrderItem.objects.filter(pk=item_id)
	
	if item_to_delete.exists():
		item_to_delete[0].delete()
		messages.info(request, "Item Deleted")
		return redirect(reverse("order_summary"))

@login_required
def order_details(request):
	existing_order = get_user_pending_order(request)
	context = {
		"order": existing_order
		}
	return render(request, "shopping_cart/order_summary.html", context)


@login_required
def checkout(request):
	existing_order = get_user_pending_order(request)
	context = {
		"order": existing_order
		}
	return render(request, "shopping_cart/checkout.html", context)

@login_required
def process_payment(request):
	#process payment
	return redirect(reverse("shopping_cart:update_records", kwargs={"order_id":order_id }))
	
@login_required
def update_transaction_records(request, order_id):
	order_to_purchase = Order.objects.filter(pk=order_id).first()
	order_to_purchase.is_ordered = True
	order_to_purchase.date_ordered = datetime.datetime.now()
	order_to_purchase.save()
	order_items = order_to_purchase.items.all()
	order_items.update(is_ordered = True, date_ordered = datetime.datetime.now())
	user_profile = get_object_or_404(Profile, user=request.user)
	order_products = [item.product for item in order_items]
	user_profile.food_ordered.add(*order_products)
	user_profile.save()
	
	messages.info(request, "Thank you, Items added")
	return redirect(reverse("users:my_profile"))

@login_required	
def success(request, **kwargs):
	return render(request, "shopping_cart/purchase_success.html", {})
		
	
	


		