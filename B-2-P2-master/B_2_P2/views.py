from django.shortcuts import render, redirect
from questions.models import Question, QuestionComment
from users.models import Profile
from questions.forms import QuestionForm, QuestionUpdateForm, QuestionCommentForm, QuestionCommentEditForm, ReplyCommentForm
from django.http import HttpResponse
from django.http import JsonResponse
from django.contrib.auth.models import User
from itertools import chain
from communities.models import Community

from django.urls import reverse
import json
from django.db.models import Q

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required

@login_required(login_url='/accounts/login')
def main_list(request):
    user = request.user
    if request.method =="POST":
        form = QuestionForm(request.POST, request.FILES)
        if form.is_valid():
            question = form.save(commit=False)
            question.user = user
            question.save()

            form.save_m2m()

            return redirect('questions_detail', pk=question.pk, slug=question.slug)
    else:
        form = QuestionForm()

    neighbors = Profile.objects.filter(
        neighbors=request.user
    )

    questions = []

    for i in neighbors:
        target_user = User.objects.get(profile=i)
        questions.append(Question.objects.filter(user=target_user))
    
    questions.append(Question.objects.filter(user=request.user))

    result_questions = sorted(chain(*questions), key=lambda instance: instance.created_on, reverse=True)

    # questions = Question.objects.all().order_by("-created_on")
    questions = result_questions
    page = request.GET.get('page', 1)
    paginator = Paginator(questions, per_page=9)

    try:
        questions = paginator.page(page)
    except PageNotAnInteger:
        questions = paginator.page(1)
    except EmptyPage:
        questions = paginator.page(paginator.num_pages)

    top_questions = Question.objects.all().order_by("-viewed", "-thumbsup")
    top_communities = Community.objects.all().order_by("-member")

    context = {
        "top_questions": top_questions[:5], 
        "top_communities": top_communities[:5], 
        "questions": questions, 
        'form': form, 
    }
    return render(request, "main_list.html", context=context)