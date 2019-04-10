import sys
import os
import json
from pprint import pprint, pformat
import time

import pyriandx.cli as cli
from pyriandx.client import client as _client
from pyriandx.log import *

spin = ['\\', '|', '/', '-']


def main(args=sys.argv[1:]):

    args = cli.parse_args(args)

    if args['--verbose'] == True:
        coloredlogs.install(level='DEBUG')
        os.environ["DEBUG_HTTP"] = "true"

    log.debug("Received arguments:\n" + str(args))

    input_file    = args['<json-file>']
    target_vcf    = args['<target-vcf>']
    output_dir    = args['--output-dir']
    username      = args['--username']
    password      = args['--password']
    institution   = args['--institution']

    client = _client(
    email=username,
    key=password,
    institution=institution
    )

    log.info("Creating case with input file: " + input_file)    
    case_id = client.create_case(input_file)
    log.info(f"Successfully created case with ID: {case_id}")

    log.info(f"Uploading target vcf {target_vcf} as case file...")
    client.upload_file(target_vcf, case_id)

    log.info("Adding sequencer run...")
    accession_number = client.parse_accession_number(input_file)
    seq_run_id = client.create_sequencer_run(accession_number)

    log.info("Creating processing job...")
    job_id = client.create_job(case_id,accession_number,seq_run_id, target_vcf)

    # #TODO: what are the other statuses?
    sys.stdout.write("\nJob is running, waiting for it to 'complete'...   ")
    status=client.get_job_status(case_id)
    count = 0
    while status != "complete" and status != "failed" and count < 60: #wait 30 mins max
        log.debug(f"Status is: {status}")
        for _ in range(15): #Check API every 30 seconds, and write out a spinny thing while we wait
            for c in spin:
                sys.stdout.write("\b%s" % c)
                sys.stdout.flush()
                time.sleep(.5)
        status=client.get_job_status(case_id)
        count = count + 1
    sys.stdout.write('\n')

    if status == "complete":
        log.info("Job has completed. Downloading report...")
        client.get_report(case_id, "output")
        log.info("\n\nDone.")
    elif status == "failed":
        log.critical(f"Job did not complete, status was {status}. Please send support request to support@pieriandx.com with the following info:")
        log.info(f"case id: {case_id}")
        log.info(f"job id: {job_id}")
        log.info(f"accession number:  {accession_number}")
        
    




if __name__ == '__main__':
    assert sys.version_info >= (3, 6), "This tool requires python3.6"
    try:
        main()
    except KeyboardInterrupt:
        pass
    