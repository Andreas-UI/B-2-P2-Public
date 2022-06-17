from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Profile
from questions.models import Question, QuestionComment
from .forms import ProfileAboutUpdateForm, ProfileImageUpdateForm, UserUpdateForm
from questions.forms import QuestionForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/accounts/login')
def users_detail(request, pk, username):
    user = User.objects.get(username=username)
    profile = Profile.objects.get(pk=pk, user=user)

    questions = Question.objects.filter(user=user).order_by("-created_on")

    if request.method =="POST":
        questionForm = QuestionForm(request.POST, request.FILES)
        aboutForm = ProfileAboutUpdateForm(request.POST, instance = profile)
        imageForm = ProfileImageUpdateForm(request.POST, request.FILES, instance = profile)
        uForm = UserUpdateForm(request.POST, instance = request.user)

        if "_user" in request.POST:
            if uForm.is_valid():
                print("user")
                uForm.save()

                newUser = User.objects.get(pk=pk)
                profile = Profile.objects.get(pk=pk, user=newUser)
                return redirect('users_detail', pk=pk, username=profile.user.username)

        if "_about" in request.POST:
            if aboutForm.is_valid():
                print("about")
                aboutForm.save()

                return redirect('users_detail', pk=pk, username=username)

        if "_image" in request.POST:
            if imageForm.is_valid():
                print("image")
                imageForm.save()

                return redirect('users_detail', pk=pk, username=username)

        if "_question" in request.POST:
            if questionForm.is_valid():
                print("question")
                question = questionForm.save(commit=False)
                question.user = request.user
                question.save()

                questionForm.save_m2m()

                return redirect('questions_detail', pk=question.pk, slug=question.slug)
        
        print("image valid")

    else:
        imageForm = ProfileImageUpdateForm(instance = profile)
        aboutForm = ProfileAboutUpdateForm(instance = profile)
        uForm = UserUpdateForm(instance = request.user)
        questionForm = QuestionForm()


    context = {
        "profile": profile, 
        "questions": questions,
        "aboutForm": aboutForm,
        "imageForm": imageForm,
        "uForm": uForm,
        "questionForm": questionForm,
    }
    return render(request, "users_detail.html", context=context)

@login_required(login_url='/accounts/login')
def users_detail_reverse(request, pk, username):
    user = User.objects.get(username=username)
    profile = Profile.objects.get(pk=pk, user=user)

    questions = Question.objects.filter(user=user).order_by("created_on")

    if request.method =="POST":
        questionForm = QuestionForm(request.POST, request.FILES)
        aboutForm = ProfileAboutUpdateForm(request.POST, instance = profile)
        imageForm = ProfileImageUpdateForm(request.POST, request.FILES, instance = profile)
        uForm = UserUpdateForm(request.POST, instance = request.user)

        if "_user" in request.POST:
            if uForm.is_valid():
                print("user")
                uForm.save()
                return redirect('users_detail', pk=pk, username=username)

        if "_about" in request.POST:
            if aboutForm.is_valid():
                print("about")
                aboutForm.save()

                return redirect('users_detail', pk=pk, username=username)

        if "_image" in request.POST:
            if imageForm.is_valid():
                print("image")
                imageForm.save()

                return redirect('users_detail', pk=pk, username=username)

        if "_question" in request.POST:
            if questionForm.is_valid():
                print("question")
                question = questionForm.save(commit=False)
                question.user = request.user
                question.save()

                questionForm.save_m2m()

                return redirect('questions_detail', pk=question.pk, slug=question.slug)
        
        print("image valid")

    else:
        imageForm = ProfileImageUpdateForm(instance = profile)
        aboutForm = ProfileAboutUpdateForm(instance = profile)
        questionForm = QuestionForm()
        uForm = UserUpdateForm(instance = request.user)

    context = {
        "profile": profile, 
        "questions": questions,
        "aboutForm": aboutForm,
        "imageForm": imageForm,
        "questionForm": questionForm,
        "uForm": uForm,
    }
    return render(request, "users_detail.html", context=context)

