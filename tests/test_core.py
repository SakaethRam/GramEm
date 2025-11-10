import pytest
from gramem_basic import rephrase, ToneEngine

def test_formal():
    assert rephrase("hello {Formal}") == "Dear Sir/Madam, hello. GRAMEM ENGINE"

def test_casual():
    assert rephrase("hey {Casual}") == "Hey! GRAMEM ENGINE"

def test_invalid():
    assert rephrase("hello {Invalid}") is None

def test_custom():
    e = ToneEngine()
    e.add_tone("Pirate", {"hello": "ahoy"})
    assert e.rephrase("hello {Pirate}") == "Ahoy. GRAMEM ENGINE"