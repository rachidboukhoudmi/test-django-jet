from django.contrib import admin
from unfold.admin import ModelAdmin, TabularInline
from .models import Category, Product, Customer, Order, OrderItem

@admin.register(Category)
class CategoryAdmin(ModelAdmin):
    list_display = ('name', 'is_active', 'created_at')
    list_filter = ('is_active',)
    search_fields = ('name',)

@admin.register(Product)
class ProductAdmin(ModelAdmin):
    list_display = ('name', 'category', 'price', 'stock', 'available')
    list_filter = ('available', 'category')
    search_fields = ('name', 'sku')
    list_editable = ('price', 'stock', 'available')
    autocomplete_fields = ('category',)

@admin.register(Customer)
class CustomerAdmin(ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'date_joined')
    search_fields = ('first_name', 'last_name', 'email')
    date_hierarchy = 'date_joined'

class OrderItemInline(TabularInline):
    model = OrderItem
    extra = 1
    autocomplete_fields = ('product',)

@admin.register(Order)
class OrderAdmin(ModelAdmin):
    list_display = ('id', 'customer', 'status', 'total_amount', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('customer__first_name', 'customer__last_name', 'customer__email')
    inlines = [OrderItemInline]
    date_hierarchy = 'created_at'