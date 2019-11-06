from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^/(?P<author_id>\w{1,11})$',views.topics)



]