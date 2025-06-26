from worker_rick.skills import help

def test_help_handle():
    result = help.handle("test input")
    assert isinstance(result, str)
    assert result  # Ensure it's not empty