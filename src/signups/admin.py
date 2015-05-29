from django.contrib import admin
from .models import SignUp, Marticle,Sarticle
# Register your models here.

class SignUpAdmin(admin.ModelAdmin):
    class Meta:
        model=SignUp
admin.site.register(SignUp,SignUpAdmin)
admin.site.register(Marticle)
admin.site.register(Sarticle)