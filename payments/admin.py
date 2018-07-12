from django.contrib import admin

from .models import CreditTransfer

"""
Register Credit Transfer Model for Admin functionalities 
So Credit Transfer can be created ,deleted and Updated from Admin site (/admin)
"""

admin.site.register(CreditTransfer)
