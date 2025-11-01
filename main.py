from extract import extract_data
from transform import transform_data
from load import load_data


if __name__ == '__main__':
    data = extract_data()
    transformed_data = transform_data(metropeak_df=data)
    load_data(transformed_data)
