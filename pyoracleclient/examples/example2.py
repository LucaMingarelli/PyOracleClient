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