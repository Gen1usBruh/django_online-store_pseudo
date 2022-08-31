from django.contrib import admin

from products.models import Product, ProductCategory, Basket, SlideListImages

# Register your models here.

admin.site.register(Product)
admin.site.register(ProductCategory)
admin.site.register(Basket)
admin.site.register(SlideListImages)


# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):
#     list_display = ('name', 'price', 'quantity', 'category')
#     fields = ('name', 'image', 'description', 'short_description', ('price', 'quantity'), 'category')
#     readonly_fields = ('short_description',)
#     ordering = ('name',)
#     search_fields = ('name',)
#
# class BasketInlineAdmin(admin.TabularInline):
#     model = Basket
#     fields = ('product', 'quantity', 'created_timestamp')
#     readonly_fields = ('product', 'created_timestamp',)
#     extra = 0