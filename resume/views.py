from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import ResumeItemForm


# @login_required
def resume(request):
    return render(request, 'resume/resume.html')


def resume_new(request):
    form = ResumeItemForm()
    return render(request, 'resume/new_resume_item.html', {'form': form})
