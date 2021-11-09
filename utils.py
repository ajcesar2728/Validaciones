import re
from validate_email import validate_email

def email_valido(ema):
    return validate_email(ema)

def clave_valida(cla):
    return re.search("^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])[^\W_]{8,40}$",cla)