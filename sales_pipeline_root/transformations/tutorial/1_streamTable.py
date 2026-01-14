# import dlt

# # creating Streaming Table

# @dlt.table(
#     name = "first_Stream_Table"
# )
# def first_Stream_Table():
#     df = spark.readStream.table("learning_spark_sql.practice_db.students_practice_table")
#     return df



# @dlt.table(
#     name = "transformed_orders"
# )
# def transformed_orders():
#     df = spark.readStream.table("first_Stream_Table")
#     return df



#     #creating a view
# @dlt.view(
#     name = "first_View"
# )
# def first_batch_view():
#     df = spark.read.table("learning_spark_sql.practice_db.students_practice_table")
#     return df
# # DBTITLE 1")