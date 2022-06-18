from django.shortcuts import render, HttpResponseRedirect, reverse

# Create your views here.
from App_content.models import PodcastModel, PostsModel, PostLoveReact


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

