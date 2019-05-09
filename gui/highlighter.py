import re
from collections import namedtuple

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QSyntaxHighlighter, QTextCharFormat, QFont


class PythonCodeHighlighter(QSyntaxHighlighter):
    Rule = namedtuple("HighlightingRule", "pattern format")

    def __init__(self, *args, **kwargs):
        super(PythonCodeHighlighter, self).__init__(*args, **kwargs)
        self.keyword_format = QTextCharFormat()
        self.keywords = []
        self.quotation_format = QTextCharFormat()
        self.quotation = None
        self.function = None
        self.function_format = QTextCharFormat()
        self.rules = []
        self.setup()

    def setup(self):
        self.keyword_format.setForeground(Qt.darkBlue)
        self.keyword_format.setFontWeight(QFont.Bold)
        self.quotation_format.setForeground(Qt.darkGreen)
        self.function_format.setForeground(Qt.darkMagenta)
        self.function_format.setFontItalic(True)

        self.keywords.extend(
            (r"\b(import)\b", r"^\W*(from)\W", r"^import\W", r"\s+as\s+")
        )
        self.quotation = (r'["\'].*?["\']',)
        self.function = (r"[A-Za-z0-9_]+(?=\()",)

        self.append_rules(self.keywords, self.keyword_format)
        self.append_rules(self.quotation, self.quotation_format)
        self.append_rules(self.function, self.function_format)

    def append_rules(self, patterns, rule):
        self.rules.extend([PythonCodeHighlighter.Rule(p, rule) for p in patterns])

    def highlightBlock(self, text):
        for rule in self.rules:
            for match in re.finditer(rule.pattern, text, re.MULTILINE):
                if match:
                    self.setFormat(match.start(), len(match.group()), rule.format)


class SqlCodeHighlighter(QSyntaxHighlighter):
    Rule = namedtuple("HighlightingRule", "pattern format")

    def __init__(self, *args, **kwargs):
        super(SqlCodeHighlighter, self).__init__(*args, **kwargs)
        self.keyword_format = QTextCharFormat()
        self.keywords = []
        self.quotation_format = QTextCharFormat()
        self.quotation = None
        self.function = None
        self.function_format = QTextCharFormat()
        self.rules = []
        self.setup()

    def setup(self):
        self.keyword_format.setForeground(Qt.darkRed)
        self.keyword_format.setFontWeight(QFont.Bold)
        self.quotation_format.setForeground(Qt.darkYellow)
        self.function_format.setForeground(Qt.darkMagenta)
        self.function_format.setFontItalic(True)

        self.keywords.extend(
            (
                r"\bselect\b",
                r"^\W*from\W",
                r"\s+as\s+",
                r"\s+in\s+",
                r"\s+join\s+",
                r"^join\s+",
                r"\s+on\s+",
                r"\s+where\s+",
                r"^where\s+",
                r"\s+order by\s+",
                r"^order by\s+",
                r"\s+using\s+",
                r"^using\s+",
            )
        )
        self.quotation = (r'["\'].*?["\']',)
        self.function = (r"[A-Za-z0-9_]+(?=\()",)

        self.append_rules(self.keywords, self.keyword_format)
        self.append_rules(self.quotation, self.quotation_format)
        self.append_rules(self.function, self.function_format)

    def append_rules(self, patterns, rule):
        self.rules.extend([PythonCodeHighlighter.Rule(p, rule) for p in patterns])

    def highlightBlock(self, text):
        for rule in self.rules:
            for match in re.finditer(rule.pattern, text, re.MULTILINE | re.IGNORECASE):
                if match:
                    self.setFormat(match.start(), len(match.group()), rule.format)
