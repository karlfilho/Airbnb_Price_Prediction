"""Data loader code"""

import pandas as pd


class DataLoader:
    def __init__(self, frontpage_path: str, rooms_path: str):
        self.frontpage_path = frontpage_path
        self.rooms_path = rooms_path
        self.frontpage_data = None
        self.rooms_data = None
        self.data = None
    
    def load_data_frontpage(self) -> pd.DataFrame:
        """Load data from the 'frontpage' json file"""
        self.frontpage_data = pd.read_json(self.frontpage_path, encoding='utf-8')
        self.frontpage_data = self.frontpage_data.drop(columns= ["Keyword", "Host", "roomName", "roomRating", "roomReviewcount"])
        return self.frontpage_data
    
    def load_data_rooms(self) -> pd.DataFrame:
        """Load data from the 'rooms' json file"""
        self.rooms_data = pd.read_json(self.rooms_path, encoding='utf-8')
        self.rooms_data = self.rooms_data.drop(columns= ["Title", "Location", "Number_of_Guests", "Number_of_Bedrooms", "Number_of_Beds", "Number_of_Bath", "Price", "Sleeping_Arrangements", "Hosted_by", "Response_Rate", "Image_1", "Image_2", "Image_3", "Current_Time"])
        return self.rooms_data
    
    def merge_data(self) -> pd.DataFrame:
        """Merge the 'frontpage' and 'rooms' dataframes"""
        if self.frontpage_data is None or self.rooms_data is None:
            raise ValueError("Data not loaded. Please load data before merging.")
        self.data = pd.merge(self.frontpage_data, self.rooms_data, left_on='roomURL', right_on='Page_URL')
        self.data = self.data.drop(columns=["Page_URL"])    # keeping the url for future cleaning
        return self.data