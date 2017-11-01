import json
import pytest

from rest_framework import status
from apps.tourist.models import User, Location, Visit
from django.urls import reverse


@pytest.mark.django_db
def test_sign_in(admin_client, user):
    response = admin_client.post(reverse("api:sign_in"),
                                 data={"username": user.username,
                                       "password": "password"})
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_register(admin_client):
    response = admin_client.post(reverse("api:register"),
                                 data={"username": "username_test",
                                       "password": "password"})
    assert response.status_code == status.HTTP_201_CREATED


@pytest.mark.django_db
def test_user_list(admin_client):
    response = admin_client.get(reverse("api:user-list"))
    result = response.json()["results"]
    assert User.objects.all().count() == len(result)


@pytest.mark.django_db
def test_user_detail(admin_client, user):
    response = admin_client.get(reverse("api:user-details",
                                        kwargs={"pk": user.id}))
    result = response.json()
    assert User.objects.filter(pk=user.id).count() == 1
    assert User.objects.get(pk=user.id).username == result["username"] == user.username


@pytest.mark.django_db
def test_user_update_put(admin_client, user):
    data = {"password": user.password,
            "username": user.username,
            "first_name": "abracadabra",
            "last_name": user.last_name,
            'email': user.email,
            "is_superuser": user.is_superuser,
            "is_staff": user.is_staff,
            'gender': user.gender,
            'birth_date': str(user.birth_date)}
    response = admin_client.put(reverse("api:user-details",
                                        kwargs={"pk": user.id}),
                                data=json.dumps(data),
                                content_type="application/json")
    result = response.json()
    assert response.status_code == status.HTTP_200_OK
    assert result["first_name"] == "abracadabra"


@pytest.mark.django_db
def test_user_update_patch(admin_client, user):
    data = {"first_name": 'abracadabra',
            "password": user.password}
    response = admin_client.patch(reverse("api:user-details",
                                          kwargs={"pk": user.id}),
                                  data=json.dumps(data),
                                  content_type="application/json")
    result = response.json()
    assert response.status_code == status.HTTP_200_OK
    assert result["first_name"] == "abracadabra"


@pytest.mark.django_db
def test_user_delete(admin_client, user):
    response = admin_client.delete(reverse("api:user-details",
                                           kwargs={"pk": user.id}))
    assert response.status_code == status.HTTP_204_NO_CONTENT


@pytest.mark.django_db
def test_user_ratio(admin_client, user_with_ratio):
    response = admin_client.get(reverse("api:user-get-ratio",
                                        kwargs={"pk": user_with_ratio.id}))
    result = response.json()
    assert 'count' in result
    assert 'avg' in result
    assert 'locations' in result
    assert result['count'] == 1
    assert result['avg'] == 9.0
    assert isinstance(result['locations'], list)


@pytest.mark.django_db
def test_location_list(admin_client):
    response = admin_client.get(reverse("api:location-list"))
    result = response.json()["results"]
    assert Location.objects.all().count() == len(result)


@pytest.mark.django_db
def test_location_create(admin_client):
    data = {"country": "1",
            "name": "name_test",
            "description": "description_test",
            "city": "city_test"}
    response = admin_client.post(reverse("api:location-list"),
                                 data=data)
    assert response.status_code == status.HTTP_201_CREATED


@pytest.mark.django_db
def test_location_update_put(admin_client, location):
    data = {"country": location.country.id,
            "name": location.name,
            "description": "abracadabra",
            "city": location.city}
    response = admin_client.put(reverse("api:location-details",
                                        kwargs={"pk": location.id}),
                                data=json.dumps(data),
                                content_type="application/json")
    result = response.json()
    assert response.status_code == status.HTTP_200_OK
    assert result["description"] == "abracadabra"


@pytest.mark.django_db
def test_location_update_patch(admin_client, location):
    data = {"description": "abracadabra"}
    response = admin_client.patch(reverse("api:location-details",
                                          kwargs={"pk": location.id}),
                                  data=json.dumps(data),
                                  content_type="application/json")
    result = response.json()
    assert response.status_code == status.HTTP_200_OK
    assert result["description"] == "abracadabra"


@pytest.mark.django_db
def test_location_detail(admin_client, location):
    response = admin_client.get(reverse("api:location-details",
                                        kwargs={"pk": location.id}))
    result = response.json()
    assert Location.objects.filter(pk=location.id).count() == 1
    assert Location.objects.get(pk=location.id).name == result["name"] == location.name


@pytest.mark.django_db
def test_location_delete(admin_client, location):
    response = admin_client.delete(reverse("api:location-details",
                                           kwargs={"pk": location.id}))
    assert response.status_code == status.HTTP_204_NO_CONTENT


@pytest.mark.django_db
def test_visit_list(admin_client):
    response = admin_client.get(reverse("api:visit-list"))
    result = response.json()["results"]
    assert Visit.objects.all().count() == len(result)


@pytest.mark.django_db
def test_visit_detail(admin_client, visit):
    response = admin_client.get(reverse("api:visit-details",
                                        kwargs={"pk": visit.id}))
    result = response.json()
    assert Visit.objects.filter(pk=visit.id).count() == 1
    assert Visit.objects.get(pk=visit.id).location.city == result["location"]["city"]
    assert Visit.objects.get(pk=visit.id).location.country.id == result["location"]["country"]


@pytest.mark.django_db
def test_visit_update_put(admin_client, visit):
    data = {"ratio": 10,
            "date": str(visit.date)}
    response = admin_client.put(reverse("api:visit-details",
                                        kwargs={"pk": visit.id}),
                                data=json.dumps(data),
                                content_type="application/json")
    result = response.json()
    assert response.status_code == status.HTTP_200_OK
    assert result["ratio"] == 10


@pytest.mark.django_db
def test_visit_update_patch(admin_client, visit):
    data = {"ratio": 10}
    response = admin_client.patch(reverse("api:visit-details",
                                          kwargs={"pk": visit.id}),
                                  data=json.dumps(data),
                                  content_type="application/json")
    result = response.json()
    assert response.status_code == status.HTTP_200_OK
    assert result["ratio"] == 10


@pytest.mark.django_db
def test_visit_delete(admin_client, visit):
    response = admin_client.delete(reverse("api:visit-details",
                                           kwargs={"pk": visit.id}))
    assert response.status_code == status.HTTP_204_NO_CONTENT


@pytest.mark.django_db
def test_location_ratio(admin_client, location_with_ratio):
    response = admin_client.get(reverse("api:location-get-ratio",
                                        kwargs={"pk": location_with_ratio.id}))
    result = response.json()
    assert 'count' in result
    assert 'avg' in result
    assert 'visitors' in result
    assert result['count'] == 1
    assert result['avg'] == 8.0
    assert isinstance(result['visitors'], list)


@pytest.mark.django_db
def test_location_add_visit(admin_client, location):
    data = {'ratio': '5'}
    response = admin_client.post(reverse("api:location-add-visit",
                                         kwargs={"pk": location.id}),
                                 data=data)
    assert response.status_code == status.HTTP_201_CREATED
