from django.contrib import admin
from .models import Tutorial
from django.db import models
# Register your models here.

class TutorialAdmin(admin.ModelAdmin):
	# # Will appear in order accordingly - overrides existing Model
	# fields = ["tutorial_published",
	# 		  "tutorial_title",
	# 		  "tutorial_content"]

	# Using fieldsets instead of fields lets you group together fields
	fieldsets = [
		("Title/date", {"fields": ["tutorial_title", "tutorial_published"]}),
		("Content", {"fields": ["tutorial_content"]})
	]

admin.site.register(Tutorial, TutorialAdmin)