from app.extensions import db
from app.models.setting import Setting


class SettingService:

    @staticmethod
    def get():

        setting = Setting.query.first()

        if setting is None:

            setting = Setting()

            db.session.add(setting)
            db.session.commit()

        return setting

    @staticmethod
    def update(data):

        setting = SettingService.get()

        setting.hospital_name = data["hospital_name"]
        setting.hospital_address = data["hospital_address"]
        setting.hospital_phone = data["hospital_phone"]
        setting.hospital_email = data["hospital_email"]
        setting.timezone = data["timezone"]

        db.session.commit()

        return setting

