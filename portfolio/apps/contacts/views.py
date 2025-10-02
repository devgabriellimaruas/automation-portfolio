from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .forms import contactsForm
from django.conf import settings

def contacts_form(request):
    form = contactsForm(request.POST or None)
    
    if request.method == "POST":
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            try:
                send_mail(
                    f"{name} - {email}",
                    message,
                    settings.DEFAULT_FROM_EMAIL,
                    [settings.DEFAULT_FROM_EMAIL],
                )
                messages.success(request, "Obrigado pelo seu contato! Responderemos o mais breve possível.")
            except:
                messages.error(request, "Ops! Houve um erro ao enviar sua mensagem. Por favor, tente novamente mais tarde.")
            return redirect('contacts')
        else:
            messages.error(request, "Ops! Há erros no formulário. Por favor, verifique e tente novamente.")
    
    return render(request, 'contacts/contacts.html', {'form': form})
