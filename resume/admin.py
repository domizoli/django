from django.contrib import admin
from .models import cv_user
from .models import cv_user_education
from .models import cv_user_language
from .models import cv_user_work_expercience

admin.site.register(cv_user)
admin.site.register(cv_user_education)
admin.site.register(cv_user_language)
admin.site.register(cv_user_work_expercience)