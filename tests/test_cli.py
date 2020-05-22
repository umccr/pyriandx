import os
from unittest import TestCase

from mockito import when, unstub, verify

from pyriandx import cli


class CLIUnitTests(TestCase):

    def setUp(self) -> None:
        os.environ['PDX_USERNAME'] = "mock"
        os.environ['PDX_PASSWORD'] = "mock"
        os.environ['PDX_INSTITUTION'] = "mock"
        os.environ['PDX_BASE_URL'] = "mock"

    def tearDown(self) -> None:
        unstub()

    def test_case(self):
        mock_case = {'id': 1}
        when(cli.Client).get_case_info(...).thenReturn(mock_case)
        case_ = cli.Case({}, ['case', '1'])
        self.assertEqual('1', case_.case_id)
        verify(cli.Client, times=1).get_case_info(...)

    def test_list(self):
        mock_case_list = [{'id': 1}, {'id': 2}]
        when(cli.Client).list_cases(...).thenReturn(mock_case_list)
        list_ = cli.List({}, ['list'])
        verify(cli.Client, times=1).list_cases(...)
        self.assertEqual(2, len(list_.cases))

    def test_upload(self):
        when(cli.Client).get_case_info(...).thenReturn({'id': 1})
        when(cli.Client).upload_file(...).thenReturn('ok')
        upload_ = cli.Upload({}, ['upload', '1234', 'file1.vcf.gz', 'file2.vcf.gz', 'file3.cnv'])
        verify(cli.Client, times=3).upload_file(...)
        self.assertIsNotNone(upload_)

    def test_create(self):
        when(cli.os.path).exists(...).thenReturn(True)
        when(cli.Client).upload_file(...).thenReturn('ok')
        when(cli.Client).create_case(...).thenReturn(1)
        create_ = cli.Create({}, ['create', 'mock_case.json', 'f1.vcf.gz', 'f2.vcf.gz', 'f3.cnv'])
        verify(cli.Client, times=1).create_case(...)
        self.assertEqual(1, create_.case_id)

    def test_run(self):
        mock_case = {
            'id': 789,
            'specimens': [
                {
                    'accessionNumber': 'SBJ00789',
                }
            ],
        }
        when(cli.Client).get_case_info(...).thenReturn(mock_case)
        when(cli.Client).create_sequencer_run(...).thenReturn(1)
        run_ = cli.Run({}, ['run', '789'])
        verify(cli.Client, times=1).create_sequencer_run(...)
        self.assertEqual(1, run_.run_id)

    def test_job(self):
        mock_case = {
            'id': 69695,
            'specimens': [
                {
                    'accessionNumber': 'SBJ00789',
                },
            ],
            'caseFiles': [
                {
                    'name': 'f1.vcf.gz',
                    'type': 'other',
                    'size': 10000,
                },
            ],
            'sequencerRuns': [
                {
                    'runId': '1'
                },
            ]
        }
        when(cli.Client).get_case_info(...).thenReturn(mock_case)
        when(cli.Client).create_job(...).thenReturn(19635)
        job_ = cli.Job({}, ['job', '69695', '1'])
        verify(cli.Client, times=1).create_job(...)
        self.assertEqual(19635, job_.job_id)

    def test_poll(self):
        mock_case = {
            'id': 69695,
            'specimens': [
                {
                    'accessionNumber': 'SBJ00789',
                },
            ],
        }
        when(cli.Client).get_case_info(...).thenReturn(mock_case)
        when(cli.Client).get_job_status(...).thenReturn("complete")
        poll_ = cli.Poll({}, ['poll', '69695', '19635'])
        verify(cli.Client, times=1).get_job_status(...)
        self.assertTrue(poll_.complete)

    def test_report(self):
        when(cli.Client).get_case_info(...).thenReturn({'id': 123, 'reports': []})
        when(cli.Client).get_report(...).thenReturn("mock_report.pdf.gz")
        report_ = cli.Report({}, ['report', '123'])
        verify(cli.Client, times=1).get_report(...)
        self.assertIsNotNone(report_)
