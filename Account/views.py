from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from Account.serializers import *

# from Account.models import User


#Generate token manually

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

# Registration
class Register_View(APIView):
    def post(self,request):
        serializer=Register_Serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        # username=serializer.data.get("username")
        # email=serializer.data.get('email')
        #Utility.send_otp_to_email(context={"username":username,"email":email})
        
        return Response({'message':'Account Create Successfully. Please Verify Your Account', 'status':status.HTTP_201_CREATED},status=status.HTTP_201_CREATED)
    
     
             
class Login_View(APIView):
    
    def post(self,request):
            serializer=Login_Serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            email=serializer.data.get('email')
            password=serializer.data.get('password')
            
            user=authenticate(email=email,password=password)
            if user is not None:
                token=get_tokens_for_user(user)
                return Response({'token':[token],'message':'Login Successfully'},status=status.HTTP_200_OK)
            
            else:
                return Response({'errors':'Email or Password is not Valid'},status=status.HTTP_400_BAD_REQUEST)
                      
                      
class Profile_View(APIView):
    permission_classes=[IsAuthenticated]
    def get(self,request):
        serializer=Profile_Serializer(request.user)
        return Response(serializer.data ,status=status.HTTP_200_OK)

class Change_Password_View(APIView):
    permission_classes=[IsAuthenticated] 
    def post(self,request):
        serializer=Change_Password_Serializer(data=request.data,context={'user':request.user})
        serializer.is_valid(raise_exception=True)
        return Response({'msg':'Password Change Successfully'},status=status.HTTP_200_OK)
       


# class Send_Email_Password_Reset_View(APIView):
#     #permission_classes=[IsAuthenticated]
#     def post(self,request):
#         serializer=Send_Email_For_Password_Reset_Serializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             token=serializer.validated_data['token']
#             uid=serializer.validated_data['uid']
#             # print(token)
#             return Response({'uid':uid,'token':token},status=status.HTTP_200_OK)
#         return Response(serializer.errors,status=status.HTTP_200_OK)
       
# class Password_Reset_View(APIView):
#     def post(self,request,uid,token):
#         serializer=Password_Reset_Serializer(data=request.data,context={'uid':uid,'token':token})
#         if serializer.is_valid(raise_exception=True):
#             return Response({'msg':'Password Change Successfully'},status=status.HTTP_200_OK)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

# class Verify_Account_View(APIView):
    
#     def post(self,request):
#         serializer=Verify_Account_Serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         return Response({
#                 'status':status.HTTP_200_OK,
#                 'message':"Your Account is Verified Now"
#                 },status=status.HTTP_200_OK)
   
     