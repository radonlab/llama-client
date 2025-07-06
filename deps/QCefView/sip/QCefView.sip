%Module(name=QCefView, language="C++")

%Import QtCore/QtCoremod.sip
%Import QtWidgets/QtWidgetsmod.sip

class QCefView : public QWidget {

%TypeHeaderCode
#include "QCefView.h"
%End

};
