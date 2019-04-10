from docopt import docopt
import sys
import os

from pyriandx.log import *

from . import __title__, __version__, __description__, PROG

#TODO: There might be the need to break this out into subcommands, like create-case, download-report, get-case-info, etc

__doc__ = f'''

{__title__} ::: {__description__}

Usage: 
   {PROG} [-hvV] [--username <username>] [--password <password>] --institution <institution> [--output-dir <output-dir>] --json <json-file> <target-vcf>
   
Options:
   -b, --base_url                  Base URL for PierianDX service [default: https://app.uat.pieriandx.com/cgw-api/v2.0.0].
   -u, --username=username         Username for PierianDX service, usually an email address. Overrides environment if it exists.
   -p, --password=password         Password for PierianDX service. Overrides environment if it exists.
   -i, --institution=institution   Institution to use for API authentication
   -j, --json                      JSON file with details for target
   -o, --output-dir=output-dir     Directory to place downloaded reports. [default: output]
   -v, --verbose                   Make output more verbose innit
   -h, --help                      Prints this help and exit
   -V, --version                   Prints the version and exits
   

Environment variables:
   DEBUG_HTTP         If defined, prints verbose information for all http transactions, enabled with --verbose/-v
   PDX_USER           If defined, uses this as username for authenticating to PierianDX
   PDX_SECRET         If defined, uses this as password for authenticating to PierianDX
   BASE_URL           If defined, uses this as base URL for PierianDX service
'''

def parse_args(argv=sys.argv[1:]):
   version = f'{__title__} (version {__version__})'
   args = docopt(__doc__, argv, help=True, version=version)

   if os.environ.get('PDX_USER') and not args['--username']:
      print()
      args['--username'] = os.environ.get('PDX_USER')
   
   if os.environ.get('PDX_SECRET') and not args['--password']:
      args['--password'] = os.environ.get('PDX_SECRET')

   if not args['--username']:
      print(__doc__)
      log.critical("\nPlease provide a username via --username flag or PDX_USER environment variable.\n")
      sys.exit(1)

   if not args['--password']:
      print(__doc__)
      log.critical("\nPlease provide a password via --password flag or PDX_SECRET environment variable.\n")
      sys.exit(1)

      
   return args
