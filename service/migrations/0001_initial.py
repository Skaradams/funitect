# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Game'
        db.create_table('service_game', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256)),
        ))
        db.send_create_signal('service', ['Game'])

        # Adding model 'UserGame'
        db.create_table('service_usergame', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('game', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['service.Game'])),
        ))
        db.send_create_signal('service', ['UserGame'])

        # Adding model 'ElementKind'
        db.create_table('service_elementkind', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('game', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['service.Game'])),
        ))
        db.send_create_signal('service', ['ElementKind'])

        # Adding model 'Element'
        db.create_table('service_element', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('kind', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['service.ElementKind'])),
        ))
        db.send_create_signal('service', ['Element'])

        # Adding model 'EventKind'
        db.create_table('service_eventkind', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('game', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['service.Game'])),
            ('sentence', self.gf('django.db.models.fields.CharField')(max_length=256)),
        ))
        db.send_create_signal('service', ['EventKind'])

        # Adding model 'Event'
        db.create_table('service_event', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('kind', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['service.EventKind'])),
        ))
        db.send_create_signal('service', ['Event'])

        # Adding model 'EventElement'
        db.create_table('service_eventelement', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('event', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['service.Event'])),
            ('element', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['service.Element'])),
            ('identity', self.gf('django.db.models.fields.CharField')(max_length=32)),
        ))
        db.send_create_signal('service', ['EventElement'])

        # Adding model 'Comment'
        db.create_table('service_comment', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('event', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['service.Event'])),
            ('text', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('service', ['Comment'])


    def backwards(self, orm):
        
        # Deleting model 'Game'
        db.delete_table('service_game')

        # Deleting model 'UserGame'
        db.delete_table('service_usergame')

        # Deleting model 'ElementKind'
        db.delete_table('service_elementkind')

        # Deleting model 'Element'
        db.delete_table('service_element')

        # Deleting model 'EventKind'
        db.delete_table('service_eventkind')

        # Deleting model 'Event'
        db.delete_table('service_event')

        # Deleting model 'EventElement'
        db.delete_table('service_eventelement')

        # Deleting model 'Comment'
        db.delete_table('service_comment')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'service.comment': {
            'Meta': {'object_name': 'Comment'},
            'event': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['service.Event']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {})
        },
        'service.element': {
            'Meta': {'object_name': 'Element'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'kind': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['service.ElementKind']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        'service.elementkind': {
            'Meta': {'object_name': 'ElementKind'},
            'game': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['service.Game']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        'service.event': {
            'Meta': {'object_name': 'Event'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'kind': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['service.EventKind']"})
        },
        'service.eventelement': {
            'Meta': {'object_name': 'EventElement'},
            'element': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['service.Element']"}),
            'event': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['service.Event']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'identity': ('django.db.models.fields.CharField', [], {'max_length': '32'})
        },
        'service.eventkind': {
            'Meta': {'object_name': 'EventKind'},
            'game': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['service.Game']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sentence': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        'service.game': {
            'Meta': {'object_name': 'Game'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        'service.usergame': {
            'Meta': {'object_name': 'UserGame'},
            'game': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['service.Game']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        }
    }

    complete_apps = ['service']
