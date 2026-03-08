import requests
from django.core.management.base import BaseCommand, CommandError
from django.contrib.gis.geos import Point
from places.models import Category, Place
from places.data_sources import DATA_SOURCES


class Command(BaseCommand):
    help = 'Import des lieux depuis Paris Open Data'

    def add_arguments(self, parser):
        parser.add_argument(
            'source',
            type=str,
            help=f'Source de données ({", ".join(DATA_SOURCES.keys())})'
        )

    def handle(self, *args, **options):
        source_name = options['source']
        
        if source_name not in DATA_SOURCES:
            raise CommandError(
                f'Source inconnue : {source_name}. '
                f'Sources disponibles : {", ".join(DATA_SOURCES.keys())}'
            )
        
        config = DATA_SOURCES[source_name]
        
        self.stdout.write(f'Début import {source_name}...')

        category, created = Category.objects.get_or_create(
            slug=config['category']['slug'],
            defaults={
                'name': config['category']['name'],
                'color': config['category']['color'],
                'icon': config['category']['icon']
            }
        )
        
        if created:
            self.stdout.write(self.style.SUCCESS(f'Catégorie "{category.name}" créée'))
        else:
            self.stdout.write(f'Catégorie "{category.name}" déjà existante')

        url = 'https://opendata.paris.fr/api/records/1.0/search/'
        params = {
            'dataset': config['dataset'],
            'rows': 1000,
        }

        self.stdout.write(f'Récupération depuis dataset "{config["dataset"]}"...')
        response = requests.get(url, params=params)
        data = response.json()

        count_created = 0
        count_updated = 0
        fields_map = config['fields_mapping']

        for record in data.get('records', []):
            fields = record.get('fields', {})
            
            geo = fields.get(fields_map['geo'])
            if not geo:
                continue
            
            latitude = geo[0]
            longitude = geo[1]
            location = Point(longitude, latitude, srid=4326)

            name = fields.get(fields_map['name'], category.name)
            address = fields.get(fields_map['address'], '')

            if address:  
                place, created = Place.objects.update_or_create(
                    name=name,
                    address=address,
                    category=category,
                    defaults={
                        'location': location,
                    }
                )
            else:  
                lat_rounded = round(latitude, 5)
                lon_rounded = round(longitude, 5)
                unique_name = f"{name} ({lat_rounded},{lon_rounded})"
                
                place, created = Place.objects.update_or_create(
                    name=unique_name,
                    category=category,
                    defaults={
                        'address': address,
                        'location': location,
        }
    )


            if created:
                count_created += 1
            else:
                count_updated += 1

        self.stdout.write(
            self.style.SUCCESS(
                f'Import {source_name} terminé : {count_created} créés, {count_updated} mis à jour'
            )
        )