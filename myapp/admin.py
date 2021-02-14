from django.contrib import admin
# from users.models import trainAdmin
from . models import account, accountAdmin, receipt,receiptAdmin, teaching, teachingAdmin, serviceteam, serviceteamAdmin
admin.site.register(account)
admin.site.register(receipt,receiptAdmin)
# admin.site.register(receipt,receiptAdmin)
admin.site.register(teaching,teachingAdmin)
admin.site.register(serviceteam,serviceteamAdmin)

# Register your models here.
