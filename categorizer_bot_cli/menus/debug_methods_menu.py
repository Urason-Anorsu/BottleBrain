"""Auto-generated menu for Debug Methods"""

from typing import Optional
from categorizer_bot_cli.utilities.display import print_error
from data_formatting.tokenizer import basic_tokenize
from helpers.conversion import parse_size_token


class DebugMethodsMenu:

    BACK_LABEL = "← Back"

    def __init__(self, ui):
        self.ui = ui

    def _build_options(self):
        options = []
        options.append(("cmd_debug_tokenizer", "Debug Tokenizer", "command"))
        options.append(("cmd_debug_normalizer", "Debug Normalizer", "command"))
        options.append(("cmd_debug_size_detector", "Debug Size Detector", "command"))
        options.append(("cmd_debug_pack_parser", "Debug Pack Parser", "command"))
        options.append(("cmd_debug_full_pipeline", "Debug Full Pipeline", "command"))
        return options

    def display(self):
        self.ui.clear()

        options = self._build_options()
        labels = [label for (_, label, kind) in options]

        if self.ui.navigation_mode == "arrows":
            labels.append(self.BACK_LABEL)

        selected = self.ui.choose(labels, title="Debug Methods")

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

        if choice == "cmd_debug_tokenizer":
            self.cmd_debug_tokenizer()
            return None

        if choice == "cmd_debug_normalizer":
            self.cmd_debug_normalizer()
            return None

        if choice == "cmd_debug_size_detector":
            self.cmd_debug_size_detector()
            return None

        if choice == "cmd_debug_pack_parser":
            self.cmd_debug_pack_parser()
            return None

        if choice == "cmd_debug_full_pipeline":
            self.cmd_debug_full_pipeline()
            return None

        print_error("Invalid choice.")
        input()
        return None

    def cmd_debug_tokenizer(self):
        self.ui.clear()
        raw = input("Enter a product string:\n> ").strip()
        tokens = basic_tokenize(raw)

        self.ui.clear()
        print("Raw Input:")
        print("   ", raw)

        print("\nBasic Tokens:")
        print("   ", tokens)

        self.ui.pause("\nPress Enter to return...")
        return None

    def cmd_debug_size_detector(self):
        self.ui.clear()
        raw = input("Enter a size token (e.g., 750ml, 1.75L, 50 floz):\n> ").strip()
        result = parse_size_token(raw)

        self.ui.clear()
        print("Raw Input:")
        print("   ", raw)

        print("\nDetected Size (ml):")
        print("   ", result)

        self.ui.pause("\nPress Enter to return...")
        return None

    def cmd_debug_normalizer(self):
        self.ui.clear()
        print("Normalizer debugging not implemented yet.")
        self.ui.pause("Press Enter to return...")
        return None

    def cmd_debug_pack_parser(self):
        self.ui.clear()
        print("Pack parser debugging not implemented yet.")
        self.ui.pause("Press Enter to return...")
        return None

    def cmd_debug_full_pipeline(self):
        self.ui.clear()
        print("Full pipeline debugging not implemented yet.")
        self.ui.pause("Press Enter to return...")
        return None
