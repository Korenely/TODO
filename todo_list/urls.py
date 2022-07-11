from django.urls import path
from todo_list.views import *


urlpatterns = [
    path("", TaskList.as_view(), name="task-list"),
    path("tags/", TagList.as_view(), name="tag-list"),
    path('tags/<int:pk>/undo', undo_task, name='undo-task'),
    path("tags/create", TagCreate.as_view(), name="tag-create"),
    path("task/create", TaskCreate.as_view(), name="task-create"),
    path('tags/<int:pk>/complete', complete_task, name='complete-task'),
    path("tags/<int:pk>/update", TagUpdate.as_view(), name="tag-update"),
    path("tags/<int:pk>/delete", TagDelete.as_view(), name="tag-delete"),
    path("task/<int:pk>/update", TaskUpdate.as_view(), name="task-update"),
    path("task/<int:pk>/delete", TaskDelete.as_view(), name="task-delete"),
]

app_name = "todo_list"
