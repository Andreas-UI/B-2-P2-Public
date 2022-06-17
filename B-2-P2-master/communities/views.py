from django.shortcuts import render, redirect
from .forms import CommunityForm, CommunityDescriptionUpdateForm, CommunityImageUpdateForm
from django.contrib.auth.models import User
from .models import Community
from questions.forms import QuestionForm
from questions.models import Question
from django.urls import reverse
from django.http import JsonResponse
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required


@login_required(login_url='/accounts/login')
def communities_search(request):
    if request.is_ajax() and request.method == "GET":
        searchText = request.GET.get('searchText')
        communities = Community.objects.filter((Q(community_name__icontains=searchText))).distinct().order_by("-created_on")

        res = None

        if (len(communities) > 0) and len(searchText) > 0 :
            data = []
            for community in communities:
                item = {
                    'name': community.community_name, 
                    'admin': community.user.username, 
                    'image': community.image.url, 
                    'url': reverse("communities_detail", kwargs={"pk":community.pk, "slug":community.slug}), 
                    'slug': community.slug,
                    'pk': community.pk,
                    'member': community.member.all().count(), 
                    'category': community.get_category_display(), 
                    'description': community.description,
                }

                data.append(item)

            res = data
        else:
            res = "Not found"

        return JsonResponse({'communities': res})
    return JsonResponse({})

@login_required(login_url='/accounts/login')
def communities_list(request):
    communities = Community.objects.all().order_by("-member")

    page = request.GET.get('page', 1)
    paginator = Paginator(communities, per_page=10)

    try:
        communities = paginator.page(page)
    except PageNotAnInteger:
        communities = paginator.page(1)
    except EmptyPage:
        communities = paginator.page(paginator.num_pages)

    recent_communities = Community.objects.all().order_by("-created_on")

    context = {
        "communities": communities, 
        "recent_communities": recent_communities[:10], 
    }

    return render(request, "communities_list.html", context=context)

@login_required(login_url='/accounts/login')
def communities_create(request):
    admin = request.user
    if request.method == "POST":
        form = CommunityForm(request.POST)
        if form.is_valid():
            community = form.save(commit=False)
            community.user = admin
            community.save()

            return redirect('communities_detail', slug=community.slug, pk=community.pk)

    else:
        form = CommunityForm()

    context = {
        "form": form,
    }

    return render(request, 'communities_create.html', context=context)

@login_required(login_url='/accounts/login')
def communities_ask(request, pk, slug):
    admin = request.user
    community = Community.objects.get(pk=pk)
    if request.method == "POST":
        form = QuestionForm(request.POST, request.FILES)
        if form.is_valid():
            question = form.save(commit=False)
            question.user = admin
            question.community = community
            question.noc = "community"
            question.save()

            form.save_m2m()

            return redirect('questions_detail', pk=question.pk, slug=question.slug)

    else:
        form = QuestionForm()

    context = {
        "form": form,
    }

    return render(request, 'communities_ask.html', context=context)

@login_required(login_url='/accounts/login')
def communities_join(request, pk, slug):
    member = request.user
    community = Community.objects.get(slug=slug, pk=pk)

    if request.method == "POST":
        if member in community.member.all():
            community.member.remove(member)
        else:
            community.member.add(member)

    return redirect('communities_detail', slug=slug, pk=pk)

@login_required(login_url='/accounts/login')
def communities_delete(request, pk, slug):
    community = Community.objects.get(pk=pk, slug=slug)
    if request.user != community.user:
        return redirect('communities_detail', pk=pk, slug=slug)

    if request.method == 'POST':
        community = Community.objects.get(pk=pk, slug=slug)
        community.delete()

    return redirect('communities_list')

@login_required(login_url='/accounts/login')
def communities_detail(request, pk, slug):
    community = Community.objects.get(pk=pk, slug=slug)
    questions = Question.objects.filter(community=community).order_by('-created_on')

    if request.method =="POST":
        descriptionForm = CommunityDescriptionUpdateForm(request.POST, instance = community)
        imageForm = CommunityImageUpdateForm(request.POST, request.FILES, instance = community)

        if "_description" in request.POST:
            if descriptionForm.is_valid():
                descriptionForm.save()

                return redirect('communities_detail', pk=pk, slug=slug)

        if "_image" in request.POST:
            if imageForm.is_valid():
                imageForm.save()

                return redirect('communities_detail', pk=pk, slug=slug)

        
        print("image valid")

    else:
        imageForm = CommunityImageUpdateForm(instance = community)
        descriptionForm = CommunityDescriptionUpdateForm(instance = community)


    context = {
        "community": community,
        'questions': questions, 
        "imageForm": imageForm, 
        "descriptionForm": descriptionForm,
    }
    return render(request, 'communities_detail.html', context=context)

@login_required(login_url='/accounts/login')
def communities_detail_popular(request, pk, slug):
    community = Community.objects.get(pk=pk, slug=slug)
    questions = Question.objects.filter(community=community).order_by('-created_on', '-viewed')

    if request.method =="POST":
        descriptionForm = CommunityDescriptionUpdateForm(request.POST, instance = community)
        imageForm = CommunityImageUpdateForm(request.POST, request.FILES, instance = community)

        if "_description" in request.POST:
            if descriptionForm.is_valid():
                descriptionForm.save()

                return redirect('communities_detail', pk=pk, slug=slug)

        if "_image" in request.POST:
            if imageForm.is_valid():
                imageForm.save()

                return redirect('communities_detail', pk=pk, slug=slug)

        
        print("image valid")

    else:
        imageForm = CommunityImageUpdateForm(instance = community)
        descriptionForm = CommunityDescriptionUpdateForm(instance = community)


    context = {
        "community": community,
        'questions': questions, 
        "imageForm": imageForm, 
        "descriptionForm": descriptionForm,
    }
    return render(request, 'communities_detail.html', context=context)