from django.forms import ModelForm
from .models import Client


class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'last_name', 'age', 'salary', 'email', 'photo', 'dt_birth', 'doc_id']