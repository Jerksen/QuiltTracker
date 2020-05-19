from django.contrib import admin
from .models import Quilt, Customer

# Register your models here.
class QuiltInline(admin.TabularInline):
    model = Quilt
    extra = 0


class CustomerAdmin(admin.ModelAdmin):
    list_display = ("firstname", "lastname", "email", "status")
    fieldsets = [
        (None, {"fields": ["firstname", "lastname"]}),
        ("Contact Info", {"fields": ["email"]}),
    ]
    inlines = [QuiltInline]
    list_filter = ["status"]
    search_fields = ["firstname", "lastname", "email"]


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Quilt)
