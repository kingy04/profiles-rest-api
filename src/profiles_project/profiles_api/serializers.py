from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    """ Serializes a name field for testing our APIView. """

    first_name = serializers.CharField(max_length=15)
