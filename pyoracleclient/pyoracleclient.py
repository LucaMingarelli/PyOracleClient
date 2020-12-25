"""Created on Thu Dec 24 10:10:01 2020
@author: Luca Mingarelli
"""
# from pyoracleclient import __file__
import ntpath
from pyoracleclient.tns_template import _TNS_TEMPLATE

_TNSORA_PATH = f'{ntpath.dirname(__file__)}/instantclient/network/admin/tnsnames.ora'


def _delete_all_tns(confirm=False):
    """Clears the file `tnsnames.ora` stored at pyoracleclient._TNSORA_PATH.
    Args:
        confirm (bool): if False (default) asks for confirmation.
        """
    print('This will reset all your tnsnames currently saved.\nDo you want to proceed? [y/n]')
    proceed = None
    while str(proceed).lower() not in ['y', 'n']:
        proceed = input() if not confirm else 'y'
        if proceed.lower()=='n':
            print('Aborted.')
        elif proceed.lower()=='y':
            file = open(_TNSORA_PATH, "r+")
            file.truncate(0)
            file.close()
        else:
            print("Expected either 'y' or 'n'.\nDo you want to proceed? [y/n]" )


def add_tns(name, protocol1, host1, port1, service_name, failover='ON', load_balance='OFF',
            protocol2=None, host2=None, port2=None):
    """Adds tns to the file tnsnames.ora from a template (pyoracleclient._TNS_TEMPLATE)"""
    new_tns = _TNS_TEMPLATE.format(_name=name, _failover=failover, _load_balance=load_balance,
                                   _protocol1=protocol1, _host1=host1, _port1=port1,
                                   _protocol2=protocol2, _host2=host2, _port2=port2,
                                   _service_name=service_name)
    with open(_TNSORA_PATH, "a") as f:
        f.write(new_tns)

def add_custom_tns(tns):
    """Adds the tns specification to the file tnsnames.ora.
    Alternatively, you can also use the template stored in pyoracleclient._TNS_TEMPLATE.
    Args:
        tns (str): The tns specification to be added to the file tnsnames.ora.
        """
    with open(_TNSORA_PATH, "a") as f:
        f.write(tns)

def print_tnsnames():
    with open(_TNSORA_PATH, "r") as f:
        for l in f: print(l)