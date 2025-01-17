from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import ResumeItemForm
from .models import ResumeItem
from django.shortcuts import redirect


def resume(request):
    skills = list(reversed(ResumeItem.objects.filter(section="SK")))
    experience = list(reversed(ResumeItem.objects.filter(section="EX")))
    education = list(reversed(ResumeItem.objects.filter(section="ED")))
    technical_interests = list(
        reversed(ResumeItem.objects.filter(section="TI")))
    return render(
        request, 'resume/resume.html', {
            'skills_list': skills,
            'experience_list': experience,
            'education_list': education,
            "technical_interests_list": technical_interests
        })


@login_required
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


@login_required
def resume_edit(request, pk):
    resume_item = get_object_or_404(ResumeItem, pk=pk)
    if request.method == "POST":
        form = ResumeItemForm(request.POST, instance=resume_item)
        if form.is_valid():
            resume_item = form.save(commit=False)
            resume_item.save()
            return redirect('resume')
    else:
        form = ResumeItemForm(instance=resume_item)
    return render(request, 'resume/new_resume_item.html', {'form': form})


@login_required
def resume_delete(request, pk):
    resume_item = get_object_or_404(ResumeItem, pk=pk)
    resume_item.delete()
    return redirect("resume")
