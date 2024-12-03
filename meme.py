import time
meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            'ROFL': 'Una respuesta a una broma',
            'SHEESH': 'Ligera desaprobación',
            'CREEPY': 'Aterrador, siniestro',
            'AGGRO': 'Ponerse agresivo/enojado',
            'CUTE': 'Se trata de una expresión que quiere decir, literalmente, adorable.',
            'BTW': 'By the way o por cierto',
            'GHOSTING': 'Cuando hablas con una persona y de repente hace bum y desaparece, esta es la palabra que lo define.'
}
for i in range(5):
    print('Hola, ¡un gusto!')
    time.sleep(2)
    print('Acá podrás aprender nuevas palabras que se utilizan en redes, para esto...')
    time.sleep(1)
    word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")

    if word in meme_dict:
        # Hacer algo si se encuentra la palabra en el diccionario
        print('Se encontró la palabra', word, 'que significa:', meme_dict[word])
    else:
        # Hacer algo si no se encuentra la palabra en el diccionario
        print('No se encontró la palabra', word)
