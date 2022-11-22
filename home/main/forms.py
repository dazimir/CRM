from .models import Task
from django.forms import ModelForm, TextInput, Textarea, DateField, DateInput, SelectDateWidget


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["title", "task", "idate"]
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'plaseholder': 'введите название'
            }),
            "task": Textarea(attrs={
                'class': 'form-control',
                'plaseholder': 'введите описание'
            }),
            "idate": SelectDateWidget()
        }
