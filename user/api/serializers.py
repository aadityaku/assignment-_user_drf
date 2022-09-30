from asyncore import write
import profile
from .models import Todo
from django.contrib.auth.models import User
from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from rest_framework.validators import UniqueValidator
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class RegisterUserSerializer(serializers.ModelSerializer):
    email=serializers.EmailField(required=True,validators=[UniqueValidator(queryset=User.objects.all())])
    password=serializers.CharField(write_only=True,required=True,validators=[validate_password])
    password2=serializers.CharField(write_only=True,required=True,validators=[validate_password])
    class Meta:
        model=User
        fields=['username','password','email','first_name','last_name','password2']
        
        extra_Kwargs={
            'first_name':{"required":True},
            'last_name':{"required":True}
        }
    def validate(self, data):
        if data.get('password') != data.get('password2'):

            raise serializers.ValidationError("Password did not match")

        return data
    
    def save(self):
        user = User()
        user.first_name = self.validated_data['first_name']
        user.last_name = self.validated_data['last_name']
        user.username = self.validated_data['username']
        user.email = self.validated_data['email']
        user.is_staff = True
        user.is_active = True
        user.set_password(self.validated_data['password'])
        
        user.save()
        return user

class TodoSerializer(serializers.ModelSerializer):
    # user_id = RegisterUserSerializer()
    class Meta:
        model=Todo
        fields= ['id','task','status']
        depth=1
    
        
    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['user_id'] = RegisterUserSerializer(instance.user_id).data
        return response