from django.contrib import admin
from .models import Kitty,Expense
# Register your models here.

class KittyAdmin(admin.ModelAdmin):
    list_display = ('event_name','person1','person1_email','person2')

class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('paid_person','amount','exp_name','date')

admin.site.register(Kitty,KittyAdmin)
admin.site.register(Expense,ExpenseAdmin)