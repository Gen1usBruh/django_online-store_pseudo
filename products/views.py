from unicodedata import category
from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

from products.models import Product, ProductCategory, Basket, SlideListImages

# Create your views here.

def index_page(request):
    return render(request, 'products/index.html')
    # 'render' combines a given template with a given context dictionary
    # and returns an HttpResponse object with that rendered text.

def products_catalog(request, category_id=None, page=1):
    context = {
        'categories': ProductCategory.objects.all(),
        # 'slide_list_photos': SlideListImages.objects.all(),
    }
    if category_id:
        products = Product.objects.filter(category_id=category_id)
    else:
        products = Product.objects.all()
    paginator = Paginator(products, 3)
    products_paginator = paginator.page(page)
    context.update({'products': products_paginator})
    return render(request, 'products/products.html', context)

@login_required
def basket_add(request, product_id):
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)
    if not baskets.exists():
        Basket.objects.create(user=request.user, product=product, quantity=1)
        # redirect to the current page
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def basket_delete(request, basket_id):
    basket = Basket.objects.get(id=basket_id)   
    basket.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

