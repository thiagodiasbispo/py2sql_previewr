from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog
from PyQt5.QtSql import QSqlQueryModel

from gui.py2sql_base_ui import Ui_Py2Sql_base
from util.shortcuts import compile_and_get_formated_sql
from exceptions import QueryObjectNotDefined
from gui.highlighter import PythonCodeHighlighter, SqlCodeHighlighter

from sample.chinook import chinook_db


class SqlPreviewWindow(QWidget):
    def __init__(self, *args, predefined_query_content="", **kwargs):
        super(SqlPreviewWindow, self).__init__(*args, **kwargs)

        self._setup(predefined_query_content)

    def _setup(self, predefined_query_content):
        self.ui = Ui_Py2Sql_base()
        self.ui.setupUi(self)

        self.ui.queryResultTableView

        self.sql_preview = None
        self.table_model = None
        self.query_file = None
        self.query = predefined_query_content

        self.ui.queryEditor.textChanged.connect(self.query_updated)

        self.ui.livePreviewCheckBox.toggled.connect(self.option_live_preview_toggled)

        self.ui.saveQueryButton.clicked.connect(self.save_query_requested)
        self.ui.openQueryButton.clicked.connect(self.open_query_file_requested)

        self.ui.exportSqlPreviewButton.clicked.connect(
            self.export_sql_preview_requested
        )

        self.db_connection = chinook_db.pyqt_connection()

        if self.db_connection:
            self.table_model = QSqlQueryModel(self)
            self.ui.queryResultTableView.setModel(self.table_model)

        self.python_highlighter = PythonCodeHighlighter(self.ui.queryEditor.document())
        self.sql_highlighter = SqlCodeHighlighter(self.ui.sqlPreviewr.document())

    def query_updated(self):
        query = self.query
        if not query:
            self.clear_contents()
            return

        try:
            self.sql_preview = compile_and_get_formated_sql(query)
            self.update_table_query_result()
            # self.query = self.format_query(query)
            self.update_status_bar("It works!")
            self.register_query_change(True)

        except Exception as e:
            self.handle_query_content_error(e)

    def clear_contents(self):
        self.clear_status_bar()
        self.sql_preview = None
        self.table_model.clear()

    def register_query_change(self, changed):
        if changed:
            self.ui.queryEditorGroupBox.setTitle("Query editor *")
        else:
            self.ui.queryEditorGroupBox.setTitle("Query editor")

    def update_table_query_result(self):
        self.table_model.setQuery(self.sql_preview, self.db_connection)
        self.table_model.query().exec_()
        self.ui.queryResultTableView.resizeColumnsToContents()

    def export_sql_preview_requested(self):
        if not self.sql_preview:
            return

        file_name = self.choose_file_to_save_data(
            "Choose file name to save sql", filter_files="SQL files (*.sql)"
        )

        if file_name:
            self._save_data_to_file(file_name, self.sql_preview)
            self.update_status_bar(f"Sql exported to: {file_name}")

    def save_query_requested(self):
        if not self.query_file_exists:
            file_name = self.choose_file_to_save_data(
                "Choose file name to save query", filter_files="Python files (*.py)"
            )
        else:
            file_name = self.query_file

        if file_name:
            self._save_data_to_file(file_name, self.query)
            self.query_file = file_name
            self.register_query_change(False)
            self.update_status_bar(f"File saved as: {file_name}")

    def update_status_bar(self, text):
        self.ui.statuslabel.setText(text)

    def clear_status_bar(self):
        self.ui.statuslabel.clear()

    def handle_query_content_error(self, exception):
        self.ui.sqlPreviewr.clear()

        if isinstance(exception, QueryObjectNotDefined):
            msg = f"Execution error: {exception}"
        elif hasattr(exception, "lineno"):
            msg = f"{ exception.__class__.__name__} on line {exception.lineno}, offset {exception.offset}."
        else:
            msg = f"Compile error: {exception}"

        self.update_status_bar(msg)

    def option_live_preview_toggled(self, toggled):
        if toggled:
            self.ui.queryEditor.textChanged.connect(self.query_updated)
        else:
            self.ui.queryEditor.textChanged.disconnect(self.query_updated)
            self.clear_status_bar()

    def open_query_file_requested(self):
        file_name = self.open_query_file()

        if file_name:
            self.edit_query_from_file(file_name)
            self.query_file = file_name
            self.register_query_change(False)
            self.clear_status_bar()

    def edit_query_from_file(self, file_name):
        with open(file_name) as f:
            file_content = f.read().strip()

        self.query = file_content

    def open_query_file(self, filter_files=None):
        filter_files = filter_files or "Python files (*.py)"
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_name, _ = QFileDialog.getOpenFileName(
            self, "Open query file", "", filter=filter_files, options=options
        )

        return file_name

    def choose_file_to_save_data(self, message, filter_files=None):
        filter_files = filter_files or "All Files (*);;"
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_name, _ = QFileDialog.getSaveFileName(
            self, message, "", filter=filter_files, options=options
        )
        return file_name

    @staticmethod
    def _save_data_to_file(file_name, data):
        with open(file_name, "w") as f:
            f.write(data)

    @property
    def query_file_exists(self):
        return self.query_file is not None

    @property
    def query(self):
        return self.ui.queryEditor.toPlainText()

    @query.setter
    def query(self, text):
        self.ui.queryEditor.setText(text)

    @property
    def sql_preview(self):
        return self.ui.sqlPreviewr.toPlainText()

    @sql_preview.setter
    def sql_preview(self, text):
        self.ui.sqlPreviewr.setText(text)

    @property
    def must_format_code_before_save(self):
        return self.ui.formatCodeBeforeSaveCheckBox.isChecked()

    def format_query(self, query):
        return query
        # cursor = self.ui.queryEditor.textCursor()
        # self.option_submit_on_change_toggled(False)
        # self.query = black.format_str(query, mode=black.FileMode())
        # self.ui.queryEditor.setTextCursor(cursor)
        # self.option_submit_on_change_toggled(True)


def run(*args, predefined_query_content=""):
    args = args or []
    app = QApplication(args)
    window = SqlPreviewWindow(predefined_query_content=predefined_query_content)
    window.show()

    return app.exec()


if __name__ == "__main__":
    import sys

    sys.exit(run())
