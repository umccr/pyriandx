# -*- coding: utf-8 -*-
import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
import datetime
from jinja2 import Environment, PackageLoader, select_autoescape

class client:
        def __init__(self,baseURL="https://app.uat.pieriandx.com"):
                self.baseURL=baseURL
                self.jinja_env = Environment(
                        loader=PackageLoader(__name__, 'templates'),
                        autoescape=False
                )

        def create_case(self,accession_number):
                """Creates case with given accession number"""
                url = self.baseURL + "/createcase"
                data={"accession_number":accession_number}
                now = datetime.datetime.utcnow().isoformat()
                template = env.get_template('create_case.json')
                request_data = template.render(accession_number='12345')
                
                
                
        def upload_file(self,filename, accession_number):
                """Upload file to given accession number"""
                pass

        def get_status(self,job_id):
                """Get status of job"""
                pass

def requests_retry_session(retries=4,backoff_factor=1,status_forcelist=(500, 502, 504),session=None):
        session = session or requests.Session()
        retry = Retry(
                total=retries,
                read=retries,
                connect=retries,
                backoff_factor=backoff_factor,
                status_forcelist=status_forcelist,
        )
        adapter = HTTPAdapter(max_retries=retry)
        session.mount('http://', adapter)
        session.mount('https://', adapter)
        return session

def postAPI(data, endpoint): 
        try: 
                r = requests_retry_session().post(url, data=data)
        except Exception as x:
                print('PostAPI call failed after retries:', x.__class__.__name__)

