from django.contrib import admin
from .models import Dish, Order
import json
from django.utils.html import format_html

admin.site.register(Dish)

class OrderAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'get_items', 'total', 'view_order')

    def get_items(self, obj):
        items_dict = json.loads(obj.items)

        text = ""
        for item, data in items_dict.items():
            text += f"{item} ({data['qty']}), "

        return text

    get_items.short_description = 'Items'

    def view_order(self, obj):
        return format_html(
            '<a href="/order/{}/" target="_blank">View</a>',
            obj.id
        )

    view_order.short_description = 'View Order'

admin.site.register(Order, OrderAdmin)