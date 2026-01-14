import dlt
from pyspark.sql.functions import sum

@dlt.table(
    name = "business_sales"
)
def business_sales():
    df_fact = spark.read.table("fact_sales")
    df_dimCust = spark.read.table("dim_customers")
    df_dimProd = spark.read.table("dim_products")
    df_join = df_fact.join(df_dimCust,df_fact.customer_id == df_dimCust.customer_id,"inner").join(df_dimProd,df_fact.product_id == df_dimProd.product_id,"inner") 
    df_prun = df_join.select("region","category","total_amount")
    df_agg = df_prun.groupBy("region","category").agg(sum("total_amount").alias("total_sales"))
    return df_agg


#equivalent sql code (pain in ass)
# def business_sales():
#     return spark.sql("""
#                      select p.category,r.region,sum(f.total_amount) as total_amount
#                      from LIVE.fact_sales f
#                      join LIVE.dim_customers r
#                      on f.customer_id = r.customer_id
#                      join LIVE.dim_products p
#                      on f.product_id = p.product_id
#                      group by p.category,r.region
#                      """)