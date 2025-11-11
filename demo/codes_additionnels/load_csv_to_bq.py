import functions_framework
from google.cloud import bigquery
import json

@functions_framework.http
def load_csv_to_bq(request):
    """
    Cloud Run HTTP trigger: attend un event JSON (Eventarc -> Cloud Storage finalize)
    """
    event = request.get_json()
    if not event:
        return "Pas d'event reçu", 400

    # Pretty print de l'event JSON
    print(json.dumps(event, indent=2))

    # Selon la structure envoyée par Eventarc, il faut adapter la lecture
    try:
        file_name = event["name"]
        bucket_name = event["bucket"]
    except KeyError:
        return "Impossible de trouver file_name ou bucket dans l'event", 400

    uri = f"gs://{bucket_name}/{file_name}"

    project_id = "gen-lang-client-0861341623"
    dataset_id = "taxi_dataset"
    table_id = file_name.split(".")[0]
    table_full_id = f"{project_id}.{dataset_id}.{table_id}"

    client = bigquery.Client()

    job_config = bigquery.LoadJobConfig(
        autodetect=True,
        skip_leading_rows=1,
        source_format=bigquery.SourceFormat.CSV,
        field_delimiter=";",
        #écrase les données
        write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE,
    )

    load_job = client.load_table_from_uri(uri, table_full_id, job_config=job_config)
    load_job.result()

    destination_table = client.get_table(table_full_id)
    print(f"✅ Chargé {destination_table.num_rows} lignes depuis {uri}", 200)
    return "OK",200