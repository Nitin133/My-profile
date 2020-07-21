from django.conf.urls import url
from .import views
urlpatterns=[
    url("regs",views.regs,name="regs"),
    url("",views.web,name="web")

]