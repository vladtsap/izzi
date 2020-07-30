from .models import User
from rest_framework import viewsets
from .serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """ API endpoint that allows view users"""
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer

