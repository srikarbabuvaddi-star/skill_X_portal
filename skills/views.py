from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import SkillNode
from .forms import SkillNodeForm

def home(request):
    return render(request, 'index.html')


def progress(request):
    return render(request, 'progress.html')


def tracker(request):
    return render(request, 'tracker.html')


def share(request):
    return render(request, 'share.html')


def profile_page(request):
    return render(request, 'profile.html')


def skill_list(request):
    nodes = SkillNode.objects.all()
    return render(request, 'skill_list.html', {'skills': nodes})


@login_required
def list_skills(request):
    nodes = SkillNode.objects.all()
    return render(request, 'skill_list.html', {'skills': nodes})

@login_required
def create_skill(request):
    if request.method == 'POST':
        form = SkillNodeForm(request.POST)
        if form.is_valid():
            node = form.save(commit=False)
            node.owner = request.user
            node.save()
            return redirect('list_skills')
    else:
        form = SkillNodeForm()
    return render(request, 'addskill.html', {'form': form})


@login_required
def addskill(request):
    return create_skill(request)


@login_required
def skill_detail(request, pk):
    node = get_object_or_404(SkillNode, pk=pk)
    return render(request, 'skill_detail.html', {'skill': node})


@login_required
def edit_skill(request, pk):
    node = get_object_or_404(SkillNode, pk=pk, owner=request.user)
    if request.method == 'POST':
        form = SkillNodeForm(request.POST, instance=node)
        if form.is_valid():
            form.save()
            return redirect('list_skills')
    else:
        form = SkillNodeForm(instance=node)
    return render(request, 'addskill.html', {'form': form, 'edit_mode': True})

@login_required
def delete_skill(request, pk):
    node = get_object_or_404(SkillNode, pk=pk, owner=request.user)
    if request.method == 'POST':
        node.delete()
        return redirect('list_skills')
    return render(request, 'skill_detail.html', {'skill': node, 'delete_prompt': True})