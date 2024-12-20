from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QMainWindow

# Импортируем страницу главного окна
from ui.windows.main_window.pages.partners_page import PartnerPageWidget

class MainWindow(QMainWindow):
    """
    Класс основного окна приложения
    """
    def __init__(self):
        super().__init__()
        # Устанавливаем заголовок окна
        self.setWindowTitle("Master_pol")

        # Создаём виджет для страницы партнёров
        self.partner_page_widget = PartnerPageWidget()
        # Устанавливаем его как центральный виджет окна
        self.setCentralWidget(self.partner_page_widget)

# Основная точка входа в приложение
if __name__ == "__main__":
    # Создаём приложение
    app = QApplication([])
    # Создаём главное окно приложения
    window = MainWindow()
    # Устанавливаем иконку приложения
    window.setWindowIcon(QIcon("ui/icons/Master_pol.ico"))
    # Отображаем главное окно
    window.showMaximized()
    # Запускаем цикл обработки событий приложения
    app.exec()
