
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import datetime

# Create your views here.
def get_info(request):
    slack_name = request.GET.get("slack_name")
    track = request.GET.get("track")

    # Validate that both query parameters are provided
    if not slack_name or not track:
        return JsonResponse(
            {"error": "Both Slack_name and track are required"}, status=400
        )

    # get the current day of the week
    current_day = datetime.datetime.utcnow().strftime("%A")

    # get the current UTC time with a +/- 2 munite window
    current_utc_time = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%H:%SZ")

    # construct a gitghub URLS based on repo and file names
    github_repo_url = "https://github.com/Abubakarauta/hngx_intern"
    github_file_url = f"{github_repo_url}/blob/main/tasks/views.py"
    # create a JSON response

    response_data = {
        "slack_name": slack_name,
        "current_day": current_day,
        "current_utc_time": current_utc_time,
        "track":track,
        "github_repo_url": github_repo_url,
        "github_file_url":github_file_url,
        "status_code":200
    }
    return JsonResponse(response_data)