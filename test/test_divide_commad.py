# calc_app/tests/test_add_command.py
from calc_app.commands.divide.divide_command import divideCommand
import pytest

@pytest.fixture
def command():
    return divideCommand()

def test_execute_addition(monkeypatch, command):
    inputs = iter(['6', '3'])

    def mock_input(prompt):
        return next(inputs)

    results = []

    def mock_print(x):
        results.append(x)

    monkeypatch.setattr('builtins.input', mock_input)
    monkeypatch.setattr('builtins.print', mock_print)  # Capture print output
    command.execute()

    assert results == ['The result is: 2.0']  # Adjust expected output to match actual output