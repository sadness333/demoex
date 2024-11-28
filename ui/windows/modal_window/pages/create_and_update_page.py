from PySide6.QtWidgets import QLabel, QMessageBox

from ui.widgets.CreateUpdatePage import Ui_CreateUpdatePage

from database.CRUDs.PartnerCRUDs import PartnerCRUD

class CreateUpdatePage(QLabel, Ui_CreateUpdatePage):
    def __init__(self, create_or_update, partner_model):
        super().__init__()
        self.setupUi(self)

        self.partner_model = partner_model

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
        PartnerCRUD.create_partner(
            type=self.TypeInput.text(),
            company_name=self.NameInput.text(),
            address=self.AddressInput.text(),
            inn=self.INNInput.text(),
            boss_name=self.BossNameInput.text(),
            phone_number=self.PhoneNumberInput.text(),
            mail=self.MailInput.text(),
            rank=int(self.RankInput.text())
        )

    def update_partner(self):

        if  (self.TypeInput.text() == "" or self.NameInput.text() == "" or self.AddressInput.text() == "" or
            self.INNInput.text() == "" or self.BossNameInput.text() == "" or self.PhoneNumberInput.text() == "" or
            self.MailInput.text() == "" or self.RankInput.text() == "" ):
            
            msg_box = QMessageBox(self)
            msg_box.setWindowTitle("Ошибка")
            msg_box.setText("При выполении операции произошла ошибка")
            msg_box.setInformativeText("Для выполнения операции требуется, чтобы все поля были заполенны")
            msg_box.show()

            return

        PartnerCRUD.update_partner(
            partner_id=self.partner_model.id,
            type=self.TypeInput.text(),
            company_name=self.NameInput.text(),
            address=self.AddressInput.text(),
            inn=self.INNInput.text(),
            boss_name=self.BossNameInput.text(),
            phone_number=self.PhoneNumberInput.text(),
            mail=self.MailInput.text(),
            rank=self.RankInput.text()
        )