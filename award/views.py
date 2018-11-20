from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .forms import NewProjectForm,VoteForm,ProfileForm
from .models import Project,Vote,Profile
from django.contrib.auth.models import User
from django.db.models import Avg
import numpy
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import ProjectSerializer,ProfileSerializer
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    if User.objects.filter(username = request.user.username).exists():
        if not Profile.objects.filter(user = request.user).exists():
            return redirect('edit_profile', username=request.user.username)    
    projects = Project.objects.all()
    return render(request,"index.html",{"projects":projects})

@login_required
def submit_project(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewProjectForm(request.POST,request.FILES)
        if form.is_valid():
            title = form.cleaned_data['title']
            image = request.FILES['image']
            url = form.cleaned_data['url']
            description = form.cleaned_data['description']
            project = Project(title = title, image = image, url = url, description = description, user = current_user)
            project.save()
        return redirect('index')
    else:
        form = NewProjectForm()
    return render(request,"submit_project.html",{"form":form})

def project(request,id):
    current_user = request.user
    project = Project.objects.get(pk=id)
    votes = Vote.objects.filter(project=project)
    profile = Profile.objects.get(user=request.user)
    vote_average = Vote.objects.filter(project=project).aggregate(Avg('design'),Avg('usability'),Avg('content'))
    try:
        total_vote_average = round(numpy.mean([vote_average['design__avg'],vote_average['usability__avg'],vote_average['content__avg']]),2)
    except:
        total_vote_average = 0
    if request.method == 'POST':
        form = VoteForm(request.POST)
        if form.is_valid():
            design = form.cleaned_data['design']
            usability = form.cleaned_data['usability']
            content = form.cleaned_data['content']
            vote = Vote(project=project, design = design,usability=usability,content=content,profile=profile)
            vote.save()
            return redirect('project',project.id)
    else:
        form = VoteForm()
    return render(request,'project.html',{"project":project,"form":form,"votes":votes,"vote_average":total_vote_average})

def profile(request,username):
    current_user = request.user
    user = User.objects.get(username=username)
    profile = Profile.objects.get(user=user)
    projects = Project.objects.filter(profile=profile)
    return render(request,'profile.html',{"profile":profile,"projects":projects})

def search(request):
    current_user = request.user
    if 'search' in request.GET and request.GET["search"]:
        search_term = request.GET.get("search")
        projects = Project.objects.filter(title__icontains=search_term)

    return render(request,'search.html',{"projects":projects})

class ProjectList(APIView):
    def get(self, request, format=None):
        all_projects = Project.objects.all()
        serializers = ProjectSerializer(all_projects, many=True)
        return Response(serializers.data)

class ProfileList(APIView):
    def get(self, request, format=None):
        all_profiles = Profile.objects.all()
        serializers = ProfileSerializer(all_profiles, many=True)
        return Response(serializers.data)

def edit_profile(request,username):
    current_user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            bio = form.save(commit=False)
            bio.user = current_user
            bio.save()
        return redirect('profile',username=current_user.username)
    elif Profile.objects.filter(user=current_user).exists():
        profile = Profile.objects.get(user=current_user)
        form = ProfileForm(instance=profile)
    else:
        form = ProfileForm()

    return render(request,'edit_profile.html',{"form":form})
