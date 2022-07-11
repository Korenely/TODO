from django.forms import ModelForm
from todo_list.models import Task, Tag


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['content', 'tags']


class TagForm(ModelForm):
    class Meta:
        model = Tag
        fields = '__all__'
