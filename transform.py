import pandas as pd



def df_missing_columns_overview(df:pd.DataFrame):

    missing_data = df.isnull().sum()

    missing_percent = (missing_data / len(df)) * 100

    print(" \n Missing Value (The Empty spaces): ")

    for col in df.columns:
        if missing_data[col] > 0:
            print(f"  {col}: {missing_data[col]:,}:missing ({missing_percent[col]:.1f}%)")


    print(f"\n Worst Offenders :")

    if len(missing_data[missing_data > 0]) > 0:
        worst_column = missing_data.idxmax()
        worst_percent = missing_percent.max()
        print(f" '{worst_column}' has {missing_data[worst_column]:,} missing values ({worst_percent:.1f}%) ")
    else:
        print('no missing values found yet')



    print(f"\n Total missing Value : {df.isnull().sum().sum():,} empty cells")

    return df



def clean_data(metropeak_df:pd.DataFrame):
    
    try:

        schema = {
            "brokeredby": "int64",      
            "status": "string",
            "price": "float64",
            "bed": "int64",
            "bath": "int64",
            "acrelot": "float64",
            "street": "string",         
            "city": "string",
            "state": "string",
            "zipcode": "string",        
            "housesize": "float64"
        }

        metropeak_df.columns = metropeak_df.columns.str.lower()
        

            #  Convert numeric IDs / codes to appropriate types
        metropeak_df["brokeredby"] = metropeak_df["brokeredby"].astype("int64")
        metropeak_df["street"] = metropeak_df["street"].astype("string")
        metropeak_df["zipcode"] = metropeak_df["zipcode"].astype("int64").astype("string")

        # Convert beds/baths to int safely
        metropeak_df["bed"] = metropeak_df["bed"].fillna(0).astype("int64")
        metropeak_df["bath"] = metropeak_df["bath"].fillna(0).astype("int64")

        # Clean categorical/text columns (strip spaces, title case)
        for col in ["status", "city", "state"]:
            metropeak_df[col] = metropeak_df[col].str.strip().str.title()


        # Final schema enforcement
        metropeak_df = metropeak_df.astype(schema, errors="ignore")

        return metropeak_df

        
    except BaseException as error:
        print(error)
        



def transform_data(metropeak_df:pd.DataFrame):


    try:
        metropeak_df = df_missing_columns_overview(metropeak_df)
        metropeak_df.fillna({
        'brokered_by': metropeak_df['brokered_by'].mean(),
        'price':metropeak_df['price'].mean(),
        'bed': metropeak_df['bed'].mean(),
        'bath': metropeak_df['bath'].mean(),
        'acre_lot': metropeak_df['acre_lot'].mean(),
        'street':'',
        'city': '',
        'state':'',
        'zip_code':metropeak_df['zip_code'].mean(),
        'house_size':metropeak_df['house_size'].mean(),
    },inplace=True)
        
        metropeak_df.drop(columns=['prev_sold_date'],inplace=True)

        metropeak_df.rename(columns={
            'brokered_by':"brokeredby",
            'acre_lot':'acreLot',
            'zip_code':'zipcode',
            'house_size':'housesize'
        },inplace=True)
        
        data = clean_data(metropeak_df)
        # print('transform data ',data.head(20))
        return data
    except BaseException as e:
        print('transform error ',e)
  
