from django.db import models
import uuid


class Orders(models.Model):
	"""Orders model"""

	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	index = models.PositiveIntegerField(default=0)
	slug = models.SlugField()

	itemName = models.CharField(max_length=200)
	orderDate = models.DateField()

	class Meta:
		db_table = "orders"
		ordering = ["index"]


class User(models.Model):
	"""User model"""

	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	slug = models.SlugField(unique=True)
	index = models.PositiveIntegerField(default=0)

	firstName = models.CharField(max_length=200)
	lastName = models.CharField(max_length=200)
	birthDate = models.DateField()
	registrationDate = models.DateField(db_index=True)

	orderID = models.ForeignKey(Orders, related_name='orderID', on_delete=models.CASCADE, db_index=True, null=True)

	class Meta:
		db_table = "users"
		ordering = ["index"]

