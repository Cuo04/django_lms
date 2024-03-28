from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
# from .models import Students
from .forms import NewUserForm, ProfileForm, UserUpdateForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm #login
from django.contrib.auth.decorators import login_required
from .models import UserProfile #myInput

# Create your views here.
def home(request):
    # template = loader.get_template('index.html')
    # return HttpResponse(template.render())
    return render(request, 'index.html')


# @login_required(login_url='login')
# def students(request):
#     mystudents = Students.objects.all().values()
#     template = loader.get_template('student_reg.html')
#     context = {
#         'mystudents' : mystudents,
#     }
#     return HttpResponse(template.render(context, request))

#creating registration form view


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            # login(request, user)
            messages.success(request, "Registration Successful.")
            return redirect("students:login")
        messages.error(request, "Unsuccessful Registration. Invalid Information")
    form = NewUserForm()
    template = loader.get_template("register.html")
    context = {
        'register_form': form,
    }
    
    #return render(request=request, template_name="register.html",)
    return HttpResponse(template.render(context, request))

def login_request(request):
    if request.method =="POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('students:dashboard')
    
        else:
            
            
            error_message = "Invalid username or password"
    else:
        
        
        form = AuthenticationForm(request)
        #error_message = None
    
    
    template = loader.get_template("login.html")
    context = {
        "form": form,
        #"error_message": error_message,
    }
    return HttpResponse(template.render(context, request))

    # return render(request, 'login.html', {
    #     'login_form': form,
    #     'error_message': error_message
    # })
    

@login_required(login_url='login')
def dashboard(request):
    # user_id = request.user.id
    # mydashboard = User.objects.filter(id=user_id)
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.userprofile)
        
        #from here myInput
        if profile_form.is_valid():
            profile = UserProfile.objects.get(user=request.user)
            profile.phone = profile_form.cleaned_data['phone']
            profile.dob = profile_form.cleaned_data['dob']
            #myInput stop
        
            user_form.save()
            profile_form.save()
            messages.success(request, 'update successful')
            #myInput
            return render(request, 'dashboard.html', {
                "profile": profile,
                'user': request.user,
                "user_form": request.user,
                "profile_form": profile_form,
                        
                    })
            #myInputStop
            #return redirect('students:dashboard')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.userprofile)    
    
    
    
    template = loader.get_template('dashboard.html')
    context = {
        'user': request.user,
        "user_form": request.user,
        "profile_form": profile_form,
        
    }
    return HttpResponse(template.render(context, request))

@login_required(login_url='login')
def logout_request(request):
    logout(request) 
    messages.info(request, "You have successfully logged out")
    return redirect('students:login')