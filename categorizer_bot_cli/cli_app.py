from categorizer_bot_cli.ui.ui_manager import UIManager
from categorizer_bot_cli.menus.categorizer_bot_cli_menu import CategorizerBotCliMenu
from categorizer_bot_cli.menus.testing_suite_menu import TestingSuiteMenu
from categorizer_bot_cli.menus.debug_methods_menu import DebugMethodsMenu
from categorizer_bot_cli.debug.debug_menu import run_debug_menu

PARENTS = {
    'categorizer_bot_cli': None,
    'testing_suite': 'categorizer_bot_cli',
    'debug_methods': 'categorizer_bot_cli',
}

def build_menus(ui):
    menus = {}
    menus['categorizer_bot_cli'] = CategorizerBotCliMenu(ui)
    menus['testing_suite'] = TestingSuiteMenu(ui)
    menus['debug_methods'] = DebugMethodsMenu(ui)
    return menus

def main():
    ui = UIManager(
        navigation_mode="arrows",
        style="box",
        arrow_style="bracket"
    )

    menus = build_menus(ui)
    current = "categorizer_bot_cli"

    while current is not None:
        menu = menus.get(current)
        if not menu:
            print(f"Invalid menu: {current}")
            break

        result = menu.handle()

        if result == "__back__":
            current = PARENTS.get(current)
            continue

        if isinstance(result, str) and result in menus:
            current = result
            continue

        if result == "-1":
            run_debug_menu(ui, menus, menu)
            continue


if __name__ == "__main__":
    main()
