.. highlight:: sh

USER GUIDE
==========

Prerequisite
------------

- First and foremost, you will need to setup credential for `Accessing the API <https://tools.pieriandx.com/confluence/display/CGWP/API+User+Guide#APIUserGuide-AccessingtheAPI>`_.
- There are two options available: pass-in options flags or setup ``PDX_`` environment variables. Latter is preferred as follows::

    export PDX_USERNAME=<YOUR_PierianDx_CGW_LOGIN_EMAIL>
    export PDX_PASSWORD=<YOUR_PierianDx_CGW_LOGIN_PASSWORD>
    export PDX_INSTITUTION=<ASK_YOUR_PierianDx_CGW_ACCOUNT_MANAGER>
    export PDX_BASE_URL=https://app.pieriandx.com/cgw-api/v2.0.0

- Otherwise, you can always pass-in options flags as follows::

    pyriandx <command> \
        -b https://app.pieriandx.com/cgw-api/v2.0.0 \
        -u me@my_org.org \
        -p my_password \
        -i my_institution

- Pass-in options flags will override their environment variables counterpart, if present.
- You can omit ``PDX_BASE_URL`` or ``-b`` flag if you want to work against UAT environment, which is set by default.


Command Concept
---------------

- CLI is designed to be driven by **command** concept.
- Therefore, its command pattern usage is as follows::

    pyriandx <command> [options] [<args>...]

- Short description about available commands are as follow::

    help        Print help and exit
    version     Print version and exit
    case        Get a case from Case API
    list        List cases from Case API, optionally apply filters to limit results
    create      Accession a new case from given input JSON file
    upload      Upload case files for given Case ID
    run         Create sequencer run for given Case ID
    job         Create informatics job for given Case ID and Run ID
    poll        Poll informatics job status for given Case ID and Job ID
    report      Get a report for given Case ID


Printing Help
-------------

- CLI has self-contained useful ``help`` sub-commands.
- To print CLI command help::

    pyriandx help
    pyriandx case help
    pyriandx list help
    pyriandx create help
    pyriandx upload help
    pyriandx run help
    pyriandx job help
    pyriandx poll help
    pyriandx report help

- Each command help contain description about usage and notes. For example::

    $ pyriandx case help
    Usage:
        pyriandx case help
        pyriandx case [options] <case-id>

    Description:
        Get a case by given ID from PierianDx CGW. It returns in JSON
        format. You can further process it e.g. pretty print by pipe
        through with program such as jq.

    Example:
        pyriandx case 69695
        pyriandx case 69695 | jq


Getting a Case
--------------

- You can query existing case with ``case`` command by passing case ID as follows::

    pyriandx case 69695

- You can redirect output to store in JSON format as follows::

    pyriandx case 69695 > case_69695.json

- You can also use external program like jq_ to pretty print JSON format as follows::

    pyriandx case 69695 | jq

.. _`jq`: https://stedolan.github.io/jq/download/


Listing all Cases
-----------------

- To query all available cases, use ``list`` command as follows::

    pyriandx list | jq

- Optionally, you can apply filters as follows::

    pyriandx list accessionNumber=SBJ000123


Accession a New Case
--------------------

- To accession a new case, first, you must prepare case input file in JSON format.
- You can refer to example provided in `CGW API User Guide`_ or `pyriandx github repo`_ as JSON input template to work out for your case.
- Once you have case input file ready, you can create a case as follows::

    pyriandx create my_case.json

- Optionally, you can provide case files (typically VCF files) as follows::

    pyriandx create my_case.json file1.vcf.gz file2.vcf.gz file3.purple.cnv

- You can also prepare a folder and stage all your case files for upload. In this case, instead of providing individual case files, you can provide this stage directory as follows::

    pyriandx create my_case.json path/to/files/for/upload/


.. _`CGW API User Guide` : https://tools.pieriandx.com/confluence/display/CGWP/API+User+Guide#APIUserGuide-AccessioningaCase
.. _`pyriandx github repo`: https://github.com/umccr/pyriandx/blob/main/pyriandx/json/create_case.json


Uploading Case Files
--------------------

- Sometime, you might want to upload additional case files or, you might have just accessioned the case only.
- At any case, you can upload case files for given case.
- For example, to upload case files for case ID ``69695`` as follows::

    pyriandx upload 69695 file1.vcf.gz file2.vcf.gz file3.cnv

- Similarly, you can stage case files in a directory for upload. And provide this stage directory as follows::

    pyriandx upload 69695 path/to/SBJ00123/


Sequencer Run
-------------

- After case has accessioned and uploaded case files, you should create sequencer run.
- For example, to create sequencer run for case ID ``69695`` as follows::

    pyriandx run 69695

- The ``run`` command return Run ID (``runId`` field as in JSON form). This is serial sequence and, start from ``1`` and, increment by ``1`` on subsequence ``run`` command invocation.
- This will create a new sequencer run entry in ``sequencerRuns`` resource node (as in JSON form) of your case model.
- You can check existing sequencer run by getting a case and filter JSON as follows::

    pyriandx case 69695 | jq '.sequencerRuns[]'

- You will need at least one sequencer run entry to kick off informatics job (explain next).


Informatics Job
---------------

- In order to create analysis informatics job, you will need accessioned case with at least one sequencer run prepared for it.
- You can check your case readiness for informatics job submission by running ``case`` command to observe the case model output in JSON format.
- Once your case is ready for run, you will need Case ID and Run ID to kick off informatics job as follows::

    pyriandx job 69695 1

- The ``job`` command returns Job ID. You will need Job ID for tracking its status by ``poll`` command (explain next).


Polling Job Status
------------------

- Once informatics job has kicked off, it will take awhile for job to be completed.
- CLI comes with ``poll`` command for monitoring job status for convenience.
- You will need Case ID and Job ID for ``poll`` command as follows::

    pyriandx poll 69695 19635

- Polling timeout at every 30 minutes. You can poll again.
- You can abort polling by ``Ctrl+C`` at any time.
- You can also (ad-hoc) get a case and filter Job ID on the return JSON using ``jq`` as follows::

    pyriandx case 69695 | jq '.informaticsJobs[] | select(.id == "19635")'

- Or, specifically on ``status`` field as follows::

    pyriandx case 69695 | jq '.informaticsJobs[] | select(.id == "19635") | .status'

- Alternatively, you can check job status in PierianDx CGW dashboard.

    **Caveat:** Polling job status is not perfected yet. So please do not rely on this feature.

Download Analysis Report
------------------------

- When case report is ready, you can download it as follows::

    pyriandx report 69695

- Alternatively, you can download it from PierianDx CGW dashboard.

    **Caveat:** Download analysis report is not perfected yet. So please do not rely on this feature.

Case Assignment
---------------

- CLI is not yet supported case assignment to personnel at the moment.
- You can follow up assign the case to curator/personnel through PierianDx CGW dashboard.

    **Caveat:** We will add to next todo if this feature is desirable.

Issues
------

- Create or vote for feature/issue requests: https://github.com/umccr/pyriandx/issues
