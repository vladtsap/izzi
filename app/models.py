from django.db import models


class Order(models.Model):
	"""Orders model"""

	id = models.AutoField(primary_key=True)
	slug = models.SlugField()

	itemName = models.CharField(max_length=200)
	orderDate = models.DateField()

	class Meta:
		db_table = "orders"
		ordering = ["id"]

	def __str__(self):
		return "{} — order #{}".format(str(self.itemName), str(self.id))


class User(models.Model):
	"""User model"""

	id = models.AutoField(primary_key=True)

	firstName = models.CharField(max_length=200)
	lastName = models.CharField(max_length=200)
	birthDate = models.DateField()
	registrationDate = models.DateField(db_index=True)

	orderID = models.ForeignKey(Order, related_name='order', on_delete=models.CASCADE, db_index=True, blank=True,
								null=True)

	class Meta:
		db_table = "users"
		ordering = ["id"]

	def __str__(self):
		return " ".format(str(self.firstName), str(self.lastName))


class UploadFile(models.Model):
	data = models.FileField(upload_to="temp/")

	def save(self, *args, **kwargs):
		super(UploadFile, self).save(*args, **kwargs)
		filename = self.data.url
		with open(filename, 'r') as f:
			print(f.read())
