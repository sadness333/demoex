from PySide6.QtWidgets import QDialog, QVBoxLayout

from ui.windows.modal_window.pages.create_and_update_page import CreateUpdatePage

class ModalWindow(QDialog):
    def __init__(self, page_choose, partner_model, create_or_update=None):
        super().__init__()

        self.setModal(True)
        self.setGeometry(450, 450, 640, 360)
        self.setFixedSize(900, 360)

        if page_choose == "create/update_partner":
            self.setWindowTitle("Окно добавления/обновления партнёра")

            page1 = CreateUpdatePage(create_or_update, partner_model)

            page1.CreateUpdateButton.setText("Добавить партнёра" if create_or_update == "create" else "Обновить партнёра")
            page1.CreateUpdateButton.clicked.connect(lambda: self.accept())

            self.layout = QVBoxLayout()
            self.layout.addWidget(page1)
            self.setLayout(self.layout)
        else:
            self.setWindowTitle("Окно просмотра заказов партнёра")

            self.layout = QVBoxLayout()
            self.layout.addWidget()
            self.setLayout(self.layout)
