from django import forms


class contactsForm(forms.Form):
    name = forms.CharField(max_length=100, label="Nome")
    email = forms.EmailField(label="Email")
    message = forms.CharField(widget=forms.Textarea, label="Mensagem")
