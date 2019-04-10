Pyriandx
========================

![Build Status](https://travis-ci.com/umccr/pyriandx.svg?branch=master)

Pyriandx is an API library for PierianDx genomic web services. 

## Getting started

Pyriandx can be used as a CLI tool OR a library. Oooh fancy!

### Using the CLI

TL;DR

```
pyriandx --username oldmate@fullysickinstitutiion.com.gov.edu.au --password h4x0r --institution institution-name --json case-file.json my-cool-vcf.vcf
```

Example `case-file.json` is in `pyriandx/json/create_case.json`.


```
PierianDX API client ::: API wrapper for PierianDx web services

Usage:
   pyriandx [-hvV] [--username <username>] [--password <password>] --institution <institution> [--output-dir <output-dir>] --json <json-file> <target-vcf>

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
```


### Using as a module
Check the `examples/` folder for some sweet example code. 
