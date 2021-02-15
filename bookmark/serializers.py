from rest_framework import serializers
from bookmark.models import Bookmark

class bookmarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = bookmark
        fields = 'url'