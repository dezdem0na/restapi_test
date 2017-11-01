from django.utils import timezone
from rest_framework import serializers
from apps.core.models import Country
from .models import User, Visit, Location


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('password', 'username', 'first_name', 'last_name', 'email',
                  'is_superuser', 'is_staff', 'gender', 'birth_date')
        depth = 1

    def create(self, validated_data):
        user = super(UserSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        user = super(UserSerializer, self).update(instance, validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user


class LocationSerializer(serializers.ModelSerializer):
    country = serializers.PrimaryKeyRelatedField(
        queryset=Country.objects.all(),
        required=True,
    )

    class Meta:
        model = Location
        fields = '__all__'


class VisitSerializer(serializers.ModelSerializer):

    class Meta:
        model = Visit
        fields = '__all__'
        depth = 1


class AddVisitSerializer(serializers.ModelSerializer):

    class Meta:
        model = Visit
        fields = ('ratio', )
        depth = 1

    def create(self, validated_data):
        localion_id = self.context['view'].kwargs['pk']
        validated_data['date'] = timezone.now()
        validated_data['user'] = self.context['request'].user
        validated_data['location'] = Location.objects.get(pk=localion_id)
        return Visit.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.date = validated_data.get('date', instance.date)
        instance.user = validated_data.get('user', instance.user)
        instance.ratio = validated_data.get('ratio', instance.ratio)
        instance.location = validated_data.get('location', instance.location)
        instance.save()
        return instance
