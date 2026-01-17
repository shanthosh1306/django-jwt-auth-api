from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model() #Returns the active user model (ProfileUser)

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','email','password']
        extra_kwargs = {
    'password': {'write_only': True}
}


    def create(self,validated_data): # We override create() in DRF serializers to ensure passwords are hashed using create_user() instead of being stored in plain text.”This will create new user.
        user = User.objects.create_user(
            validated_data['username'],
            validated_data['email'],
            validated_data['password'])
        return user