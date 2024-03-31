import pandas as pd


if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):

    # lower capital letters in columns, remove whitespaces
    data.columns = data.columns \
                    .str.replace(' ', '_') \
                    .str.lower()

    # cast numeric columns
    data['mal_id'] = pd.to_numeric(data['mal_id'], errors='coerce')
    data['days_watched'] = pd.to_numeric(data['days_watched'], errors='coerce')
    data['mean_score'] = pd.to_numeric(data['mean_score'], errors='coerce')
    data['watching'] = pd.to_numeric(data['watching'], errors='coerce')
    data['completed'] = pd.to_numeric(data['completed'], errors='coerce')
    data['on_hold'] = pd.to_numeric(data['on_hold'], errors='coerce')
    data['dropped'] = pd.to_numeric(data['dropped'], errors='coerce')
    data['plan_to_watch'] = pd.to_numeric(data['plan_to_watch'], errors='coerce')
    data['total_entries'] = pd.to_numeric(data['total_entries'], errors='coerce')
    data['rewatched'] = pd.to_numeric(data['rewatched'], errors='coerce')
    data['episodes_watched'] = pd.to_numeric(data['episodes_watched'], errors='coerce')

    # using the following for dates because
    # df = data.astype(dtype=anime_dtypes, copy=True, errors='raise') -- does not work!
    data['birthday'] = pd.to_datetime(data['birthday'], errors='coerce')
    data['joined'] = pd.to_datetime(data['joined'], errors='coerce')

    return data


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
