# from pyspark.sql.types import StructType, StructField, StringType, IntegerType, LongType, DoubleType

# default_schema = StructType([ 
#     StructField(UID, StringType(), True), 
#     StructField(TIMESTAMP, LongType(), True), 
#     StructField(LATITUDE, DoubleType(), True), 
#     StructField(LONGITUDE, DoubleType(), True), 
# ]) 



UID = 'uid'
TIMESTAMP = 'timestamp'
MERCATOR_COORD = 'mercator_coord'
MERCATOR_X = 'x'
MERCATOR_Y = 'y'
LATITUDE = 'latitude'
LONGITUDE = 'longitude'
DATE = 'date'
DATE_HOUR = 'date_hour'
DAY_OF_WEEK = 'day_of_week'


DEFAULT_SPEEDS = {'park': 2/1.96,
                  'home': 0.75/1.96,
                  'work': 0.75/1.96,
                  'retail': 1.75/1.96}

FAST_SPEEDS = {'park': 2.5/1.96,
                  'home': 1/1.96,
                  'work': 1/1.96,
                  'retail': 2/1.96}

SLOW_SPEEDS = {'park': 1.5/1.96,
               'home': 0.5/1.96,
               'work': 0.5/1.96,
               'retail': 1.5/1.96}

DEFAULT_STILL_PROBS = {'park': 0.5,
                       'home': 0.9,
                       'work': 0.9,
                       'retail': 0.5}


FAST_STILL_PROBS = {'park': 0.1,
                       'home': 0.75,
                       'work': 0.75,
                       'retail': 0.2}

SLOW_STILL_PROBS = {'park': 0.75,
                       'home': 0.95,
                       'work': 0.95,
                       'retail': 0.75}