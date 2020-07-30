from django.db import models
import os


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
	file = models.FileField()

	def save(self, *args, **kwargs):
		"""Parse .csv and save new users to db"""
		super(UploadFile, self).save(*args, **kwargs)
		filename = self.file.url

		with open(filename, 'r') as file:
			data = file.read()
			data = data[data.index('\n') + 1:]
			for line in data.split('\n'):
				first_name, last_name, birth_date, registration_date = line.split(',')

				new_user = User(
					firstName=first_name,
					lastName=last_name,
					birthDate=birth_date.replace('/', '-'),
					registrationDate=registration_date.replace('/', '-')
				)
				new_user.save()

		os.remove(filename)  # don't leave anything in our folder
		UploadFile.objects.filter(file=filename).delete()  # and also nothing in our db
