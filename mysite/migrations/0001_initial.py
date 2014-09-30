# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):
    def forwards(self, orm):
        # Adding model 'Phrase'
        db.create_table(u'mysite_phrase', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('month', self.gf('django.db.models.fields.IntegerField')(default=15)),
            ('day', self.gf('django.db.models.fields.IntegerField')(default=15)),
            ('body', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('mysite', ['Phrase'])


    def backwards(self, orm):
        # Deleting model 'Phrase'
        db.delete_table(u'mysite_phrase')


    models = {
        'mysite.phrase': {
            'Meta': {'object_name': 'Phrase'},
            'body': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'day': ('django.db.models.fields.IntegerField', [], {'default': '15'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'month': ('django.db.models.fields.IntegerField', [], {'default': '15'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        }
    }

    complete_apps = ['mysite']