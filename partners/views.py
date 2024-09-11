from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Partner
from .forms import PartnerForm

# Admin Login
def admin_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

# Dashboard
@login_required
def dashboard(request):
    partners_count = Partner.objects.count()
    partners = Partner.objects.all()
    return render(request, 'dashboard.html', {'partners': partners, 'partners_count': partners_count})

# Partner List
@login_required
def partner_list(request):
    search_query = request.GET.get('search', '')
    if search_query:
        partners = Partner.objects.filter(name__icontains=search_query)
    else:
        partners = Partner.objects.all()
    return render(request, 'partner_list.html', {'partners': partners})

# Add New Partner
@login_required
def add_partner(request):
    if request.method == 'POST':
        form = PartnerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('partner_list')
    else:
        form = PartnerForm()
    return render(request, 'add_partner.html', {'form': form})

# Partner Details
@login_required
def partner_detail(request, pk):
    partner = get_object_or_404(Partner, pk=pk)
    return render(request, 'partner_detail.html', {'partner': partner})

# Edit Partner
@login_required
def edit_partner(request, pk):
    partner = get_object_or_404(Partner, pk=pk)
    if request.method == 'POST':
        form = PartnerForm(request.POST, instance=partner)
        if form.is_valid():
            form.save()
            return redirect('partner_list')
    else:
        form = PartnerForm(instance=partner)
    return render(request, 'edit_partner.html', {'form': form})