from django.shortcuts import render, get_object_or_404
from .models import Dish, Order
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

def menu(request):
    dishes = Dish.objects.all()
    return render(request, "menu/menu.html", {"dishes": dishes})

@csrf_exempt
def save_order(request):
    if request.method == "POST":
        data = json.loads(request.body)

        order = Order.objects.create(
        items=data.get("items"),
        total=data.get("total"),
        name=data.get("name"),
        phone=data.get("phone"),
        address=data.get("address")
)

    return JsonResponse({
         "status": "success",
         "order_id": order.id
})
    
import json

def order_detail(request, id):
    order = get_object_or_404(Order, id=id)

    items = json.loads(order.items)

    # 🔥 ADD THIS LOOP
    for item in items:
        items[item]['subtotal'] = items[item]['price'] * items[item]['qty']

    return render(request, "menu/order_detail.html", {
        "order": order,
        "items": items
    })

def payment_page(request, id):
    order = Order.objects.get(id=id)
    return render(request, 'menu/payment.html', {'order': order, 'total': order.total})