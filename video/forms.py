from django import forms
from .models import VideoConference

class VideoConferenceForm(forms.ModelForm):
    class Meta: model = VideoConference; fields = ['uid']