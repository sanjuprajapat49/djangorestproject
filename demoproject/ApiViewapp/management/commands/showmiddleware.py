from django.core.management.base import BaseCommand
from django.conf import settings

class Command(BaseCommand):
    help = "This command is show all the middlewares"
    
    def handle(self, *args, **kwargs):
        print("Active Middlewares: \n")
        
        for i in settings.MIDDLEWARE:
            print(i)
            
        
        