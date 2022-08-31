from django.contrib import admin

from users.models import User

# Register your models here.

admin.site.register(User)

# from products.admin import BasketInlineAdmin
# @admin.register(User)
# class UserAdmin(admin.ModelAdmin):
#     inlines = (BasketInlineAdmin, )
