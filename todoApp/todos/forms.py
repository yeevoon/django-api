from django import forms
from .models import Todo, Uploads

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ["title", "text", "created_at"]

class UploadsForm(forms.ModelForm):
    class Meta:
        model = Uploads
        fields = ('description','uploaded_file',)
 