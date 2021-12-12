import pyoracleclient as pyoc


def test_tns():
  pyoc.delete_all_tns()
  pyoc.add_tns(name='FSSDB', service_name='servicename.prd.tns',
               protocol1='TCP', host1='host1address', port1=1000,
               protocol2='TCP', host2='host1address', port2=1000)
  
def test_custom_tns():
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
