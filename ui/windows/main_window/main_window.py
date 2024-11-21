from PySide6.QtWidgets import QApplication, QMainWindow

from ui.windows.main_window.pages.partners_page import PartnerPageWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Master_pol")
        self.setGeometry(400, 400, 960, 540)

        self.partner_page_widget = PartnerPageWidget()
        self.setCentralWidget(self.partner_page_widget)

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()