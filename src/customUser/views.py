from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from customUser.forms import RegistrationForm, CustomUserAuthenticationForm, CustomUserChangeForm
from customUser.models import CustomUser
from django.contrib import messages

def custom_user_list_view(request):

    currentCustomUser = request.user
    if not currentCustomUser.is_staff:
        return redirect("home")

    template = "custom_user_list.html"

    custom_user_list = CustomUser.objects.all()

    context = {"custom_user_list": custom_user_list}
    return render(request, template, context)

def custom_user_add_view(request):

    currentCustomUser = request.user
    if not currentCustomUser.is_staff:
        return redirect("home")

    template = "custom_user_add.html"
    context = {}

    if request.POST:
        try:
            form = RegistrationForm(request.POST)
            if form.is_valid():
                form.save()
                email = form.cleaned_data.get("email")
                raw_password = form.cleaned_data.get("password1")
                custom_user = authenticate(email=email, password=raw_password)

                messages.success(request, "User was created")
            else:
                context["form"] = form
        except Exception as e:
            messages.warning(
                request, "The user could not be created: Error: {}".format(e)
            )
    else:
        form = RegistrationForm()
        context["form"] = form
    return render(request, template, context)    

def custom_user_update_view(request, pk):

    currentCustomUser = request.user
    if not currentCustomUser.is_staff:
        return redirect("home")  

    template = "custom_user_update.html"          

    custom_user = get_object_or_404(CustomUser, pk=pk)
    if request.method == "POST":

        form = CustomUserChangeForm(request.POST, instance=custom_user)
        try:
            if form.is_valid():
                form.save()
                form.initial = {
                    "first_name": request.POST["first_name"],
                    "last_name": request.POST["last_name"],
                }
                messages.success(request, "Your account has been updated")

        except Exception as e:
            messages.warning(request, "The account was not saved due to an error")
    else:
        form = CustomUserChangeForm(
            instance=custom_user,
            initial={
                "first_name": custom_user.first_name,
                "last_name": custom_user.last_name,
            },
        )

    context = {"form": form, "custom_user": custom_user}
    return render(request, template, context)   

def custom_user_delete_view(request, pk):

    currentCustomUser = request.user
    if not currentCustomUser.is_staff:
        return redirect("home")

    template = "custom_user_delete.html"

    custom_user = get_object_or_404(CustomUser, pk=pk)

    try:
        if request.method == "POST":
            form = CustomUserChangeForm(request.POST, instance=custom_user)
            custom_user.delete()
            return redirect("customUserList") 
        else:
            form = CustomUserChangeForm(
                instance=custom_user,
                initial={
                    "email": custom_user.email,
                    "first_name": custom_user.first_name,
                    "last_name": custom_user.last_name,
                },
            )
    except Exception as e:
        messages.warning(
            request, "The account could not be deleted: Error: {}".format(e)
        )

    context = {"form": form, "custom_user": custom_user}
    return render(request, template, context) 

def home_screen_view(request):
    template = "home.html"
    context = {}

    users = CustomUser.objects.all()
    context["users"] = users

    return render(request, template, context)


def registration_view(request):

    currentCustomUser = request.user
    if not currentCustomUser.is_staff:
        return redirect("home")

    template = "register.html"
    context = {}

    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get("email")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(email=email, password=raw_password)
            login(request, user)
            return redirect("home")
        else:
            context["registration_form"] = form
    else:
        form = RegistrationForm()
        context["form"] = form
    return render(request, template, context)


def logout_view(request):
    logout(request)
    return redirect("home")


def login_view(request):

    customUser = request.user
    if customUser.is_authenticated:
        return redirect("home")

    template = "login.html"
    context = {}

    form = CustomUserAuthenticationForm()

    if request.POST:
        form = CustomUserAuthenticationForm(request.POST)
        if form.is_valid():
            email = request.POST["email"]
            password = request.POST["password"]
            customUser = authenticate(email=email, password=password)

            if customUser:
                login(request, customUser)
                return redirect("home")
        else:
            form = CustomUserAuthenticationForm(
                initial={ "email": "",}
            )

    context["form"] = form
    return render(request, template, context)


def custom_user_update_my_data_view(request):

    if not request.user.is_authenticated:
        return redirect("login")

    template = "custom_user_update_my_data.html"

    context = {}
    
    if request.POST:
        try:
            form = CustomUserChangeForm(request.POST, request.FILES, instance=request.user)
            if form.is_valid():          
                form.save()
                messages.success(request, "Your account has been updated")
        except Exception as e:
            messages.warning(
                request, "The account could not be updated: Error: {}".format(e)
            )


    form = CustomUserChangeForm(
        initial={
            "email": request.user.email,
            "first_name": request.user.first_name,
            "last_name": request.user.last_name,
            "profile_picture": request.user.profile_picture,
        }
    )

    context["form"] = form
    return render(request, template , context)
