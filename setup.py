from setuptools import setup
        
# these lines allow the version to be specified in Makefile.private
import os
version = os.environ.get("MODULEVER", "0.0")
        
setup(
    install_requires = ['dls_pmaclib>=1.4'], # require statements go here
    name = 'dls_pmaccontrol',
    version = version,
    description = 'Module',
    author = 'Ulrik Kofoed Pedersen',
    author_email = 'Ulrik.Pedersen@diamond.ac.uk',    
    packages = ['dls_pmaccontrol'],
    entry_points = {'console_scripts': [
        'dls-pmac-control.py = dls_pmaccontrol.motor:main']},
    include_package_data = True,
    package_data = {'': ['*.png']},        
    zip_safe = False
    )        
