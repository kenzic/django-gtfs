# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Agency'
        db.create_table('gtfs_agency', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.TextField')()),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('timezone', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('agency_id', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('lang', self.gf('django.db.models.fields.CharField')(max_length=2, null=True, blank=True)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('fare_url', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
        ))
        db.send_create_signal('gtfs', ['Agency'])

        # Adding model 'Zone'
        db.create_table('gtfs_zone', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('zone_id', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
        ))
        db.send_create_signal('gtfs', ['Zone'])

        # Adding model 'Stop'
        db.create_table('gtfs_stop', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('stop_id', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('desc', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('geopoint', self.gf('django.contrib.gis.db.models.fields.PointField')(null=True, blank=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('zone', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['gtfs.Zone'], null=True, blank=True)),
            ('location_type', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('parent_station', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['gtfs.Stop'], null=True, blank=True)),
        ))
        db.send_create_signal('gtfs', ['Stop'])

        # Adding model 'RouteType'
        db.create_table('gtfs_routetype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('value', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('gtfs', ['RouteType'])

        # Adding model 'Route'
        db.create_table('gtfs_route', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('route_id', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
            ('agency', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['gtfs.Agency'], null=True, blank=True)),
            ('short_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('long_name', self.gf('django.db.models.fields.TextField')()),
            ('desc', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('route_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['gtfs.RouteType'])),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('color', self.gf('django.db.models.fields.CharField')(default='FFFFFF', max_length=6)),
            ('text_color', self.gf('django.db.models.fields.CharField')(default='000000', max_length=6)),
        ))
        db.send_create_signal('gtfs', ['Route'])

        # Adding model 'Service'
        db.create_table('gtfs_service', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('service_id', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
        ))
        db.send_create_signal('gtfs', ['Service'])

        # Adding model 'Direction'
        db.create_table('gtfs_direction', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('value', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('gtfs', ['Direction'])

        # Adding model 'Block'
        db.create_table('gtfs_block', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('block_id', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
        ))
        db.send_create_signal('gtfs', ['Block'])

        # Adding model 'Shape'
        db.create_table('gtfs_shape', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('shape_id', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
            ('geopoint', self.gf('django.contrib.gis.db.models.fields.PointField')()),
            ('pt_sequence', self.gf('django.db.models.fields.IntegerField')()),
            ('dist_traveled', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
        ))
        db.send_create_signal('gtfs', ['Shape'])

        # Adding model 'Trip'
        db.create_table('gtfs_trip', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('route', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['gtfs.Route'])),
            ('service', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['gtfs.Service'])),
            ('trip_id', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
            ('headsign', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('direction', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['gtfs.Direction'], null=True, blank=True)),
            ('block', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['gtfs.Block'], null=True, blank=True)),
            ('shape', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['gtfs.Shape'], null=True, blank=True)),
        ))
        db.send_create_signal('gtfs', ['Trip'])

        # Adding model 'PickupType'
        db.create_table('gtfs_pickuptype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('value', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('gtfs', ['PickupType'])

        # Adding model 'DropOffType'
        db.create_table('gtfs_dropofftype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('value', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('gtfs', ['DropOffType'])

        # Adding model 'StopTime'
        db.create_table('gtfs_stoptime', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('trip', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['gtfs.Trip'])),
            ('arrival_time', self.gf('django.db.models.fields.TimeField')()),
            ('departure_time', self.gf('django.db.models.fields.TimeField')()),
            ('stop', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['gtfs.Stop'])),
            ('stop_sequence', self.gf('django.db.models.fields.IntegerField')()),
            ('headsign', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('pickup_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['gtfs.PickupType'], null=True, blank=True)),
            ('shape_dist_traveled', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
        ))
        db.send_create_signal('gtfs', ['StopTime'])

        # Adding model 'Calendar'
        db.create_table('gtfs_calendar', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('service', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['gtfs.Service'])),
            ('monday', self.gf('django.db.models.fields.IntegerField')()),
            ('tuesday', self.gf('django.db.models.fields.IntegerField')()),
            ('wednesday', self.gf('django.db.models.fields.IntegerField')()),
            ('thursday', self.gf('django.db.models.fields.IntegerField')()),
            ('friday', self.gf('django.db.models.fields.IntegerField')()),
            ('saturday', self.gf('django.db.models.fields.IntegerField')()),
            ('sunday', self.gf('django.db.models.fields.IntegerField')()),
            ('start_date', self.gf('django.db.models.fields.DateField')()),
            ('end_date', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal('gtfs', ['Calendar'])

        # Adding model 'ExceptionType'
        db.create_table('gtfs_exceptiontype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('value', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('gtfs', ['ExceptionType'])

        # Adding model 'CalendarDate'
        db.create_table('gtfs_calendardate', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('service', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['gtfs.Service'])),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('exception_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['gtfs.ExceptionType'])),
        ))
        db.send_create_signal('gtfs', ['CalendarDate'])

        # Adding model 'Fare'
        db.create_table('gtfs_fare', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fare_id', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
        ))
        db.send_create_signal('gtfs', ['Fare'])

        # Adding model 'PaymentMethod'
        db.create_table('gtfs_paymentmethod', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('vale', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('gtfs', ['PaymentMethod'])

        # Adding model 'FareAttribute'
        db.create_table('gtfs_fareattribute', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fare', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['gtfs.Fare'])),
            ('price', self.gf('django.db.models.fields.FloatField')()),
            ('currency', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('payment_method', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['gtfs.PaymentMethod'])),
            ('transfers', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('transfer_duration', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal('gtfs', ['FareAttribute'])

        # Adding model 'FareRule'
        db.create_table('gtfs_farerule', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fare', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['gtfs.Fare'])),
            ('route', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['gtfs.Route'], null=True, blank=True)),
            ('origin', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='origin', null=True, to=orm['gtfs.Zone'])),
            ('destination', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='destination', null=True, to=orm['gtfs.Zone'])),
            ('contains', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='contains', null=True, to=orm['gtfs.Zone'])),
        ))
        db.send_create_signal('gtfs', ['FareRule'])

        # Adding model 'Frequency'
        db.create_table('gtfs_frequency', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('trip', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['gtfs.Trip'])),
            ('start_time', self.gf('django.db.models.fields.TimeField')()),
            ('end_time', self.gf('django.db.models.fields.TimeField')()),
            ('headway_secs', self.gf('django.db.models.fields.IntegerField')()),
            ('exact_times', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal('gtfs', ['Frequency'])

        # Adding model 'Transfer'
        db.create_table('gtfs_transfer', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('from_stop', self.gf('django.db.models.fields.related.ForeignKey')(related_name='from_stop', to=orm['gtfs.Stop'])),
            ('to_stop', self.gf('django.db.models.fields.related.ForeignKey')(related_name='to_stop', to=orm['gtfs.Stop'])),
            ('transfer_type', self.gf('django.db.models.fields.IntegerField')()),
            ('min_transfer_time', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal('gtfs', ['Transfer'])


    def backwards(self, orm):
        
        # Deleting model 'Agency'
        db.delete_table('gtfs_agency')

        # Deleting model 'Zone'
        db.delete_table('gtfs_zone')

        # Deleting model 'Stop'
        db.delete_table('gtfs_stop')

        # Deleting model 'RouteType'
        db.delete_table('gtfs_routetype')

        # Deleting model 'Route'
        db.delete_table('gtfs_route')

        # Deleting model 'Service'
        db.delete_table('gtfs_service')

        # Deleting model 'Direction'
        db.delete_table('gtfs_direction')

        # Deleting model 'Block'
        db.delete_table('gtfs_block')

        # Deleting model 'Shape'
        db.delete_table('gtfs_shape')

        # Deleting model 'Trip'
        db.delete_table('gtfs_trip')

        # Deleting model 'PickupType'
        db.delete_table('gtfs_pickuptype')

        # Deleting model 'DropOffType'
        db.delete_table('gtfs_dropofftype')

        # Deleting model 'StopTime'
        db.delete_table('gtfs_stoptime')

        # Deleting model 'Calendar'
        db.delete_table('gtfs_calendar')

        # Deleting model 'ExceptionType'
        db.delete_table('gtfs_exceptiontype')

        # Deleting model 'CalendarDate'
        db.delete_table('gtfs_calendardate')

        # Deleting model 'Fare'
        db.delete_table('gtfs_fare')

        # Deleting model 'PaymentMethod'
        db.delete_table('gtfs_paymentmethod')

        # Deleting model 'FareAttribute'
        db.delete_table('gtfs_fareattribute')

        # Deleting model 'FareRule'
        db.delete_table('gtfs_farerule')

        # Deleting model 'Frequency'
        db.delete_table('gtfs_frequency')

        # Deleting model 'Transfer'
        db.delete_table('gtfs_transfer')


    models = {
        'gtfs.agency': {
            'Meta': {'object_name': 'Agency'},
            'agency_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'fare_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lang': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'timezone': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        'gtfs.block': {
            'Meta': {'object_name': 'Block'},
            'block_id': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'gtfs.calendar': {
            'Meta': {'object_name': 'Calendar'},
            'end_date': ('django.db.models.fields.DateField', [], {}),
            'friday': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'monday': ('django.db.models.fields.IntegerField', [], {}),
            'saturday': ('django.db.models.fields.IntegerField', [], {}),
            'service': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['gtfs.Service']"}),
            'start_date': ('django.db.models.fields.DateField', [], {}),
            'sunday': ('django.db.models.fields.IntegerField', [], {}),
            'thursday': ('django.db.models.fields.IntegerField', [], {}),
            'tuesday': ('django.db.models.fields.IntegerField', [], {}),
            'wednesday': ('django.db.models.fields.IntegerField', [], {})
        },
        'gtfs.calendardate': {
            'Meta': {'object_name': 'CalendarDate'},
            'date': ('django.db.models.fields.DateField', [], {}),
            'exception_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['gtfs.ExceptionType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'service': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['gtfs.Service']"})
        },
        'gtfs.direction': {
            'Meta': {'object_name': 'Direction'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'value': ('django.db.models.fields.IntegerField', [], {})
        },
        'gtfs.dropofftype': {
            'Meta': {'object_name': 'DropOffType'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'value': ('django.db.models.fields.IntegerField', [], {})
        },
        'gtfs.exceptiontype': {
            'Meta': {'object_name': 'ExceptionType'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'value': ('django.db.models.fields.IntegerField', [], {})
        },
        'gtfs.fare': {
            'Meta': {'object_name': 'Fare'},
            'fare_id': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'gtfs.fareattribute': {
            'Meta': {'object_name': 'FareAttribute'},
            'currency': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'fare': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['gtfs.Fare']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'payment_method': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['gtfs.PaymentMethod']"}),
            'price': ('django.db.models.fields.FloatField', [], {}),
            'transfer_duration': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'transfers': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'gtfs.farerule': {
            'Meta': {'object_name': 'FareRule'},
            'contains': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'contains'", 'null': 'True', 'to': "orm['gtfs.Zone']"}),
            'destination': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'destination'", 'null': 'True', 'to': "orm['gtfs.Zone']"}),
            'fare': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['gtfs.Fare']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'origin': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'origin'", 'null': 'True', 'to': "orm['gtfs.Zone']"}),
            'route': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['gtfs.Route']", 'null': 'True', 'blank': 'True'})
        },
        'gtfs.frequency': {
            'Meta': {'object_name': 'Frequency'},
            'end_time': ('django.db.models.fields.TimeField', [], {}),
            'exact_times': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'headway_secs': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'start_time': ('django.db.models.fields.TimeField', [], {}),
            'trip': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['gtfs.Trip']"})
        },
        'gtfs.paymentmethod': {
            'Meta': {'object_name': 'PaymentMethod'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'vale': ('django.db.models.fields.IntegerField', [], {})
        },
        'gtfs.pickuptype': {
            'Meta': {'object_name': 'PickupType'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'value': ('django.db.models.fields.IntegerField', [], {})
        },
        'gtfs.route': {
            'Meta': {'object_name': 'Route'},
            'agency': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['gtfs.Agency']", 'null': 'True', 'blank': 'True'}),
            'color': ('django.db.models.fields.CharField', [], {'default': "'FFFFFF'", 'max_length': '6'}),
            'desc': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'long_name': ('django.db.models.fields.TextField', [], {}),
            'route_id': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'route_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['gtfs.RouteType']"}),
            'short_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'text_color': ('django.db.models.fields.CharField', [], {'default': "'000000'", 'max_length': '6'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        'gtfs.routetype': {
            'Meta': {'object_name': 'RouteType'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'value': ('django.db.models.fields.IntegerField', [], {})
        },
        'gtfs.service': {
            'Meta': {'object_name': 'Service'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'service_id': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        },
        'gtfs.shape': {
            'Meta': {'object_name': 'Shape'},
            'dist_traveled': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'geopoint': ('django.contrib.gis.db.models.fields.PointField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pt_sequence': ('django.db.models.fields.IntegerField', [], {}),
            'shape_id': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        },
        'gtfs.stop': {
            'Meta': {'object_name': 'Stop'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'desc': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'geopoint': ('django.contrib.gis.db.models.fields.PointField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location_type': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'parent_station': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['gtfs.Stop']", 'null': 'True', 'blank': 'True'}),
            'stop_id': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'zone': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['gtfs.Zone']", 'null': 'True', 'blank': 'True'})
        },
        'gtfs.stoptime': {
            'Meta': {'object_name': 'StopTime'},
            'arrival_time': ('django.db.models.fields.TimeField', [], {}),
            'departure_time': ('django.db.models.fields.TimeField', [], {}),
            'headsign': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pickup_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['gtfs.PickupType']", 'null': 'True', 'blank': 'True'}),
            'shape_dist_traveled': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'stop': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['gtfs.Stop']"}),
            'stop_sequence': ('django.db.models.fields.IntegerField', [], {}),
            'trip': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['gtfs.Trip']"})
        },
        'gtfs.transfer': {
            'Meta': {'object_name': 'Transfer'},
            'from_stop': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'from_stop'", 'to': "orm['gtfs.Stop']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'min_transfer_time': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'to_stop': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'to_stop'", 'to': "orm['gtfs.Stop']"}),
            'transfer_type': ('django.db.models.fields.IntegerField', [], {})
        },
        'gtfs.trip': {
            'Meta': {'object_name': 'Trip'},
            'block': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['gtfs.Block']", 'null': 'True', 'blank': 'True'}),
            'direction': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['gtfs.Direction']", 'null': 'True', 'blank': 'True'}),
            'headsign': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'route': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['gtfs.Route']"}),
            'service': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['gtfs.Service']"}),
            'shape': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['gtfs.Shape']", 'null': 'True', 'blank': 'True'}),
            'trip_id': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        },
        'gtfs.zone': {
            'Meta': {'object_name': 'Zone'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'zone_id': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        }
    }

    complete_apps = ['gtfs']
