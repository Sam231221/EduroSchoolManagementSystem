from django.contrib import admin

from MUtilities.models import Membership, MemebershipPlan


class MembershipPlanAdmin(admin.TabularInline):
   model = MemebershipPlan
   extra = 5
  
class MembershipAdmin(admin.ModelAdmin):
   inlines = [MembershipPlanAdmin]   
   
admin.site.register(Membership, MembershipAdmin)

