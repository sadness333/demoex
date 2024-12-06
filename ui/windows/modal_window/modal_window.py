from PySide6.QtWidgets import QDialog, QVBoxLayout

# Импорт страницы для добавления и обновления партнёра
from ui.windows.modal_window.pages.create_and_update_page import CreateUpdatePage
# Импорт страницы для просмотра заказов
from ui.windows.modal_window.pages.orders_page import OrderPageWidget


class ModalWindow(QDialog):
    """
    Класс модального окна
    """
    def __init__(self, parent, page_choose, create_or_update=None, partner_model=None):
        super().__init__(parent)

        # Устанавливаем модальность окна
        self.setModal(True)
        # Задаём размеры и фиксированную ширину/высоту окна
        self.setGeometry(450, 450, 640, 360)
        self.setFixedSize(900, 360)

        if page_choose == "create/update_partner":
            # Настраиваем окно для добавления/обновления партнёра
            self.setWindowTitle("Окно добавления/обновления партнёра")

            # Создаём и добавляем страницу добавления/обновления партнёра
            page1 = CreateUpdatePage(self, parent, create_or_update, partner_model)
            self.layout = QVBoxLayout()
            self.layout.addWidget(page1)
            self.setLayout(self.layout)
        else:
            # Настраиваем окно для просмотра заказов
            self.setWindowTitle("Окно просмотра заказов партнёра")

            # Создаём и добавляем страницу просмотра заказов
            page2 = OrderPageWidget(partner_model.id)
            self.layout = QVBoxLayout()
            self.layout.addWidget(page2)
            self.setLayout(self.layout)

    def close_modal_window(self):
        """
        Закрытие модального окна с принятием текущего состояния.
        """
        self.accept()
