from django.urls import path
from . import views

urlpatterns = [
    path("", views.register, name="register"),
    path("login/", views.login, name="login"),
    path("register/", views.register, name="register"),
    path("adduser/", views.adduser, name="adduser"),
    path("verify/", views.verify, name="verify"),
    path("update/<int:id>", views.update, name="update"),
    path("updateForm/<int:id>", views.updateForm, name="updateForm"),
    path("insurance/", views.insurance, name="insurance"),
    path("policy",views.policy, name='policy'),
    path("dashboard/<int:id>", views.dashboard, name="dashboard"),
    path("policy_cat", views.policy_cat, name="policy_cat"),



    path("ad_insurance/", views.ad_insurance, name="ad_insurance"),
    path("ad_dashboard", views.ad_dashboard, name="ad_dashboard"),

    path("ad_show_users", views.ad_show_users, name="ad_show_users"),
    path("ad_update_u/<int:id>", views.ad_update_u, name="ad_update_u"),
    path("ad_upd_form/<int:id>", views.ad_upd_form, name="ad_upd_form"),
    path("ad_delete_u/<int:id>", views.ad_delete_user, name="ad_delete_user"),
    path("ad_new_user", views.ad_new_user, name="ad_new_user"),
    path("ad_add_new_user", views.ad_add_new_user, name="ad_add_new_user"),
    
    path("ad_policy_cat", views.ad_policy_cat, name="ad_policy_cat"),
    
    path("ad_policy", views.ad_policy, name="ad_policy"),
    path("ad_update_p/<int:id>", views.ad_update_p, name="ad_update_p"),
    path("ad_upd_pform/<int:id>", views.ad_upd_pform, name="ad_upd_pform"),
    path("ad_add_policy", views.ad_add_policy, name="ad_add_policy"),
    path("ad_add_new_policy", views.ad_add_new_policy, name="ad_add_new_policy"),
    path("ad_delete_policy/<int:id>", views.ad_delete_policy, name="ad_delete_policy"),

    path("ad_h_policy",views.ad_h_policy, name="ad_h_policy"),
    path("ad_update_h_policy/<int:id>",views.ad_update_h_policy, name="ad_update_h_policy"),
    path("ad_updated_h_policy/<int:id>",views.ad_updated_h_policy, name="ad_updated_h_policy"),
    path("ad_delete_h_policy/<int:id>",views.ad_delete_h_policy, name="ad_delete_h_policy"),
    path("ad_add_h_policy",views.ad_add_h_policy, name="ad_add_h_policy"),
    path("ad_added_h_policy",views.ad_added_h_policy, name="ad_added_h_policy"),
]
