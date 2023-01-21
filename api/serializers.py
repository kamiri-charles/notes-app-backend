from rest_framework.serializers import ModelSerializer, ReadOnlyField
from .models import Note, User
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password


class NoteSerializer(ModelSerializer):
    # Return owner's username instead of id
    owner = ReadOnlyField(source='owner.username')

    class Meta:
        model = Note
        fields = '__all__'



class UserSerializer(ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = '__all__'

    def create(self, validated_data):
        instance = get_user_model()(
            username=validated_data['username'],
            password=make_password(validated_data['password']),
            is_staff=True,
            is_active=True
        )
        instance.save()
        
        return instance