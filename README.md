# takehomepay

A Python package created to work out tax, pension and national insurance contributions in the UK by year.


Installation 
------------
Currently the library is not on the PyPi, so it can be installed from Github or cloned and installed using the setup.py file as below:

    python3 -m setup install

Usage
-----
    
    from takehomepay import TwentyTwentyThree

    tt = TwentyTwentyThree()
    tt.calculate_tax(gross=20_000, deductions=0)
    tt.calculate_national_insurance(gross=20_000)


Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