@login_required(login_url='/accounts/login')
def users_detail_solved(request, pk, username):
    user = User.objects.get(username=username)
    profile = Profile.objects.get(pk=pk, user=user)

    questions = Question.objects.filter(user=user, solved=True).order_by("-created_on")

    if request.method =="POST":
        questionForm = QuestionForm(request.POST, request.FILES)
        aboutForm = ProfileAboutUpdateForm(request.POST, instance = profile)
        imageForm = ProfileImageUpdateForm(request.POST, request.FILES, instance = profile)
        uForm = UserUpdateForm(request.POST, instance = request.user)

        if "_user" in request.POST:
            if uForm.is_valid():
                print("user")
                uForm.save()
                return redirect('users_detail', pk=pk, username=username)

        if "_about" in request.POST:
            if aboutForm.is_valid():
                print("about")
                aboutForm.save()

                return redirect('users_detail', pk=pk, username=username)

        if "_image" in request.POST:
            if imageForm.is_valid():
                print("image")
                imageForm.save()

                return redirect('users_detail', pk=pk, username=username)

        if "_question" in request.POST:
            if questionForm.is_valid():
                print("question")
                question = questionForm.save(commit=False)
                question.user = request.user
                question.save()

                questionForm.save_m2m()

                return redirect('questions_detail', pk=question.pk, slug=question.slug)
        
        print("image valid")

    else:
        imageForm = ProfileImageUpdateForm(instance = profile)
        aboutForm = ProfileAboutUpdateForm(instance = profile)
        questionForm = QuestionForm()
        uForm = UserUpdateForm(instance = request.user)

    context = {
        "profile": profile, 
        "questions": questions,
        "aboutForm": aboutForm,
        "imageForm": imageForm,
        "uForm": uForm,
        "questionForm": questionForm,
    }
    return render(request, "users_detail.html", context=context)

@login_required(login_url='/accounts/login')
def users_detail_unsolved(request, pk, username):
    user = User.objects.get(username=username)
    profile = Profile.objects.get(pk=pk, user=user)

    questions = Question.objects.filter(user=user, solved=False).order_by("-created_on")

    if request.method =="POST":
        questionForm = QuestionForm(request.POST, request.FILES)
        aboutForm = ProfileAboutUpdateForm(request.POST, instance = profile)
        imageForm = ProfileImageUpdateForm(request.POST, request.FILES, instance = profile)
        uForm = UserUpdateForm(request.POST, instance = request.user)

        if "_user" in request.POST:
            if uForm.is_valid():
                print("user")
                uForm.save()
                return redirect('users_detail', pk=pk, username=username)

        if "_about" in request.POST:
            if aboutForm.is_valid():
                print("about")
                aboutForm.save()

                return redirect('users_detail', pk=pk, username=username)

        if "_image" in request.POST:
            if imageForm.is_valid():
                print("image")
                imageForm.save()

                return redirect('users_detail', pk=pk, username=username)

        if "_question" in request.POST:
            if questionForm.is_valid():
                print("question")
                question = questionForm.save(commit=False)
                question.user = request.user
                question.save()

                questionForm.save_m2m()

                return redirect('questions_detail', pk=question.pk, slug=question.slug)
        
        print("image valid")

    else:
        imageForm = ProfileImageUpdateForm(instance = profile)
        aboutForm = ProfileAboutUpdateForm(instance = profile)
        questionForm = QuestionForm()
        uForm = UserUpdateForm(instance = request.user)

    context = {
        "profile": profile, 
        "questions": questions,
        "aboutForm": aboutForm,
        "imageForm": imageForm,
        "uForm": uForm,
        "questionForm": questionForm,
    }
    return render(request, "users_detail.html", context=context)

@login_required(login_url='/accounts/login')
def users_detail_connect(request, pk, username):
    user = request.user
    if request.method == 'POST':
        target_user = User.objects.get(username=username)
        target_object = Profile.objects.get(user=target_user)

        if user in target_object.neighbors.all():
            target_object.neighbors.remove(user)
            target_object.save()
            print("removed")

        else:
            target_object.neighbors.add(user)
            target_object.save()
            print("add")

    return redirect('users_detail', pk=pk, username=username)

