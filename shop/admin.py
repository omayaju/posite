from mptt.admin import MPTTModelAdmin
from django.contrib import admin
from shop.models import Category, Product, Order

class CategoryAdmin(admin.ModelAdmin):
    fields = ['name', 'parent', 'img', 'description']
    list_display = ('name', 'parent', 'id')

class ProductAdmin(admin.ModelAdmin):
    fields = ['name', 'description', 'category', 'cost', 'sdesc', 'compos', 'app', 'care', 'img', 'back', 'action']
    list_display = ('name', 'category', 'action')
    search_fields = ['name']

class OrderAdmin(admin.ModelAdmin):
    fields = ['pername', 'perphone', 'peremail', 'prodlist']
    list_display = ('id', 'pername', 'perphone', 'peremail')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)