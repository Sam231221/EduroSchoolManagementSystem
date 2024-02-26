from django.contrib import admin
from .models import Student, EducationalInstitution
from .models import Teacher


# Register your models here.


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','email', 'full_name', 'gender',
                    'date_of_birth', 'blood_group', 'religion']
    search_fields = ['email', 'first_name', 'last_name']
    list_filter = ['gender', 'blood_group', 'religion']
    readonly_fields = ['full_name']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name','bio', 'gender', 'date_of_birth', 'blood_group',
         'religion', 'section', 'class_no', 'roll', 'admission_id', 'parent_name', 'address', 'phone', 'photo')}),
        ('Permissions', {'fields': ('is_active', 'is_staff',
         'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )


class TeacherAdmin(admin.ModelAdmin):
    list_display = ('id','first_name', 'last_name', 'email', 'gender', 'date_of_birth', 'mobile', 'joining_date',
                    'qualification', 'experience', 'address', 'city', 'state', 'zip_code', 'country', 'is_active')
    list_filter = ('gender', 'is_active')
    search_fields = ('first_name', 'last_name', 'email')
    list_editable = ('is_active',)

    # Add custom validation for the password field
 


admin.site.register(Teacher, TeacherAdmin)


@admin.register(EducationalInstitution)
class EducationalInstitutionAdmin(admin.ModelAdmin):
    list_display = ['name', 'owner', 'type',
                    'category', 'accreditation_status']
    search_fields = ['name', 'owner__email']
    readonly_fields = ['id']
