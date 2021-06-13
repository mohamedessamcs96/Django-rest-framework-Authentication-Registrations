from rest_framework import fields, serializers


from django.contrib.auth.models import User


#user serializer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=('id','username','email')

#Register Serilizer

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=('id','username','email','password')
        extra_kwargs={'password':{'write_only':True}}

def create(self,validated_data):
    user=User.objects.create_user(validated_data['username'],validated_data['email',validated_data['password']])
    return user