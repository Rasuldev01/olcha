from django import template

register = template.Library()


@register.filter
def price_filter(request, price):
    price = str(price)
    price = price[::-1]
    count = 0
    price_new = ""
    for i in price:
        if count % 3 == 0:
            price_new += " "
        price_new += i
        count = count + 1
    price_new = price_new[::-1]
    return price_new
