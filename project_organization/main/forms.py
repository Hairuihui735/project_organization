from django import forms
from .models import Project, ConsultationQueue

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'start_date', 'end_date', 'image']

class ConsultationQueueForm(forms.ModelForm):
    class Meta:
        model = ConsultationQueue
        fields = ['full_name', 'phone_number', 'photo']
        labels = {
            'full_name': 'ФИО',
            'phone_number': 'Номер телефона',
            'photo': 'Фото',
        }