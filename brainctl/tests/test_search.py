from worker_rick.skills import search

def test_search_handle():
    result = search.handle("test input")
    assert isinstance(result, str)
    assert result  # Ensure it's not empty