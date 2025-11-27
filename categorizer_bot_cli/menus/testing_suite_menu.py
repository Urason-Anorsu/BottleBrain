"""Auto-generated menu for Testing Suite"""

from typing import Optional
from categorizer_bot_cli.utilities.display import print_error
from tests import test_registry


class TestingSuiteMenu:

    BACK_LABEL = "← Back"

    def __init__(self, ui):
        self.ui = ui

    def _build_options(self):
        options = []
        options.append(("cmd_view_available_tests", "View Available Tests", "command"))
        options.append(("cmd_multi_run_tests", "Run Tests", "multi"))
        return options

    def display(self):
        self.ui.clear()

        options = self._build_options()
        labels = [label for (_, label, kind) in options]

        if self.ui.navigation_mode == "arrows":
            labels.append(self.BACK_LABEL)

        selected = self.ui.choose(labels, title="Testing Suite")

        if selected in ("__back__", self.BACK_LABEL):
            return "__back__", "back"

        if selected == "-1":
            return "-1", "debug"

        for (key, label, kind) in options:
            if label == selected:
                if kind == "multi":
                    return key, "multi"
                return key, kind

        return None, None

    def handle(self) -> Optional[str]:
        choice, kind = self.display()

        if choice == "__back__":
            return "__back__"

        if choice == "-1":
            return "-1"

        if choice == "cmd_view_available_tests":
            self.cmd_view_available_tests()
            return None

        if choice == "cmd_multi_run_tests":
            return self.cmd_multi_run_tests()

        print_error("Invalid choice.")
        input()
        return None

    def cmd_view_available_tests(self):
        self.ui.clear()

        names = test_registry.list_all_tests()

        print("Available Tests:\n")
        for n in names:
            print("  •", n)

        self.ui.pause("\nPress Enter to return...")
        return None

    def cmd_multi_run_tests(self):
        self.ui.clear()

        names = test_registry.list_all_tests()

        choices = self.ui.choose_multi(names, title="Select tests to run")

        if not choices:
            return None

        self.ui.clear()
        print("Running selected tests:\n")

        passed = 0
        failed = 0

        for name in choices:
            try:
                test_registry.run_single(name)
                print(f"  ✓ {name}")
                passed += 1
            except Exception as e:
                print(f"  ✗ {name}")
                print("    Error:", e)
                failed += 1

        print("\nSummary:")
        print(f"  Passed: {passed}")
        print(f"  Failed: {failed}")

        self.ui.pause("\nPress Enter to return...")
        return None
