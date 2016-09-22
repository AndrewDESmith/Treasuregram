from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
# Get all of the Treasure objects to pass to the template (import the Treasure class from models.py in the same directory).
from .models import Treasure
from .forms import TreasureForm, LoginForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def index(request):
    treasures = Treasure.objects.all()
    form = TreasureForm()
    # A context is a dictionary that maps template variable names to Python objects.
    # Create an empty form on the homepage and pass it to the template to display, alongside the listed treasures:
    return render(request, 'index.html', { 'treasures': treasures, 'form': form })

def detail(request, treasure_id):
    treasure = Treasure.objects.get(id=treasure_id)
    # Pass the data from the urlpatterns into the template:
    return render(request, 'detail.html', {'treasure': treasure})

def post_treasure(request):
    # Create an instance of the form from the request:
    # request.FILES gives the view access to our uploaded files to save the image field.
    form = TreasureForm(request.POST, request.FILES)
    if form.is_valid():
        # Read the data in the form fields and save it to the database.  This step creates a new treasure object for us, since the form is linked to the Treasure model (specified in the forms.py code).  Commit the treasure object directly from the form to the database:
        # We can't yet save the contents of the form as a treasure object (commit = false), since user is a required entry for a treasure, and is not present on a form submission...
        treasure = form.save(commit = False)
        # ...so we add a user to the treasure (the user is sent along with the request), so that the treasure has a user association with it:
        treasure.user = request.user
        treasure.save()
    # Redirect back to the homepage:
    return HttpResponseRedirect('/')

def profile(request, username):
    # Check for a User.username entry against the passed-in username:
    user = User.objects.get(username = username)
    # Find treasures associated with the passed in user:
    treasures = Treasure.objects.filter(user = user)
    # Show (render) the user's treasures on the user profile page:
    return render(request, 'profile.html', {'username': username, 'treasures': treasures})

def login_view(request):
    # Are a username and password being submitted using this url?
    if request.method == 'POST':
        # Create the login form:
        form = LoginForm(request.POST)
        if form.is_valid():
            u = form.cleaned_data['username']
            p = form.cleaned_data['password']
            # Authenticate using the submitted username and password, which returns the authenticated user (if they exist):
            user = authenticate(username = u, password = p)
            # If authenticate() returns a user:
            if user is not None:
                # .is_active is a boolean that is set to false when the intention is to disable or delete an account (the latter so that foreign keys don't break)
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/')
                else:
                    print('The account has been disabled!')
            # No user with that username and password are in the database (user is None):
            else:
                print('The username and password were incorrect.')
    # Display login form:
    else:
        form = LoginForm()
        return render(request, 'login.html', { 'form': form })

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

def like_treasure(request):
    # Get the treasure_id from the AJAX request:
    treasure_id = request.POST.get('treasure_id', None)

    likes = 0
    # Check that the treasure_id was received from the GET request:
    if (treasure_id):
        # Look up the treasure that corresponds to the submitted id:
        treasure = Treasure.objects.get(id=int(treasure_id))
        if treasure is not None:
            # Increment the existing number of likes, and update the likes attribute for the treasure:
            likes = treasure.likes + 1
            treasure.likes = likes
            treasure.save()

    # Return the updated likes value back to the AJAX:
    return HttpResponse(likes)
