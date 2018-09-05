# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Author(models.Model):
    paper = models.ForeignKey('Paper', models.DO_NOTHING, db_column='paper', primary_key=True)
    researcher = models.ForeignKey('Researcher', models.DO_NOTHING, db_column='researcher', blank=True, null=True)
    position = models.IntegerField(blank=True, primary_key=True)
    signature = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'Author'
        unique_together = (('position', 'paper'),)
  
    def __str__(self):
        return self.researcher, self.paper.num


class Conference(models.Model):
    id = models.IntegerField(unique=True, blank=True, primary_key=True)
    acronym = models.CharField(max_length=15, blank=True, null=True)
    name = models.CharField(max_length=250, blank=True, null=True)
    editor = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        db_table = 'Conference'

    def __str__(self):
        return self.id, self.name


class ConferencePaper(models.Model):
    paper = models.ForeignKey('Paper', models.DO_NOTHING, db_column='paper', primary_key=True)
    conference = models.ForeignKey('Conference', models.DO_NOTHING, db_column='conference', blank=True, null=True)
    edition = models.TextField(blank=True, null=True)
    isbn = models.TextField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    place = models.TextField(blank=True, null=True)
    editor = models.TextField(blank=True, null=True)
    type = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        db_table = 'Conference_paper'
        unique_together = (('paper', 'conference'),)

    def __str__(self):
        return self.paper.num, self.conference.name


class ConferenceQuality(models.Model):
    conference = models.ForeignKey('Conference', models.DO_NOTHING, db_column='conference', primary_key=True)
    quality = models.ForeignKey('Quality', models.DO_NOTHING, db_column='quality', primary_key=True)

    class Meta:
        db_table = 'Conference_quality'
        unique_together = (('conference', 'quality'),)

    def __str__(self):
        return self.conference.name, self.quality


class Journal(models.Model):
    id = models.IntegerField(unique=True, blank=True, primary_key=True )
    acronym = models.CharField(max_length=15, blank=True, null=True)
    name = models.TextField(blank=True, null=False)
    issn = models.CharField(max_length=15, blank=True, null=True)
    alt_issn = models.CharField(max_length=15, blank=True, null=True)
    isbn = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        db_table = 'Journal'

    def __str__(self):
        return self.id, self.name


class JournalPaper(models.Model):
    num = models.ForeignKey('Paper', models.DO_NOTHING, db_column='num', unique=True, primary_key=True)
    journal = models.ForeignKey('Journal', models.DO_NOTHING, db_column='journal', blank=True, null=True)
    issue = models.CharField(max_length=10, blank=True, null=True)
    volume = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        db_table = 'Journal_paper'
        unique_together = (('num', 'journal'),)

    def __str__(self):
        return self.num.num, self.journal.name


class Media(models.Model):
    paper = models.ForeignKey('Paper', models.DO_NOTHING, db_column='paper', primary_key=True)
    link = models.TextField(primary_key=True)

    class Meta:
        db_table = 'Media'
        unique_together = (('paper', 'link'),)

    def __str__(self):
        return self.link


class Paper(models.Model):
    num = models.IntegerField(unique=True, blank=True, primary_key=True)
    reference = models.CharField(unique=True, max_length=25, blank=True, null=True)
    title = models.TextField(blank=True, null=True)  # This field type is a guess.
    year = models.IntegerField(blank=True, null=True)
    doi = models.TextField(blank=True, null=True)
    pages = models.TextField(blank=True, null=True)  # This field type is a guess.
    nauthors = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'Paper'

    def __str__(self):
        return self.num, self.title, self.year


class PaperQuality(models.Model):
    paper = models.ForeignKey('Paper', models.DO_NOTHING, db_column='paper', primary_key=True)
    quality = models.ForeignKey('Quality', models.DO_NOTHING, db_column='quality', primary_key=True)
    description = models.CharField(max_length=300, blank=True, null=True)

    class Meta:
        db_table = 'Paper_quality'
        unique_together = (('paper', 'quality'),)

    def __str__(self):
        return self.paper.num, self.quality


class Participate(models.Model):
    project = models.ForeignKey('Project', models.DO_NOTHING, db_column='project', primary_key=True)
    researcher = models.ForeignKey('Researcher', models.DO_NOTHING, db_column='researcher', primary_key=True)
    roll = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'Participate'
        unique_together = (('project', 'researcher'),)

    def __str__(self):
        return self.project.title, self.researcher


class Project(models.Model):
    num = models.IntegerField(unique=True, primary_key=True)
    identificador = models.CharField(unique=True, max_length=30, blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    amount = models.TextField(blank=True, null=True)  # This field type is a guess.
    from_date = models.DateField(blank=True, null=True)
    to_date = models.DateField(blank=True, null=True)
    type = models.TextField(blank=True, null=True)
    other = models.TextField(blank=True, null=True)
    fund = models.TextField(blank=True, null=True)
    nresearchers = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'Project'

    def __str__(self):
        return self.num, self.title


class Quality(models.Model):
    id = models.CharField(unique=True, max_length=10, blank=True, primary_key=True)
    qindex = models.ForeignKey('QualityIndex', models.DO_NOTHING, db_column='qindex', blank=True, null=True)
    for_field = models.CharField(db_column='for', max_length=1, blank=True, null=True)  # Field renamed because it was a Python reserved word.
    value = models.TextField(blank=True, null=True)  # This field type is a guess.
    description = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        db_table = 'Quality'

    def __str__(self):
        return self.id


class QualityIndex(models.Model):
    id = models.CharField(unique=True, max_length=10, blank=True, primary_key=True)
    name = models.TextField(blank=True, null=True)
    web = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'Quality_index'

    def __str__(self):
        return self.id


class Researcher(models.Model):
    login = models.CharField(unique=True, max_length=15, primary_key=True)
    name = models.TextField()
    surnames = models.TextField()
    extern = models.IntegerField(blank=True, null=True)
    category = models.CharField(max_length=5, blank=True, null=True)
    roll = models.IntegerField(blank=True, null=True)
    signature = models.TextField(blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        db_table = 'Researcher'

    def __str__(self):
        return self.login
