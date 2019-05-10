"""
    Project main file, from which the application loop can be started e que main window can show up.
"""

from os import path

import sys
from query_code_compiler import default_compiler


def _recompile_ui_if_changed():
    """
    This function verifies if the py2sql_base.ui file was modified
    since its last compilation and recompile it has happened

    """

    ui_file = path.join("gui", "py2sql_base.ui")
    ui_compiled_file = path.join("gui", "py2sql_base_ui.py")

    if path.getmtime(ui_file) > path.getmtime(ui_compiled_file):
        from PyQt5.uic import compileUi  # Just import if it is necessary

        with open(ui_compiled_file, "w") as f:
            compileUi(ui_file, f, import_from="gui/img")


def main():
    _recompile_ui_if_changed()
    from gui import py2sql_main_window

    sys.exit(
        py2sql_main_window.run(
            predefined_query_content=default_compiler.DEFAULT_CONTENT
        )
    )


if __name__ == "__main__":
    main()
