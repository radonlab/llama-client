class QCefContext : public QObject {

%TypeHeaderCode
#include "QCefContext.h"
%End

public:
    QCefContext(QCoreApplication* app, int argc, char** argv, const QCefConfig* config);
    static QCefContext* instance();
    ~QCefContext();
    void addLocalFolderResource(const QString& path, const QString& url, int priority = 0);
    void addArchiveResource(const QString& path, const QString& url, const QString& password = "", int priority = 0);
    bool addCookie(const QString& name, const QString& value, const QString& domain, const QString& url);
    bool deleteAllCookies();
    bool addCrossOriginWhitelistEntry(const QString& sourceOrigin,
                                      const QString& targetSchema,
                                      const QString& targetDomain,
                                      bool allowTargetSubdomains);
    bool removeCrossOriginWhitelistEntry(const QString& sourceOrigin,
                                         const QString& targetSchema,
                                         const QString& targetDomain,
                                         bool allowTargetSubdomains);
    bool clearCrossOriginWhitelistEntry();
    const QCefConfig* cefConfig() const;

protected:
    bool init(const QCefConfig* config);
    void uninit();
};
