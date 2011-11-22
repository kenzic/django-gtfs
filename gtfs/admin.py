from django.contrib.gis import admin
from gtfs.models import Agency, Zone, Stop, RouteType, Route, Service, Direction, Block, Shape, Trip, PickupType, DropOffType, StopTime, Calendar, ExceptionType, CalendarDate, Fare, PaymentMethod, FareAttribute, FareRule, Frequency, Transfer
                                    
admin.site.register(Stop, admin.OSMGeoAdmin) 
admin.site.register(Shape, admin.OSMGeoAdmin)
admin.site.register(Agency)
admin.site.register(Zone)
admin.site.register(RouteType)                  
admin.site.register(Route)
admin.site.register(Service)
admin.site.register(Direction)
admin.site.register(Block)
admin.site.register(Trip)
admin.site.register(PickupType)
admin.site.register(DropOffType)
admin.site.register(StopTime)
admin.site.register(Calendar)
admin.site.register(ExceptionType)
admin.site.register(CalendarDate)
admin.site.register(Fare)
admin.site.register(PaymentMethod)
admin.site.register(FareAttribute)
admin.site.register(FareRule)
admin.site.register(Frequency)  
admin.site.register(Transfer)