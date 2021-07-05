from rest_framework import serializers
from .models import Proudct,Category

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model=Category
        fields='__all__'

class ProductSerializerGet(serializers.ModelSerializer):
    category=CategorySerializer()
    class Meta:
        model=Proudct
        fields='__all__'

        def get_photo_url(self, obj):
            request = self.context.get('request')
            photo_url = obj.fingerprint.url
            return request.build_absolute_uri(photo_url)

class ProductSerializerPost(serializers.ModelSerializer):
    class Meta:
        model=Proudct
        fields='__all__'

