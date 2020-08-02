from django.shortcuts import render
from .forms import UserRegisterForm
from django.core.mail import send_mail

# Create your views here.


def register(request):
    context = {
        'registered': False,
        'form': UserRegisterForm(),
    }
    if request.method == 'POST':
        context['form'] = UserRegisterForm(request.POST)
        if(context['form'].is_valid()):
            context['form'].save()
            context['registered'] = True
            subject = 'Welcome to ' + request.get_host()
            body = 'Your account has been created on ' + request.get_host() + '.\n' + 'Your username: ' + \
                context['form'].cleaned_data.get('username') + '.'
            send_mail(
                subject,
                body,
                'admin@{{request.get_host}}.com',
                [context['form'].cleaned_data.get('email')]
            )
        else:
            return render(request, 'users/register.html', context)

    context['form'] = UserRegisterForm()
    return render(request, 'users/register.html', context)
