from pyqtbuild import PyQtBindings, PyQtProject, QmakeBuilder
from sipbuild import Option


class QCefViewBindings(PyQtBindings):
    def __init__(self, project):
        super().__init__(project, "QCefView")

    def get_options(self):
        options = super().get_options()
        options += [
            Option("cef_incdir", help="the CEF include dir", metavar="DIR"),
            Option("cef_libdir", help="the CEF library dir", metavar="DIR"),
            Option("cef_lib", help="the CEF library", metavar="LIB"),
        ]
        return options

    def apply_user_defaults(self, tool):
        return super().apply_user_defaults(tool)


class QCefViewProject(PyQtProject):
    def __init__(self):
        super().__init__()
        self.builder_factory = QmakeBuilder
        self.bindings_factories = [QCefViewBindings]

    def apply_user_defaults(self, tool):
        return super().apply_user_defaults(tool)
