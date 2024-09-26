from django import template


register = template.Library()


@register.filter(name='calc_subtotal')
def calc_subtotal(price, vat, quantity):
    return (price + vat) * quantity