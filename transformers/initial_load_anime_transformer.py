import pandas as pd
import datetime as dt

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

# UTIL FUNCTION
def get_start_date(date_string):
    if str.lower(date_string[:3]) in [
        'jan', 'feb', 'mar', 'apr',
        'may', 'jun', 'jul','aug',
        'sep','oct', 'nov', 'dec'
        ]:
            if ' to ' in date_string:
                try:
                    start_date = dt.datetime.strptime(date_string.split(' to ')[0], '%b %d, %Y')
                    end_date = dt.datetime.strptime(date_string.split(' to ')[1], '%b %d, %Y')
                except:
                    start_date = None
                    end_date = None
            else:
                try:
                    start_date = dt.datetime.strptime(date_string, '%b %d, %Y')
                    end_date = dt.datetime.strptime(date_string, '%b %d, %Y')
                except:
                    start_date = None
                    end_date = None
    else:
        start_date = None
        end_date = None
    return start_date

def get_end_date(date_string):
    if str.lower(date_string[:3]) in [
        'jan', 'feb', 'mar', 'apr',
        'may', 'jun', 'jul','aug',
        'sep','oct', 'nov', 'dec'
        ]:
            if ' to ' in date_string:
                try:
                    start_date = dt.datetime.strptime(date_string.split(' to ')[0], '%b %d, %Y')
                    end_date = dt.datetime.strptime(date_string.split(' to ')[1], '%b %d, %Y')
                except:
                    start_date = None
                    end_date = None
            else:
                try:
                    start_date = dt.datetime.strptime(date_string, '%b %d, %Y')
                    end_date = dt.datetime.strptime(date_string, '%b %d, %Y')
                except:
                    start_date = None
                    end_date = None
    else:
        start_date = None
        end_date = None
    
    return end_date
    

@transformer
def transform(data, *args, **kwargs):

    # lower capital letters in columns, remove whitespaces
    data.columns = data.columns \
                    .str.replace(' ', '_') \
                    .str.lower()

    # cast numeric columns
    data['score'] = pd.to_numeric(data['score'], errors='coerce')
    data['episodes'] = pd.to_numeric(data['episodes'], errors='coerce')
    data['rank'] = pd.to_numeric(data['rank'], errors='coerce')
    data['popularity'] = pd.to_numeric(data['popularity'], errors='coerce')
    data['favorites'] = pd.to_numeric(data['favorites'], errors='coerce')
    data['scored_by'] = pd.to_numeric(data['scored_by'], errors='coerce')
    data['members'] = pd.to_numeric(data['members'], errors='coerce')

    # get specific dates from 'aired' columns
    data['aired_start'] = data['aired'].apply(get_start_date)
    data['aired_end'] = data['aired'].apply(get_end_date)

    anime_dtypes = {
        'anime_id': pd.Int64Dtype(),
        'name': str,
        'english_name': str,
        'other_name': str,
        'score': float,
        'genres': str,
        'synopsis': str,
        'type': str,
        'episodes': float,
        'aired': str,
        'aired_start': 'datetime64[D]',
        'aired_end': 'datetime64[D]',
        'premiered': str,
        'status': str,
        'producers': str,
        'licensors': str,
        'studios': str,
        'source': str,
        'duration': str,
        'rating': str,
        'rank': float,
        'popularity': pd.Int64Dtype(),
        'favorites': float,
        'scored_by': float,
        'members': float,
        'image_url': str,
    }
    # apply dtypes to data
    df = data.astype(dtype=anime_dtypes, copy=True, errors='raise')

    # sort the columns
    df = df[[
        'anime_id',
        'name',
        'english_name',
        'other_name',
        'score',
        'genres',
        'synopsis',
        'type',
        'episodes',
        'aired',
        'aired_start',
        'aired_end',
        'premiered',
        'status',
        'producers',
        'licensors',
        'studios',
        'source',
        'duration',
        'rating',
        'rank',
        'popularity',
        'favorites',
        'scored_by',
        'members',
        'image_url',
    ]]

    return df


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
