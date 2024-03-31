from mage_ai.settings.repo import get_repo_path
from mage_ai.io.bigquery import BigQuery
from mage_ai.io.config import ConfigFileLoader
from pandas import DataFrame
from os import path

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter


@data_exporter
def export_data_to_big_query(df: DataFrame, **kwargs) -> None:

    table_id = 'anime-analytics-418714.test_mage_ny_taxi.yellow_cab_data'
    config_path = path.join(get_repo_path(), 'io_config.yaml')
    config_profile = 'default'

    # let's just cut the number of rows for now
    df = df.iloc[:50000]
    print('starting loading to bigquery...')

    BigQuery.with_config(ConfigFileLoader(config_path, config_profile)).export(
        df,
        table_id,
        if_exists='replace',  # Specify resolution policy if table name already exists
    )

    print('done loading to bigquery!')
