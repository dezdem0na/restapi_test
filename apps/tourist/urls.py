from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token
from .schema import SwaggerSchemaView
from .views import (LocationDetailsView, LocationListView, RegisterUserView,
                    VisitListView, VisitDetailsView, LocationAddVisitView,
                    LocationGetRatioView, UserListView, UserDetailsView,
                    UserGetRatioView)


urlpatterns = [

    url(r'^docs/',
        SwaggerSchemaView.as_view(),
        name="docs"),

    url(r'^sign_in/$',
        obtain_jwt_token,
        name="sign_in"),

    url(r'^register/$',
        RegisterUserView.as_view(),
        name="register"),

    url(r'^users/$',
        UserListView.as_view(),
        name="user-list"),

    url(r'^users/(?P<pk>\d+)/$',
        UserDetailsView.as_view(),
        name="user-details"),

    url(r'^users/(?P<pk>\d+)/ratio/$',
        UserGetRatioView.as_view(),
        name="user-get-ratio"),

    url(r'^locations/$',
        LocationListView.as_view(),
        name="location-list"),

    url(r'^locations/(?P<pk>\d+)/$',
        LocationDetailsView.as_view(),
        name="location-details"),

    url(r'^locations/(?P<pk>\d+)/visit/$',
        LocationAddVisitView.as_view(),
        name="location-add-visit"),

    url(r'^locations/(?P<pk>\d+)/ratio/$',
        LocationGetRatioView.as_view(),
        name="location-get-ratio"),

    url(r'^visits/$',
        VisitListView.as_view(),
        name="visit-list"),

    url(r'^visits/(?P<pk>\d+)/$',
        VisitDetailsView.as_view(),
        name="visit-details"),
]
