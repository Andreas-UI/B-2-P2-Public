from django.shortcuts import render, redirect
from .models import Question, QuestionComment
from .forms import QuestionForm, QuestionUpdateForm, QuestionCommentForm, QuestionCommentEditForm, ReplyCommentForm
from django.http import HttpResponse
from django.http import JsonResponse

from django.urls import reverse
import json
from django.db.models import Q

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required

from taggit.models import TaggedItem

# Create your views here.
@login_required(login_url='/accounts/login')
def questions_tag(request, tag):
    questions = Question.objects.all().filter(tags__name=tag).order_by("-created_on")

    page = request.GET.get('page', 1)
    paginator = Paginator(questions, per_page=10)

    try:
        questions = paginator.page(page)
    except PageNotAnInteger:
        questions = paginator.page(1)
    except EmptyPage:
        questions = paginator.page(paginator.num_pages)

    context = {
        "questions": questions, 
        "tag": tag, 
    }
    return render(request, "questions_tag.html", context=context)

@login_required(login_url='/accounts/login')
def questions_category(request, category):
    questions = Question.objects.all().filter(category=category).order_by("-created_on")

    page = request.GET.get('page', 1)
    paginator = Paginator(questions, per_page=10)

    try:
        questions = paginator.page(page)
    except PageNotAnInteger:
        questions = paginator.page(1)
    except EmptyPage:
        questions = paginator.page(paginator.num_pages)

    category =questions[0].get_category_display()

    context = {
        "questions": questions, 
        "category": category,

    }
    return render(request, "questions_category.html", context=context)

@login_required(login_url='/accounts/login')
def questions_list(request):
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

    questions = Question.objects.all().order_by("-created_on")
    page = request.GET.get('page', 1)
    paginator = Paginator(questions, per_page=9)

    try:
        questions = paginator.page(page)
    except PageNotAnInteger:
        questions = paginator.page(1)
    except EmptyPage:
        questions = paginator.page(paginator.num_pages)

    top_questions = Question.objects.all().order_by("-viewed", "-thumbsup")

    context = {
        "questions": questions, 
        "top_questions": top_questions[:10], 
        'form': form, 
    }
    return render(request, "questions_list.html", context=context)

@login_required(login_url='/accounts/login')
def questions_search(request):
    if request.is_ajax() and request.method == "GET":
        searchText = request.GET.get('searchText')
        questions = Question.objects.filter((Q(title__icontains=searchText))).distinct().order_by("-created_on")

        res = None

        if (len(questions) > 0) and len(searchText) > 0 :
            data = []
            for question in questions:
                item = {
                    'title': question.title, 
                    'date': question.created_on.strftime('%m/%d/%Y'), 
                    'author': question.user.username, 
                    'image': question.user.profile.image.url, 
                    'url': reverse("questions_detail", kwargs={"pk":question.pk, "slug":question.slug}), 
                }

                data.append(item)

            res = data
        else:
            res = "Create or search question"

        return JsonResponse({'questions': res})
    return JsonResponse({})

@login_required(login_url='/accounts/login')
def questions_ask(request):
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

    context = {
        'form': form, 
    }

    return render(request, 'questions_ask.html', context=context)

