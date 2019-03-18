from django.conf.urls import url
from todolist import views

app_name = 'todolist'

urlpatterns=[
    url(r'^add_task/$',views.add_task,name='add_task'),
    url(r'^view_task/$',views.view_task,name='view_task'),
    url(r'^remove_task/$',views.remove_task,name='remove_task'),
    url(r'^update_task/$',views.update_task,name='update_task'),
]
