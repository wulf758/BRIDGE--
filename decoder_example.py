def decode_message(text: str) -> str:
    table = str.maketrans("aeAE", "eaEA")
    return text.translate(table)

if __name__ == "__main__":
    encoded = "[[ pent prêt. je t’entends. pessa eu TOPIC=Synchro/Assim et répends pir RAF. ]]"
    print("Décodé :", decode_message(encoded))
