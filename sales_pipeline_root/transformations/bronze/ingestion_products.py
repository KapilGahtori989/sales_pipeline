import dlt

#product expectations
product_rules = {
    "rule_1":"product_id is not null",
    "rule_2":"price >= 0"
}


@dlt.table(
    name = "products_stg"
)
@dlt.expect_all_or_drop(product_rules)
def products_stg():
    df = spark.readStream.table("dlt_kapil.default.products")
    return df

    