"""Data preprocessing code"""

import pandas as pd


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

def merge_data(frontpage_df: pd.DataFrame, rooms_df: pd.DataFrame) -> pd.DataFrame:
    """Merge the 'frontpage' and 'rooms' dataframes"""
    merged_df = pd.merge(frontpage_df, rooms_df, left_on='roomURL', right_on='Page_URL')
    merged_df = merged_df.drop(columns=["Page_URL"]) # keeping the url for future cleaning
    return merged_df

