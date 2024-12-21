from dj_rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers

class SinglePasswordRegisterSerializer(RegisterSerializer):
    # 비밀번호 확인 x
    password2 = None

    def validate(self, data):
        if 'password1' not in data:
            raise serializers.ValidationError({"password1": "Password is required."})
        return data

    def save(self, request):
        user = super().save(request)
        user.set_password(self.validated_data['password1'])
        user.save()
        return user
