from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, JsonResponse
from social_django.views import auth as social_auth
import requests
from django.http import HttpResponseRedirect
import json
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder
import datetime
from django.contrib.auth import get_user_model
from django.views.decorators.http import require_http_methods
from .decorators import *
from django.contrib.auth.models import Group

from django.views.decorators.http import require_POST

from django.contrib.auth.models import User
from django.contrib import messages
from .models import *
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
# from zerobouncesdk import ZeroBounce, ZBException
from .models import *
from .mixins import *
import re
from django.contrib.auth.decorators import login_required

from django.core.mail import send_mail
import random
from django.template.loader import render_to_string
from django.utils.html import strip_tags

# Create your views here.

# def loginuser(request):

#     return render(request, 'login.html')


def home(request):
    return render(request, 'home.html')


def newCustomer(request):
    premises = Premises.objects.all().values()
    print(premises)
    # print(states.values())
    context = {
        'premises': premises
    }
    return render(request, 'Customer_register.html', context)


def verify_email(email):
    # zero_bounce = ZeroBounce("62ea741ed3b04ec595b3fe207fa67d88")

    api_key = '62ea741ed3b04ec595b3fe207fa67d88'
    url = f'https://api.zerobounce.net/v2/validate?api_key={api_key}&email={email}'
    # url=f'https://api.zerobounce.in/v2/getapiusage?api_key=your-api-key

    response = requests.get(url)
    data = response.json()
    print(data)

    if data['status'] == 'valid':
        print("Email is valid.")
        return True
    elif data['status'] == 'invalid':
        print("Email is invalid.")
        return False
    else:
        print("Email status is unknown.")
        return 'NOT FOUND'

# Usage example


def register(request):
    if request.method == 'POST':
        username = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        contact = int(request.POST['contact'])
        premise = request.POST['premise']
        # customer=Customer(name=username,email=email,contact=contact,premise=premise)
        # customer.save()
        check_email = User.objects.filter(email=email)
        if check_email.exists():
            messages.warning(request, "Email already exist!")
            return redirect('register')

        else:
            user = User.objects.create_user(username, email, password)
            # user.contact = contact
            # user.premises = premise
            customer = Customer(user=user,
                                name=username, contact=contact, premise=premise)
            group = Group.objects.get(name="customer")
            user.groups.add(group)
            print("group", group)
            customer.save()
            # new_customer = Customer(contact=contact,
            #                   premise=premise)
            # new_customer.save()
            # customer.save()
            # user.save()

            messages.success(
                request, "Your account has been created successfully!")
            return redirect('login_user')
        # ans = verify_email(email)
        # if ans:
        #     return HttpResponse("verified sucssfully!!!")
    return redirect('register')
#


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        # mobile_or_email = ''
        # print("verifymobilenumber check",verify_mobile_number(username))
        if username.isdigit():
            print("digit hai bhai")
            if(verify_mobile_number("+"+str(91)+str(username))):
                print(username)  # 9022913464
                otp = generate_otp()
                print(otp)
                send_otp_on_mobile_no(int(str(91) + str(username)), otp)
                request.session['otp'] = otp
                context = {
                    'username': username
                }
                return render(request, 'verify_otp.html', context)
            else:
                messages.warning(
                    request, "Please enter a valid number or Email ")
        else:
            print('email hai bhai text', username)
            otp = generate_otp()
            print(otp)
            send_otp_email(username, otp)
            request.session['otp'] = otp
            context = {
                'username': username
            }
            return render(request, 'verify_otp.html', context)
        print("username", username)

        #    <!-- {% url 'otp_verification'username%} -->

        # user=None
        # if username.isdigit():
        #     get_user = Customer.objects.get(contact=username)

        #     print(get_user.name)
        # # user_name=get_user.name
        #     print(get_user.user.email)
        # # print(get_user.contact)
        #     print("user model username: ",get_user.user.username)
        # new_user=User.objects.filter(username=get_user.user.username).values()
        # print("new user: ",new_user)
        # print("username by filter: ",new_user[0]['username'])

        # user = authenticate(request, username=get_user.user.username)
        # print(user)

        #     customer = Customer.objects.get(contact=username)
        #     user = customer.user

        #     print("customer user :",user)
        #     # print("authenticat user :",user)
        #     # print("check active status: ",new_user.is_active)
        # else:
        #     user = User.objects.get(email=username)
        #     print("email user: ",user)
        #     # print(get_user_byfilter[0]['username'])
        # user = authenticate(request, username=get_user.user.username)
        # print(user)
        # if user is not None:
        #     # User authentication successful
        #     login(request, user)
        #     print('logged in')
        #     return redirect('login_user')  # Redirect to the dashboard or any other desired page
        # else:
        #     # User authentication failed
        #     error_message = 'Invalid email or password. Please try again.'
        #     return render(request, 'login.html', {'error_message': error_message})

    return render(request, 'login.html')


