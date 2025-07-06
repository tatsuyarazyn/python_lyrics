import time

baris_lyrics = [
    ("the one that got away", 0.09, 1.4),
    ("all this money can't buy me a time machine", 0.08, 1.3),
    ("nooooooo......", 0.1, 1.2),
    ("can't replace you with a million rings", 0.09, 1.3),
    ("nooooooo......", 0.07, 1.2),
    ("I should've told you what you meant to me", 0.09, 1.2),
    ("whooouuu......", 0.07, 1.2),
    ("cause now I pay the price", 0.1, 1.2),
    ("In another life", 0.2, 1.2),
    ("I would be your girl", 0.08, 1.5),
    ("We keep all our promises", 0.08, 1.1),
    ("Be us against the world", 0.08, 1.1),
]

def animasi_per_karakter(teks, delay=0.0):
    for huruf in teks:
        print(huruf, end='', flush=True)
        time.sleep(delay)
    print() 

for lyrics, delay_huruf, jeda_baris in baris_lyrics:
    animasi_per_karakter(lyrics, delay_huruf)
    time.sleep(jeda_baris)