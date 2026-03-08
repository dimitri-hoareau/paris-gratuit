"""
Configuration des sources de données Paris Open Data
"""

DATA_SOURCES = {
    'toilettes': {
        'dataset': 'sanisettesparis',
        'category': {
            'name': 'Toilettes publiques',
            'slug': 'toilettes-publiques',
            'color': '#3b82f6',
            'icon': 'toilet'
        },
        'fields_mapping': {
            'name': 'adresse',
            'address': 'adresse',
            'geo': 'geo_point_2d',
            'pmr': 'acces_pmr',
        },
        'is_open_24_7': True,
    },
    'fontaines': {
        'dataset': 'fontaines-a-boire',
        'category': {
            'name': "Fontaines d'eau potable",
            'slug': 'fontaines-eau-potable',
            'color': '#06b6d4',
            'icon': 'droplet'
        },
        'fields_mapping': {
            'name': 'libelle',
            'address': 'adresse',
            'geo': 'geo_point_2d',
        },
        'is_open_24_7': True,
    },
}