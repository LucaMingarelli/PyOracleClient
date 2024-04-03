"""Created on Thu Dec 24 10:10:01 2020
@author: Luca Mingarelli
"""
from pathlib import Path

from pyoracleclient import __file__
import ntpath, os, shutil
from datetime import datetime
from pyoracleclient.tns_template import _TNS_TEMPLATE

_ROOT = ntpath.dirname(__file__)
_TNSORA_PATH = f'{_ROOT}/instantclient/network/admin/tnsnames.ora'
_SQLNETORA_PATH = f'{_ROOT}/instantclient/network/admin/sqlnet.ora'
_INSTANTCLIENT_PATH = f"{_ROOT}/instantclient"

def _clean_client_dir():
    if os.path.exists(_INSTANTCLIENT_PATH):
        date=datetime.now()
        tempdir = f'{_ROOT}/.temp/{str(date.year)+str(date.month)}/{str(date)}'
        os.makedirs(tempdir, exist_ok=True)
        os.system(f"mv '{_INSTANTCLIENT_PATH}' '{tempdir}'")

def get_client(version='19.3.0.0.0', sys='linux', url=None):
    """Downloads an oracle instant client. By default for linux 64. To obtain a client for a different system
    provide the corresponding url instead.
    Visit 'https://www.oracle.com/database/technologies/instant-client/downloads.html',
    choose your version, and copy the download link. For example for version 19.3.0.0.0 linux 64b,
    this will be in the form:
    'https://download.oracle.com/otn_software/linux/instantclient/193000/instantclient-basic-linux.x64-19.3.0.0.0dbru.zip'
    Args:
        version (str or None): Version to be downloaded
        sys (str or None): by default 'linux'.
        url (str or None): Alternatively provide url from which the download should occur.
    """
    _clean_client_dir()
    import requests, zipfile
    from tqdm import tqdm
    ORACLE_ROOT = f"https://download.oracle.com/otn_software/{sys}/instantclient"
    url = url or f"{ORACLE_ROOT}/{version.replace('.', '')}/instantclient-basic-{sys}.x64-{version}dbru.zip"
    r = requests.get(url, allow_redirects=True, stream=True)
    total_size = r.headers.get('content-length')
    zip_file = f"{_ROOT}/instantclient{version[:4].replace('.', '_')}.zip"

    with open(zip_file, 'wb') as f:
        bar = tqdm(total=int(total_size), desc=f'Getting client, v.{version[:4]}',
                   unit_scale=True, unit='bytes')
        for data in r.iter_content(chunk_size=4096):
            f.write(data)
            bar.update(4096)

    # Unzip client
    with zipfile.ZipFile(zip_file, "r") as zip_ref:
        zip_ref.extractall(f"{_ROOT}/")
    os.remove(zip_file)

    # Drop version from directory name
    client_dir = [d for d in os.listdir(_ROOT)
                  if os.path.isdir(f"{_ROOT}/{d}")
                  and d[:13] == 'instantclient'][0]
    source = f"{_ROOT}/{client_dir}"
    destination = _INSTANTCLIENT_PATH
    if os.path.exists(destination):
        shutil.rmtree(destination, ignore_errors=True)
    os.makedirs(destination, exist_ok=True)
    # os.system(f"mv '{source}' '{destination}/'")
    os.rename(source, destination)
    with open(f"{destination}/__init__.py", 'a+'):
        pass
    try:
        if not os.path.exists(_TNSORA_PATH):
            with open(_TNSORA_PATH, 'a+'): pass
        if not os.path.exists(_SQLNETORA_PATH):
            with open(_SQLNETORA_PATH, 'a+'): pass
    except:
        pass

    print(f"\nOracle Instant Client version {version} stored at '{_ROOT}/instantclient'.")


def delete_all_tns(confirm=False):
    """Clears the file `tnsnames.ora` stored at pyoracleclient._TNSORA_PATH.
    Args:
        confirm (bool): if False (default) asks for confirmation.
        """
    if not confirm: print('This will reset all your tnsnames currently saved.\nDo you want to proceed? [y/n]')
    proceed = None
    while str(proceed).lower() not in ['y', 'n']:
        proceed = input() if not confirm else 'y'
        if proceed.lower() == 'n':
            print('Aborted.')
        elif proceed.lower() == 'y':
            if os.path.exists(_TNSORA_PATH):
                with open(_TNSORA_PATH, "r+") as f: f.truncate(0)
        else:
            print("Expected either 'y' or 'n'.\nDo you want to proceed? [y/n]")


def add_tns(name, protocol1, host1, port1, service_name, failover='ON', load_balance='OFF',
            protocol2=None, host2=None, port2=None):
    """Adds tns to the file tnsnames.ora from a template (pyoracleclient._TNS_TEMPLATE)"""
    new_tns = _TNS_TEMPLATE.format(_name=name, _failover=failover, _load_balance=load_balance,
                                   _protocol1=protocol1, _host1=host1, _port1=port1,
                                   _protocol2=protocol2, _host2=host2, _port2=port2,
                                   _service_name=service_name)

    if not os.path.exists(_TNSORA_PATH):
        os.makedirs(ntpath.dirname(_TNSORA_PATH), exist_ok=True)
        Path(_TNSORA_PATH).touch()
    with open(_TNSORA_PATH, "a+") as f:
        f.write(new_tns)
        f.write('\n')


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
        for l in f: print(l, end='')

def _clear_temp():
    if os.path.exists(f'{_ROOT}/.temp'):
        date=datetime.now()
        date=str(date.year)+str(date.month)
        for dir in os.listdir(f'{_ROOT}/.temp'):
            if date>dir:
                os.system(f"rm -rfd '{_ROOT}/.temp/{dir}'")

