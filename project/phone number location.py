import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier

ch_number=phonenumbers.parse("+918769205415","CH")
print(geocoder.description_for_number(ch_number,"en"))

ro_number=phonenumbers.parse("+918769205415","RO")
print(carrier.name_for_number(ro_number,"en"))
print(carrier.name_for_number(ch_number,"en"))