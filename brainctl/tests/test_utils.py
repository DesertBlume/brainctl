from worker_rick.skills import utils

def test_utils_handle():
    result = utils.handle("test input")
    assert isinstance(result, str)
    assert result  # Ensure it's not empty