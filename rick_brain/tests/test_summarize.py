from worker_rick.skills import summarize

def test_summarize_handle():
    result = summarize.handle("test input")
    assert isinstance(result, str)
    assert result  # Ensure it's not empty