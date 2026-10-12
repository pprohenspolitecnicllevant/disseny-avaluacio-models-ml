"""Genera demanda_balears.csv: demanda elèctrica diària de les Illes Balears
(Red Eléctrica) amb el temps de cada dia a l'aeroport de Palma (AEMET).

La demanda es consulta a l'API pública REData de Red Eléctrica, que no demana
cap clau. Les columnes meteorològiques surten de meteo_palma.csv, el fitxer AEMET
del repositori, que ha d'estar al seu lloc.

Ús, des de l'arrel del repositori:

    python UT02-Regressio_lineal_polinomica/demanda_electrica/generar_demanda_balears.py

L'alumnat no l'ha d'executar: els notebooks carreguen el CSV per URL.
"""

import json
import urllib.request
from pathlib import Path

import pandas as pd

AQUI = Path(__file__).resolve().parent
METEO = AQUI.parents[1] / "UT01-Entorn_de_treball_primer_model" / "aemet" / "meteo_palma.csv"
SORTIDA = AQUI / "demanda_balears.csv"

# Sistema elèctric balear (Mallorca-Menorca i Eivissa-Formentera) a REData
API = (
    "https://apidatos.ree.es/es/datos/demanda/evolucion"
    "?start_date={any}-01-01T00:00&end_date={any}-12-31T23:59"
    "&time_trunc=day&geo_trunc=electric_system&geo_limit=baleares&geo_ids=8743"
)
ANYS = range(2015, 2026)

# Temps del dia a l'aeroport de Palma: temperatures (°C), pluja (mm), hores de sol
# i vent mitjà (m/s)
TEMPS = ["tmed", "tmax", "tmin", "prec", "sol", "velmedia"]


def demanda_any(any_):
    """Torna la demanda diària d'un any, en MWh, com a llista de (data, valor)."""
    with urllib.request.urlopen(API.format(any=any_), timeout=60) as resposta:
        dades = json.load(resposta)
    valors = dades["included"][0]["attributes"]["values"]
    return [(v["datetime"][:10], v["value"]) for v in valors]


def main():
    files = [fila for any_ in ANYS for fila in demanda_any(any_)]
    demanda = pd.DataFrame(files, columns=["fecha", "demanda"])
    demanda["fecha"] = pd.to_datetime(demanda["fecha"])
    demanda["demanda"] = (demanda["demanda"] / 1000).round(3)  # MWh -> GWh

    meteo = pd.read_csv(METEO, parse_dates=["fecha"])[["fecha", "any", "mes", "dia_any"] + TEMPS]

    df = meteo.merge(demanda, on="fecha", how="inner")
    df["cap_de_setmana"] = (df["fecha"].dt.dayofweek >= 5).astype(int)
    df = df[["fecha", "any", "mes", "dia_any", "cap_de_setmana"] + TEMPS + ["demanda"]]

    df.to_csv(SORTIDA, index=False, date_format="%Y-%m-%d")
    print(f"{len(df)} dies, del {df['fecha'].min():%Y-%m-%d} al {df['fecha'].max():%Y-%m-%d} -> {SORTIDA.name}")


if __name__ == "__main__":
    main()
