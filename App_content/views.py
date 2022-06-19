from django.http import HttpResponse
from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth.models import User

# Create your views here.
from App_content.models import PodcastModel, PostsModel, PostLoveReact, SyllabusModel, ConnectionRequestModel


def new_podcast(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        cover_image = request.FILES.get('cover_image')
        audio_file = request.FILES.get('audio_file')
        description = request.POST.get('description')
        audio_model = PodcastModel(host=request.user, title=title, description=description, cover_image=cover_image,
                                   audio_file=audio_file)
        audio_model.save()
        return HttpResponseRedirect(reverse('App_post:home'))
    return render(request, 'App_content/add_podcast.html')


def podcast_listview(request):
    pod_list = PodcastModel.objects.filter(status=True)
    content = {
        'pod_list': pod_list,
    }
    return render(request, 'App_content/podcast_listview.html', context=content)


def new_post(request):
    if request.method == 'POST':
        post = request.POST.get('title')
        image1 = request.FILES.get('post_image1')
        image2 = request.FILES.get('post_image2')
        image3 = request.FILES.get('post_image3')
        post_model = PostsModel(author=request.user, post_image1=image1, post_image2=image2, post_image3=image3,
                                my_text=post)
        post_model.save()
        return HttpResponseRedirect(reverse('App_post:home'))
    return render(request, 'App_content/new_post.html')


def post_listview(request):
    post_list = PostsModel.objects.filter(status=True)
    content = {
        'post_list': post_list,
    }
    return render(request, 'App_content/post_listview.html', context=content)


def post_react(request, pk):
    post = PostsModel.objects.get(id=pk)
    try:
        react = PostLoveReact.objects.get(post=post, user=request.user)
        if react.liked is False:
            react.liked = True
            react.save()
        else:
            react.liked = False
            react.save()
    except Exception as e:
        react_model = PostLoveReact(post=post, user=request.user, liked=True)
        react_model.save()
    return HttpResponseRedirect(reverse('App_content:post-listview'))


# -----------------------------syllabus--------------------------------------------#

def add_syllabus(request):
    if request.method == 'POST':
        uni = request.POST.get('university')
        dept = request.POST.get('department')
        session = request.POST.get('session')
        syllabus = request.FILES.get('syllabus')
        syllabus_model = SyllabusModel(user=request.user, university=uni, department=dept, session=session,
                                       syllabus=syllabus)
        syllabus_model.save()
        return HttpResponseRedirect(reverse('App_post:home'))
    return render(request, 'App_content/add_syllabus.html')


def syllabus_listview(request):
    syllabuses = SyllabusModel.objects.filter(status=True)
    content = {
        'syllabuses': syllabuses,
    }
    return render(request, 'App_content/syllabus_listview.html', context=content)

# -----------------------------------------------connections---------------------------------------- #


def connection_request(request, user_id):
    from_user = request.user
    to_user = User.objects.get(id=user_id)
    connect_request, created = ConnectionRequestModel.objects.get_or_create(from_user=from_user, to_user=to_user)
    if created:
        return HttpResponse('Connection request sent')
    else:
        return HttpResponse('connection request was already sent')


def accept_connection_request(request, request_id):
    connect_request = ConnectionRequestModel.objects.get(id=request_id)
    if connect_request.to_user == request.user:
        connect_request.to_user.connections.add(connect_request.from_user)
        connect_request.from_user.connections.add(connect_request.to_user)
        connect_request.delete()
        return HttpResponse('connection request is accepted.')
    else:
        return HttpResponse('request is not accepted.')
