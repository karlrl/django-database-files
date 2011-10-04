# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'File.name'
        db.add_column('database_files_file', 'name', self.gf('django.db.models.fields.TextField')(default='_unspecified_'), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'File.name'
        db.delete_column('database_files_file', 'name')


    models = {
        'database_files.file': {
            'Meta': {'object_name': 'File'},
            'content': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {}),
            'size': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['database_files']
