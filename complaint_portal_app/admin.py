from django.contrib import admin
from .models import State, Premises, Customer, Customer_complaint, OE_list,Customer_Feedback,Customer_status_Log
from django.contrib.auth.models import User

# Register your models here.


class StateAdmin(admin.ModelAdmin):
    list_display = ('id', 'StateName')


class PremisesAdmin(admin.ModelAdmin):
    list_display = ('id', 'PremisesName')


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'contact', 'premise')


class Customer_complaint_Admin(admin.ModelAdmin):
    list_display = ('id','user', 'pest_type', 'severity', 'premise',
                    'remark', 'status', 'date')
class Customer_Feedback_Admin(admin.ModelAdmin):
    list_display=('id','feedback')

class Customer_status_Log_Admin(admin.ModelAdmin):
    list_display=('id',"complaint_id","complaint_request_status",'message','timestamp')

admin.site.register(Customer_status_Log,Customer_status_Log_Admin)
admin.site.register(State, StateAdmin)
admin.site.register(Premises, PremisesAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Customer_complaint, Customer_complaint_Admin)
admin.site.register(Customer_Feedback, Customer_Feedback_Admin)



##############OE Details####################
class OE_Admin(admin.ModelAdmin):
    list_display = ('id', 'name')


admin.site.register(OE_list, OE_Admin)
