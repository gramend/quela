from django.contrib import admin

from .models import (
    Tag,
    Question,
)

admin.site.register([
    Tag,
    Question,
])
