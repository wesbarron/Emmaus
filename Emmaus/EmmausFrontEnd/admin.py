from django.contrib import admin
from .models import TodoItem, GatheringInformation, BoardMember, Pilgrim

# Register your models here.
admin.site.register(TodoItem)
admin.site.register(GatheringInformation)
admin.site.register(BoardMember)
admin.site.register(Pilgrim)