from pyqtbuild import PyQtBindings, PyQtProject, QmakeBuilder


class QCefViewBindings(PyQtBindings):
    def __init__(self, project):
        super().__init__(project, "QCefView")


class QCefViewProject(PyQtProject):
    def __init__(self):
        super().__init__()
        self.builder_factory = QmakeBuilder
        self.bindings_factories = [QCefViewBindings]

    def apply_user_defaults(self, tool):
        return super().apply_user_defaults(tool)
