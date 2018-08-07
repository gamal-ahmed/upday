import pandas as pd
import os

def read_tsv_file(file_path):
    try:
        if os.stat(file_path).st_size > 0:
            print("reading tsv file with in pandas.....")
            return pd.read_csv(file_path,delimiter='\t',encoding='utf-8')
        else:
           print ("empty file")
    except OSError:
       print("No file")



def no_of_event_for_each_category_user(df,event_type):
    if df is None:
        raise ValueError
    result=df[df.event_type==event_type].groupby(['user_uid', 'category'])['event_type'].agg(['count']).reset_index()
    return result;



def pandas_main():
    df=read_tsv_file("data.tsv")
    print(" \n \n result : \n")
    print(no_of_event_for_each_category_user(df,"teaser_opened"))
