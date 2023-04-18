from pprint import pprint
def show_as_pandasDf(spark_df):
    temp=spark_df
    temp=temp.withColumn("InvoiceDate", temp["InvoiceDate"].cast("Date"))
    return temp.toPandas()
    
def show_as_pandasDf_T(spark_df):
    temp=spark_df
    temp=temp.withColumn("InvoiceDate", temp["InvoiceDate"].cast("Date"))
    return temp.toPandas().T

def show_head_as_pandasDf(spark_df):
    temp=spark_df
    temp=temp.withColumn("InvoiceDate", temp["InvoiceDate"].cast("Date"))
    return temp.limit(10).toPandas()

def show_head_as_pandasDf_T(spark_df):
    temp=spark_df
    temp=temp.withColumn("InvoiceDate", temp["InvoiceDate"].cast("Date"))
    return temp.limit(10).toPandas().T


    