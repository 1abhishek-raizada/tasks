from django.apps import AppConfig
import threading
from .tracker import start_listeners

class EventsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'events'

    def ready(self):
        print('app loaded and starting')
        threading.Thread(target=start_listeners,daemon=True).start()
