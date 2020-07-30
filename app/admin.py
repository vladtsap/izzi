from django.contrib import admin
from .models import User, Order


class UserAdmin(admin.ModelAdmin):
	fields = ('firstName', 'lastName', 'registrationDate', 'orderID')


class OrderAdmin(admin.ModelAdmin):
	fields = ('id', 'itemName', 'orderDate')
	readonly_fields = ['id']


admin.site.register(User, UserAdmin)
admin.site.register(Order, OrderAdmin)
