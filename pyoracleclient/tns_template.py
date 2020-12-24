_TNS_TEMPLATE = """{_name} = (DESCRIPTION=
                                 (ADDRESS_LIST=(FAILOVER = {_failover})
                                               (LOAD_BALANCE = {_load_balance})
                                               (ADDRESS=(PROTOCOL={_protocol1})
                                                        (HOST={_host1})
                                                        (PORT={_port1}))
                                               (ADDRESS=(PROTOCOL={_protocol1})
                                                        (HOST={_host2})
                                                        (PORT={_port2})))
                                 (CONNECT_DATA=(SERVER=dedicated)
                                               (SERVICE_NAME={_service_name}))
                             )"""