# @login_required(login_url='login_user')
def otp_verification(request, username):

    if request.method == 'POST':
        # Retrieve entered OTP from the form
        entered_otp = request.POST.get('OTP')

        # Retrieve stored OTP from the session or database
        stored_otp = request.session.get('otp')

        if entered_otp == stored_otp:
            # OTP is valid, proceed with login or desired action
            # Add your login logic here or perform the desired action
            get_user = None
            name = None
            email = None
            contact = None
            premise = None
            if username.isdigit():
                #
                customer = Customer.objects.get(contact=username)
                # print("customer_contact",customer.contact)
                get_user = customer.user
                # name=get_user.username
                # email=get_user.email
                # contact=customer.contact
                # premise=customer.premise
                # print("contact: ", customer.contact)
                # print('username : ', get_user.username)
                # print('email : ', get_user.email)
                # print('premise : ', customer.premise)

            else:
                get_user = User.objects.get(email=username)
                customer = Customer.objects.get(user=get_user)
                # contact = customer.contact
                # email=get_user.email
                # name=get_user.username
                # premise=customer.premise
                # print("get_user",get_user)

                print("email user: ", get_user)

                print("bard ki help se ho gaya: ", contact)
            context = {
                "name": name,
                "email": email,
                "contact": contact,
                "premise": premise
            }
            if get_user is not None:
                # User authentication successful
                login(request, get_user)
                print('logged in :', get_user)

                # Redirect to the dashboard or any other desired page
                return render(request, 'OE_dashboard.html')
            else:
                # User authentication failed
                error_message = 'Invalid email or password. Please try again.'
                return render(request, 'login.html', {'error_message': error_message})

                print(get_user)

            # Clear the OTP from the session
            del request.session['otp']

            # Redirect to success page or perform further actions
            # return redirect('registration_success')
            # return HttpResponse('success!!!')
        else:
            # OTP is invalid, display an error message or take appropriate action
            # Add your error handling logic here
            return HttpResponse("Invalid OTP!")
    return render(request, 'OE_dashboard.html')


@login_required(login_url='login_user')
@allowed_users(allowed_roles=['customer'])
def complain(request):
    if request.method == "POST":
        email = request.POST.get('email')
        pest_type = request.POST['pest_type']
        severity = request.POST['severity']
        date = request.POST['date']
        remark = request.POST['remark']
        # user = User.objects.get(email=email)
        user = request.user

        customer = Customer.objects.get(user=user)
        premise_name = customer.premise
        premise = get_object_or_404(Premises, PremisesName=premise_name)

        # request.user se krna jab already logged in hai user to fir se q object get kr rha hai
        # user.contact = contact
        user.premises = premise
        customer_complaint = Customer_complaint(user=user, premise=premise,
                                                pest_type=pest_type, severity=severity, date=date, remark=remark)
        customer_complaint.save()
        messages.success(
            request, "Your form has been submitted successfully!")
        return redirect('complain')

    return render(request, 'complain_form.html')


@login_required(login_url='login_user')
@allowed_users(allowed_roles=['customer'])
def complain_form(request):
    user = request.user
    customer = Customer.objects.get(user=user)
    name = user.username
    email = user.email
    contact = customer.contact
    premise = customer.premise

    context = {
        'name': name,
        'email': email,
        'contact': contact,
        'premise': premise
    }
   
    return render(request, 'complain_form.html', context)

# check list of complaints of logged user


@login_required(login_url='login_user')
@allowed_users(allowed_roles=['customer'])
def customer_history(request, id):

    # user = request.user
    # user_name = user.username
    print("logged user", request.user)
    all_complaints_of_user = Customer_complaint.objects.filter(
        user=request.user).values()
    print("all complaints of user", all_complaints_of_user)

    for complain in all_complaints_of_user:
        print("complain", complain)
        for c in complain:
            print("c", c)
    context = {
        'allComplaints': all_complaints_of_user
    }

    return render(request, 'allComplaints.html', context)


def view_logs(request, id):
    logs = Customer_status_Log.objects.filter(complaint_id=id).values()
    context = {
        "customer_status_log_list": logs
    }
    print("logs: ", logs)
    return render(request, "view_logs.html", context)


@login_required(login_url='login_user')
def logout_user(request):
    logout(request)
    return redirect('/')


#def social_login(request):

#    return render(request, 'social_login.html')

# def google_login(request):
#     # Call the social_auth view from social_django
#     response = social_auth(request, 'google-oauth2')

#     # Customize the response as needed
#     if isinstance(response, HttpResponse):
#         # Handle the HttpResponse returned by social_auth
#         return response

#     # Handle other cases if necessary
#     return HttpResponse("Login successful!")


