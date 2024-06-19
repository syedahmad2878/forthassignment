# calc_app/tests/test_goodbye_command.py
from calc_app.commands.goodbye.goodbye_command import goodbyeCommand
import pytest

@pytest.fixture
def command():
    return goodbyeCommand()

def test_execute_addition(monkeypatch, command):
    #inputs = iter(['6', '3'])

    def mock_input(prompt):
        return next(inputs)

    results = []

    def mock_print(x):
        results.append(x)

    monkeypatch.setattr('builtins.input', mock_input)
    monkeypatch.setattr('builtins.print', mock_print)  # Capture print output
    command.execute()

    assert results == ['GoodBye World!']  # Adjust expected output to match actual output