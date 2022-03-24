from django.contrib import admin

# Register your models here.
from .models import Poll
admin.site.register(Poll)

from .models import Choice
admin.site.register(Choice)

from .models import Vote
admin.site.register(Vote)
