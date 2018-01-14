from django.conf.urls import url
from .views import question, moderator,moderatorviews,deletequest

urlpatterns = [
    url(r'^$', question, name='index'),
    url(r'^moderator/(?P<id>\d+)/$', moderator, name='moderator'),
    url(r'^moderatorview$', moderatorviews, name='moderatorviews'),
    url(r'^moderator/(?P<id>\d+)/deletequest/$', deletequest, name='deletequests'),

]

