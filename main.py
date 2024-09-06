from dataclasses import dataclass
from collections import defaultdict

import yaml
from gensim.models.fasttext import load_facebook_model


MIN_SIMILARITY = 0.5


@dataclass
class Line:
    text: str
    number: int
    song: "Song"


@dataclass
class Song:
    name: str
    lines: list[Line]

    def str_line(self, line: Line) -> str:
        parts = [f"[ {self.name} ]"]
        n = line.number
        i = line.number - 1

        if i - 1 >= 0:
            parts.append("   ...")
            parts.append(f"   {n - 1}  {self.lines[i - 1].text}")

        parts.append(f"-> {n}  {self.lines[i].text}  <-")

        if i + 1 < len(self.lines):
            parts.append(f"   {n + 1}  {self.lines[i + 1].text}")
            parts.append("   ...")

        return "\n".join(parts)


def clean_word(word: str) -> str:
    word = word.lower()
    return word.strip("!¡?¿,.()-")


def main():
    with open("resources/stopwords.txt") as f:
        data = f.readlines()
        stopwords = {line.strip() for line in data if line.strip()}
        stopwords.add("")

    print("Cargando letras...")
    with open("resources/letras.yaml") as f:
        data = yaml.load(f, Loader=yaml.Loader)
        songs = data["canciones"]

    index = defaultdict(list)

    for song in songs:
        lines = song["letras"].splitlines()
        lines = [
            Line(text=line, number=i + 1, song=None) for i, line in enumerate(lines)
        ]

        song = Song(name=song["nombre"], lines=lines)

        for line in song.lines:
            line.song = song
            words = [
                w
                for w in (clean_word(word) for word in line.text.split())
                if w not in stopwords
            ]

            for word in words:
                index[word].append(line)

    print("Cargando vectores...")
    wv = load_facebook_model("resources/embeddings-l-model.bin").wv
    min_similarity = MIN_SIMILARITY
    print("Listo.\n")

    while True:
        q = input("Palabra: ")
        if not q:
            break

        try:
            min_similarity = float(q)
            print("coeficiente de similitud mínimo actual:", min_similarity)
            continue
        except ValueError:
            pass
        print()

        results = 0
        for word, lines in index.items():
            similarity = 0
            if q in wv.key_to_index and word in wv.key_to_index:
                similarity = wv.similarity(word, q)

            if similarity > min_similarity:
                for line in lines:
                    results += 1
                    print(line.song.str_line(line))
                    print()
                    print("similitud:", similarity)
                    print()

        print("resultados:", results)
        print("----------------------------------------")
        print()


if __name__ == "__main__":
    main()
