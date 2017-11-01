from django.db.models import Avg
from django.db.models.base import ObjectDoesNotExist
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework.generics import (RetrieveUpdateDestroyAPIView,
                                     ListCreateAPIView, CreateAPIView,
                                     ListAPIView)
from .serializers import (LocationSerializer, VisitSerializer,
                          AddVisitSerializer, UserSerializer)
from .models import User, Visit, Location


class RegisterUserView(CreateAPIView):
    """
    post:
    Create user
    """
    model = get_user_model().objects.all()
    serializer_class = UserSerializer


class UserListView(ListAPIView):
    """
    get:
    Show all users
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailsView(RetrieveUpdateDestroyAPIView):
    """
    get:
    Show user

    put:
    Update user

    patch:
    Update user

    delete:
    Delete user
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserGetRatioView(APIView):
    """
    get:
    Show information about user's visits. Such as visited
    locations, number of visits and average rating that
    user gave to all visited locations.
    """

    def get(self, request, format=None, **kwargs):
        try:
            user = User.objects.get(pk=kwargs.get('pk'))
        except ObjectDoesNotExist:
            raise NotFound

        visits_set = user.visits.all()
        count = visits_set.count()
        avg = visits_set.aggregate(Avg('ratio')).get('ratio__avg')
        locations = [{'id': visit.location.id} for visit in visits_set]

        return Response({
            'count': count,
            'avg': avg,
            'locations': locations
        })


class LocationListView(ListCreateAPIView):
    """
    get:
    Show all locations

    post:
    Create new location
    """
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class LocationDetailsView(RetrieveUpdateDestroyAPIView):
    """
    get:
    Show location

    put:
    Update location

    patch:
    Update location

    delete:
    Delete location
    """
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class LocationAddVisitView(CreateAPIView):
    """
    post:
    Create visit for location
    """
    serializer_class = AddVisitSerializer


class LocationGetRatioView(APIView):
    """
    get:
    Show information about location. Such as visitors,
    number of visits and average rating.
    """

    def get(self, request, format=None, **kwargs):
        try:
            location = Location.objects.get(pk=kwargs.get('pk'))
        except ObjectDoesNotExist:
            raise NotFound

        visits_set = location.visits.all()
        count = visits_set.count()
        avg = visits_set.aggregate(Avg('ratio')).get('ratio__avg')
        # distinct visitors
        # visitors = [{'id': visit.get('user')} for visit
        #             in visits_set.values('user').distinct()]
        visitors = [{'id': visit.user.id} for visit in visits_set]

        return Response({
            'count': count,
            'avg': avg,
            'visitors': visitors
        })


class VisitListView(ListAPIView):
    """
    get:
    Show all visits
    """
    queryset = Visit.objects.all()
    serializer_class = VisitSerializer


class VisitDetailsView(RetrieveUpdateDestroyAPIView):
    """
    get:
    Show visit

    put:
    Update visit

    patch:
    Update visit

    delete:
    Delete visit
    """

    queryset = Visit.objects.all()
    serializer_class = VisitSerializer
