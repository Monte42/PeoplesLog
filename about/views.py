from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required(redirect_field_name='next', login_url='signin')
def about_us_view(request):
    return render(request, 'about_us.html')
