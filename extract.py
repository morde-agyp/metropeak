import pandas as pd




def extract_data(filepath='./data/raw/Metropeak.csv'):
    try:
        metropeak_df = pd.read_csv(filepath)
        return metropeak_df
    except BaseException as e:
        print(e)

