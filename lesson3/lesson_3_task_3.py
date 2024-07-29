from Address import Address
from Mailing import Mailing

to_adress = Address("426000", "Ижевск", "К. Маркса", "256", "13")
from_adress = Address("624200", "Лесной", "Ленина", "31", "2")
mailing = Mailing(to_adress, from_adress, "500", 255484586650 )

print(f"Отправление {mailing.track} из {mailing.from_adress.index}, {mailing.from_adress.city}, "
      f" {mailing.from_adress.street}, {mailing.from_adress.number_house} - {mailing.from_adress.apartment}, "
      f"в {mailing.to_adress.index}, {mailing.to_adress.city}, {mailing.to_adress.street} "
      f"{mailing.to_adress.number_house} - {mailing.to_adress.apartment}. Стоимость {mailing.cost} рублей." )