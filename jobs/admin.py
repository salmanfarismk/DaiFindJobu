from django.contrib import admin
from .models import Profile, Company, Job, Skill, Application

admin.site.register(Profile)
admin.site.register(Company)
admin.site.register(Job)
admin.site.register(Skill)
admin.site.register(Application)


