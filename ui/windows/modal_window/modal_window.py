from PySide6.QtWidgets import QDialog, QVBoxLayout

from ui.windows.modal_window.pages.create_and_update_page import CreateUpdatePage

class ModalWindow(QDialog):
    def __init__(self, parent, page_choose, create_or_update=None, partner_model=None):
        super().__init__(parent)

        self.setModal(True)
        self.setGeometry(450, 450, 640, 360)
        self.setFixedSize(900, 360)

        if page_choose == "create/update_partner":
            self.setWindowTitle("Окно добавления/обновления партнёра")

            page1 = CreateUpdatePage(self, parent, create_or_update, partner_model)

            self.layout = QVBoxLayout()
            self.layout.addWidget(page1)
            self.setLayout(self.layout)
        else:
            self.setWindowTitle("Окно просмотра заказов партнёра")

            self.layout = QVBoxLayout()
            self.layout.addWidget()
            self.setLayout(self.layout)

    def close_modal_window(self):
        self.accept()
