%Module(name=QCefView, language="C++")

%Import QtCore/QtCoremod.sip
%Import QtWidgets/QtWidgetsmod.sip

%Include QCefConfig.sip
%Include QCefContext.sip
%Include QCefSetting.sip

class QCefView : public QWidget {

%TypeHeaderCode
#include "QCefView.h"
%End

};
