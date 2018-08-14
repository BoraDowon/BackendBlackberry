from django.contrib.auth.models import User
from rest_framework import serializers
from accounts.models import Profile


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        field = ('username', 'last_name', 'first_name', 'email')


class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=True)

    class Meta:
        model = Profile
        fields = ('user', 'university_id')

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = UserSerializer.create(UserSerializer(), validated_data=user_data)
        client, created = Profile.objects.update_or_create(user=user, university_id=validated_data.pop('university_id'))

        return client
