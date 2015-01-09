# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Instance'
        db.create_table(u'instances_instance', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ami_id', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('instance_type', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('availability_zone', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('access_key_id', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('secret_access_key', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('running', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'instances', ['Instance'])


    def backwards(self, orm):
        # Deleting model 'Instance'
        db.delete_table(u'instances_instance')


    models = {
        u'instances.instance': {
            'Meta': {'object_name': 'Instance'},
            'access_key_id': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'ami_id': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'availability_zone': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'instance_type': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'running': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'secret_access_key': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['instances']