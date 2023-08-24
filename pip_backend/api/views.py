
from api.models import User
from api.serializers import UserSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password
import re
from rest_framework import status


from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

# Token login function 
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['email'] = user.email
        

        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


@api_view(['POST'])
def signup(request):
    data = request.data
    if re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', data['email']):    
        if request.method == 'POST':
            user = User.objects.create(
                name=data['name'],
                email=data['email'],
                mobile=data['mobile'],
                password=make_password(data['password']),
            )
            serializer = UserSerializer(user, many=False)
            return Response("registered success")
    else:
        return Response({"error": "Invalid email format"}, status=status.HTTP_400_BAD_REQUEST)

# fetching all registered user
@api_view(['GET'])
def getting_all_users(request):
    users =  User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)



        
    