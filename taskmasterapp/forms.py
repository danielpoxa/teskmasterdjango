from django import froms
from .models import Task 

class TaskForm(form.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'due_date', 'priority']
        widgets = {

                'due_date': forms.DateInput(attrs={'type': 'date'}),
                'priority': forms.Select(),

        }