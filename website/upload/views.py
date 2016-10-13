from django.contrib.auth import authenticate, login

from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.shortcuts import redirect
from django.utils.crypto import get_random_string
import models
import forms

import pygal
from pygal.style import BlueStyle

import datetime

from mods.filetochart import filetodata

# Create your views here.

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
'''
def index(request):
    chart = pygal.Line(style=BlueStyle, stroke_style={'width': 3}, dots_size=4)
    chart.title = 'Example'
    chart.x_labels = range(0,11)
    chart.add('Hello', [10,10,30,50,20,40,60,80,100,30,10])
    chart.add('Goodbye', [51,50,41,20,20,40,70,31,51,68,25])

    chart = chart.render_data_uri()

    args = {}
    args['chart'] = chart

    return redirect('/upload/')

    return render(request, 'upload/index.html', context=args)
'''

def index(request):
    if not request.user.is_authenticated():
        args = {}
        args['failed'] = False
        if request.method == 'POST':
            userform = forms.RegisterForm(request.POST)
            if userform.is_valid():
                user = userform.save(commit=False)

                user.set_password(user.password)
                user.save()
            else:
                args['failed'] = True
                args['form_errors'] = userform.errors
        else:
            userform = forms.RegisterForm()

        args['registerform'] = userform
        return render(request, 'upload/index.html', context=args)
    else:
        ################### REPLACE WITH REDIRECT ###################
        return redirect('/cloud/')

def login(request):
    args={}

    if not request.user.is_authenticated():
        if request.method == 'POST':
            userform = forms.CstmLoginForm(data=request.POST)
            print("User is none1")
            if userform.is_valid():
                print("User is none2")
                userformsave = userform.save(commit=False)
                user = authenticate(username=userformsave.username, password=userformsave.password)

                if user is not None:
                    print("Not none")
                    if user.is_active:
                        print("Is active")
                        login(request, user)
                        return redirect('/upload/file/', request)

            else:
                args['form_errors'] = userform.errors
        else:
            userform = forms.LoginForm()
    else:
        return redirect('/cloud/')

    args['loginform'] = userform
    return render(request, 'upload/account/login.html', context=args)

def cloud(request):
    context = {}
    folders = []
    files = []

    pk = request.user.pk

    try:
        folders = models.Folder.objects.filter(owner=pk, parent=None)
    except:
        pass

    context['folders'] = folders
    context['files'] = files
    return render(request, 'upload/cloud.html', context=context)

def upload(request):
    if request.method == 'POST':
        uploadform = forms.FileUploadForm(request.POST, request.FILES)
        if uploadform.is_valid():
            #file = FileField.objects.create()
            x = get_random_string(12)
            newfile = models.File(file_id = x,file = request.FILES['file'], owner = request.user , name = request.POST['name'], description = request.POST['description'], date_time = datetime.datetime.now(), ip_address = get_client_ip(request))
            newfile.save()
            #uploadform.save()
            #return file(request, x)
            return redirect('/file/%s'%x)
    else:
        uploadform = forms.FileUploadForm()


    args = {}
    args['form'] = uploadform
    return render(request, 'upload/upload.html', context=args)
    #return render(request, 'upload/upload.html')

def file(request, file_id):
    try:
        _file = models.File.objects.filter(file_id=file_id)[0]
    except(IndexError):
        return HttpResponse("Oops! No such file.")

    _name = _file.name
    _description = _file.description
    args = {}
    try:
        _file
        #print _file.file().read()
        #return HttpResponse("<h2>Hi %s</h2>"%str(_file[0].file.read()))
        chart = filetodata(_file.file)

        args['chart'] = chart
        args['name'] = _name
        args['description'] = _description
        return render(request, 'upload/file.html', context=args)
        #return render(request, 'upload/index.html', context=args)
        #return redirect('/file/'+file_id, request, context=args)
    except:
        return HttpResponse("No such thing")
