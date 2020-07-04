from django.shortcuts import render
from django.forms import ValidationError
from second_app.forms import NewUserForm
from first_app.views import index as ind
# Create your views here.


def index(request):
    form = NewUserForm()
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return ind(request)
        raise ValidationError("Form Is Invalid!")
    return render(request, 'second_app/users.html', {'form': form})
