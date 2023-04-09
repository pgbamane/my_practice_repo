from django.shortcuts import render
from .models import Customer, Profile


# Create your views here.

def customer_details_manage(request):
    if request.method == "GET":
        # customers = Customer.objects.all()
        # # return render(request, template_name="customer/customer_manage.html",
        # #               context={'customers': customers})
        # new_cust = Customer(name="Prishy",
        #                     phone_number="8767565676",
        #                     city="Melbourne")
        # new_cust.save()
        profile = Profile.objects.all()

        return render(request, template_name="customer/customer_manage.html",
                      context={})
