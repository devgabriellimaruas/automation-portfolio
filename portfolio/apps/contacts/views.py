from django.shortcuts import render, redirect
from .forms import contactsForm
from django.core.mail import send_mail
from django.conf import settings


def contacts_form(request):
    form = contactsForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        message = form.cleaned_data['message']
        send_mail(
            f"{name} - {email}",
            message,
            settings.DEFAULT_FROM_EMAIL,
            [settings.DEFAULT_FROM_EMAIL],
        )
        return redirect('contacts')
    return render(request, 'contacts/contacts.html', {'form': form})
