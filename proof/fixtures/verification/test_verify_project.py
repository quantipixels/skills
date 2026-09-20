import unittest

from verify_project import build_parser


class VerifyProjectTest(unittest.TestCase):
    def test_workdir_is_required(self):
        with self.assertRaises(SystemExit):
            build_parser().parse_args([])
        parsed = build_parser().parse_args([
            "--workdir", "owned", "--url", "http://127.0.0.1:1234", "get"
        ])
        self.assertEqual("owned", str(parsed.workdir))
        self.assertEqual("get", parsed.operation)
