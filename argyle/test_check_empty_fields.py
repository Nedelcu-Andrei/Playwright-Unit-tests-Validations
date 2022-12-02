import pytest
from upwork import check_empty_fields


def test_invalid_type_empty_fields():
    mock_list = [1, 2, 3]
    with pytest.raises(AttributeError):
        check_empty_fields(mock_list)


def test_valid_type_empty_fields():
    mock_data = {
        "data": ""
    }
    check_empty_fields(mock_data)
    assert mock_data['data'] == "No available information."