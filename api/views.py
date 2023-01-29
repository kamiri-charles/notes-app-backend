from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Note, User
from .serializers import NoteSerializer, UserSerializer
from django.contrib.auth import login, logout, authenticate

# Create your views here.
@api_view(['GET'])
def info(req):
    api_urls = {
        'Notes ': '/api/notes/',
        'Detail': '/api/notes/<str:pk>/',
        'Create': '/api/create-note/',
        'Update': '/api/notes/update/<str:pk>/',
        'Delete': '/api/notes/delete/<str:pk>/',
        'User Create': '/api/user/new/',
        'User Update': '/api/users/update/<str:pk>/',
        'User Delete': '/api/users/delete/<str:pk>/',
    }
    return Response(api_urls)


@api_view(['GET'])
def notes(req, username):
    notes = Note.objects.filter(owner__username=username)
    serializer = NoteSerializer(notes, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def note_detail(req, pk):
    note = Note.objects.get(id=pk)
    serializer = NoteSerializer(note, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def note_create(req):
    serializer = NoteSerializer(data=req.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
def note_update(req, pk):
	note = Note.objects.get(id=pk)
	serializer = NoteSerializer(instance=note, data=req.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['DELETE'])
def note_delete(req, pk):
	note = Note.objects.get(id=pk)
	note.delete()

	return Response('Note deleted')


@api_view(['GET'])
def user(req):
    user = req.user

    if user.is_anonymous:
        return Response({'err': 'User is not authenticated'})
    
    else:
        serializer = UserSerializer(user, many=False)
        return Response(serializer.data)



@api_view(['POST'])
def user_create(req):
	serializer = UserSerializer(data=req.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['UPDATE'])
def user_update(req, username):
	user = User.objects.get(username=username)
	serializer = UserSerializer(instance=user, data=req.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['DELETE'])
def user_delete(req, username):
	user = User.objects.get(username=username)
	user.delete()

	return Response('User deleted')



# Sign in user
@api_view(['POST'])
def user_sign_in(req):
    username = req.data['username']
    password = req.data['password']

    user = authenticate(req, username=username, password=password)

    if user is not None:
        login(req, user)
        return Response({'signed_in': True})

    else:
        return Response({'err': 'The username or password entered is incorrect.\nThe username and password are case sensitive.'})


# Sign out user
@api_view(['GET'])
def user_sign_out(req):
    logout(req)
    return Response({'status': 'success'})