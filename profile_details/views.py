from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from profile_details.models import UserProfile

# Create your views here.


@api_view(['POST'])
def add_userprofile(request):
    name=request.POST.get('name',None)
    email=request.POST.get('email',None)
    phone_number=request.POST.get('phone_number',None)
    dob=request.POST.get('dob',None)
    location=request.POST.get('location',None)
    if name is None or email is None or phone_number is None or dob is None or location is None:
        context={
            'message':'name/email/phone_number/dob/location is missing'
        }
        return Response(context,status=status.HTTP_400_BAD_REQUEST)
    else:
        try:
            new_record=UserProfile.objects.create(
                name=name,
                email=email,
                phone_number=phone_number,
                dob=dob,
                location=location
            )
            new_record.save()
            context={
                'message':'successfully added the UserProfile',
                'data':{
                    'name':new_record.name,
                    'email':new_record.email,
                    'phone_number':new_record.phone_number,
                    'dob':new_record.dob,
                    'location':new_record.location
                }
            }
            return Response(context,status=status.HTTP_200_OK)
        except ValueError:
            context={
                'message':'invalid name'
            }
            return Response(context,status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def list_userprofile(request):
    all_userprofile=UserProfile.objects.all()
    data=[]
    for userprofile in all_userprofile:
        temp={
            'userprofile_id':userprofile.id,
            'name':userprofile.name,
            'email':userprofile.email,
            'phone_number':userprofile.email,
            'dob':userprofile.dob,
            'loaction':userprofile.location
        }
        data.append(temp)
        context={
            'data':data
        }
        return Response(context,status=status.HTTP_200_OK)