def questions_detail(request, pk, slug):
    user = request.user
    item = Question.objects.get(pk=pk, slug=slug)

    if user.is_authenticated:
        if user in item.viewed.all():
            pass
        else:
            item.viewed.add(user)

        # Handling the comment
        if request.method == "POST":
            formComment = QuestionCommentForm(request.POST, request.FILES)
            formQuestion = QuestionForm(request.POST, request.FILES)
            formReply = ReplyCommentForm(request.POST)

            if '_comment' in request.POST:
                if formComment.is_valid():
                    comment = formComment.save(commit=False)
                    comment.user = user
                    comment.question = item
                    comment.save()

                    return redirect('questions_detail', pk=item.pk, slug=item.slug)

            if '_reply' in request.POST:
                if formReply.is_valid():
                    comment_id = int(request.POST.get('comment_id'))
                    comment = QuestionComment.objects.get(pk=comment_id)
                    reply = formReply.save(commit=False)
                    reply.user = user
                    reply.comment = comment
                    reply.save()

                    return redirect('questions_detail', pk=item.pk, slug=item.slug)

            if '_question' in request.POST:
                if formQuestion.is_valid():
                    question = formQuestion.save(commit=False)
                    question.user = user
                    question.save()

                    formQuestion.save_m2m()

                    return redirect('questions_detail', pk=question.pk, slug=question.slug)
        
        else:
            formComment = QuestionCommentForm()
            formQuestion = QuestionForm()
            formReply = ReplyCommentForm()


    comments = QuestionComment.objects.filter(question=item).order_by("-pinned", "-created_on")
    solved = any([i.pinned for i in comments])

    if solved:
        item.solved = solved
    else:
        item.solved = solved

    item.save()

    related_category = Question.objects.filter(category=item.category)
    related_items = TaggedItem.objects.none()
    for tag in item.tags.all():
        #build queryset of all TaggedItems
        related_items |= tag.taggit_taggeditem_items.all()

    #TaggedItem doesn't have a direct link to the object, have to grab ids
    ids = related_items.values_list('object_id', flat=True)
    related_questions =  Question.objects.filter(id__in=ids, category=item.category).exclude(id=item.id).order_by('-created_on')[:5]


    if user.is_authenticated:
        context = {
            "item": item, 
            "formComment": formComment, 
            "formQuestion": formQuestion, 
            "formReply": formReply, 
            "comments": comments, 
            "related_questions": related_questions, 
        }
    else:
        context = {
            "item": item, 
            "comments": comments, 
            "related_questions": related_questions, 
        }
    return render(request, 'questions_detail.html', context=context)

@login_required(login_url='/accounts/login')
def questions_detail_pin(request, comment_pk, pk, slug):
    if request.method == "POST":
        question = Question.objects.get(pk=pk, slug=slug)
        comment = QuestionComment.objects.get(pk=comment_pk)

        if comment.pinned:
            comment.pinned = False
        else:
            comment.pinned = True

        comment.save()        


        return redirect('questions_detail', pk=pk, slug=slug)
    
    return redirect('questions_detail', pk=pk, slug=slug)
    
@login_required(login_url='/accounts/login')
def questions_detail_bookmark(request, pk, slug):
    user = request.user
    if request.method == "POST":
        question = Question.objects.get(pk=pk, slug=slug)

        if user in question.bookmark.all():
            question.bookmark.remove(user)
        else:
            question.bookmark.add(user)
        
        question.save()

    return redirect('questions_detail', pk=pk, slug=slug)

@login_required(login_url='/accounts/login')
def questions_detail_thumbsup(request, pk, slug):
    user = request.user
    if request.method == "POST":
        question = Question.objects.get(pk=pk, slug=slug)

        code = None

        if user in question.thumbsup.all():
            question.thumbsup.remove(user)
            code = 0
        else:
            if user in question.thumbsdown.all():
                question.thumbsdown.remove(user)
                question.thumbsup.add(user)
                code = 1
            else:
                question.thumbsup.add(user)
                code = 2
        
        question.save()

        thumbsup = question.thumbsup.all().count()
        thumbsdown = question.thumbsdown.all().count()
        
        data = {
            "code": code, 
            "thumbs": thumbsup-thumbsdown, 
            "thumbsup": thumbsup, 
        }
        return HttpResponse(json.dumps(data))

    return redirect('questions_detail', pk=pk, slug=slug)
    
@login_required(login_url='/accounts/login')
def questions_detail_thumbsdown(request, pk, slug):
    user = request.user
    if request.method == "POST":
        question = Question.objects.get(pk=pk, slug=slug)

        code = None

        if user in question.thumbsdown.all():
            question.thumbsdown.remove(user)
            code = 0
        else:
            if user in question.thumbsup.all():
                question.thumbsup.remove(user)
                question.thumbsdown.add(user)
                code = 1
            else:
                question.thumbsdown.add(user)
                code = 2
        
        question.save()

        thumbsup = question.thumbsup.all().count()
        thumbsdown = question.thumbsdown.all().count()
        
        data = {
            "code": code, 
            "thumbs": thumbsup-thumbsdown, 
            "thumbsup": thumbsup, 
        }
        return HttpResponse(json.dumps(data))

    return redirect('questions_detail', pk=pk, slug=slug)

