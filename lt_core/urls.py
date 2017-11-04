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

'''
# topics
url(r'^topics/$', views.topics, name='topics'),
# one topic
url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
# add topic
url(r'^new_topic/$', views.new_topic, name='new_topic'),
# add entry
url(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),
# edit entry
url(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry, name='edit_entry'),
'''