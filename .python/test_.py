import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from primes import isprime


@pytest.mark.parametrize("input,expected", [
    (1, False), (2, True), (3, True), (4, False), (5, True), 
    (6679, True), (6683, False), (6689, True), (6691, True), (6697, False),
    (6701, True), (6703, True), (6707, False),(6709, True), (6711, False),
    (6719, True), (6723, False), (6733, True), (6737, True), (6743, False),
    (6761, True), (6763, True), (6767, False), (6779, True), (6781, True), 
    (6787, False), (6791, True), (6793, True), (6697, False), (6803, True), 
    (6819, False), (6823, True), (6827, True), (6829, True), (6831, False), (6833, True),
    ])
def test(input, expected):
    assert isprime(input) == expected
