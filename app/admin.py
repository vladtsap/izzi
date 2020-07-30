from django.contrib import admin
from .models import User, Order


class UserAdmin(admin.ModelAdmin):
	fields = ('id', 'firstName', 'lastName', 'registrationDate', 'orderID', 'birthDate')
	list_display = ['id','firstName', 'lastName', 'registrationDate', 'orderID']
	readonly_fields = ['id']


class OrderAdmin(admin.ModelAdmin):
	fields = ('id', 'itemName', 'orderDate')
	list_display = ['id', 'itemName', 'orderDate']
	readonly_fields = ['id']


admin.site.register(User, UserAdmin)
admin.site.register(Order, OrderAdmin)
