from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
#peter
import urllib
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Comment
from .forms import CommentForm
GOOGLE_RECAPTCHA_SECRET_KEY = '6Leb-z4UAAAAAAnB4IAfIULJ2RMD70jsLTA8kqm_'
#peter

# Views here
def landing(request):
    return render(request, 'home/landing_page.html')

def index(request):
    return render(request, 'home/base_home.html')

def support(request):
    return render(request, 'home/support.html')

def help(request):
    return render(request, 'home/help.html')

def announcements(request):
    return render(request, 'home/announcements.html')

def dashboard(request):
    return render(request, 'dashboard/dashboard.html')

def important(request):
    return render(request, 'dashboard/important.html')

def indexSipun(request):
    return render(request, 'home/base_sipun_index.html')

def registerSipun(request):
    return render(request, 'home/base_sipun_register.html')

def signupSipun(request):
    return render(request, 'home/base_sipun_signup.html')

def orderFormSipun(request):
    return render(request, 'home/base_sipun_orderForm.html')

#peter
def comments(request):
    comments_list = Comment.objects.order_by('-created_at')

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():

            ''' Begin reCAPTCHA validation '''
            recaptcha_response = request.POST.get('g-recaptcha-response')
            url = 'https://www.google.com/recaptcha/api/siteverify'
            values = {
                'secret': GOOGLE_RECAPTCHA_SECRET_KEY,
                'response': recaptcha_response
            }
            data = urllib.parse.urlencode(values).encode()
            req =  urllib.request.Request(url, data=data)
            response = urllib.request.urlopen(req)
            result = json.loads(response.read().decode())
            ''' End reCAPTCHA validation '''

            if result['success']:
                form.save()
                messages.success(request, 'New comment added with success!')
                return render(request, 'dashboard/dashboard.html')
            else:
                messages.error(request, 'Invalid reCAPTCHA. Please try again.')

            return redirect('dashboard/important.html')
    else:
        form = CommentForm()

#    return render(request, 'dashboard/dashboard.html', {'comments': comments_list, 'form': form})
    return redirect('dashboard/important.html')
#peter
