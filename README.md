# PyOracleClient <img src="https://github.com/LucaMingarelli/PyOracleClient/raw/master/pyoracleclient/res/icon.png" width=" 70"/>


[![CircleCI](https://dl.circleci.com/status-badge/img/gh/LucaMingarelli/PyOracleClient/tree/master.svg?style=svg)](https://dl.circleci.com/status-badge/redirect/gh/LucaMingarelli/PyOracleClient/tree/master)
[![version](https://img.shields.io/badge/version-0.2.5-success.svg)](#)
[![PyPI Latest Release](https://img.shields.io/pypi/v/PyOracleClient.svg)](https://pypi.org/project/PyOracleClient/)
[![License](https://img.shields.io/pypi/l/PyOracleClient.svg)](https://github.com/LucaMingarelli/PyOracleClient/blob/master/LICENSE.txt)
[![Downloads](https://static.pepy.tech/personalized-badge/pyoracleclient?period=total&units=international_system&left_color=grey&right_color=blue&left_text=Downloads)](https://pepy.tech/project/pyoracleclient)
<a href="https://www.buymeacoffee.com/lucamingarelli" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/arial-yellow.png" alt="Buy Me A Coffee" style="height: 30px !important;width: 109px !important;" ></a>

## About

This package provides access to Oracle Instant Client's binaries, 
necessary to connect to Oracle databases with `cx_Oracle`.

# Installation
You can install with pip as:

`pip install pyoracleclient`

## Example


After installation you want to download the oracle instant client: you can do this via the following:
```python
import pyoracleclient as pyoc

pyoc.get_client(version='19.3.0.0.0', sys='linux', url=None)
```

By default version 19.3 for linux 64bits is downloaded. 
To obtain a client for a different system provide the corresponding `url` instead.
Visit 'https://www.oracle.com/database/technologies/instant-client/downloads.html',
choose your version, and copy the download link. 
For example for version `19.3.0.0.0` linux 64b, this will be in the form:
`https://download.oracle.com/otn_software/linux/instantclient/193000/instantclient-basic-linux.x64-19.3.0.0.0dbru.zip`.

You can now add tns names via the `pyoracleclient.add_tns` function as shown below.
```python
import pyoracleclient as pyoc

pyoc._delete_all_tns()

pyoc.add_tns(name='FSSDB', service_name='servicename.prd.tns',
             protocol1='TCP', host1='host1address', port1=1000,
             protocol2='TCP', host2='host1address', port2=1000)
```
Alternatively you can append your own tns specification as a string as follows:
```python
import pyoracleclient as pyoc

pyoc.add_custom_tns("""yourtnsname = (DESCRIPTION=
                    (ADDRESS_LIST=(FAILOVER=ON)
                                  (LOAD_BALANCE = OFF)
                                  (ADDRESS=(PROTOCOL=TCP)
                                           (HOST=host1address)
                                           (PORT=1000))
                                  (ADDRESS=(PROTOCOL=TCP)
                                           (HOST=host1address)
                                           (PORT=1000)))
                                  (CONNECT_DATA=(SERVER=dedicated)
                                  (SERVICE_NAME=servicename.prd.tns)))
                    """)
```


Finally, you can also fill the `tnsnames.ora` file manually. 
Its location can be found in the variable `pyoracleclient._TNSORA_PATH`.

# Author
Luca Mingarelli, 2020

**You find this work useful?** <a href="https://www.buymeacoffee.com/lucamingarelli" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/arial-yellow.png" alt="Buy Me A Coffee" style="height: 30px !important;width: 109px !important;" ></a>

[![Python](https://img.shields.io/static/v1?label=made%20with&message=Python&color=blue&style=for-the-badge&logo=Python&logoColor=white)](#)


