from csv import DictReader
from django.core.management.base import BaseCommand, CommandError
from gtfs.models import Agency
                   
GTFS_FILES = ["agency.txt", 
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
            self.stdout.write("Treating directory %s " % root_dir)
            