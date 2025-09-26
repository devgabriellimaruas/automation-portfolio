from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings


def contact_form(request):
    form = ContactForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        # Pega os dados do formulário
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        message = form.cleaned_data['message']

        # Exemplo: enviar email (configurar EMAIL_BACKEND no settings.py)
        send_mail(
            f"{name} - {email}",
            message,
            settings.DEFAULT_FROM_EMAIL,
            [settings.DEFAULT_FROM_EMAIL],  # ou outro email de destino
        )

        return redirect('contact_success')  # página de sucesso
    else:
        form = ContactForm()

    return render(request, 'contact/contact.html', {'form': form})
