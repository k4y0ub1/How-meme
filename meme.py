meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            'ROFL': 'Una respuesta a una broma',
            'SHEESH': 'Ligera desaprobación',
            'CREEPY': 'Aterrador, siniestro',
            'AGGRO': 'Ponerse agresivo/enojado'
}

word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")

if word in meme_dict:
    # Hacer algo si se encuentra la palabra en el diccionario
    print('Se encontró la palabra',word,'que significa:',meme_dict[word])
else:
    # Hacer algo si no se encuentra la palabra en el diccionario
    print('No se encontró la palabra',word)
