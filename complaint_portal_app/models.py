from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
# from social_django.models import UserSocialAuth
# from allauth.socialaccount.signals import social_account_added
from complaint_portal import settings
from django.db import models
from django.db.models.signals import post_save
from django.core.mail import send_mail
 
# Create your models here.


# @receiver(social_account_added)
# def grab_user_info(request, sociallogin, **kwargs):
#     user = sociallogin.user
#     if isinstance(user, User):
#         # The user is already created and logged in
#         email = user.email
#         name = user.get_full_name()
#     else:
#         # The user is being created
#         social_user = UserSocialAuth.objects.get(user=user)
#         email = social_user.extra_data.get('email')
#         name = social_user.extra_data.get('name')

#     # Use the email and name as needed
#     print('Email:', email)
#     print('Name:', name)


class State(models.Model):
    StateName = models.CharField(max_length=100)
    # Add other fields for the state

    def __str__(self):
        return self.StateName


class Premises(models.Model):
    PremisesName = models.CharField(max_length=100)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    # Add other fields for the premises

    def __str__(self):
        return self.PremisesName





class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL,null=True,blank=True)

    name=models.CharField(max_length=50,default="")
    # email=models.EmailField(max_length=50,default="")
    contact=models.IntegerField(unique=True)
    premise=models.CharField(max_length=60,default="")
    
    def __str__(self):
        return self.name 

class Customer_complaint(models.Model):
    STATUS_CHOICES = (
        ('under_scrutiny', 'Complaint Under Scrutiny'),
        ('progressed', 'Progressed'),
        ('resolved', 'Resolved'),
        ('not_addressed', 'Not Addressed'),
    )
    user = models.ForeignKey(User, on_delete=models.SET_NULL,null=True,blank=True)
    premise=models.ForeignKey(Premises,on_delete=models.SET_NULL,null=True,blank=True)
    pest_type=models.CharField(max_length=50,default="")
    severity=models.CharField(max_length=50,default="") 
    remark=models.TextField(max_length=300)
    date= models.DateField()
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default="under_scrutiny")


    def __str__(self):
        return self.user.username 

class Customer_status_Log(models.Model):
    # user = models.ForeignKey(User, on_delete=models.SET_NULL,null=True,blank=True)

    complaint_request_status = models.ForeignKey(Customer_complaint, on_delete=models.SET_NULL,null=True,blank=True)
    complaint_id=models.IntegerField(default=0)
    message = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)

class Customer_Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL,null=True,blank=True)

    customer_complaint=models.ForeignKey(Customer_complaint,on_delete=models.SET_NULL,null=True,blank=True)
    feedback=models.CharField(max_length=250 ,null=False)

######## OE models starts ##########

class OE_list(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL,null=True,blank=True)
    OE_premise=models.ForeignKey(Premises,on_delete=models.SET_NULL,null=True,blank=True)
    name=models.CharField(max_length=250)
    # email=models.CharField(max_length=250,default="")
    password=models.CharField(max_length=250)
    def __str__(self):
        return self.name




#### tracking status of complaint using django signals #####
# @receiver(post_save, sender=Customer_complaint)
# def send_complaint_status_email(sender, instance, created, **kwargs):
#     if created:
#         subject = 'Complaint Status Update'
#         message = f'Your complaint with ID {instance.id} has been under scrutiny'
#         send_mail(subject, message,'alamshamshad598@gmail.com', [instance.user.email])

#     elif instance.status == 'progressed':
#         subject = 'Complaint Status Update'
#         message = f'Your complaint with ID {instance.id} has been progressed.'
#         send_mail(subject, message, 'shamshad.alam@rentokil-pci.com', [instance.user.email])

#     elif instance.status == 'resolved':
#         subject = 'Complaint Status Update'
#         message = f'Your complaint with ID {instance.id} has been resolved.'
#         send_mail(subject, message,'shamshad.alam@rentokil-pci.com', [instance.user.email])

#     elif instance.status == 'not_addressed':
#         subject = 'Complaint Status Update'
#         message = f'Your complaint with ID {instance.id} has not been addressed.'
#         send_mail(subject, message,'shamshad.alam@rentokil-pci.com', [instance.user.email])

# Custom method to update complaint status by operation executive
# def update_complaint_status(complaint_id, status):
#     complaint = Customer_complaint.objects.get(id=complaint_id)
#     complaint.status = status
#     complaint.save()

#     # Send email notification to customer
#     subject = 'Complaint Status Update'
#     message = f'Your complaint with ID {complaint_id} has been updated to {status}.'
#     send_mail(subject, message, f'{request.user.email}', [complaint.user.email])