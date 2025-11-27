"""Auto-generated menu for categorizer_bot_cli"""

from typing import Optional
from categorizer_bot_cli.utilities.display import GREEN, print_error, color_text

class CategorizerBotCliMenu:

    BACK_LABEL = "← Back"

    def __init__(self, ui):
        self.ui = ui

    # Build (key, label, kind) option list
    def _build_options(self):
        options = []

        options.append(("testing_suite", "Testing Suite", "submenu"))
        options.append(("debug_methods", "Debug Methods", "submenu"))

        options.append(("cmd_run_bot", "Run Bot", "command"))

        return options

    # Display
    def display(self):
        self.ui.clear()

        options = self._build_options()

        labels = [label for (_, label, kind) in options]

        if self.ui.navigation_mode == "arrows":
            labels.append(self.BACK_LABEL)

        selected = self.ui.choose(labels, title="Categorizer Bot CLI")

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

        if choice == "testing_suite": return "testing_suite"
        if choice == "debug_methods": return "debug_methods"

        if choice == "cmd_run_bot": self.cmd_run_bot(); return None

        print_error("Invalid choice.")
        input()
        return None

    def cmd_run_bot(self):
        """TODO: Implement command 'Run Bot'"""
        self.ui.clear()
        print("TODO: Command: Run Bot")
        self.ui.pause("Press Enter to return...")
        return None


