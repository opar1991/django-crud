from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from . forms import SignUpForm, AddMembersForm
from .models import Members

# Create your views here.

def home(request):
    #grab everything from table Members
    members = Members.objects.all()
    #check login
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        #lets authunticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been logged in")
            return redirect('home')
        else:
            messages.success(request, "There was a problem loggin you in")
            return redirect('home')
    else:
        return render(request, 'baseapp/index.html', {'members':members})
def login_user(request):
    pass
def logout_user(request):
    logout(request)
    messages.success(request, "You have logged out..")
    return redirect('home')
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Authenticate and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'You have successfully registered')
            return redirect('home')
        else:
            # Add error message and re-render the form with errors
            messages.error(request, 'Registration failed. Please correct the errors below.')
    else:
        form = SignUpForm()

    # Render the template with form context for both GET and invalid POST requests
    context = {'form': form}
    return render(request, 'baseapp/register.html', context)
    
def member_records(request, pk):
    #first check if the user is logged in before displayin the records
    if request.user.is_authenticated:
        #look up records
        members_record = Members.objects.get(id=pk)
        return render(request, 'baseapp/members.html', {'members_record':members_record})
    else:
        messages.success(request, 'You must log in to view this')
        return redirect('home')
def delete_members(request, pk):
    if request.user.is_authenticated:
        delete_record = Members.objects.get(id=pk)
        delete_record.delete()
        messages.success(request, 'Record successfully deleted')
        return redirect('home')
    else:
        messages.success(request, 'You must be logged')
        return redirect('home')
def add_members(request):
    form = AddMembersForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == 'POST':
            if form.is_valid():
                new_members = form.save()
                messages.success(request, "Member successfully added")
                return redirect('home')
        return render(request, 'baseapp/add_members.html', {'form':form})
    else:
        messages.success(request, "You must be logged in to do this operation")
        return redirect('home')
def update_members(request, pk):
    if request.user.is_authenticated:
        try:
            current_record = Members.objects.get(id=pk)
        except Members.DoesNotExist:
            messages.error(request, "Member not found")
            return redirect('home')  # Or redirect to an appropriate page if member not found

        form = AddMembersForm(request.POST or None, instance=current_record)
        
        if form.is_valid():
            form.save()
            messages.success(request, "Record successfully updated")
            return redirect('home')  # Redirect to a success page or member details page
        
        # If form is not valid, render the form with the current record
        return render(request, 'baseapp/update_members.html', {'form': form, 'current_record': current_record})

    else:
        # Handle case where user is not authenticated
        messages.error(request, "You must be logged in to update members.")
        return redirect('home')  # Redirect to the login page or another appropriate pag







