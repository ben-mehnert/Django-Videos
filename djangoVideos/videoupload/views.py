from django.shortcuts import render, redirect, HttpResponseRedirect
from .forms import VideoForm
from .models import Video, Tag
from django.contrib import messages



def videospage(request, tag_name=None):
    if tag_name:
        # Use iexact to perform a case-insensitive match on the tag name
        videos = Video.objects.filter(tags__name__iexact=tag_name)
    else:
        # No tag provided, retrieve all videos
        videos = Video.objects.all()
    all_tags = Tag.objects.all()
    return render(request, "videos.html", {'videos': videos, 'tag_name': tag_name, 'all_tags': all_tags})

def upload_video(request):
    print("Upload video view function called")  # Debug statement
    
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            print("Form is valid")  # Debug statement
            video = form.save()
            print("Video saved successfully")  # Debug statement
            # Redirect to the videos list page
            return redirect('all_videos')  # or 'videos_with_tag' if desired
        else:
            # Handle form validation errors
            messages.error(request, 'There was an error in the form. Please correct the errors and try again.')
    else:
        form = VideoForm()

    return render(request, 'upload_video.html', {'form': form})