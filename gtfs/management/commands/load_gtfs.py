from csv import DictReader
from django.core.management.base import BaseCommand, CommandError    
from django.contrib.gis.geos import fromstr
from datetime import time
from gtfs.models import Agency, Stop, Zone, Route, RouteType, Service, Direction, Block, Shape, Trip, PickupType, DropOffType, StopTime  
import os
                   
GTFS_FILES = [
    "agency.txt", 
    "stops.txt", 
    "routes.txt", 
    "trips.txt", 
    "stop_times.txt", 
    "calendar.txt", 
    "calendar_dates.txt",
    "fare_attributes.txt",
    "fare_rules.txt",
    "shapes.txt",
    "frequencies.txt",
    "transfers.txt"]
    
class Command(BaseCommand):
    args = 'dir'
    help = "Import all the gtfs data it can from the specified directory"
    
    def handle(self, *args, **options):
        for root_dir in args:
            self.stdout.write("Treating directory %s\n" % root_dir)
            # load agency :
            """self._load_agency(root_dir)
            self._load_stops(root_dir)
            self._load_routes(root_dir)
            self._load_shapes(root_dir)
            self._load_trips(root_dir)"""
            self._load_stop_times(root_dir)
                               
    def _load_stop_times(self, root_dir): 
        fields = [('headsign', 'stop_headsign'),
            ('shape_dist_traveled', 'shape_dist_traveled')]
        def create_cmd(line):
            arrival_time = time(*map(int, check_field(line, 'arrival_time').split(":")))
            departure_time = time(*map(int, check_field(line, 'departure_time').split(":"))) 
            (stop, created) = StopTime.objects.get_or_create(trip=Trip.objects.get(trip_id=check_field(line, 'trip_id')),
                                    stop=Stop.objects.get(stop_id=check_field(line, 'stop_id')), 
                                    arrival_time=arrival_time,
                                    departure_time=departure_time,
                                    stop_sequence=check_field(line, 'stop_sequence'))
            # create pickup_type
            if check_field(line, 'pickup_type', optional=True):
                stop.pickup_type = PickupType.objects.get(value=check_field(line, 'pickup_type'))
                
            # check drop off type :
            if check_field(line, 'drop_off_type', optional=True):
                stop.drop_off_type = DropOffType.objects.get(value = check_field(line, 'drop_off_type'))
            return (stop, created)
             
        self._load(root_dir, "stop_times.txt", create_cmd, fields, optional=False)
        
    def _load_stops(self, root_dir):  
        fields = [('desc', 'stop_desc'),
            ('code', 'stop_code'),
            ('url', 'stop_url'), 
            ('location_type', 'location_type')]
        def create_cmd(line):
            (stop, created) = Stop.objects.get_or_create(stop_id=check_field(line, 'stop_id'), 
                                    name=check_field(line, 'stop_name'),
                                    geopoint=fromstr("POINT(%s %s)" % 
                                        (float(check_field(line, 'stop_lat')), float(check_field(line, 'stop_lon')))))
            # create zone
            if check_field(line, 'zone_id', optional=True):
                (zone, created) = Zone.objects.get_or_create(zone_id=check_field(line, 'zone_id'))
                stop.zone = zone 
            # check parent station :
            if check_field(line, 'parent_station', optional=True):
                try :
                    stop.parent_station = Stop.objects.get(stop_id = check_field(line, 'parent_station', optional=True))
                except:
                    pass
            return (stop, created)
             
        self._load(root_dir, "stops.txt", create_cmd, fields, optional=False)
                                                                              
    def _load_routes(self, root_dir):  
        fields = [('desc', 'route_desc'),
            ('url', 'route_url'),
            ('color', 'route_color'),
            ('text_color', 'route_text_color')]
        def create_cmd(line): 
            (route, created) = Route.objects.get_or_create(route_id=check_field(line, 'route_id'), 
                                    short_name=check_field(line, 'route_short_name'),
                                    long_name=check_field(line, 'route_long_name'), 
                                    route_type=RouteType.objects.get(value=check_field(line, 'route_type')))
            # link related agency
            if check_field(line, 'agency_id', optional=True):
                try:
                    route.agency = Agency.objects.get(agency_id=check_field(line, 'agency_id'))       
                except:
                     self.stderr.write("No agency with id %s " % check_field(line, 'agency_id'))
            return (route, created)

        self._load(root_dir, "routes.txt", create_cmd, fields, optional=False)

    def _load_trips(self, root_dir):  
        fields = [('headsign', 'trip_headsign'), 
            ('shape_id', 'shape_id')]
        def create_cmd(line): 
            (trip, created) = Trip.objects.get_or_create(route=Route.objects.get(route_id=check_field(line, 'route_id')), 
                                    service=Service.objects.get_or_create(service_id=check_field(line, 'service_id'))[0],
                                    trip_id=check_field(line, 'trip_id'))
            # link related direction_id
            if check_field(line, 'direction_id', optional=True):
                trip.direction = Direction.objects.get(value=check_field(line, 'direction_id'))       
            if check_field(line, 'block_id', optional=True):
                trip.block = Block.objects.get_or_create(block_id=check_field(line, 'block_id'))[0]
            return (trip, created)

        self._load(root_dir, "trips.txt", create_cmd, fields, optional=False)

    def _load_shapes(self, root_dir):  
        fields = [('dist_traveled', 'shape_dist_traveled'), ]
        def create_cmd(line):    
            geopoint = fromstr("POINT(%s %s)" % (float(check_field(line, 'shape_pt_lat')), float(check_field(line, 'shape_pt_lon'))))
            return Shape.objects.get_or_create(shape_id=check_field(line, 'shape_id'), 
                                    geopoint=geopoint,
                                    pt_sequence=check_field(line, 'shape_pt_sequence'))
        self._load(root_dir, "shapes.txt", create_cmd, fields, optional=True)

    def _load_agency(self, root_dir):  
        fields = [('agency_id', 'agency_id'),
            ('lang', 'agency_lang'),
            ('phone', 'agency_phone'),
            ('fare_url', 'agency_fare_url')]
        def create_cmd(line):
            return Agency.objects.get_or_create(name=check_field(line, 'agency_name'), 
                                    url=check_field(line, 'agency_url'),
                                    timezone=check_field(line, 'agency_timezone'))

        self._load(root_dir, "agency.txt", create_cmd, fields, optional=False)
                     
    def _load(self, root_dir, filename, get_or_create_cmd, fields, optional=False):
        count = 0
        try:   
            reader = DictReader(open(os.path.join(root_dir, filename), 'rb'))
            for line in reader:
                (obj, created) = get_or_create_cmd(line)                    
                for key, value in fields:
                    if not obj.__dict__[key] and check_field(line, value, optional=True):
                        obj.__dict__[key] = check_field(line, value)
                        
                obj.save()
                count += 1  
            self.stdout.write("%s loaded from %s\n" % (count, filename))
        except CommandError, r:
            raise r
        except Exception, e:
            raise CommandError("Could not load %s data properly, failed at line %s. Fix the following problems, this file is required : " % (filename, count) + str(e) )
        
                
def check_field(reader, field, optional=False):
    if field in reader and reader[field]:
        return reader[field]
    elif not optional:                                    
        raise CommandError("Field %s was empty or non-present in file" % field)
    else:
        return None