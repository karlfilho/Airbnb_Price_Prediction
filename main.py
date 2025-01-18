from src.data.data_loader import DataLoader
# import os

# # get the base directory
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# # get the data file paths
# frontpage_path = os.path.join(BASE_DIR, 'Airbnb_Price_Prediction', 'src', 'data', 'raw', 'frontpage.json')
# rooms_path = os.path.join(BASE_DIR, 'Airbnb_Price_Prediction', 'src', 'data', 'raw', 'rooms.json')

# data file paths
frontpage_path = "D:\\portfolio\\Airbnb_Price_Prediction\\src\\data\\raw\\frontpage.json"
rooms_path = "D:\\portfolio\\Airbnb_Price_Prediction\\src\\data\\raw\\rooms.json"

def main():
    # loading data
    data_loader = DataLoader(frontpage_path, rooms_path)
    data_loader.load_data_frontpage()
    data_loader.load_data_rooms()

    merged_data = data_loader.merge_data()

    # printing the first 5 rows of the data
    print(merged_data.head())

if __name__ == "__main__":
    main()
