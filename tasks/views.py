from django.shortcuts import render
import datetime
from django.http import JsonResponse
from .models import ApiInfo
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("Happy Internship")



def get_info(request):
    slack_name = request.GET.get('slack_name', '')
    track = request.GET.get('track', '')

    # Get current UTC time with validation of +/-2 minutes
    current_time = datetime.datetime.utcnow()
    current_time_with_offset = current_time + datetime.timedelta(minutes=2)

    # Define GitHub URLs
    github_file_url = "https://github.com/Abubakarauta/hngx_intern/blob/main/tasks/views.py"
    github_repo_url = "https://github.com/Abubakarauta/hngx_intern"

    # Create a new instance of ApiInfo
    api_info = ApiInfo(slack_name=slack_name, track=track)
    api_info.save()

    # Create the JSON response
    response = {
        "slack_name": slack_name,
        "current_day": current_time.strftime('%A'),
        "utc_time": current_time_with_offset.strftime('%Y-%m-%dT%H:%M:%SZ'),
        "track": track,
        "github_file_url": github_file_url,
        "github_repo_url": github_repo_url,
        "status_code": 200
    }

    return JsonResponse(response)
