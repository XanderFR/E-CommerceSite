from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Product, Order

# Register your models here.

admin.site.site_header = "E-Commerce Site"
admin.site.site_title = "ABC Shopping"
admin.site.index_title = "Manage ECommerce Site"


class ProductAdmin(admin.ModelAdmin):
    def change_category_to_default(self, request, queryset):
        queryset.update(category="default")
    # Admin Mode Customization Code
    change_category_to_default.short_description = 'Default Category'
    list_display = ('title', 'price', 'discount_price', 'category', 'description')  # Product data table
    search_fields = ('title', 'category')
    actions = ('change_category_to_default',)
    list_editable = ('price', 'category')

admin.site.register(Product, ProductAdmin)
admin.site.register(Order)
