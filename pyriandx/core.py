# -*- coding: utf-8 -*-
import datetime
import json
import logging as log
import pkg_resources
from pprint import pprint
from utilities import requests_retry_session
import time

class client:
        log.basicConfig(level=log.DEBUG)

        def __init__(self, email, key, institution, baseURL="https://app.uat.pieriandx.com/cgw-api/v2.0.0"):
                self.baseURL=baseURL
                self.headers = {
                        'X-Auth-Email':email,
                        'X-Auth-Key':key,
                        'X-Auth-Institution':institution
                }
                self.email = email
                self.key = key
                self.institution = institution
                self.DATA_PATH = pkg_resources.resource_filename('pyriandx', 'json/') #this is required to import static data from the module

        def create_case(self,data):
                """Creates case with given accession number"""
                # log.debug("Got data for case {}".format(data))

                with open(self.DATA_PATH + 'create_case.json', 'r') as f:
                        request_data = json.load(f)

                request_data["specimens"][0]["accessionNumber"] = data["accessionNumber"]
                pprint(request_data)
                self.postAPI(request_data, "/case")
                
                
        def upload_file(self,filename, accession_number):
                """Upload file to given accession number"""
                pass

        def get_status(self,job_id):
                """Get status of job"""
                pass

        def postAPI(self,data, endpoint): 
                url = self.baseURL + endpoint
                log.debug("Sending request to {}".format(url))
                t0 = time.time()

                post_headers = self.headers
                post_headers['Content-Type'] = "application/json"
                post_headers['Accept-Encoding'] = "*"


                # with open("request-debug.json", "w") as data_file:
                #         json.dump(data, data_file, indent=2)


                try: 
                        response = requests_retry_session(post_headers).post(url, json=data)
                except Exception as x:
                        log.critical('{} call failed after retry: {}'.format(endpoint, x))
                else:
                        if(response.status_code == 200):
                                log.debug('call to {} succeeded'.format(endpoint))
                                log.debug(response.text)
                        else:
                                log.critical('call to {} failed. Error code was {}'.format(endpoint, response.status_code))
                finally:
                        t1 = time.time()
                        log.debug("call took {} seconds".format(t1 - t0))


