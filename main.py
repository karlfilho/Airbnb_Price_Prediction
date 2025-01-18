from data import DataLoader, DataPreprocessing

# data file paths
frontpage_path = "D:\\portfolio\\Airbnb_Price_Prediction\\src\\data\\raw\\frontpage.json"
rooms_path = "D:\\portfolio\\Airbnb_Price_Prediction\\src\\data\\raw\\rooms.json"

def main():
    # loading data
    data_loader = DataLoader(frontpage_path, rooms_path)
    data_loader.load_data_frontpage()
    data_loader.load_data_rooms()

    merged_data = data_loader.merge_data()

    # Cleaning data
    data_cleaner = DataPreprocessing(merged_data)
    clean_data = data_cleaner.cleaning()

    print(merged_data.head())

if __name__ == "__main__":
    main()
