import dlt

customer_rules = {
    "rule_1":"customer_id is not null",
    "rule_2":"customer_name >= 0"
}


@dlt.table(
    name = "customers_stg"
)
@dlt.expect_all(customer_rules)
def custmers_stg():
    df = spark.readStream.table("dlt_kapil.default.customers")
    return df