@login_required(login_url='login_user')
def redirectuser(request):
    return render(request, 'redirect.html')


######### Operation Executive Logic starts ###############

def Operation_executive(request):

    return redirect('OE_login')


def OE_login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        
        # Try to retrieve the user object based on the email provided
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            # messages.warning(request, "Invalid credentials---!")
            return HttpResponseRedirect(request.path_info)
        
        # Authenticate the user using the provided username and password
        user_obj = authenticate(username=user.username, password=password)
        if user_obj is not None:
            if user_belongs_to_admin_group(user_obj):
                print("logging!!!")
                login(request, user_obj)
                print("logged", request.user)
                return render(request, 'OE_dashboard.html', {"user": user_obj})
            else:
                messages.warning(request, "Invalid credentials!")
                print("user is not from the admin group")
                return redirect('OE_login')
        else:
            messages.warning(request, "Invalid credentials!")
            return HttpResponseRedirect(request.path_info)

    return render(request, "OE_login.html")


@login_required(login_url='login_user')
@allowed_users(allowed_roles=['admin'])
def All_complaints(request):
    logged_in_operation_executive = request.user
    try:
        operation_executive = OE_list.objects.get(user=logged_in_operation_executive)
    except OE_list.DoesNotExist:
        return HttpResponse("Operation Executive data does not exist. Please contact the admin.")
    except MultipleObjectsReturned:
        # Handle the case when multiple objects are returned for the query
        # You can choose one of the objects or handle it based on your application's logic.
        operation_executive = OE_list.objects.filter(user=logged_in_operation_executive).first()
    premise_name = operation_executive.OE_premise
    print("premise name: ",premise_name)
    all_complaints = Customer_complaint.objects.filter(premise=premise_name).values()
    print("All complaints: ", all_complaints)

    context = {
        "allComplaints": all_complaints,
        'under_scrutiny': all_complaints.filter(status='under_scrutiny').count(),
        'progressed': all_complaints.filter(status='progressed').count(),
        'resolved': all_complaints.filter(status='resolved').count(),
        'not_addressed': all_complaints.filter(status='not_addressed').count(),
        "premise_name": premise_name
    }
    # Below function was done to return data in json form to frontend, was using jquery ajax never delete it
    # def queryset_to_json(all_complaints):
    #     """Converts a QuerySet into a JSON response."""
    #     data = []

    #     def default(o):
    #         if isinstance(o, datetime.date):
    #             return o.isoformat()
    #         else:
    #             return o
    #     for item in all_complaints:
    #         json_item = json.dumps(item, default=default)
    #         data.append(json_item)
    #     return data

    # json_response = queryset_to_json(all_complaints)

    return render(request, 'all_complaint_table.html', context)


#   Track status of complaints
@login_required(login_url='login_user')
@allowed_users(allowed_roles=['admin'])
def track_status(request, id):
    complain = Customer_complaint.objects.filter(id=id).values()
    print("complain with value: ", complain)
    complaint_status = complain[0]['status']
    print("complain status", complaint_status)
    print("id is:  ", id)
    print("user while tracking status: ", request.user)
    context = {
        'status': complain,
        'complaint_status': complaint_status
    }
    return render(request, "status.html", context)


# Updating staus of complaint by Opertaion executive
@login_required(login_url='login_user')
@allowed_users(allowed_roles=['admin'])
@require_POST
def update_complaint_status(request, id):

   

    status = request.POST.get("status")
   
    # Send email notification to customer

    print("before try")
    try:
        complaint = Customer_complaint.objects.get(id=id)
        complaint.status = status
        complaint.save()

        # creating logs for every update
        msg = f"Your complaint request has been modified by {request.user}"
        print("complaint", complaint)
        customer_status_Log = Customer_status_Log(
            complaint_request_status=complaint, complaint_id=id, message=msg)
        customer_status_Log.save()

        subject = 'Complaint Status Update'
        email_message = f'Your complaint with ID {id} has been updated to {status}.'
        send_mail(subject, email_message, f'{request.user.email}', [
                  complaint.user.email])
        return JsonResponse({"success": True})
    except Customer_complaint.DoesNotExist:
        return JsonResponse({"success": False})
## status Update#######


def complaint_feedback(request):
    if request.method == "POST":
        user = request.user
        customer_complaint = Customer_complaint.objects.get(id=10)
        customer_feedback = request.POST.get('feedback')
        feedback = Customer_Feedback(
            user=user, customer_complaint=customer_complaint, feedback=customer_feedback)
        feedback.save()
        print("customer feedback", customer_feedback)
        subject = 'Complaint Status Feedback Update'
        message = f'Your Feedback for complaint ID {customer_complaint.id} has been received successfuly!.'
        send_mail(subject, message, f'{request.user.email}', [
                  customer_complaint.user.email])
    return render(request, 'customer_feedback_form.html')

