"""Genera empreses_balears.csv: les empreses amb activitat econòmica de les Illes
Balears, a partir del directori d'empreses DIRCE-IB de l'IBESTAT (any 2024).

El fitxer original es publica amb llicència CC-BY al catàleg de dades obertes de
l'IBESTAT. Porta el NIF i la raó social de cada empresa; aquí els traiem, perquè
per als notebooks no calen, i en deixem només les columnes categòriques. La forma
jurídica no ve com a columna, però es dedueix de la lletra inicial del NIF.

Ús, des de l'arrel del repositori:

    python UT03-Correlacions_preparacio_variables/ibestat_empreses/generar_empreses_balears.py

L'alumnat no l'ha d'executar: els notebooks carreguen el CSV per URL.
"""

import io
import urllib.request
from pathlib import Path

import pandas as pd

AQUI = Path(__file__).resolve().parent
SORTIDA = AQUI / "empreses_balears.csv"

FONT = (
    "https://ibestat.es/edatos/apps/catalogo/dataset/98ed9a01-f691-4de8-a834-f284fdaad175/"
    "resource/e9c46a4e-6f14-4647-8574-16ffc06c00f0/download/empreses_dirceib_2024.csv"
)

# Codis d'ESTRATO del fitxer original, de menys a més assalariats
TRAMS = {
    1: "Sense assalariats",
    2: "D'1 a 9",
    3: "De 10 a 49",
    4: "De 50 a 199",
    5: "200 o més",
}

# Lletra inicial del NIF d'una persona jurídica -> forma jurídica
FORMES = {
    "A": "Societat anònima",
    "B": "Societat limitada",
    "C": "Societat col·lectiva",
    "D": "Societat comanditària",
    "E": "Comunitat de béns",
    "F": "Cooperativa",
    "G": "Associació o fundació",
    "H": "Comunitat de propietaris",
    "J": "Societat civil",
    "N": "Entitat estrangera",
    "P": "Corporació local",
    "Q": "Organisme públic",
    "R": "Entitat religiosa",
    "S": "Administració de l'Estat o autonòmica",
    "U": "Unió temporal d'empreses",
    "V": "Altres",
    "W": "Establiment d'entitat no resident",
}

# Seccions de la CNAE-2009: primera divisió (dos dígits) de cada secció
SECCIONS = [
    (1, "Agricultura, ramaderia i pesca"),
    (5, "Indústries extractives"),
    (10, "Indústria manufacturera"),
    (35, "Energia elèctrica i gas"),
    (36, "Aigua, sanejament i residus"),
    (41, "Construcció"),
    (45, "Comerç"),
    (49, "Transport i emmagatzematge"),
    (55, "Hostaleria"),
    (58, "Informació i comunicacions"),
    (64, "Finances i assegurances"),
    (68, "Activitats immobiliàries"),
    (69, "Activitats professionals i tècniques"),
    (77, "Activitats administratives i auxiliars"),
    (84, "Administració pública"),
    (85, "Educació"),
    (86, "Sanitat i serveis socials"),
    (90, "Activitats artístiques i d'oci"),
    (94, "Altres serveis"),
    (97, "Llars que ocupen personal domèstic"),
    (99, "Organismes extraterritorials"),
]


def sector(cnae):
    """Torna el nom de la secció CNAE d'un codi de quatre dígits."""
    divisio = int(str(cnae)[:2])
    return [nom for inici, nom in SECCIONS if divisio >= inici][-1]


def main():
    with urllib.request.urlopen(FONT, timeout=120) as resposta:
        crues = resposta.read()
    orig = pd.read_csv(io.BytesIO(crues), sep="\t", encoding="cp1252", dtype=str)

    df = pd.DataFrame({
        "illa": orig["ISLA"],
        "municipi": orig["MUNICIPIO"],
        "sector": orig["COD_CNAE"].map(sector),
        "forma_juridica": orig["NIF"].str[0].map(FORMES),
        "assalariats": orig["ESTRATO"].astype(int).map(TRAMS),
    })
    assert df.notna().all().all(), "hi ha codis sense traduir"

    df.to_csv(SORTIDA, index=False)
    print(f"{len(df)} empreses -> {SORTIDA.name}")


if __name__ == "__main__":
    main()
