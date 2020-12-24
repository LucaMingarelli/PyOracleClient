import pyoracleclient as pyoc

pyoc._delete_all_tns()

pyoc.add_tns(name='FSSDB', service_name='servicename.prd.tns',
             protocol1='TCP', host1='host1address', port1=1000,
             protocol2='TCP', host2='host1address', port2=1000)