@login_required(login_url='/accounts/login')
def users_detail_answers(request, pk, username):
    user = User.objects.get(username=username)
    profile = Profile.objects.get(pk=pk, user=user)

    if request.method =="POST":
        questionForm = QuestionForm(request.POST, request.FILES)
        aboutForm = ProfileAboutUpdateForm(request.POST, instance = profile)
        imageForm = ProfileImageUpdateForm(request.POST, request.FILES, instance = profile)
        uForm = UserUpdateForm(request.POST, instance = request.user)

        if "_user" in request.POST:
            if uForm.is_valid():
                print("user")
                uForm.save()
                return redirect('users_detail', pk=pk, username=username)

        if "_about" in request.POST:
            if aboutForm.is_valid():
                print("about")
                aboutForm.save()

                return redirect('users_detail_answers', pk=pk, username=username)

        if "_image" in request.POST:
            if imageForm.is_valid():
                print("image")
                imageForm.save()

                return redirect('users_detail_answers', pk=pk, username=username)

        if "_question" in request.POST:
            if questionForm.is_valid():
                print("question")
                question = questionForm.save(commit=False)
                question.user = request.user
                question.save()

                questionForm.save_m2m()

                return redirect('questions_detail', pk=question.pk, slug=question.slug)
        
        print("image valid")

    else:
        imageForm = ProfileImageUpdateForm(instance = profile)
        aboutForm = ProfileAboutUpdateForm(instance = profile)
        questionForm = QuestionForm()
        uForm = UserUpdateForm(instance = request.user)

    comments = QuestionComment.objects.filter(user=user).order_by("-created_on")

    context = {
        "profile": profile, 
        "comments": comments,
        "aboutForm": aboutForm,
        "imageForm": imageForm,
        "uForm": uForm,
        "questionForm": questionForm,
    }
    return render(request, "users_detail_answers.html", context=context)

@login_required(login_url='/accounts/login')
def users_detail_answers_reverse(request, pk, username):
    user = User.objects.get(username=username)
    profile = Profile.objects.get(pk=pk, user=user)

    if request.method =="POST":
        questionForm = QuestionForm(request.POST, request.FILES)
        aboutForm = ProfileAboutUpdateForm(request.POST, instance = profile)
        imageForm = ProfileImageUpdateForm(request.POST, request.FILES, instance = profile)
        uForm = UserUpdateForm(request.POST, instance = request.user)

        if "_user" in request.POST:
            if uForm.is_valid():
                print("user")
                uForm.save()
                return redirect('users_detail', pk=pk, username=username)

        if "_about" in request.POST:
            if aboutForm.is_valid():
                print("about")
                aboutForm.save()

                return redirect('users_detail_answers', pk=pk, username=username)

        if "_image" in request.POST:
            if imageForm.is_valid():
                print("image")
                imageForm.save()

                return redirect('users_detail_answers', pk=pk, username=username)

        if "_question" in request.POST:
            if questionForm.is_valid():
                print("question")
                question = questionForm.save(commit=False)
                question.user = request.user
                question.save()

                questionForm.save_m2m()

                return redirect('questions_detail', pk=question.pk, slug=question.slug)
        
        print("image valid")

    else:
        imageForm = ProfileImageUpdateForm(instance = profile)
        aboutForm = ProfileAboutUpdateForm(instance = profile)
        questionForm = QuestionForm()
        uForm = UserUpdateForm(instance = request.user)

    comments = QuestionComment.objects.filter(user=user).order_by("created_on")

    context = {
        "profile": profile, 
        "comments": comments,
        "aboutForm": aboutForm,
        "imageForm": imageForm,
        "uForm": uForm,
        "questionForm": questionForm,
    }
    return render(request, "users_detail_answers.html", context=context)

