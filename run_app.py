import os

from service.user_events_pyspark import pyspark_main
from service.user_events_pandas import pandas_main
if __name__ == '__main__':
    print(" \n \n run task 1 Goal 1 ... \n")
    pandas_main()
    print(" \n \n run task 1 Goal 2 ... \n")
    pyspark_main()
