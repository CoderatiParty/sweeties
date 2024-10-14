from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):

    readonly_fields = ('order_number', 'user_profile', 'date',
                       'grand_total', 'original_cart',
                       'stripe_pid')

    fields = ('order_number', 'user_profile', 'date',
              'grand_total', 'original_cart', 'stripe_pid')

    list_display = ('user_profile', 'order_number', 'date', 'grand_total',)

    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)