@login_required(login_url='/accounts/login')
def questions_comment_upvote(request, comment_pk, pk, slug):
    user = request.user
    if request.method == "POST":
        question = Question.objects.get(pk=pk, slug=slug)
        comment = QuestionComment.objects.get(pk=comment_pk)

        code = None

        if user in comment.upvote.all():
            comment.upvote.remove(user)
            code = 0
        else:
            if user in comment.downvote.all():
                comment.downvote.remove(user)
                comment.upvote.add(user)
                code = 1
            else:
                comment.upvote.add(user)
                code = 2

        
        comment.save()

        upvote = comment.upvote.all().count()
        downvote = comment.downvote.all().count()
        
        data = {
            "code": code, 
            "upvote": upvote, 
        }
        return HttpResponse(json.dumps(data))
    return redirect('questions_detail', pk=pk, slug=slug)

@login_required(login_url='/accounts/login')
def questions_comment_downvote(request, comment_pk, pk, slug):
    user = request.user
    if request.method == "POST":
        question = Question.objects.get(pk=pk, slug=slug)
        comment = QuestionComment.objects.get(pk=comment_pk)

        code = None

        if user in comment.downvote.all():
            comment.downvote.remove(user)
            code = 0
        else:
            if user in comment.upvote.all():
                comment.upvote.remove(user)
                comment.downvote.add(user)
                code = 1
            else:
                comment.downvote.add(user)
                code = 2
        
        comment.save()

        upvote = comment.upvote.all().count()
        downvote = comment.downvote.all().count()
        
        data = {
            "code": code, 
            "upvote": upvote, 

        }
        
        return HttpResponse(json.dumps(data))
    return redirect('questions_detail', pk=pk, slug=slug)

@login_required(login_url='/accounts/login')
def questions_comment_edit(request, comment_pk, pk, slug):
    comment = QuestionComment.objects.get(pk = comment_pk)
    question = Question.objects.get(pk=pk, slug=slug)

    if request.user != comment.user:
        return redirect('questions_detail', pk=pk, slug=slug)

    if request.method =="POST":
        form = QuestionCommentEditForm(request.POST or None, instance = comment)
        formQuestion = QuestionForm(request.POST, request.FILES)


        if "_comment" in request.POST:
            if form.is_valid():
                edit = form.save(commit=False)
                edit.edited = True
                edit.save()
                return redirect('questions_detail', pk=pk, slug=slug)

        if '_question' in request.POST:
            if formQuestion.is_valid():
                question = formQuestion.save(commit=False)
                question.user = request.user
                question.save()

                formQuestion.save_m2m()

                return redirect('questions_detail', pk=question.pk, slug=question.slug)

    else:
        form = QuestionCommentEditForm(instance = comment)
        formQuestion = QuestionForm()

    context = {
        "question": question, 
        "form": form,
        "formQuestion": formQuestion, 
    }

    return render(request, "questions_edit.html", context=context)

@login_required(login_url='/accounts/login')
def questions_detail_update(request, pk, slug):
    question = Question.objects.get(pk=pk, slug=slug)
    if request.user != question.user:
        return redirect('questions_detail', pk=pk, slug=slug)

    if request.method =="POST":
        form = QuestionUpdateForm(request.POST or None, instance = question)
        formQuestion = QuestionForm(request.POST, request.FILES)

        if "_update" in request.POST:
            if form.is_valid():
                update = form.save(commit=False)
                update.edited = True
                update.save()

                return redirect('questions_detail', pk=pk, slug=slug)

        if '_question' in request.POST:
            if formQuestion.is_valid():
                question = formQuestion.save(commit=False)
                question.user = request.user
                question.save()

                formQuestion.save_m2m()

                return redirect('questions_detail', pk=question.pk, slug=question.slug)

    else:
        form = QuestionUpdateForm(instance = question)
        formQuestion = QuestionForm()

    context = {
        "question": question,
        "form": form,
        "formQuestion": formQuestion, 
    }

    return render(request, "questions_update.html", context=context)

@login_required(login_url='/accounts/login')
def questions_comment_delete(request, comment_pk, pk, slug):
    comment = QuestionComment.objects.get(pk=comment_pk)
    if request.user != comment.user:
        return redirect('questions_detail', pk=pk, slug=slug)

    if request.method == 'POST':
        comment = QuestionComment.objects.get(pk=comment_pk)
        comment.delete()

    return redirect('questions_detail', pk=pk, slug=slug)

@login_required(login_url='/accounts/login')
def questions_delete(request, pk, slug):
    question = Question.objects.get(pk=pk, slug=slug)
    if request.user != question.user:
        return redirect('questions_detail', pk=pk, slug=slug)

    if request.method == 'POST':
        question = Question.objects.get(pk=pk, slug=slug)
        question.delete()

    return redirect('questions_list')



