from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import ResumeItemForm
from .models import ResumeItem
from django.shortcuts import redirect


# @login_required
def resume(request):
    skills = ResumeItem.objects.filter(section="SK")
    experience = ResumeItem.objects.filter(section="EX")
    education = ResumeItem.objects.filter(section="ED")
    technical_interests = ResumeItem.objects.filter(section="TI")
    return render(
        request, 'resume/resume.html', {
            'skills_list': skills,
            'experience_list': experience,
            'education_list': education,
            "technical_interests_list": technical_interests
        })


def resume_new(request):
    if request.method == "POST":
        form = ResumeItemForm(request.POST)
        if form.is_valid():
            resume_item = form.save(commit=False)
            resume_item.save()
            return redirect('resume')
    else:
        form = ResumeItemForm()
    return render(request, 'resume/new_resume_item.html', {'form': form})
