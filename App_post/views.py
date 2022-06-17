from django.shortcuts import render, HttpResponseRedirect, reverse

# Create your views here.
from App_post.models import PartnerRequestModel, JobPostModel, PartnerApplicationModel


def home(request):
    return render(request, 'App_post/home.html')


def partner_request(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        participants = int(request.POST.get('total_participants'))
        location = request.POST.get('location')
        activity_type = request.POST.get('type')
        duration = request.POST.get('project_duration')
        skills = request.POST.get('required_skills')
        deadline = request.POST.get('application_deadline')
        file = request.FILES.get('related_file')
        description = request.POST.get('description')
        request_model = PartnerRequestModel(title=title, type=activity_type, total_participants=participants,
                                            project_duration=duration, location=location,
                                            author=request.user, required_skills=skills,
                                            application_deadline=deadline, related_file=file, description=description)
        request_model.save()
        return HttpResponseRedirect(reverse('App_post:home'))
    return render(request, 'App_post/partner_request.html')


def job_post(request):
    if request.method == 'POST':
        job_title = request.POST.get('job_title')
        company_name = request.POST.get('company_name')
        position = request.POST.get('position')
        work_type = request.POST.get('type')
        vacancies = int(request.POST.get('total_vacancies'))
        category = request.POST.get('category')
        location = request.POST.get('location')
        gender = request.POST.get('gender')
        skills = request.POST.get('required_skills')
        responsibilities = request.POST.get('job_responsibilities')
        description = request.POST.get('job_description')
        deadline = request.POST.get('application_deadline')
        experience = request.POST.get('experience')
        job_model = JobPostModel(author=request.user, job_title=job_title, company_name=company_name, position=position, category=category, work_type=work_type, total_vacancies=vacancies, location=location, required_skills=skills, job_description=description, job_responsibilities=responsibilities, experience=experience, gender_specification=gender, application_deadline=deadline)
        job_model.save()
        return HttpResponseRedirect(reverse('App_post:home'))
    return render(request, 'App_post/job_post.html')


def display_partner_requests(request):
    requests = PartnerRequestModel.objects.all()
    content = {
        'requests': requests,
    }

    return render(request, 'App_post/display_requests.html', context=content)


def apply_for_participation(request, pk):
    project = PartnerRequestModel.objects.get(id=pk)
    if request.method == 'POST':
        reason = request.POST.get('reason')
        apply_model = PartnerApplicationModel(activity=project, participant=request.user, reason_of_participation=reason)
        apply_model.save()
        return HttpResponseRedirect(reverse('App_post:home'))
    return render(request, 'App_post/apply_for_participation.html')
