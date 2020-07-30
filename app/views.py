from .models import User
from rest_framework import viewsets
from .serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
	"""API endpoint that allows view users"""
	serializer_class = UserSerializer
	queryset = User.objects.all()

	def get_queryset(self):
		"""Filtering query"""
		queryset = User.objects.all()

		registration_date = self.request.query_params.get('date', None)
		registration_date_from = self.request.query_params.get('datefrom', None)
		registration_date_to = self.request.query_params.get('dateto', None)

		if registration_date is not None:  # if we have exact date
			queryset = queryset.filter(registrationDate=registration_date)
		else:
			if registration_date_from and registration_date_to is not None:  # both 'from' and 'to' params
				queryset = queryset.filter(registrationDate__gte=registration_date_from)
				queryset = queryset.filter(registrationDate__lte=registration_date_to)
			elif registration_date_from is not None:  # only 'from' param
				queryset = queryset.filter(registrationDate__gte=registration_date_from)
			elif registration_date_to is not None:  # only 'to' param
				queryset = queryset.filter(registrationDate__lte=registration_date_to)

		return queryset
