import getpass
import hashlib
import re
import unittest

# # Izpis števil od 1 do 30 povrsti
# for i in range(1, 31):
#     print(i)
#
# geslo = input("Vnesite geslo: ")
# print("Vneseno geslo je:", geslo)

# # zakrito geslo
# geslo = getpass.getpass("Vnesite geslo: ")
# print("Vneseno geslo je:", geslo)

# Vnesite geslo - Zaženi z debugerjem
# Vnesite geslo
# geslo = getpass.getpass("Vnesite geslo: ")
#
# # Zakriptirajte geslo
# hashed_geslo = hashlib.sha256(geslo.encode()).hexdigest()
#
# # Izpišite zakriptirano geslo
# print("Zakriptirano geslo:", hashed_geslo)

# seznam_sadja = ['jabolko', 'banana', 'cesnja', 'figa', 'ananas']
#
# for index, sadje in enumerate(seznam_sadja, start=0):
#     print(f'Sadje {index}: {sadje}')


email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

def preveri_email(email):
    status = re.match(email_regex, email)
    print(f'Status: {status} Email: {email}')
    if status:
        return True
    else:
        return False

# # Uporaba funkcije za preverjanje e-poštnega naslova
# email = "primer@email.com"
# if preveri_email(email):
#     print("E-poštni naslov je veljaven.")
# else:
#     print("E-poštni naslov ni veljaven.")


class TestPreveriEmail(unittest.TestCase):

    def test_veljaven_email(self):
        self.assertTrue(preveri_email("primer@email.com"))
        self.assertTrue(preveri_email("uporabnik123@example.com"))
        self.assertTrue(preveri_email("ime.priimek@poddomena.example.org"))

    def test_neveljaven_email(self):
        self.assertFalse(preveri_email("neveljaven_email"))
        self.assertFalse(preveri_email("email@.com"))
        self.assertFalse(preveri_email("email@example"))
        self.assertFalse(preveri_email("email@.org"))
        self.assertFalse(preveri_email("email@example."))
        self.assertFalse(preveri_email("email@.example."))
        self.assertFalse(preveri_email("@example.com"))


if __name__ == '__main__':
    unittest.main()