@login_required(login_url='/accounts/login')
def users_detail_answers_pinned(request, pk, username):
    user = User.objects.get(username=username)
    profile = Profile.objects.get(pk=pk, user=user)

    if request.method =="POST":
        questionForm = QuestionForm(request.POST, request.FILES)
        aboutForm = ProfileAboutUpdateForm(request.POST, instance = profile)
        imageForm = ProfileImageUpdateForm(request.POST, request.FILES, instance = profile)
        uForm = UserUpdateForm(request.POST, instance = request.user)

        if "_user" in request.POST:
            if uForm.is_valid():
                print("user")
                uForm.save()
                return redirect('users_detail', pk=pk, username=username)

        if "_about" in request.POST:
            if aboutForm.is_valid():
                print("about")
                aboutForm.save()

                return redirect('users_detail_answers', pk=pk, username=username)

        if "_image" in request.POST:
            if imageForm.is_valid():
                print("image")
                imageForm.save()

                return redirect('users_detail_answers', pk=pk, username=username)

        if "_question" in request.POST:
            if questionForm.is_valid():
                print("question")
                question = questionForm.save(commit=False)
                question.user = request.user
                question.save()

                questionForm.save_m2m()

                return redirect('questions_detail', pk=question.pk, slug=question.slug)
        
        print("image valid")

    else:
        imageForm = ProfileImageUpdateForm(instance = profile)
        aboutForm = ProfileAboutUpdateForm(instance = profile)
        questionForm = QuestionForm()
        uForm = UserUpdateForm(instance = request.user)

    comments = QuestionComment.objects.filter(user=user, pinned=True).order_by("-created_on")

    context = {
        "profile": profile, 
        "comments": comments,
        "aboutForm": aboutForm,
        "imageForm": imageForm,
        "uForm": uForm,
        "questionForm": questionForm,
    }
    return render(request, "users_detail_answers.html", context=context)

@login_required(login_url='/accounts/login')
def users_detail_answers_unpinned(request, pk, username):
    user = User.objects.get(username=username)
    profile = Profile.objects.get(pk=pk, user=user)

    if request.method =="POST":
        questionForm = QuestionForm(request.POST, request.FILES)
        aboutForm = ProfileAboutUpdateForm(request.POST, instance = profile)
        imageForm = ProfileImageUpdateForm(request.POST, request.FILES, instance = profile)
        uForm = UserUpdateForm(request.POST, instance = request.user)

        if "_user" in request.POST:
            if uForm.is_valid():
                print("user")
                uForm.save()
                return redirect('users_detail', pk=pk, username=username)

        if "_about" in request.POST:
            if aboutForm.is_valid():
                print("about")
                aboutForm.save()

                return redirect('users_detail_answers', pk=pk, username=username)

        if "_image" in request.POST:
            if imageForm.is_valid():
                print("image")
                imageForm.save()

                return redirect('users_detail_answers', pk=pk, username=username)

        if "_question" in request.POST:
            if questionForm.is_valid():
                print("question")
                question = questionForm.save(commit=False)
                question.user = request.user
                question.save()

                questionForm.save_m2m()

                return redirect('questions_detail', pk=question.pk, slug=question.slug)
        
        print("image valid")

    else:
        imageForm = ProfileImageUpdateForm(instance = profile)
        aboutForm = ProfileAboutUpdateForm(instance = profile)
        questionForm = QuestionForm()
        uForm = UserUpdateForm(instance = request.user)

    comments = QuestionComment.objects.filter(user=user, pinned=False).order_by("-created_on")

    context = {
        "profile": profile, 
        "comments": comments,
        "aboutForm": aboutForm,
        "imageForm": imageForm,
        "uForm": uForm,
        "questionForm": questionForm,
    }
    return render(request, "users_detail_answers.html", context=context)

@login_required(login_url='/accounts/login')
def users_detail_bookmark(request):
    user = request.user
    questions = Question.objects.filter(bookmark=user)

    context = {
        "questions": questions,
    }
    return render(request, "users_detail_bookmark.html", context=context)

