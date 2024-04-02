if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):
    print(data.shape)
    print(data.head())
    
    # cast columns to int
    # i mean, it's already int in the raw file, but just for making sure
    columns_to_convert = ['user_id', 'anime_id', 'rating']
    data[columns_to_convert] = data[columns_to_convert].astype(int)
    print(data.dtypes)
    return data


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
