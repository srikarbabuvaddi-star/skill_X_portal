from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import ProfileMetadata
from .forms import ProfileMetadataForm

@login_required
def view_and_edit_profile(request):
    meta, _ = ProfileMetadata.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = ProfileMetadataForm(request.POST, instance=meta)
        if form.is_valid():
            form.save()
            return redirect('view_and_edit_profile')
    else:
        form = ProfileMetadataForm(instance=meta)
    return render(request, 'skills/profile.html', {'form': form, 'meta': meta})