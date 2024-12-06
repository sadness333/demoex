from PySide6.QtWidgets import QLabel, QMessageBox

# Импорт пользовательского интерфейса для страницы добавления/обновления партнёра
from ui.widgets.CreateUpdatePage import Ui_CreateUpdatePage

# Импорт CRUD операций для работы с сущностями партнёров
from database.CRUDs.PartnerCRUDs import PartnerCRUD


class CreateUpdatePage(QLabel, Ui_CreateUpdatePage):
    """
    Класс страницы для добавления или обновления данных о партнёре.
    Позволяет заполнять поля для создания нового партнёра или изменять существующего.
    """
    def __init__(self, parent, main_window, create_or_update, partner_model):
        super().__init__(parent)
        self.setupUi(self)  # Инициализация пользовательского интерфейса

        self.parent = parent  # Родительский элемент (например, модальное окно)
        self.main_window = main_window  # Главное окно приложения
        self.partner_model = partner_model  # Модель партнёра для редактирования

        # Устанавливаем текст кнопки в зависимости от режима (создание или обновление)
        self.CreateUpdateButton.setText("Добавить партнёра" if create_or_update == "create" else "Обновить партнёра")

        if create_or_update == "update":
            # Если режим "обновление", заполняем поля значениями из модели партнёра
            self.TypeInput.setText(str(partner_model.type))
            self.NameInput.setText(str(partner_model.company_name))
            self.AddressInput.setText(str(partner_model.address))
            self.INNInput.setText(str(partner_model.inn))
            self.BossNameInput.setText(str(partner_model.boss_name))
            self.PhoneNumberInput.setText(str(partner_model.phone_number))
            self.MailInput.setText(str(partner_model.mail))
            self.RankInput.setText(str(partner_model.rank))

            # Подключаем кнопку к методу обновления
            self.CreateUpdateButton.clicked.connect(self.update_partner)
        else:
            # Подключаем кнопку к методу создания
            self.CreateUpdateButton.clicked.connect(self.create_partner)

    def create_partner(self):
        """
        Метод для создания нового партнёра. Проверяет заполнение полей и их корректность.
        Если всё корректно, вызывает соответствующую CRUD-операцию и обновляет интерфейс.
        """
        # Считываем данные из полей ввода
        company_type = self.TypeInput.text()
        company_name = self.NameInput.text()
        address = self.AddressInput.text()
        inn = self.INNInput.text()
        boss_name = self.BossNameInput.text()
        phone_number = self.PhoneNumberInput.text()
        mail = self.MailInput.text()
        rank = self.RankInput.text()

        # Проверяем, что все поля заполнены
        if (not company_type or not company_name or not address or not inn or not boss_name or not phone_number or
                not mail or not rank):
            QMessageBox.critical(self, "Ошибка", "Все поля должны быть заполнены")
            return

        # Проверяем, что поле "Рейтинг" содержит число
        try:
            rank = int(rank)
        except ValueError:
            QMessageBox.critical(self, "Ошибка", "В поле 'Рейтинг' должны быть введены цифры")
            return

        # Вызываем CRUD-операцию для создания партнёра
        PartnerCRUD.create_partner(
            type=company_type,
            company_name=company_name,
            address=address,
            inn=inn,
            boss_name=boss_name,
            phone_number=phone_number,
            mail=mail,
            rank=rank
        )

        # Закрываем модальное окно
        self.parent.close_modal_window()

        # Обновляем список партнёров в главном окне
        self.main_window.update_scroll_area()

    def update_partner(self):
        """
        Метод для обновления данных существующего партнёра. Проверяет заполнение полей и их корректность.
        Если всё корректно, вызывает соответствующую CRUD-операцию и обновляет интерфейс.
        """
        # Считываем данные из полей ввода
        company_type = self.TypeInput.text()
        company_name = self.NameInput.text()
        address = self.AddressInput.text()
        inn = self.INNInput.text()
        boss_name = self.BossNameInput.text()
        phone_number = self.PhoneNumberInput.text()
        mail = self.MailInput.text()
        rank = self.RankInput.text()

        # Проверяем, что все поля заполнены
        if (not company_type or not company_name or not address or not inn or not boss_name or not phone_number or
                not mail or not rank):
            QMessageBox.critical(self, "Ошибка", "Все поля должны быть заполнены")
            return

        # Проверяем, что поле "Рейтинг" содержит число
        try:
            rank = int(rank)
        except ValueError:
            QMessageBox.critical(self, "Ошибка", "В поле 'Рейтинг' должны быть введены цифры")
            return

        # Вызываем CRUD-операцию для обновления данных партнёра
        PartnerCRUD.update_partner(
            partner_id=self.partner_model.id,
            type=company_type,
            company_name=company_name,
            address=address,
            inn=inn,
            boss_name=boss_name,
            phone_number=phone_number,
            mail=mail,
            rank=rank
        )

        # Закрываем модальное окно
        self.parent.close_modal_window()

        # Обновляем список партнёров в главном окне
        self.main_window.update_scroll_area()
