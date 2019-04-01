import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
import logging as log
import http.client as http_client
import os

if os.environ.get('DEBUG_HTTP'):
        http_client.HTTPConnection.debuglevel = 5

def requests_retry_session(headers,retries=4,backoff_factor=1,status_forcelist=(500, 502, 504),session=None):
        requests.Session()
        session = session or requests.Session()
        retry = Retry(
                total=retries,
                read=retries,
                status=retries,
                connect=retries,
                backoff_factor=backoff_factor,
                status_forcelist=status_forcelist,
                method_whitelist=['HEAD', 'TRACE', 'GET', 'PUT', 'OPTIONS', 'DELETE','POST']
        )
        adapter = HTTPAdapter(max_retries=retry)
        session.mount('http://', adapter)
        session.mount('https://', adapter)
        session.headers.update(headers)
        return session

def get_filename_from_response(cd):
    """
    Get filename from content-disposition
    """
    if not cd:
        return None
    fname = re.findall('filename=(.+)', cd)
    if len(fname) == 0:
        return None
    return fname[0]