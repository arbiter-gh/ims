from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from .models import *
from .forms import *

# Create your views here.


def login(request):
    return render(request, "login.html")


def register(request):
    return render(request, "register.html")


def home(request):
    return render(request, "home.html")


def adduser(request):
    if request.method == "POST":
        u = user()
        u.user_type = request.POST.get("usertype")
        u.f_name = request.POST.get("f_name")
        u.l_name = request.POST.get("l_name")
        u.email = request.POST.get("email")
        u.phone = request.POST.get("phone")
        u.gender = request.POST.get("genderInput")
        u.password = request.POST.get("password")
        u.save()

        messages.success(request, f"Registration Successful. Now you can login.")
        return redirect("login")

    return redirect("register")


def verify(request):
    usertype = request.POST.get("usertype")
    email = request.POST.get("email")
    password = request.POST.get("password")

    try:
        u = user.objects.get(user_type=usertype, email=email, password=password)
        if u.user_type == "admin":
            return render(request, "ad_insurance.html", {"u": u})
        return render(request, "insurance.html", {"u": u})
    except:
        messages.warning(request, f"Email/Password wrong!")
        return redirect("login")


def insurance(request):
    return render(request, "insurance.html")


def ad_insurance(request):
    # u = user.objects.get(id=id)
    return render(request, "ad_insurance.html")


def update(request, id):
    u = user.objects.get(id=id)
    context = {
        "u": u,
    }
    return render(request, "update.html", context)


def updateForm(request, id):
    u = user.objects.get(id=id)
    f = uform(request.POST, instance=u)
    context = {
        "u": u,
    }

    if f.is_valid():
        f.save()
        return render(request, "insurance.html", context)
    return render(request, "update.html", context)


def policy(request):
    policies = term_insurance.objects.all()

    return render(request, "policy.html", {"policies": policies})


def ad_show_users(request):
    users = user.objects.all()
    return render(request, "ad_show_user.html", {"users": users})


def ad_update_u(request, id):
    u = user.objects.get(id=id)
    return render(request, "ad_update_u.html", {"u": u})


def ad_upd_form(request, id):
    u = user.objects.get(id=id)
    f = ad_update_form(request.POST, instance=u)

    if f.is_valid():
        f.save()
        return redirect("ad_show_users")
    return render(request, "ad_update.html", {"u": u})


def ad_delete_user(request, id):
    u = user.objects.get(id=id)
    u.delete()
    return redirect("ad_show_users")


def ad_new_user(request):
    return render(request, "ad_new_user.html")


def ad_add_new_user(request):
    if request.method == "POST":
        u = user()
        u.user_type = request.POST.get("usertype")
        u.f_name = request.POST.get("f_name")
        u.l_name = request.POST.get("l_name")
        u.email = request.POST.get("email")
        u.phone = request.POST.get("phone")
        u.gender = request.POST.get("genderInput")
        u.password = request.POST.get("password")
        u.save()

        return redirect("ad_show_users")

    return redirect("ad_new_user")


def ad_policy(request):
    policies = term_insurance.objects.all()
    return render(request, "ad_policy.html", {"policies": policies})


def ad_update_p(request, id):
    p = term_insurance.objects.get(id=id)
    return render(request, "ad_update_p.html", {"p": p})


def ad_upd_pform(request, id):
    p = term_insurance.objects.get(id=id)
    f = ad_update_pform(request.POST, instance=p)

    if f.is_valid():
        f.save()
        return redirect("ad_policy")
    return redirect("ad_update_p", {"p": p})


def ad_add_policy(request):
    return render(request, "ad_add_policy.html")


def ad_add_new_policy(request):
    if request.method == "POST":
        p = term_insurance()
        p.insuor = request.POST.get("insuor")
        p.life_cover = request.POST.get("life_cover")
        p.cover_till_age = request.POST.get("cover_till_age")
        p.claim_settelment = request.POST.get("claim_settelment")
        p.pay_monthly = request.POST.get("pay_monthly")
        p.save()

        return redirect("ad_policy")


def ad_delete_policy(request, id):
    p = term_insurance.objects.get(id=id)
    p.delete()
    return redirect("ad_policy")


def ad_h_policy(request):
    obj = health_insurance.objects.all()
    return render(request, "ad_h_policy.html", {"obj": obj})


def ad_update_h_policy(request, id):
    obj = health_insurance.objects.get(id=id)
    return render(request, "ad_update_h_policy.html", {"obj": obj})


def ad_updated_h_policy(request, id):
    h = health_insurance.objects.get(id=id)
    f = ad_update_h_form(request.POST, instance=h)

    if f.is_valid():
        f.save()
        return redirect("ad_h_policy")
    return redirect("ad_update_h_policy", {"obj": h})


def ad_delete_h_policy(request, id):
    h = health_insurance.objects.get(id=id)
    h.delete()
    return redirect("ad_h_policy")

def ad_add_h_policy(request):
    return render(request, "ad_add_h_policy.html")


def ad_added_h_policy(request):
    if request.method == "POST":
        try:
            h = health_insurance()
            h.policy_name = request.POST.get("policy_name")
            h.cover_amount = request.POST.get("cover_amount")
            h.policy_period = request.POST.get("policy_period")
            h.pay_monthly = request.POST.get("pay_monthly")

            h.save()

            return redirect("ad_h_policy")
        except:
            return redirect("ad_add_h_policy")
    return redirect("ad_add_h_policy")


def ad_policy_cat(request):
    return render(request, "ad_policy_cat.html")

def ad_dashboard(request):
    return render(request, "ad_dashboard.html")

def dashboard(request,id):
    u = user.objects.get(id=id)
    return render(request, "dashboard.html",{'u':u})

def policy_cat(request):
    return render(request, "policy_cat.html")