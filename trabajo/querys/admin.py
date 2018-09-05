from django.contrib import admin

# Register your models here.

from .models import Author, Conference, ConferencePaper, ConferenceQuality, Journal, JournalPaper, Media, Paper, PaperQuality, Participate, Project, Quality, QualityIndex, Researcher

admin.site.register(Author)
admin.site.register(Conference)
admin.site.register(ConferencePaper)
admin.site.register(ConferenceQuality)
admin.site.register(Journal)
admin.site.register(JournalPaper)
admin.site.register(Media)
admin.site.register(Paper)
admin.site.register(PaperQuality)
admin.site.register(Participate)
admin.site.register(Project)
admin.site.register(Quality)
admin.site.register(QualityIndex)
admin.site.register(Researcher)

