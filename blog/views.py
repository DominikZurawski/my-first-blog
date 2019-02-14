from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Post

def index(request):
    latest_question_list = Post.objects.order_by('-created_date')[:5]
    output = ', '.join([q.title for q in latest_question_list])
    return HttpResponse(output)