# forms.py
import os
import cv2
import uuid
from django import forms
from .models import Video, Tag
from django.conf import settings

class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['name', 'video_file', 'tags']

    # Define predefined tags
    predefined_tags = ['DDK', 'SDK', 'Dan']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Create predefined tags if they don't exist
        for tag_name in self.predefined_tags:
            tag, created = Tag.objects.get_or_create(name=tag_name)
            if created:
                print(f"Created tag: {tag_name}")

        # Update widget for tags field to use CheckboxSelectMultiple
        self.fields['tags'].widget = forms.CheckboxSelectMultiple()

        # Update queryset for tags field
        self.fields['tags'].queryset = Tag.objects.filter(name__in=self.predefined_tags)

    def save(self, commit=True):
        video = super().save(commit=False)

        # Generate thumbnail
        if 'video_file' in self.cleaned_data:
            video_file = self.cleaned_data['video_file']
            thumbnail = self.generate_thumbnail(video_file)
            video.thumbnail = thumbnail

        if commit:
            video.save()
            self.save_m2m()
        return video

    def generate_thumbnail(self, video_file):
        # Get the temporary file path
        video_file_path = video_file.temporary_file_path()

        # Read the first frame of the video using OpenCV
        cap = cv2.VideoCapture(video_file_path)
        success, frame = cap.read()
        cap.release()

        # Generate a UUID for the thumbnail filename
        thumbnail_uuid = str(uuid.uuid4())
        thumbnail_filename = thumbnail_uuid + '.jpg'

        # Construct the thumbnail path relative to MEDIA_ROOT
        thumbnail_relative_path = os.path.join('thumbnails', thumbnail_filename)
        thumbnail_path = os.path.join(settings.MEDIA_ROOT, thumbnail_relative_path)

        # Save the thumbnail with the UUID filename
        cv2.imwrite(thumbnail_path, frame)

        # Return the relative path to the generated thumbnail
        return thumbnail_relative_path