__about__ = "Oracle instant client binaries to be used together with cx_Oracle."
__version__= '0.0.5'
__author__ = 'Luca Mingarelli'
__email__ = "lucamingarelli@me.com"
__url__ = "https://github.com/LucaMingarelli/pyoracleclient"

import os
from pyoracleclient.pyoracleclient import *
from pyoracleclient.pyoracleclient import _TNSORA_PATH, _SQLNETORA_PATH

if not os.path.exists(_TNSORA_PATH):
    open(_TNSORA_PATH,'a').close()
if not os.path.exists(_SQLNETORA_PATH):
    open(_SQLNETORA_PATH,'a').close()