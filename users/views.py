


from users.serializers import RegisterSerializer
from .models import Profile
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.auth import AuthToken



# Create your views here.

@api_view(['POST'])
def register_api(request):
    serialize = RegisterSerializer(data=request.data)
    serialize.is_valid(raise_exception=True)
    user = serialize.save()
    _ , token = AuthToken.objects.create(user)
    return Response({
        'user_info':{
            'id':user.id,
            'username':user.username,
            'email':user.email
        },
        'token':token
    })


@api_view(['POST'])
def login_api(request):
    serializer = AuthTokenSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.validated_data['user']
    
    profile = Profile.objects.get(user=user.id)
    
    
    _ , token = AuthToken.objects.create(user)
    if profile.success == True:
        return Response({
            'user_info':{
                'id':user.id,
                'username':user.username,
                'email':user.email,               
                },
            'token':token
        })
    return Response({'error': 'not Success'},status=400)

@api_view(['GET'])
def get_user_data_api(request):
    user = request.user
    if user.is_authenticated:
        return Response({
        'user_info':{
            'id':user.id,
            'username':user.username,
            'email':user.email
        },
        })
    return Response({'error': 'not authenticated'},status=400)