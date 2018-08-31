from django.contrib import auth
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from django.views.generic import TemplateView


@csrf_protect
class AuthenticationView(TemplateView):

    def login(request):
        template_name = 'login.html'

        if request.user.is_authenticated:
            return redirect('booking-table')

        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)

            if user is not None:
                auth.login(request, user)
                if request.POST['remember_me'] == '1':
                    request.session.set_expiry(604800)
                return redirect('booking-table')

            else:
                messages.error(request, 'Incorrect Username or Password')

        return render(request, template_name)


    
    def logout(request):
        auth.logout(request)
        return redirect('login')