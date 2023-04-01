import re


def validate_swiss_iban(iban):
    # Entfernen von Leerzeichen aus der IBAN
    iban = iban.replace(" ", "")

    # Überprüfen, ob die IBAN mit CH beginnt
    if not iban.startswith("CH"):
        return False

    # Überprüfen der Länge der IBAN
    if len(iban) != 21:
        return False

    # Überprüfen, ob die IBAN nur aus Zahlen und Buchstaben besteht
    if not re.match("^[a-zA-Z0-9]*$", iban[2:]):
        return False

    return True
