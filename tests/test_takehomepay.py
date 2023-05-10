#!/usr/bin/env python
from takehomepay import takehomepay


def test_twentytwentytwo():
    tt = takehomepay.TwentyTwentyTwo()
    assert float(tt.calculate_tax(20_000, 0)) == 1486.0, "Error on 20k"
    assert float(tt.calculate_tax(60_000, 0)) == 11_432.0, "Error on 60k"
    assert float(tt.calculate_tax(200_000, 0)) == 74_960.0, "Error on 200k"
