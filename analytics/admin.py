from django.contrib import admin
from .models import Visitors


class VisitorsAdmin(admin.ModelAdmin):
    list_display = ["ip_add", "user_agent", "path", "created"]
    order_by = ["-created"]
    list_filter = ["path", "created"]


admin.site.register(Visitors, VisitorsAdmin)
