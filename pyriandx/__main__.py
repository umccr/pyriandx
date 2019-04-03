import sys
import os
import logging as log
import json
from pprint import pprint, pformat

import pyriandx.cli as cli
import pyriandx

def main(args=sys.argv[1:]):
    args = cli.parse_args(args)

    # print("args bruh:" + str(args))

    client = pyriandx.client(
    email=args['--username'],
    key=args['--password'],
    institution=args['--institution']
    )

    input_file = args['<json-file>']

    log.debug("Creating case with input file:\n " + input_file)    
    case_id = client.create_case(input_file)
    log.info("Case ID: " + str(case_id))
    

if __name__ == '__main__':
    assert sys.version_info >= (3, 6), "This tool requires python3.6"
    main()