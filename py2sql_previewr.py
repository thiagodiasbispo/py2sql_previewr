from os import path

import sys
from query_code_compiler import default_compiler


def recompile_ui_if_changed():
    ui_file = path.join("gui", "py2sql_base.ui")
    ui_compiled_file = path.join("gui", "py2sql_base_ui.py")

    if path.getmtime(ui_file) > path.getmtime(ui_compiled_file):
        from PyQt5.uic import compileUi

        with open(ui_compiled_file, "w") as f:
            compileUi(ui_file, f, import_from="gui/img")


def main():
    recompile_ui_if_changed()
    from gui import py2sql_main_window

    sys.exit(
        py2sql_main_window.run(
            predefined_query_content=default_compiler.DEFAULT_CONTENT
        )
    )


if __name__ == "__main__":
    main()
