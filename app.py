import os

import sys

import webbrowser



from PySide6.QtCore import Slot, QUrl, QTimer



from PySide6.QtGui import QIcon, QGuiApplication

from PySide6.QtWebEngineCore import QWebEnginePage, QWebEngineDownloadRequest, QWebEngineProfile

from PySide6.QtWebEngineWidgets import QWebEngineView


from PySide6.QtWidgets import (
    QApplication, QFileDialog, QHBoxLayout, QMainWindow,
    QSystemTrayIcon, QWidget
)


def asset_path(asset_name):

    """Return absolute path to an asset in the assets folder.



    Parameters

    ----------

    asset_name: str

        Name of the file inside the ``assets`` directory.



    Returns

    -------

    str | None

        Full path if the file exists, otherwise ``None``.

    """

    path = os.path.join(os.path.dirname(__file__), "assets", asset_name)

    return path if os.path.isfile(path) else None





def get_qss_path(qss_name):

    """Return absolute path to a qss file next to this module.



    Parameters

    ----------

    qss_name: str

        File name of the qss file (e.g. ``'about_dialog.qss'``).



    Returns

    -------

    str

        Full path.

    """

    return os.path.join(os.path.dirname(__file__), qss_name)





def show_notification(title, msg, app=None):

    """

    Show custom notification in the system tray

    """

    if app is None:

        app = QApplication.instance()

    icon_path = asset_path('logo.png')

    tray_icon = QSystemTrayIcon(QIcon(icon_path) if icon_path else QIcon(), parent=app)

    tray_icon.show()

    tray_icon.showMessage(

        title, msg, QSystemTrayIcon.Information, 5000)





class TempPage(QWebEnginePage):

    """

    Temporary page to facilitate capturing the URLs of any clicked links

    """

    def __init__(self, webview, profile, parent=None):

        super().__init__(profile, parent)

        self.web = webview

        self.urlChanged.connect(self.handle_url_changed)

        self.allowlist = [

            'mail.proton.me', 'calendar.proton.me', 'drive.proton.me', 'account.proton.me']



    @Slot(QUrl)

    def handle_url_changed(self, url: QUrl):

        if url.host() not in self.allowlist:

            webbrowser.open(url.toString())

        else:

            self.web.load(url)

        self.deleteLater()





class ProtonWebPage(QWebEnginePage):

    """

    Custom web page for loading Proton services

    """

    def __init__(self, profile, parent=None):

        super().__init__(profile, parent)



    def createWindow(self, _):

        return TempPage(self.parent(), self.profile(), self)





class ProtonWebView(QWebEngineView):

    """

    Custom QWebEngineView for Protodesk

    """

    def __init__(self, profile, parent=None):

        super().__init__(profile, parent)

        self.setPage(ProtonWebPage(profile, self))

        profile = self.page().profile()

        profile.downloadRequested.connect(self.handle_download)



        # load initial page: Proton Mail

        self.page().setUrl(QUrl('https://mail.proton.me'))

        # Theme toggle will be handled by the main app



    def handle_download(self, download: QWebEngineDownloadRequest):

        """

        Handle a file download request

        """

        suggested_filename = download.downloadFileName()

        save_path, _ = QFileDialog.getSaveFileName(self, 'Save File', suggested_filename)

        if save_path:

            download.setDownloadDirectory(os.path.dirname(save_path))

            download.accept()

            self.check_download_status(download)

        else:

            download.cancel()



    def check_download_status(self, download: QWebEngineDownloadRequest):

        """

        Periodically check if a download is finished and show a notification if it is.

        """

        if download.isFinished():

            if download.state() == QWebEngineDownloadRequest.DownloadState.DownloadCompleted:

                show_notification('Download Complete', 'File has been downloaded successfully')

            else:

                show_notification('Download Failed', download.errorString())

        else:

            QTimer.singleShot(500, lambda: self.check_download_status(download))







class ProtonDesktopApp(QMainWindow):

    """

    Main application window for ProtonDeskX

    """

    def __init__(self):

        super().__init__()







        self.setWindowTitle('ProtonDeskX')



        # window size and position

        screen_geometry = QGuiApplication.primaryScreen().availableGeometry()

        screen_width, screen_height = screen_geometry.width(), screen_geometry.height()

        self.setGeometry(0, 0, screen_width, screen_height)



        self.central_widget = QWidget(self)

        self.main_layout = QHBoxLayout(self.central_widget)

        self.main_layout.setContentsMargins(0, 0, 0, 0)

        self.main_layout.setSpacing(0)

        self.setCentralWidget(self.central_widget)



        # styles for tooltips

        self.setStyleSheet('''

            QToolTip {

                background-color: #333333;

                color: #ffffff;

                font: 14px;

                border: 1px solid #888888;

                padding: 5px;

                opacity: 200;

            }

        ''')





        # enable on-disk persistence for session data

        profile = QWebEngineProfile('protodesk')



        # webview

        self.web = ProtonWebView(profile, self)

        self.main_layout.addWidget(self.web)



        self.main_layout.setStretchFactor(self.web, 1)





if __name__ == "__main__":

    app = QApplication(sys.argv)

    app.setWindowIcon(QIcon(asset_path('logo.png')))

    if '--headless' in sys.argv:

        print("Running in headless mode")

        sys.exit(0)

    window = ProtonDesktopApp()

    window.show()

    sys.exit(app.exec())

