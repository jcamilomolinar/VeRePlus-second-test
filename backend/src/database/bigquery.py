def searchData(query):
  from google.cloud import bigquery
  import os
  # Set the path to the credentials file
  os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "database/velezreyesplus-2nd-test.json"

  # Create a BigQuery client
  client = bigquery.Client()

  # Run the query
  queryJob = client.query(query)

  # Get the results
  results = queryJob.result()

  # Parse the results into a list of dictionaries 
  parsed_results = []
  for row in results:
    parsed_results.append(dict(row.items()))

  return parsed_results