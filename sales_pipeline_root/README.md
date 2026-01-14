# first_pipeline

This folder defines all source code for the 'sales_pipeline' pipeline:

- `explorations`: Ad-hoc notebooks used to explore the data processed by this pipeline.
- `transformations`: All dataset definitions and transformations.
- `utilities`: Utility functions and Python modules used in this pipeline.

## Getting Started

To get started, go to the `transformations` folder -- most of the relevant source code lives there:

* By convention, every dataset under `transformations` is in a separate file.
* Take a look at the sample under "sample_users_first_pipeline.py" to get familiar with the syntax.
  Read more about the syntax at https://docs.databricks.com/ldp/developer/python-ref.
* Use `Run file` to run and preview a single transformation.
* Use `Run pipeline` to run _all_ transformations in the entire pipeline.
* Use `+ Add` in the file browser to add a new data set definition.
* Use `Schedule` to run the pipeline on a schedule!

For more tutorials and reference material, see https://docs.databricks.com/ldp.

View the live dashboard here: [Databricks Dashboard](https://dbc-d7b360d9-7f1f.cloud.databricks.com/dashboardsv3/01f0f1181cfb1c549ea9f7ca9ba9f7e8/published?o=2924169760416465&f_5bebfc30%7E9299cc83=West&f_6834a68f%7Etotal-sales-vs-category=%257B%2522columns%2522%253A%255B%2522x%2522%255D%252C%2522rows%2522%253A%255B%255B%2522Stationery%2522%255D%255D%257D)



<img width="883" height="531" alt="business_sales_dashboard" src="https://github.com/user-attachments/assets/9d735ee6-8ff3-420f-a4db-6dbbad2c8987" />
