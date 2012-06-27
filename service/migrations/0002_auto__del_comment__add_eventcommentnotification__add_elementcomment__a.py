# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting model 'Comment'
        db.delete_table('service_comment')

        # Adding model 'EventCommentNotification'
        db.create_table('service_eventcommentnotification', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('game', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['service.Game'])),
            ('timestamp', self.gf('django.db.models.fields.IntegerField')()),
            ('comment', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['service.EventComment'])),
        ))
        db.send_create_signal('service', ['EventCommentNotification'])

        # Adding model 'ElementComment'
        db.create_table('service_elementcomment', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('element', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['service.Element'])),
            ('text', self.gf('django.db.models.fields.TextField')()),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
        ))
        db.send_create_signal('service', ['ElementComment'])

        # Adding model 'ElementSketchNotification'
        db.create_table('service_elementsketchnotification', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('game', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['service.Game'])),
            ('timestamp', self.gf('django.db.models.fields.IntegerField')()),
            ('sketch', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['service.ElementSketch'])),
        ))
        db.send_create_signal('service', ['ElementSketchNotification'])

        # Adding model 'EventComment'
        db.create_table('service_eventcomment', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('event', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['service.Event'])),
            ('text', self.gf('django.db.models.fields.TextField')()),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
        ))
        db.send_create_signal('service', ['EventComment'])

        # Adding model 'ElementNotification'
        db.create_table('service_elementnotification', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('game', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['service.Game'])),
            ('timestamp', self.gf('django.db.models.fields.IntegerField')()),
            ('element', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['service.Element'])),
        ))
        db.send_create_signal('service', ['ElementNotification'])

        # Adding model 'ElementCommentNotification'
        db.create_table('service_elementcommentnotification', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('game', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['service.Game'])),
            ('timestamp', self.gf('django.db.models.fields.IntegerField')()),
            ('comment', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['service.ElementComment'])),
        ))
        db.send_create_signal('service', ['ElementCommentNotification'])

        # Adding model 'ElementSketch'
        db.create_table('service_elementsketch', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('element', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['service.Element'])),
            ('sketch_source', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
        ))
        db.send_create_signal('service', ['ElementSketch'])

        # Adding model 'EventNotification'
        db.create_table('service_eventnotification', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('game', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['service.Game'])),
            ('timestamp', self.gf('django.db.models.fields.IntegerField')()),
            ('event', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['service.Event'])),
        ))
        db.send_create_signal('service', ['EventNotification'])

        # Adding field 'Element.user'
        db.add_column('service_element', 'user', self.gf('django.db.models.fields.related.ForeignKey')(default=0, to=orm['auth.User']), keep_default=False)

        # Adding field 'Event.user'
        db.add_column('service_event', 'user', self.gf('django.db.models.fields.related.ForeignKey')(default=0, to=orm['auth.User']), keep_default=False)


    def backwards(self, orm):
        
        # Adding model 'Comment'
        db.create_table('service_comment', (
            ('text', self.gf('django.db.models.fields.TextField')()),
            ('event', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['service.Event'])),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('service', ['Comment'])

        # Deleting model 'EventCommentNotification'
        db.delete_table('service_eventcommentnotification')

        # Deleting model 'ElementComment'
        db.delete_table('service_elementcomment')

        # Deleting model 'ElementSketchNotification'
        db.delete_table('service_elementsketchnotification')

        # Deleting model 'EventComment'
        db.delete_table('service_eventcomment')

        # Deleting model 'ElementNotification'
        db.delete_table('service_elementnotification')

        # Deleting model 'ElementCommentNotification'
        db.delete_table('service_elementcommentnotification')

        # Deleting model 'ElementSketch'
        db.delete_table('service_elementsketch')

        # Deleting model 'EventNotification'
        db.delete_table('service_eventnotification')

        # Deleting field 'Element.user'
        db.delete_column('service_element', 'user_id')

        # Deleting field 'Event.user'
        db.delete_column('service_event', 'user_id')


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
        'service.element': {
            'Meta': {'object_name': 'Element'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'kind': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['service.ElementKind']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'service.elementcomment': {
            'Meta': {'object_name': 'ElementComment'},
            'element': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['service.Element']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'service.elementcommentnotification': {
            'Meta': {'object_name': 'ElementCommentNotification'},
            'comment': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['service.ElementComment']"}),
            'game': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['service.Game']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'timestamp': ('django.db.models.fields.IntegerField', [], {})
        },
        'service.elementkind': {
            'Meta': {'object_name': 'ElementKind'},
            'game': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['service.Game']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        'service.elementnotification': {
            'Meta': {'object_name': 'ElementNotification'},
            'element': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['service.Element']"}),
            'game': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['service.Game']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'timestamp': ('django.db.models.fields.IntegerField', [], {})
        },
        'service.elementsketch': {
            'Meta': {'object_name': 'ElementSketch'},
            'element': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['service.Element']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sketch_source': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'service.elementsketchnotification': {
            'Meta': {'object_name': 'ElementSketchNotification'},
            'game': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['service.Game']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sketch': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['service.ElementSketch']"}),
            'timestamp': ('django.db.models.fields.IntegerField', [], {})
        },
        'service.event': {
            'Meta': {'object_name': 'Event'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'kind': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['service.EventKind']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'service.eventcomment': {
            'Meta': {'object_name': 'EventComment'},
            'event': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['service.Event']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'service.eventcommentnotification': {
            'Meta': {'object_name': 'EventCommentNotification'},
            'comment': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['service.EventComment']"}),
            'game': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['service.Game']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'timestamp': ('django.db.models.fields.IntegerField', [], {})
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
        'service.eventnotification': {
            'Meta': {'object_name': 'EventNotification'},
            'event': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['service.Event']"}),
            'game': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['service.Game']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'timestamp': ('django.db.models.fields.IntegerField', [], {})
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
