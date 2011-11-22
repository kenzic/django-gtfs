# -*- coding: utf-8 -*-
from django.contrib.gis.db import models 

class Agency(models.Model):
    name = models.TextField()
    url = models.URLField()
    timezone = models.CharField(max_length=255)
    agency_id = models.CharField(max_length=255, null=True, blank=True)
    lang = models.CharField(max_length=2, null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    fare_url = models.URLField(null=True, blank=True)
      
class Zone(models.Model):
    """ Define the fare zone""" 
    zone_id = models.CharField(max_length=255, unique=True)
    
class Stop(models.Model):
    stop_id = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    url = models.URLField()    
    desc = models.TextField(null=True, blank=True)
    geopoint = models.PointField(null=True, blank=True)
    code = models.CharField(max_length=255, null=True, blank=True)
    zone = models.ForeignKey(Zone, null=True, blank=True)
    location_type = models.IntegerField(null=True, blank=True) #TODO add choices for 0=blank=Stop and 1=Station
    parent_station = models.ForeignKey('self', null=True, blank=True)  
    objects = models.GeoManager()       
                                            
class RouteType(models.Model):
    """Referential data"""  
    name = models.CharField(max_length=50)
    description = models.TextField()
    value = models.IntegerField(unique=True)
    
class Route(models.Model):
    route_id = models.CharField(max_length=255, unique=True)
    agency = models.ForeignKey(Agency, null=True, blank=True)
    short_name = models.CharField(max_length=255)
    long_name = models.TextField()
    desc = models.TextField(null=True, blank=True)
    route_type = models.ForeignKey(RouteType)
    url = models.URLField(null=True, blank=True)
    color = models.CharField(max_length=6, default="FFFFFF")
    text_color = models.CharField(max_length=6, default="000000")
    
class Service(models.Model):
    service_id = models.CharField(max_length=255, unique=True)
                          
class Direction(models.Model):
    """Referential data"""
    name = models.CharField(max_length=20)
    value = models.IntegerField(unique=True)
                                  
class Block(models.Model):
    block_id = models.CharField(max_length=255, unique=True)
                                                          
class Shape(models.Model):
    shape_id = models.CharField(max_length=255)
    geopoint = models.PointField()
    pt_sequence = models.IntegerField()
    dist_traveled = models.FloatField(null=True, blank=True) 
    objects = models.GeoManager()
    
class Trip(models.Model):
    route = models.ForeignKey(Route)
    service = models.ForeignKey(Service)
    trip_id = models.CharField(max_length=255, unique=True)
    headsign = models.TextField(null=True, blank=True)
    direction = models.ForeignKey(Direction, null=True, blank=True)
    block = models.ForeignKey(Block, null=True, blank=True)
    shape_id = models.CharField(max_length=255, null=True, blank=True)
                                                                     
class PickupType(models.Model):
    """Referential data"""
    name = models.CharField(max_length=255)
    value = models.IntegerField()
                                  
class DropOffType(models.Model):
    """Referential data"""
    name = models.CharField(max_length=255)
    value = models.IntegerField()
    
class StopTime(models.Model):
    trip = models.ForeignKey(Trip)
    arrival_time = models.TimeField()
    departure_time = models.TimeField()
    stop = models.ForeignKey(Stop)
    stop_sequence = models.IntegerField()
    headsign = models.TextField(null=True, blank=True)
    pickup_type = models.ForeignKey(PickupType, null=True, blank=True)
    drop_off_type = models.ForeignKey(DropOffType, null=True, blank=True)
    shape_dist_traveled = models.FloatField(null=True, blank=True)
    
class Calendar(models.Model):
     service = models.ForeignKey(Service)
     monday = models.IntegerField()
     tuesday = models.IntegerField()
     wednesday = models.IntegerField()
     thursday = models.IntegerField()
     friday = models.IntegerField()
     saturday = models.IntegerField()
     sunday = models.IntegerField()
     start_date = models.DateField()
     end_date = models.DateField()                  

class ExceptionType(models.Model):
    """Referential data"""
    name = models.CharField(max_length=255)
    value = models.IntegerField()
     
class CalendarDate(models.Model):
    service = models.ForeignKey(Service)
    date = models.DateField()
    exception_type = models.ForeignKey(ExceptionType)
    
class Fare(models.Model):
    fare_id = models.CharField(max_length=255, unique=True)
                                                    
class PaymentMethod(models.Model):
    name = models.CharField(max_length=50)
    vale = models.IntegerField()
    
class FareAttribute(models.Model):
    fare = models.ForeignKey(Fare)
    price = models.FloatField()
    currency = models.CharField(max_length=3)
    payment_method = models.ForeignKey(PaymentMethod)
    transfers = models.IntegerField(null=True, blank=True)
    transfer_duration = models.IntegerField(null=True, blank=True) # duration in seconds

class FareRule(models.Model):
    fare = models.ForeignKey(Fare)
    route = models.ForeignKey(Route, null=True, blank=True)
    origin = models.ForeignKey(Zone, null=True, blank=True, related_name="origin")
    destination = models.ForeignKey(Zone, null=True, blank=True, related_name="destination")
    contains = models.ForeignKey(Zone, null=True, blank=True, related_name="contains")
    
class Frequency(models.Model):
    trip = models.ForeignKey(Trip)
    start_time = models.TimeField()
    end_time = models.TimeField()
    headway_secs = models.IntegerField()
    exact_times = models.IntegerField(null=True, blank=True)
    
class Transfer(models.Model):
    from_stop = models.ForeignKey(Stop, related_name="from_stop")
    to_stop = models.ForeignKey(Stop, related_name="to_stop")
    transfer_type = models.IntegerField()
    min_transfer_time = models.IntegerField(null=True, blank=True)