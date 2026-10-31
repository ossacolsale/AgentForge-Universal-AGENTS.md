"""Unit tests for non-blocking documentation-size advisories."""

from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from scripts.validate_repo import documentation_warnings


class DocumentationWarningTests(unittest.TestCase):
    def test_current_template_has_no_warnings(self):
        root = Path(__file__).resolve().parents[1]
        self.assertEqual(documentation_warnings(root), [])

    def test_oversized_agent_and_index_are_advisories(self):
        with TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / "AGENTS.md").write_text("a" * 8001, encoding="utf-8")
            (root / "docs/ai").mkdir(parents=True)
            (root / "docs/ai/INDEX.md").write_text("a" * 3001, encoding="utf-8")
            warnings = documentation_warnings(root)
            self.assertEqual(len(warnings), 2)
            self.assertTrue(any("AGENTS.md" in warning for warning in warnings))
            self.assertTrue(any("INDEX.md" in warning for warning in warnings))

    def test_active_handoff_over_limit_warns(self):
        with TemporaryDirectory() as temporary:
            root = Path(temporary)
            state = root / "docs/ai/SESSION-STATE.md"
            state.parent.mkdir(parents=True)
            state.write_text("Status: Active\n" + "word " * 151, encoding="utf-8")
            self.assertEqual(len(documentation_warnings(root)), 1)

    def test_inactive_handoff_with_stale_history_warns(self):
        with TemporaryDirectory() as temporary:
            root = Path(temporary)
            state = root / "docs/ai/SESSION-STATE.md"
            state.parent.mkdir(parents=True)
            state.write_text("Status: Inactive\n" + "word " * 151, encoding="utf-8")
            self.assertEqual(len(documentation_warnings(root)), 1)


if __name__ == "__main__":
    unittest.main()
