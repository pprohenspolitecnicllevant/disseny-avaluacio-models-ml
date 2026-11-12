"""Genera pluja_palma.csv: el temps diari a l'aeroport de Palma (AEMET) preparat
per classificar si demà plourà, per als notebooks d'AEMET de la UT4.

Parteix de meteo_palma.csv, el fitxer AEMET del repositori. Hi fa tres coses
perquè l'alumnat no s'hagi d'entretenir a filtrar:

- treu els anys 2024 i 2025, que són el test segellat i no s'obren fins a la UT10;
- treu els pocs dies amb alguna mesura absent;
- afegeix `pluja_forta_dema`: 1 si demà cauen més de 10 mm.

Ús, des de l'arrel del repositori:

    python UT04-Classificacio_logistica_knn/aemet/preparar_pluja_palma.py

L'alumnat no l'ha d'executar: els notebooks carreguen el CSV per URL.
"""

from pathlib import Path

import pandas as pd

AQUI = Path(__file__).resolve().parent
METEO = AQUI.parents[1] / "UT01-Entorn_de_treball_primer_model" / "aemet" / "meteo_palma.csv"
SORTIDA = AQUI / "pluja_palma.csv"

# Mesures del dia: temperatures (°C), pluja (mm), vent mitjà i ratxa (m/s),
# hores de sol i pressió (hPa)
MESURES = ["tmed", "tmin", "tmax", "prec", "velmedia", "racha", "sol", "presMax", "presMin"]

# Més de 10 mm en un dia: uns deu dies l'any a Palma
LLINDAR_PLUJA_FORTA = 10


def main():
    df = pd.read_csv(METEO)
    df = df[df["fecha"] < "2024-01-01"]
    df = df.dropna(subset=MESURES + ["prec_dema"])

    df["pluja_forta_dema"] = (df["prec_dema"] > LLINDAR_PLUJA_FORTA).astype(int)
    df = df[["fecha", "mes"] + MESURES + ["plou_dema", "pluja_forta_dema"]]

    df.to_csv(SORTIDA, index=False)
    print(f"{SORTIDA.name}: {len(df)} dies, "
          f"plou l'endemà el {df['plou_dema'].mean():.1%}, "
          f"pluja forta el {df['pluja_forta_dema'].mean():.1%}")


if __name__ == "__main__":
    main()
