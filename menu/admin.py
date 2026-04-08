from django.contrib import admin
from .models import Order, Dish   # ✅ add Dish

from .models import Order

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone', 'total')

    def changelist_view(self, request, extra_context=None):
        from django.db.models import Sum

        total_sales = Order.objects.aggregate(Sum('total'))['total__sum'] or 0
        total_orders = Order.objects.count()

        extra_context = extra_context or {}
        extra_context['total_sales'] = total_sales
        extra_context['total_orders'] = total_orders

        return super().changelist_view(request, extra_context=extra_context)

admin.site.register(Order, OrderAdmin)
admin.site.register(Dish)        # ✅ add this line