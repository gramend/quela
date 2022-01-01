from django.contrib import admin

from .models import (
    Category,
    Question,
    Answer,
)

admin.site.register([
    Category,
    Question,
    Answer,
])
