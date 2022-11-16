from django.urls import path
from . import views

urlpatterns = [
	path("", views.index, name="index"),
	path("add/", views.add, name="add"),
	path("add/addrecord", views.addrecord, name="addrecord"),
	path("delete/<int:id>", views.delete, name="delete"),
	path("update/<int:id>", views.update, name="update"),
	path("update/updaterecord/<int:id>", views.updaterecord, name="updaterecord"),
	path("addcomment/", views.addcomment, name="addcomment"),
	path("addcomment/submitcomment", views.submitcomment, name="submitcomment"),
	path("deletecomment/<int:id>", views.deletecomment, name="deletecomment"),
]