"""Data preprocessing code"""

import pandas as pd
import unicodedata


def normalize_text(text: str) -> str:
    """Function to normalize the strings"""
    text = unicodedata.normalize('NFKD', text)  # Normalize Unicode characters
    text = text.encode('ascii', 'ignore').decode('ascii')  # Remove non-ASCII characters
    return text.strip()

def aggregate_amenity(amenity: str) -> str:
    """Function to aggregate amenities"""
    for keyword, category in aggregation_map.items():
        if keyword.lower() in amenity.lower():
            return category
    return amenity

aggregation_map = {
    'wifi': 'WiFi',
    'hd': 'HDTV',
    'tv': 'TV',
    'netflix': 'Streaming Service',
    'prime': 'Streaming Service',
    'roku': 'Streaming Service',
    'disney+': 'Streaming Service',
    'hbo max': 'Streaming Service',
    'streaming': 'Streaming Service',
    'parking': 'Parking',
    'garage': 'Parking',
    'carport': 'Parking',
    'ac': 'Air Conditioning',
    'air conditioning': 'Air Conditioning',
    'pool': 'Pool',
    'hot tub': 'Bathtub',
    'sauna': 'Sauna',
    'fireplace': 'Fireplace',
    'microwave': 'Microwave',
    'washer': 'Washer',
    'dryer': 'Dryer',
    'refrigerator': 'Refrigerator',
    'smoke alarm': 'Smoke Alarm',
    'carbon monoxide alarm': 'Carbon Monoxide Alarm',
    'bathroom': 'Bathroom',
    'kitchen': 'Kitchen',
    'patio': 'Patio',
    'balcony': 'Balcony',
    'backyard': 'Backyard',
    'view': 'View',
    'security cameras': 'Security Cameras',
    'ev charger': 'EV Charger',
    'breakfast': 'Breakfast',
    'pets allowed': 'Pets Allowed',
    'luggage dropoff allowed': 'Luggage Dropoff Allowed',
    'step-free access': 'Accessible',
    'step-free path': 'Accessible',
    'step-free guest entrance': 'Accessible',
    'crib': 'Crib',
    'high chair': 'High Chair',
    'pack ’n play/travel crib': 'Crib',
    'bathtub': 'Bathtub'
}

class DataPreprocessing:
    def __init__(self, data: pd.DataFrame):
        self.data = data
        self.unique_amenities = None

    def cleaning(self):
        # renaming columns for consistency
        self.data = self.data.rename(columns={
            'roomTitle' : 'roomType',
            'Rating' : 'rating',
            'Number_of_Reviews' : 'countReviews',
            'Amenities': 'amenities',
            })
        
        # dropping duplicates
        self.data = self.data.drop_duplicates()

        # fixing 'roomType' column
        self.data['roomType'] = self.data['roomType'].str.split().str[0]  # selecting the first word
        self.data['roomType'] = self.data['roomType'].astype('category')  # transforming in category dtype´

        # fixing 'roomPrice' column
        self.data['roomPrice'] = self.data['roomPrice'].str.extract('(\d+)').astype(float)  # keeping just the numerical values
        
        # fixing 'hostType' column
        self.data['hostType'] = self.data['hostType'].apply(normalize_text)  # apply normalization to the hostType column
        self.data['hostType'] = self.data['hostType'].replace({              # replace specific problematic strings
            'Preferido dos hospedes\nPreferido dos hospedes': 'preferido',
            'Superhost\nSuperhost': 'superhost',
            'De 18 a 20 de set.\n18  20 de set.': None,
            '': 'no_class'
            }).astype('category')
        
        # working on 'amenities' column
        self.data['amenities'] = self.data['amenities'].str.split('\n')
        self.data['amenities'] = self.data['amenities'].apply(lambda amenities: [aggregate_amenity(amenity) for amenity in amenities])
        self.unique_amenities = set(amenity for amenities in self.data['amenities'] for amenity in amenities)  # flatten the list of amenities and get unique values

        # creating separate columns for eacch amenity
        for amenity in self.unique_amenities:
            self.data[amenity] = self.data['amenities'].apply(lambda x: 1 if amenity in x else 0)

        # drop the original 'amenities' column
        self.data = self.data.drop(columns=['amenities'])

        return self.data