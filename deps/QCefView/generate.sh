#!/usr/bin/env bash
sed -e 's/QCefBrowserId/int/g' -e 's/QCefFrameId/QString/g' tpl/QCefView.sip.in
