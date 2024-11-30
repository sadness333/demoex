from PySide6.QtWidgets import QLabel, QMessageBox

from ui.widgets.CreateUpdatePage import Ui_CreateUpdatePage

from database.CRUDs.PartnerCRUDs import PartnerCRUD


class CreateUpdatePage(QLabel, Ui_CreateUpdatePage):
    def __init__(self, parent, main_window, create_or_update, partner_model):
        super().__init__(parent)
        self.setupUi(self)

        self.parent = parent
        self.main_window = main_window
        self.partner_model = partner_model

        self.CreateUpdateButton.setText("Добавить партнёра" if create_or_update == "create" else "Обновить партнёра")

        if create_or_update == "update":
            self.TypeInput.setText(str(partner_model.type))
            self.NameInput.setText(str(partner_model.company_name))
            self.AddressInput.setText(str(partner_model.address))
            self.INNInput.setText(str(partner_model.inn))
            self.BossNameInput.setText(str(partner_model.boss_name))
            self.PhoneNumberInput.setText(str(partner_model.phone_number))
            self.MailInput.setText(str(partner_model.mail))
            self.RankInput.setText(str(partner_model.rank))

            self.CreateUpdateButton.clicked.connect(self.update_partner)
        else:
            self.CreateUpdateButton.clicked.connect(self.create_partner)


    def create_partner(self):

        company_type=self.TypeInput.text()
        company_name=self.NameInput.text()
        address=self.AddressInput.text()
        inn=self.INNInput.text()
        boss_name=self.BossNameInput.text()
        phone_number=self.PhoneNumberInput.text()
        mail=self.MailInput.text()
        rank=self.RankInput.text()

        if (not company_type or not company_name or not address or not inn or not boss_name or not phone_number or
            not mail or not rank):
            QMessageBox.critical(self, "Ошибка", "Все поля должны быть заполнены")
            return

        try:
            rank = int(rank)
        except ValueError:
            QMessageBox.critical(self, "Ошибка", "В поле 'Рейтинг' должны быть введены цифры")
            return


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

        self.parent.close_modal_window()

        self.main_window.update_scroll_area()

    def update_partner(self):

        company_type=self.TypeInput.text()
        company_name=self.NameInput.text()
        address=self.AddressInput.text()
        inn=self.INNInput.text()
        boss_name=self.BossNameInput.text()
        phone_number=self.PhoneNumberInput.text()
        mail=self.MailInput.text()
        rank=self.RankInput.text()

        if (not company_type or not company_name or not address or not inn or not boss_name or not phone_number or
                not mail or not rank):
            QMessageBox.critical(self, "Ошибка", "Все поля должны быть заполнены")
            return

        try:
            rank = int(rank)
        except ValueError:
            QMessageBox.critical(self, "Ошибка", "В поле 'Рейтинг' должны быть введены цифры")
            return

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

        self.parent.close_modal_window()

        self.main_window.update_scroll_area()