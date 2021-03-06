from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404, JsonResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

from datetime import timedelta, datetime

from .models import UserState, Topic, Record
#from .forms import TopicForm, EntryForm

# Create your views here.

def index(request):
    if not request.user.is_authenticated:
        return render(request, 'lt_core/intro.html')

    userStates = UserState.objects.filter(user=request.user)
    if len(userStates) == 0:
        userState = UserState(user=request.user)
        userState.save()
    else:
        userState = userStates[0]
    
    if userState.is_start:
        return render(request, 'lt_core/timer.html', {'userState': userState})

    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    return render(request, 'lt_core/index.html', {'topics': topics})

@login_required
def start_timer(request, topic_id):
    userState = UserState.objects.filter(user=request.user)[0]
    topic = Topic.objects.get(id=topic_id)
    userState.is_start = True
    userState.last_start_topic = topic
    userState.last_start_time = datetime.now()
    userState.save()
    return JsonResponse({'success': True})

@login_required
def stop_timer(request):
    loss_second = request.POST.get('loss_second', 0)
    if loss_second:
        loss_second = int(loss_second)
    else:
        loss_second = 0
    
    userState = UserState.objects.filter(user=request.user)[0]
    topic = userState.last_start_topic
    start_time = userState.last_start_time
    end_time = datetime.now()
    loss_delta = timedelta(seconds=loss_second)
    delta = (end_time - start_time) - loss_delta

    userState.is_start = False
    userState.save()

    record = Record(topic=topic, start_time=start_time, end_time=end_time, loss_delta=loss_delta, delta=delta)
    record.save()

    topic.total_delta = topic.total_delta + delta
    topic.save()

    return JsonResponse({'success': True})

@login_required
def add_topic(request):
    parent_id = request.POST.get('parent_id')
    if parent_id:
        parent = Topic.objects.get(id=int(parent_id))
    else:
        parent = None
    text = request.POST.get('text', 'untitled')
    topic = Topic(owner=request.user, text=text, parent=parent)
    topic.save()
    return JsonResponse({'success': True})

@login_required
def edit_topic(request):
    topic_id = request.POST.get('topic_id')
    text = request.POST.get('text', 'untitled')
    topic = Topic.objects.get(id=int(topic_id))
    topic.text = text
    topic.save()
    return JsonResponse({'success': True})

@login_required
def del_topic(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    topic.delete()
    return JsonResponse({'success': True})

@login_required
def records(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    records = topic.record_set.order_by('-start_time')
    context = {'records': records}
    return render(request, 'lt_core/records.html', context)

@login_required
def del_record(request, record_id):
    record = Record.objects.get(id=record_id)
    new_total_delta = record.topic.total_delta - record.delta
    record.topic.total_delta = new_total_delta
    record.topic.save()
    record.delete()
    return JsonResponse({'success': True})
