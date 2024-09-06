# Patricio Rey y sus Vectorcitos de Ricota
Búsqueda por similitud semántica para canciones de Patricio Rey y sus Redonditos de Ricota, utilizando [FastText](https://fasttext.cc/).

Ejemplo de uso:
```bash
Palabra: insecto

[ Queso Ruso ]
   ...
   19  Mordiéndote la lengua por poco me engañás.
-> 20  Sentís la mosca joder detrás de la oreja  <-
   21  Y chupás la fruta sin poder morderla;
   ...

similitud: 0.54570127

[ Un Poco de Amor Francés ]
   ...
   16  Dijo y me conquistó
-> 17  (de esa miel no comen las hormigas).  <-

similitud: 0.5460269
```

## Instalar

Se requiere de Python 3.11 o superior así también como [Poetry](https://python-poetry.org/).
**Se recomienda contar con al menos 16 GB de RAM (preferiblemente 32).**

```bash
git clone https://github.com/federicotdn/patricio-rey-y-sus-vectorcitos-de-ricota.git
cd patricio-rey-y-sus-vectorcitos-de-ricota
poetry install
```

Luego, se debe descargar el archivo de vectores FastText SUC para texto en español (formato `.bin`) de https://github.com/dccuchile/spanish-word-embeddings:
```bash
make download-model
```

El archivo tiene un tamaño de 5.6 GB.

## Uso

Una vez instaladas las dependencias y descargado el modelo, se puede ejecutar el script de búsqueda de similitud semántica:
```bash
make run
```

El script solicitará una palabra y mostrará las canciones de Patricio Rey y sus Redonditos de Ricota que contienen la palabra ingresada, ordenadas por similitud semántica. Por ejemplo, buscando por la palabra "noche" se obtienen canciones con las palabras "amanecer", "noche", "día", etc.

Por defecto, la [similitud coseno](https://es.wikipedia.org/wiki/Similitud_coseno) mínima para encontrar canciones es de 0.5. Este valor puede ser modificado ingresando un número en lugar de una palabra (por ejemplo, `0.6`). Modificando este valor se pueden obtener resultados más o menos restrictivos.

## Licencia

Este proyecto está bajo la licencia MIT. Ver el archivo [LICENSE](LICENSE) para más detalles.