# -*- coding: utf-8 -*-
import datetime
import json
import logging as log
import pkg_resources
from pprint import pprint, pformat
import time

from .utilities import requests_retry_session

class client:
        log.basicConfig(level=log.DEBUG)

        def __init__(self, email, key, institution, baseURL="https://app.uat.pieriandx.com/cgw-api/v2.0.0"):
                self.baseURL=baseURL
                self.headers = {
                        'X-Auth-Email':email,
                        'X-Auth-Key':key,
                        'X-Auth-Institution':institution
                }
                self.DATA_PATH = pkg_resources.resource_filename('pyriandx', 'json/') #this is required to import static data from the module

        def create_case(self,data):
                """Creates case with given accession number"""

                with open(self.DATA_PATH + 'create_case.json', 'r') as f:
                        request_data = json.load(f)

                request_data["specimens"][0]["accessionNumber"] = data["accessionNumber"]
                log.debug("Creating case with data:")
                log.debug(pformat(request_data))
                response = self.post_api("/case",data=request_data).json()
                return response["id"]

        def create_sequencer_run(self,data):
                """Creates case with given accession number"""

                with open(self.DATA_PATH + 'create_sequencer_run.json', 'r') as f:
                        request_data = json.load(f)

                request_data["specimens"][0]["accessionNumber"] = data["accessionNumber"]
                log.debug("Creating sequencer run with data:")
                log.debug(pformat(request_data))
                response = self.post_api("/sequencerRun",data=request_data).json()
                return response["id"]

        def create_job(self,case_id, accession_number):
                """Creates job with given accession number"""

                with open(self.DATA_PATH + 'create_job.json', 'r') as f:
                        request_data = json.load(f)


                request_data["input"][0]["accessionNumber"] = str(accession_number)

                log.debug("Creating job with case_id: " + str(case_id) + " accession_number: " + str(accession_number))

                endpoint = "/case/"+str(case_id)+"/informaticsJobs"

                self.post_api(endpoint,data=request_data)

                
                
        def upload_file(self,filename, case_id):
                """Upload file to given accession number"""
                files = {'file': open(filename, 'rb')}
                endpoint = "/case/"+str(case_id)+"/caseFiles/"+filename
                log.debug("Upload file to endpoint: " + endpoint)
                self.post_api(endpoint,files=files)



        def get_status(self,job_id):
                """Get status of job"""
                pass
        
        def add_sequencer_run(self,accession_number):
                """Add sequencer run"""
                pass
        
        def get_case_info(self,case_id):
                """Get case info for given case ID"""
                return self.get_api("/case/"+str(case_id))


        def get_api(self, endpoint): 
                """Internal function to create get requests to the API"""
                url = self.baseURL + endpoint
                log.debug("Sending request to {}".format(url))
                t0 = time.time()

                try: 
                        response = requests_retry_session(self.headers).get(url)
                except Exception as x:
                        log.critical('{} call failed after retry: {}'.format(endpoint, x))
                else:
                        if(response.status_code == 200):
                                log.debug('call to {} succeeded'.format(endpoint))
                                return json.loads(response.text)
                        else:
                                log.critical('call to {} failed. Error code was {}'.format(endpoint, response.status_code))
                                log.critical("server responded with " + response.text)
                                
                finally:
                        t1 = time.time()
                        log.debug("call took {} seconds".format(t1 - t0))


        def post_api(self, endpoint, data=None, files=None): 
                """Internal function to create post requests to the API"""
                url = self.baseURL + endpoint
                log.debug("Sending request to {}".format(url))
                t0 = time.time()

                post_headers = self.headers
                if data is not None:        
                        post_headers['Content-Type'] = "application/json"
                        post_headers['Accept-Encoding'] = "*"

                # uncomment if youd like to inspect the json data we're sending
                # with open("request-debug.json", "w") as data_file:
                #         json.dump(data, data_file, indent=2)

                try: 
                        response = requests_retry_session(post_headers,retries=0).post(url, json=data, files=files)
                except Exception as x:
                        log.critical('{} call failed after retry: {}'.format(endpoint, x))
                else:
                        if(response.status_code == 200):
                                log.debug("call to " + endpoint + " succeeded")
                                log.debug("response was " + response.text)
                                return response
                        else:
                                log.critical('Call to {} failed. Error code was {}'.format(endpoint, response.status_code))
                                log.critical("server responded with " + response.text)
                                #what to return here?
                finally:
                        t1 = time.time()
                        log.debug("Call took {} seconds".format(t1 - t0))


