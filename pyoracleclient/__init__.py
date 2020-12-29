__about__ = "Oracle instant client binaries to be used together with cx_Oracle."
__version__= '0.2.5'
__author__ = 'Luca Mingarelli'
__email__ = "lucamingarelli@me.com"
__url__ = "https://github.com/LucaMingarelli/pyoracleclient"

from pyoracleclient.pyoracleclient import *
from pyoracleclient.pyoracleclient import _clear_temp

_clear_temp()