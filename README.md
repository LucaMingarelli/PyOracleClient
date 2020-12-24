# PyOracleClient <img src="" width="200"/>


[![version](https://img.shields.io/badge/version-0.0.1-success.svg)](#)

## About

This package contains an Oracle Instant Client's binaries, 
necessary to connect to Oracle databases with `cx_Oracle`.

# Installation
You can install with pip as:

`pip install pyoracleclient`

## Example

You can add tns names via the `pyoracleclient.add_tns` function as shown below.
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

[![Python](https://img.shields.io/static/v1?label=made%20with&message=Python&color=blue&style=for-the-badge&logo=Python&logoColor=white)](#)

