from django.http.response import HttpResponseRedirect
from basicbanking.models import Transaction
from django.shortcuts import redirect, render
from basicbanking.models import Customer
from django.urls import reverse
from django.contrib import messages

# Create your views here.
def home(request):
    customers = Customer.objects.all()
    return render(request, 'basicbanking/home.html', {'customers' : customers})

def home_post(request,key):
    customers = Customer.objects.all()
    customer = Customer.objects.get(id=key)
    if request.method == 'POST':
        transaction_amt = ""
        return render(request, 'basicbanking/customer.html', {'customers' : customers, 'customer':customer, 'transaction_amt':transaction_amt})
    
    return render(request, 'basicbanking/customer.html', {'customers' : customers, 'customer':customer,})

def transaction(request,key):
    if request.method == 'POST':
        From = Customer.objects.get(id=key).name
        To = Customer.objects.get(id=request.POST["customer__list"]).name
        transaction_amt = request.POST["amount"]

        if transaction_amt == "":
            print("tran:", transaction_amt)
            messages.error(request, 'Amount can not be empty!')
            return HttpResponseRedirect(reverse('post-home', args=(key,)))

        if int(transaction_amt) > Customer.objects.get(id=key).current_balance:
            messages.error(request, 'Insufficient Balance!')
            return HttpResponseRedirect(reverse('post-home', args=(key,)))

        Transaction.objects.create(
            From = From,
            To = To,
            transaction_amt = int(transaction_amt),
        )

        remaining = Customer.objects.get(id=key).current_balance - int(transaction_amt);
        ob = Customer.objects.get(id=key)
        ob.current_balance = remaining
        ob.save()

        ob = Customer.objects.get(id=request.POST["customer__list"])
        ob.current_balance += int(transaction_amt)
        ob.save()

        msg = "Transaction Successful!"
        return render(request, 'basicbanking/transaction.html', {'transactions' : Transaction.objects.all().order_by('-datetime'), 'msg':msg})
    
    return render(request, 'basicbanking/transaction.html', {'transactions' : Transaction.objects.all().order_by('-datetime')})

