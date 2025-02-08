from address import Address
from mailing import Mailing

to_add = Address("123456", "Moscow", "Red Square", "18", "4")
from_add = Address("136548", "Moscow", "Lesnaya", "10", "65")

mailing = Mailing(to_add, from_add, "999", "777-777")

print(mailing)
