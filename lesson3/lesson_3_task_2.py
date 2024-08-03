from smartphone import Smartphone

catalog = []

phone1 = Smartphone("Samsung", "Galaxy S8", "+79107350066" )
phone2 = Smartphone("Samsung", "Galaxy S20FE", "+79107560066" )
phone3 = Smartphone("Xiaomi", "Redmi not 7", "+79101140066" )
phone4 = Smartphone("Apple", "Iphone 8 SE", "+79057620066" )
phone5 = Smartphone("HTC", "One", "+79043110066" )

catalog.append(phone1)
catalog.append(phone2)
catalog.append(phone3)
catalog.append(phone4)
catalog.append(phone5)

for phone in catalog:
    print(f"{phone.brand} {phone.model}, {phone.number}")