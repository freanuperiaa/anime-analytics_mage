import pyarrow as pa
import pyarrow.parquet as pq
import os


if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter


os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/home/src/default_repo/gcp-creds/service-account.json'


bucket_name = 'fperia-anime-bucket'
object_key = 'ratings.parquet'
project_id = 'anime-analytics-418714'

table_name = 'anime_ratings'
root_path = f'{bucket_name}/{table_name}'


@data_exporter
def export_data(data, *args, **kwargs):

    data = data.iloc[80000000:]

    table = pa.Table.from_pandas(data)

    # write to GCS
    gcs = pa.fs.GcsFileSystem()
    pq.write_to_dataset(
        table,
        root_path=root_path,
        filesystem=gcs
    )

