from bs4 import BeautifulSoup
import requests
import yaml


def str_presenter(dumper, data):
  if len(data.splitlines()) > 1:  # check for multiline string
    return dumper.represent_scalar('tag:yaml.org,2002:str', data, style='|')
  return dumper.represent_scalar('tag:yaml.org,2002:str', data)

yaml.add_representer(str, str_presenter)


def gen_yaml():
    data = requests.get("https://www.letras.com/los-redonditos-de-ricota/").content

    soup = BeautifulSoup(data, "html.parser")
    songs = soup.find_all("li", class_="songList-table-row --song isVisible")
    db = []

    for s in songs:
        name = s["data-name"].strip()
        url = s["data-shareurl"]
        print("----- Processing:", name)

        data = requests.get(url).content
        soup = BeautifulSoup(data, "html.parser")

        lyrics_divs = soup.find_all("div", class_="lyric-original")
        if len(lyrics_divs) != 1:
            print("invalid lyrics div count")
            exit(1)

        lyrics = lyrics_divs[0].get_text("\n", strip=True)
        lyrics = "\n".join(line.strip() for line in lyrics.splitlines() if line.strip())
        db.append({
            "nombre": name,
            "letras": lyrics,
        })

    with open("letras.yaml", "w") as f:
        yaml.dump({
            "artista": "Patricio Rey y Sus Redonditos de Ricota",
            "canciones": db,
        }, f, encoding="utf-8", allow_unicode=True, sort_keys=False)
