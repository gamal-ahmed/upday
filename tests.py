import os
import pandas as pd
from pandas.util.testing import assert_frame_equal

import unittest
from service.user_events_pandas import read_tsv_file,no_of_event_for_each_category_user
from service.user_events_pyspark import no_of_event_for_each_category_user as spark_events
from service.user_events_pyspark import read_tsv_file as spark_read

TEST_DATA_DIR = 'testdata'



class TestPandasModule(unittest.TestCase):
    def test_readfile_and_fail(self):
        self.assertRaises(OSError,read_tsv_file(""))
    def test_get_event_no(self):
        data_df=read_tsv_file("data.tsv")
        expected_data_df=read_tsv_file(TEST_DATA_DIR+"/no_of_teaser_opened_event_for_each_category_user.tsv")
        result=no_of_event_for_each_category_user(data_df,"teaser_opened")
        print (result)
        print("/n /n")
        print(expected_data_df)
        assert_frame_equal(expected_data_df,result)
