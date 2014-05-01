# -*- coding: utf-8 -*-

from django.contrib.auth.models import User, Group

from rest_framework import viewsets
from quickstart.serializers import UserSerializer, GroupSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objecs.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed od edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
