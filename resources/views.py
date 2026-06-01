from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import CourseMaterial
from .forms import CourseMaterialForm

@login_required
def materials_repository(request):
    if request.method == 'POST':
        form = CourseMaterialForm(request.POST)
        if form.is_valid():
            material = form.save(commit=False)
            material.uploader = request.user
            material.save()
            return redirect('materials_repository')
    else:
        form = CourseMaterialForm()
    vault = CourseMaterial.objects.all()
    return render(request, 'vault.html', {'vault': vault, 'form': form})