from substitution_ciphers import Substition_Ciphers

substituion_ciphers = Substition_Ciphers()

if substituion_ciphers.check_text():
    if substituion_ciphers.check_method():
        bruh = substituion_ciphers.encrypt()
print(bruh)