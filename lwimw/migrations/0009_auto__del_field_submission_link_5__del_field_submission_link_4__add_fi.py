# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Submission.link_5'
        db.delete_column(u'lwimw_submission', 'link_5')

        # Deleting field 'Submission.link_4'
        db.delete_column(u'lwimw_submission', 'link_4')

        # Adding field 'Submission.image_1'
        db.add_column(u'lwimw_submission', 'image_1',
                      self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Submission.image_2'
        db.add_column(u'lwimw_submission', 'image_2',
                      self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Submission.image_3'
        db.add_column(u'lwimw_submission', 'image_3',
                      self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Submission.used_theme'
        db.add_column(u'lwimw_submission', 'used_theme',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)


        # Changing field 'Submission.link_3'
        db.alter_column(u'lwimw_submission', 'link_3', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'Submission.link_2'
        db.alter_column(u'lwimw_submission', 'link_2', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'Submission.link_1'
        db.alter_column(u'lwimw_submission', 'link_1', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

        # Changing field 'Post.image'
        db.alter_column(u'lwimw_post', 'image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True))

    def backwards(self, orm):
        # Adding field 'Submission.link_5'
        db.add_column(u'lwimw_submission', 'link_5',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True),
                      keep_default=False)

        # Adding field 'Submission.link_4'
        db.add_column(u'lwimw_submission', 'link_4',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True),
                      keep_default=False)

        # Deleting field 'Submission.image_1'
        db.delete_column(u'lwimw_submission', 'image_1')

        # Deleting field 'Submission.image_2'
        db.delete_column(u'lwimw_submission', 'image_2')

        # Deleting field 'Submission.image_3'
        db.delete_column(u'lwimw_submission', 'image_3')

        # Deleting field 'Submission.used_theme'
        db.delete_column(u'lwimw_submission', 'used_theme')


        # Changing field 'Submission.link_3'
        db.alter_column(u'lwimw_submission', 'link_3', self.gf('django.db.models.fields.CharField')(default='', max_length=255))

        # Changing field 'Submission.link_2'
        db.alter_column(u'lwimw_submission', 'link_2', self.gf('django.db.models.fields.CharField')(default='', max_length=255))

        # User chose to not deal with backwards NULL issues for 'Submission.link_1'
        raise RuntimeError("Cannot reverse this migration. 'Submission.link_1' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'Submission.link_1'
        db.alter_column(u'lwimw_submission', 'link_1', self.gf('django.db.models.fields.CharField')(max_length=255))

        # User chose to not deal with backwards NULL issues for 'Post.image'
        raise RuntimeError("Cannot reverse this migration. 'Post.image' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'Post.image'
        db.alter_column(u'lwimw_post', 'image', self.gf('django.db.models.fields.files.ImageField')(max_length=100))

    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'lwimw.category': {
            'Meta': {'object_name': 'Category'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'lwimw.contest': {
            'Meta': {'object_name': 'Contest'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number': ('django.db.models.fields.PositiveIntegerField', [], {'unique': 'True'}),
            'start_time': ('django.db.models.fields.DateTimeField', [], {}),
            'theme': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'lwimw.post': {
            'Meta': {'object_name': 'Post'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'posts'", 'to': u"orm['auth.User']"}),
            'body': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'contest': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'posts'", 'to': u"orm['lwimw.Contest']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'lwimw.rating': {
            'Meta': {'object_name': 'Rating'},
            'artistry': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'comments': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'innovation': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'overall': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'rater': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'ratings'", 'to': u"orm['auth.User']"}),
            'refinement': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'submission': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'ratings'", 'to': u"orm['lwimw.Submission']"}),
            'theme': ('django.db.models.fields.PositiveIntegerField', [], {})
        },
        u'lwimw.submission': {
            'Meta': {'object_name': 'Submission'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'submissions'", 'to': u"orm['lwimw.Category']"}),
            'comments': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'contest': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'submissions'", 'to': u"orm['lwimw.Contest']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_1': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'image_2': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'image_3': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'link_1': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'link_2': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'link_3': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'receive_ratings': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'used_theme': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'submissions'", 'to': u"orm['auth.User']"})
        }
    }

    complete_apps = ['lwimw']