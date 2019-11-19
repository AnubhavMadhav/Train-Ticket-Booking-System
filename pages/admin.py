from django.contrib import admin
#from .models import Book
from .models import Train, Ticket, Coach

# Register your models here.
##admin.site.register(Book)
admin.site.register(Train)
admin.site.register(Ticket)
admin.site.register(Coach)