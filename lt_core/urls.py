""" learing_logs URL """

from django.conf.urls import url

from . import views

urlpatterns = [
    # main page
    url(r'^$', views.index, name='index'),
    url(r'^start_timer/(?P<topic_id>\d+)/$', views.start_timer, name='start_timer'),
    url(r'^stop_timer/$', views.stop_timer, name='stop_timer'),
    url(r'^add_topic/$', views.add_topic, name='add_topic'),
    url(r'^edit_topic/$', views.edit_topic, name='edit_topic'),
    url(r'^del_topic/(?P<topic_id>\d+)/$', views.del_topic, name='del_topic'),
    url(r'^records/(?P<topic_id>\d+)/$', views.records, name='records'),
    url(r'^del_record/(?P<record_id>\d+)/$', views.del_record, name='del_record'),
]
