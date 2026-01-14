import dlt
from pyspark.sql.functions import *
from pyspark.sql.types import IntegerType

@dlt.view(
    name = "customers_enr_view"
)
def products_enr_view():
    df = spark.readStream.table("customers_stg")
    df = df.withColumn("customer_name",upper(col("customer_name")))
    return df


dlt.create_streaming_table(
    name = "customers_enr"
)

dlt.create_auto_cdc_flow(
    target = "customers_enr",
    source = "customers_enr_view",
    keys = ["customer_id"],
    sequence_by = "last_updated",
    ignore_null_updates = False,
    stored_as_scd_type = 1
)