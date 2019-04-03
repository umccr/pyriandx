import pyriandx
import random
import time
import sys
import os

if not os.environ.get('PYRIAN_KEY'):
    print("PYRIAN_KEY not set in environment! Please set with your pieriandx password and try again.")
    sys.exit(1)


client = pyriandx.client(
    email="oldmate@fullysick.edu.gov.au",
    key=os.environ.get('PYRIAN_KEY'), #Do not hardcode creds please :)
    institution="xxxxx"
    )

accession_number = random.randint(1,9999)
data = {}
data["accessionNumber"] = accession_number

case_id = client.create_case(data)
print("got case id ", case_id)

case_info = client.get_case_info(case_id)
print("got case info:")
print(case_info)

print("uploading file...")
client.upload_file('example.vcf', case_id)

print("creating job...")
client.create_job_vcf(case_id)

print("Waiting for job to finish...")
status=client.get_job_status(case_id)
while status != "complete":
    print("Sleeping for 60 seconds before continuing...")
    time.sleep(60)
    status=client.get_job_status(case_id)

print("Downloading report...")
client.get_report(case_id, "output")

