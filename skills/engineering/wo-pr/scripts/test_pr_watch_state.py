import os
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import pr_watch


class WatchStateTests(unittest.TestCase):
    def test_default_state_directory_uses_os_user_state_only(self):
        with tempfile.TemporaryDirectory() as state_home, patch.dict(
            os.environ, {"XDG_STATE_HOME": state_home}, clear=False
        ):
            result = pr_watch._state_directory(Path("/tmp/example-repository"))

        self.assertEqual(result, Path(state_home) / "qp" / "wo-pr")
        self.assertNotIn(".qp", result.parts)


if __name__ == "__main__":
    unittest.main()
