from django.contrib import admin

from .models import City,Train, Station, StationPrice, Voyage, Wagon

admin.site.register(City)
admin.site.register(Train)
admin.site.register(StationPrice)
admin.site.register(Station)
admin.site.register(Voyage)
admin.site.register(Wagon)
