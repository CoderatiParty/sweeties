from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ('order_number', 'date',
                       'grand_total',
                       'stripe_pid')

    fields = ('order_number', 'user_profile', 'first_name', 'last_name',
              'street_address1', 'street_address2', 'town_or_city', 'county',
              'post_or_zipcode', 'country', 'phone_number', 'email',
                'date', 'order_total', 'grand_total', 'original_cart', 'stripe_pid')

    list_display = ('order_number', 'first_name',
                    'last_name', 'date', 'grand_total',)

    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)