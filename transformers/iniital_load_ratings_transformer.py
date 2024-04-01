import pandas as pd

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):
    return data


@test
def test_output_not_none(output, *args) -> None:
    assert output is not None, 'The output is undefined'
