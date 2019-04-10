import os
import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
import http.client as http_client
from pyriandx.log import *

def requests_retry_session(headers,retries=4,backoff_factor=1,status_forcelist=(500, 502, 504),session=None, upload=False):
        if os.environ.get('DEBUG_HTTP') and upload == False: #We don't need to see every byte being uploaded in verbose mode
                http_client.HTTPConnection.debuglevel = 5
        else:
                http_client.HTTPConnection.debuglevel = 0

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
