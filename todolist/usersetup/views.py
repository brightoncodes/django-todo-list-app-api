from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import View
from .form import UserForm

# Create your views here.
class UserFormView(View):
    form_class = UserForm
    template_name = 'registration_form.html'

    # display blank form
    def get(self,request):
        form = self.form_class(None)
        return render(request,self.template_name, {'form': form})

    # process form data
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():

            user = form.save(commit=False)

            #cleaned data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            # returns User objects if credentials are correct
            user = authenticate(request,username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request,user)
                    return redirect('todo:index')

        return render(request,self.template_name, {'form': form})


def logout_route(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('login')