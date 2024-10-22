from django.shortcuts import render,redirect
from services.models import user

def login(request):
    msg = ''
    request.session['is_logged_in'] = False
    request.session['template_id'] = False
    try:
        if request.method == 'POST':
            mail = request.POST.get('email')
            password = request.POST.get('password')
            check = user.objects.filter(mail=mail,password=password)
            if check:
                firstname = check[0].firstname
                lastname = check[0].lastname
                contact = check[0].contact
                request.session['is_logged_in'] = True
                request.session['firstname'] = firstname
                request.session['lastname'] = lastname
                request.session['contact'] = contact
                request.session['mail'] = mail
                return redirect('home')
            else:
                msg = "Wrong Credentials"
    except:
        pass
    return render(request,'login.html',{'msg':msg})

def register(request):
    msg = ""
    try:
        if request.method == 'POST':
            firstName = request.POST.get('firstname')
            lastName = request.POST.get('lastname')
            mail = request.POST.get('email')
            contact = request.POST.get('contact')
            password = request.POST.get('password')

            if len(contact) == 10 and len(password)<=14:
                model_data = user(firstname=firstName,lastname=lastName,mail=mail,contact=contact,password=password)
                model_data.save()
                msg = "Your details are saved successfully"
    except:
        pass
    return render(request,'register.html',{"msg":msg})

def home(request):
    request.session['clicked_trynow'] = False
    if request.session.get('is_logged_in'):
        name = request.session.get('firstname')
        if request.method == 'POST':
            request.session['clicked_trynow'] = True
            return redirect('designs')
        return render(request,'entry.html',{'name':name})
    else:
        return redirect('login')

def designs(request):
    request.session['template_id'] = False
    if request.session.get('is_logged_in') and request.session.get('clicked_trynow'):
        if request.method == 'POST':
            template_id = request.POST.get('button')
            request.session['template_id'] = template_id
            return redirect('template')
        return render(request,'designs.html')
    else:
        return redirect('home')

def template(request):
    if request.session.get('is_logged_in') and request.session.get('template_id'):
        phone = request.session.get('contact')
        mail = request.session.get('mail')
        firstname = request.session.get('firstname')
        lastname = request.session.get('lastname')
        if request.method == 'POST':
                designation = request.POST.get('designation')
                location = request.POST.get('location')
                about = request.POST.get('about')
                company = request.POST.get('company')
                work = request.POST.get('work')
                education = request.POST.get('education')
                college = request.POST.get('college')
                skill1 = request.POST.get('skill1')
                skill2 = request.POST.get('skill2')
                skill3 = request.POST.get('skill3')
                skill4 = request.POST.get('skill4')
                
                data = {
                'firstname':firstname,
                'lastname':lastname,
                'phone':phone,
                'mail':mail ,
                'designation':designation,
                'location':location,
                'about':about,
                'company':company,
                'work':work,
                'education':education,
                'college':college,
                'skill1':skill1,
                'skill2':skill2,
                'skill3':skill3,
                'skill4':skill4,
                }
                temp = request.session.get('template_id')
                return render(request,f'{temp}.html',data)
        return render(request,'form.html',{'fname':firstname,'lname':lastname,'phone':phone,'mail':mail})
    else:
        return redirect('designs')