from django.contrib import admin
from . import models


admin.site.register(models.ProjectDocument)
admin.site.register(models.ProjectComponent)
admin.site.register(models.ProjectDocumentComponent)
admin.site.register(models.CBWPQuantum)