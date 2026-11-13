import pytest

from tinystats import mean


def test_mean_of_integers():
    assert mean([1, 2, 3]) == 2.0


def test_mean_of_floats():
    assert mean([0.5, 1.5]) == pytest.approx(1.0)

def test_zero():
    with pytest.raises(ValueError, match ="values must not be empty"):
        mean([])

# Exercise: the empty-list case is not tested yet.
# Codecov shows the `raise ValueError` line as not covered.
# Write a test with `pytest.raises(ValueError)` to cover it.