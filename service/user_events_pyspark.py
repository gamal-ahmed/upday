
from pyspark.sql import SparkSession
import os


def read_tsv_file(file_path):
    try:
        if os.stat(file_path).st_size > 0:
            spark=initialize_spark()
            print("\n reading tsv file with in spark.....")
            return spark.read.load(file_path,format="csv", sep="\t",header="true")
        else:
           print ("empty file")
    except OSError:
       print("No file")

def initialize_spark():
    print("\n initializing SparkSession .......")
    return SparkSession \
    .builder \
    .appName("user_events_pyspark") \
    .config("spark.some.config.option", "") \
    .getOrCreate()

def no_of_event_for_each_category_user(df,event_type):
    if df is None:
        raise ValueError
    df=df[df.event_type==event_type].groupby(['user_uid', 'category']).count()
    return df;


def pyspark_main():
    df=read_tsv_file("data.tsv")
    print(" \n \n result : \n")
    no_of_event_for_each_category_user(df,"teaser_opened").show()
