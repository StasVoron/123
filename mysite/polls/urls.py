from django.conf.urls import patterns, url

from polls import views

urlpatterns = patterns('',
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    # ex: /polls/2/
    url(r'^specifics/(?P<question_id>\d+)/$', views.detail, name='detail'),
    # /results/
    url(r'^(?P<question_id>\d+)/results/$', views.results, name='results'),
    # /vote/
    url(r'^(?P<question_id>\d+)/vote/$', views.vote, name='vote'),
)