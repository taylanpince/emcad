# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Project.order'
        db.add_column('projects_project', 'order', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0), keep_default=False)

        # Adding field 'Category.order'
        db.add_column('projects_category', 'order', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0), keep_default=False)

        # Adding field 'Photo.order'
        db.add_column('projects_photo', 'order', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Project.order'
        db.delete_column('projects_project', 'order')

        # Deleting field 'Category.order'
        db.delete_column('projects_category', 'order')

        # Deleting field 'Photo.order'
        db.delete_column('projects_photo', 'order')


    models = {
        'projects.category': {
            'Meta': {'object_name': 'Category'},
            'blurb': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'order': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '255', 'db_index': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'projects.photo': {
            'Meta': {'object_name': 'Photo'},
            'caption': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'order': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'photos'", 'to': "orm['projects.Project']"})
        },
        'projects.project': {
            'Meta': {'object_name': 'Project'},
            'blurb': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'projects'", 'to': "orm['projects.Category']"}),
            'content': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'order': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '255', 'db_index': 'True'}),
            'subtitle': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['projects']
