from rest_framework import serializers
from .models import SocialMediaPost

class ManageHashTagsGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMediaPost
        fields = '__all__'

        