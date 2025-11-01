from sqlalchemy import create_engine
import pandas as pd
import os
from dotenv import load_dotenv
load_dotenv(override=True)


connection_str = f'postgresql://{os.getenv("user")}:{os.getenv("password")}@{os.getenv("host")}:{os.getenv("port")}/{os.getenv("dbname")}'


def load_data(metropeak_df:pd.DataFrame,properties:str='property',connect_st:str=connection_str):
    engine = create_engine(connect_st)

    metropeak_df.to_sql(properties, con=engine, index=False, if_exists="append")