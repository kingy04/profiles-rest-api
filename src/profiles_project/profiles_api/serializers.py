from rest_framework import serializers

from . import models

class HelloSerializer(serializers.Serializer):
    """ Serializes a name field for testing our APIView. """

    first_name = serializers.CharField(max_length=15)

class UserProfileSerializer(serializers.ModelSerializer):
    """ A serializer for our user profile objects. """

    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'first_name', 'last_name', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        """ Create and return a new user. """

        user = models.UserProfile(
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user

class ProfileFeedItemSerializer(serializers.ModelSerializer):
    """ A serializer for profile feed items. """

    class Meta:
        model = models.ProfileFeedItem
        fields = ('id', 'user_profile', 'status_text', 'created_on')
        extra_kwargs = {'user_profile': {'read_only': True}}
