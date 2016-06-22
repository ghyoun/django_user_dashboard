from django.shortcuts import render, HttpResponse, redirect
from .models import User, Message, Comment
# Create your views here.
def remove(request, id):
    User.userManager.get(id=id).delete()
    return redirect('/dashboard/admin')

def edit(request):
    return render(request, 'edit.html')

def editAdmin(request, id):
    context = {
        'user_id' : id
    }
    return render(request, 'editAdmin.html', context)

def editInfo(request):
    user_id = request.session['id']
    user = User.objects.get(id=user_id)
    user.email = request.POST['email']
    user.first_name = request.POST['first_name']
    user.last_name = request.POST['last_name']
    user.save()
    return redirect('/dashboard')

def editPassword(request):
    user_id = request.session['id']
    if (not User.userManager.updatePassword(request.POST['password'], request.POST['password_confirmation'], user_id)):
        return redirect('/dashboard')
    else:
        return HttpResponse('errors')

def editDescription(request):
    user_id = request.session['id']
    user = User.objects.get(id=user_id)
    user.description = request.POST['description']
    user.save()
    return redirect('/dashboard')

def new_user(request):
    return render(request, 'new_user.html')

def specificEditInfo(request, id):
    user = User.objects.get(id=id)
    user.email = request.POST['email']
    user.first_name = request.POST['first_name']
    user.last_name = request.POST['last_name']
    user.user_level = request.POST['user_level']
    user.save()
    return redirect('/dashboard/admin')

def specificEditPassword(request, id):
    if (not User.userManager.updatePassword(request.POST['password'], request.POST['password_confirmation'], id)):
        return redirect('/dashboard/admin')
    else:
        return HttpResponse('errors')

def profile(request, id):
    user = User.objects.get(id=id)
    try:
        messages = Message.objects.filter(user_id=user)
        comments = Comment.objects.all()
    except:
        messages = None
    context = {
        'user' : user,
        'messages' : messages,
        'comments' : comments
    }
    return render(request, 'show.html', context)

def post_message(request, id):
    Message.messageManager.addUser(request.POST['message'], id, request.session['id'])
    return redirect('/dashboard')

def post_comment(request, id, id2):
    Comment.commentManager.addComment(request.POST['comment'], id, id2)
    return redirect('/dashboard')
