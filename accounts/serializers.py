from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password

from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.validators import UniqueValidator

from django.contrib.auth import authenticate

class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required = True,
        validators = [UniqueValidator(queryset=User.objects.all())],
    )

    password = serializers.CharField(
        write_only = True,
        required = True,
        validators = [validate_password],
    )

    password2 = serializers.CharField( #비밀번호 확인을 위한 필드
        write_only = True,
        required = True,
    )

    class Meta:
        model = User
        #username = ID, first_name = 사용자 이름, password2 = 비밀번호 검증용
        fields = ('first_name', 'email', 'password', 'password2')

    def validate(self, data): #password와 password2의 일치 여부 확인
        if data['password'] != data['password2']:
            raise serializers.ValidationError(
                {"password" : "비밀번호가 일치하지 않습니다."}
            )
        return data
    
    def create(self, validated_data):
        user = User.objects.create_user(
            username = validated_data['email'],
            first_name = validated_data['first_name'],
            email = validated_data['email'],
        )
        
        # 비밀번호 해싱하여 저장
        user.set_password(validated_data['password'])
        user.save()
        token = Token.objects.create(user=user)
        return user
    

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True, write_only = True)
    #write_only = True : 클라이언트 -> 서버의 역직렬화는 가능하지만 서버 -> 클라이언트는 불가능
    def validate(self, data):
        user = authenticate(username=data['email'], password=data['password'])
        if user:
            # 기존 토큰 삭제
            Token.objects.filter(user=user).delete()
            # 새로운 토큰 생성
            token, created = Token.objects.get_or_create(user=user)
            return token
        
        raise serializers.ValidationError( # 가입된 유저가 없을 경우
            {
                "error" : "잘못된 정보입니다."
            }
        )