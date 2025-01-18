"""Data loader code"""

import pandas as pd


class DataLoader:
    def __init__(self, frontpage_path: str, rooms_path: str):
        self.frontpage_path = frontpage_path
        self.rooms_path = rooms_path
        self.frontpage_data = None
        self.rooms_data = None
        self.merged_data = None
    
    def load_data_frontpage(self) -> pd.DataFrame:
        """Load data from the 'frontpage' json file"""
        frontpage_data = pd.read_json(self.frontpage_path, encoding='utf-8')
        frontpage_data = frontpage_data.drop(columns= ["Keyword", "Host", "roomName", "roomRating", "roomReviewcount"], inplace=True)
        return frontpage_data
    
    def load_data_rooms(self) -> pd.DataFrame:
        """Load data from the 'rooms' json file"""
        rooms_data = pd.read_json(self.rooms_path, encoding='utf-8')
        rooms_data = rooms_data.drop(columns= ["Title", "Location", "Number_of_Guests", "Number_of_Bedrooms", "Number_of_Beds", "Number_of_Bath", "Price", "Sleeping_Arrangements", "Hosted_by", "Response_Rate", "Image_1", "Image_2", "Image_3", "Current_Time"], inplace=True)
        return rooms_data
    
    def merge_data(self) -> pd.DataFrame:
        """Merge the 'frontpage' and 'rooms' dataframes"""
        merged_data = pd.merge(self.frontpage_data, self.rooms_data, left_on='roomURL', right_on='Page_URL')
        merged_data = merged_data.drop(columns=["Page_URL"])    # keeping the url for future cleaning
        return merged_data