@login_required(login_url='/accounts/login')
def users_detail_follower(request, pk, username):
    user = User.objects.get(username=username)
    profile = Profile.objects.get(user=user)
    follower = profile.neighbors.all

    if request.method =="POST":
        questionForm = QuestionForm(request.POST, request.FILES)
        aboutForm = ProfileAboutUpdateForm(request.POST, instance = profile)
        imageForm = ProfileImageUpdateForm(request.POST, request.FILES, instance = profile)
        uForm = UserUpdateForm(request.POST, instance = request.user)

        if "_user" in request.POST:
            if uForm.is_valid():
                print("user")
                uForm.save()
                return redirect('users_detail', pk=pk, username=username)

        if "_about" in request.POST:
            if aboutForm.is_valid():
                print("about")
                aboutForm.save()

                return redirect('users_detail', pk=pk, username=username)

        if "_image" in request.POST:
            if imageForm.is_valid():
                print("image")
                imageForm.save()

                return redirect('users_detail', pk=pk, username=username)

        if "_question" in request.POST:
            if questionForm.is_valid():
                print("question")
                question = questionForm.save(commit=False)
                question.user = request.user
                question.save()

                questionForm.save_m2m()

                return redirect('questions_detail', pk=question.pk, slug=question.slug)

    else:
        imageForm = ProfileImageUpdateForm(instance = profile)
        aboutForm = ProfileAboutUpdateForm(instance = profile)
        questionForm = QuestionForm()
        uForm = UserUpdateForm(instance = request.user)

    context = {
        "profile": profile, 
        "follower": follower,
        "aboutForm": aboutForm,
        "imageForm": imageForm,
        "uForm": uForm,
        "questionForm": questionForm,
    }

    return render(request, "users_detail_neighbors_follower.html", context=context)

@login_required(login_url='/accounts/login')
def users_detail_following(request, pk, username):
    user = User.objects.get(username=username)
    profile = Profile.objects.get(user=user)
    following = profile.user.neighbors.all

    if request.method =="POST":
        questionForm = QuestionForm(request.POST, request.FILES)
        aboutForm = ProfileAboutUpdateForm(request.POST, instance = profile)
        imageForm = ProfileImageUpdateForm(request.POST, request.FILES, instance = profile)
        uForm = UserUpdateForm(request.POST, instance = request.user)

        if "_user" in request.POST:
            if uForm.is_valid():
                print("user")
                uForm.save()
                return redirect('users_detail', pk=pk, username=username)

        if "_about" in request.POST:
            if aboutForm.is_valid():
                print("about")
                aboutForm.save()

                return redirect('users_detail', pk=pk, username=username)

        if "_image" in request.POST:
            if imageForm.is_valid():
                print("image")
                imageForm.save()

                return redirect('users_detail', pk=pk, username=username)

        if "_question" in request.POST:
            if questionForm.is_valid():
                print("question")
                question = questionForm.save(commit=False)
                question.user = request.user
                question.save()

                questionForm.save_m2m()

                return redirect('questions_detail', pk=question.pk, slug=question.slug)

    else:
        imageForm = ProfileImageUpdateForm(instance = profile)
        aboutForm = ProfileAboutUpdateForm(instance = profile)
        questionForm = QuestionForm()
        uForm = UserUpdateForm(instance = request.user)

    context = {
        "profile": profile, 
        "following": following,
        "aboutForm": aboutForm,
        "imageForm": imageForm,
        "uForm": uForm,
        "questionForm": questionForm,
    }

    return render(request, "users_detail_neighbors_following.html", context=context)

@login_required(login_url='/accounts/login')
def users_update(request):
    user = request.user
    profile = Profile.objects.get(user=user)

    if request.method =="POST":
        uForm = UserUpdateForm(request.POST, instance = request.user)
        if uForm.is_valid():
            print("user")
            uForm.save()

            newUser = User.objects.get(pk=user.pk)
            profile = Profile.objects.get(pk=user.pk, user=newUser)
            return redirect('users_detail', pk=user.pk, username=profile.user.username)

    else:
        uForm = UserUpdateForm(instance = request.user)

    context = {
        "uForm": uForm,
    }

    return render(request, "users_update.html", context=context)

from django.contrib.auth import logout
@login_required(login_url='/accounts/login')
def logout_request(request):
    logout(request)

    return redirect("/questions")