import sys
from unittest import TestCase

from pyriandx import cli


class HelpUnitTests(TestCase):

    def test_main_no_args(self):
        """Test calling main without arguments print help and exit with code 0"""
        with self.assertRaises(SystemExit) as x:
            sys.argv = ['pyriandx']
            cli.main()
        self.assertEqual(x.exception.code, 0)

    def test_case_no_args(self):
        with self.assertRaises(SystemExit) as x:
            cli.Case(None, None)
        print(x.exception)
        assert "Usage" in x.exception.code, self.fail()

    def test_case_help(self):
        with self.assertRaises(SystemExit) as x:
            cli.Case({}, ['case', 'help'])
        self.assertEqual(x.exception.code, 0)

    def test_list_help(self):
        with self.assertRaises(SystemExit) as x:
            cli.List({}, ['list', 'help'])
        self.assertEqual(x.exception.code, 0)

    def test_upload_help(self):
        with self.assertRaises(SystemExit) as x:
            cli.Upload({}, ['upload', 'help'])
        self.assertEqual(x.exception.code, 0)

    def test_create_help(self):
        with self.assertRaises(SystemExit) as x:
            cli.Create({}, ['create', 'help'])
        self.assertEqual(x.exception.code, 0)

    def test_run_help(self):
        with self.assertRaises(SystemExit) as x:
            cli.Run({}, ['run', 'help'])
        self.assertEqual(x.exception.code, 0)

    def test_job_help(self):
        with self.assertRaises(SystemExit) as x:
            cli.Job({}, ['job', 'help'])
        self.assertEqual(x.exception.code, 0)

    def test_poll_help(self):
        with self.assertRaises(SystemExit) as x:
            cli.Poll({}, ['poll', 'help'])
        self.assertEqual(x.exception.code, 0)

    def test_report_help(self):
        with self.assertRaises(SystemExit) as x:
            cli.Report({}, ['report', 'help'])
        self.assertEqual(x.exception.code, 0)
