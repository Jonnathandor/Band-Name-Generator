import pytest
from band_name_generator import band_name_generator

def test_band_name_generator(monkeypatch, capsys):
    # Create an iterator with the expected inputs
    inputs = iter(['Jonathan', 'New York', 'Whiskers'])
    # Use the lambda function to call next() on the iterator
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    
    # Run the generator function
    band_name_generator()
    
    # Capture the output
    captured = capsys.readouterr()
    
    # Assert to check if the output is as expected
    assert "Your band name could be: New York Whiskers" in captured.out

def test_band_name_generator_different_input(monkeypatch, capsys):
    # Create an iterator with the expected inputs
    inputs = iter(['Alice', 'Los Angeles', 'Rex'])
    # Same as above, set the input to return the next value from the iterator
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    
    # Run the generator function
    band_name_generator()
    
    # Capture the output
    captured = capsys.readouterr()
    
    # Assert to check if the output is as expected
    assert "Your band name could be: Los Angeles Rex" in captured.out
