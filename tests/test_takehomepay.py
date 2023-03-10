#!/usr/bin/env python
from takehomepay import takehomepay


def test_twentytwentytwo():
    tt = takehomepay.TwentyTwentyTwo()
    print(tt.calculate_tax(25_000, 0))