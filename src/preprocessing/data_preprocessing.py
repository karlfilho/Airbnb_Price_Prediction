import pandas as pd
import numpy as np

def load_data_frontpage(frontpage_path: str) -> pd.DataFrame:
    """Load data from the 'frontpage' json file"""
    frontpage_df = pd.read_json(frontpage_path, encoding='utf-8')
    frontpage_df = frontpage_df.drop(columns= ["Keyword", "Host", "roomName", "roomRating", "roomReviewcount"], inplace=True)
    return frontpage_df

def load_data_rooms(rooms_path: str) -> pd.DataFrame:
    """Load data from the 'rooms' json file"""
    rooms_df = pd.read_json(rooms_path, encoding='utf-8')
    rooms_df = rooms_df.drop(columns= ["Title", "Location", "Number_of_Guests", "Number_of_Bedrooms", "Number_of_Beds", "Number_of_Bath", "Price", "Sleeping_Arrangements", "Hosted_by", "Response_Rate", "Image_1", "Image_2", "Image_3", "Current_Time"], inplace=True)
    return rooms_df
