from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.edit import CreateView, UpdateView
from django.views import generic
from django.forms import formset_factory
from .models import Quilt, Customer
from .forms import CustomerForm

# Create your views here.
def customer_list(request):
    customers = Customer.get_active_customers()
    return render(request, "quilttracker/customer_index.html", {"customers": customers})


def customer_detail(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    return render(request, "quilttracker/customer_detail.html", {"customer": customer})


def customer_new(request):
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            customer = form.save(commit=False)
            customer.save()
            return redirect("customer_detail", pk=customer.pk)
    else:
        form = CustomerForm()
    return render(request, "quilttracker/customer_edit.html", {"form": form})


def customer_edit(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == "POST":
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            customer = form.save(commit=False)
            customer.save()
            return redirect("customer_detail", pk=customer.pk)
    else:
        form = CustomerForm(instance=customer)

    return render(request, "quilttracker/customer_edit.html", {"form": form})
