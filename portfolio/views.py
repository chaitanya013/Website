from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Contact, Blogs, Internship

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def internshipdetails(request):

    if not request.user.is_authenticated:
        messages.warning(request,'Please login to access')
        return redirect("/auth/login/")
    if request.method=='POST':
        fname= request.POST.get('name')
        femail= request.POST.get('email')
        fusn= request.POST.get('usn')
        fcollege=request.POST.get('cname')
        foffer = request.POST.get('offerletter')
        fstartdate = request.POST.get('startdate')
        fenddate = request.POST.get('enddate')
        fprojreport=request.POST.get('projreport')


        # converting to uppercase

        fname=fname.upper()
        fusn=fusn.upper()
        fcollege=fcollege.upper()
        fprojreport=fprojreport.upper()
        foffer=foffer.upper()

        check1=Internship.objects.filter(usn=fusn)
        check2=Internship.objects.filter(email=femail)
        if check1 or check2:
            messages.warning(request,"Your Details Already Stored")
            return redirect("/internshipdetails")

        query= Internship(fullname=fname, usn=fusn, email=femail, college_name=fcollege, offer_status=foffer, start_date=fstartdate,
        end_date=fenddate, project_report=fprojreport)
        query.save()

        messages.success(request, 'Form Is Submited Successfully')
        return redirect('/internshipdetails')
    return render(request, 'internship.html')

def handleblog(request):
    posts= Blogs.objects.all()
    context= {'posts': posts}
    return render(request, 'handleblog.html', context)

def contact(request):
    if request.method=='POST':
        fname= request.POST.get('name')
        femail= request.POST.get('email')
        fphoneno= request.POST.get('num')
        fdesc= request.POST.get('desc')
        query= Contact(name=fname,email=femail,number=fphoneno,description=fdesc)
        query.save()
        messages.success(request, 'Thanks for contacting us. We will get back you soon!')
        return redirect('/contact')
    return render(request, 'contact.html')
