# 5134 — Disseny i avaluació de models basats en aprenentatge automàtic

Material docent del mòdul professional **5134** del cicle d'especialització
**IAD41 — Aprenentatge automàtic, gestió de dades i entrenament**
(Politècnic Llevant, curs 2026-27).

El mòdul són **220 hores** repartides en 12 unitats de treball. L'enfocament és
**pràctic**: construir models i avaluar-los, no derivar fórmules.

## Com fer servir els notebooks

Estan pensats per executar-se a **Google Colab**. No cal instal·lar res ni
descarregar cap fitxer: les dades es carreguen per URL des d'aquest mateix
repositori.

| Notebook | Obre a Colab |
|---|---|
| NB 1.1 — Presa de contacte amb les dades | [obrir](https://colab.research.google.com/github/pprohenspolitecnicllevant/disseny-avaluacio-models-ml/blob/main/UT01-Entorn_de_treball_primer_model/aemet/NB_1_1_presa_de_contacte.ipynb) |
| NB 1.2 — El teu primer model, de principi a fi | [obrir](https://colab.research.google.com/github/pprohenspolitecnicllevant/disseny-avaluacio-models-ml/blob/main/UT01-Entorn_de_treball_primer_model/aemet/NB_1_2_primer_model.ipynb) |
| NB 1.1 — Presa de contacte *(versió pingüins)* | [obrir](https://colab.research.google.com/github/pprohenspolitecnicllevant/disseny-avaluacio-models-ml/blob/main/UT01-Entorn_de_treball_primer_model/penguins/NB_1_1_presa_de_contacte_PINGUINS.ipynb) |
| NB 1.2 — El teu primer model *(versió pingüins)* | [obrir](https://colab.research.google.com/github/pprohenspolitecnicllevant/disseny-avaluacio-models-ml/blob/main/UT01-Entorn_de_treball_primer_model/penguins/NB_1_2_primer_model_PINGUINS.ipynb) |

Cada cel·la de codi va acompanyada de la seva explicació: els notebooks fan de
guió de classe, no només d'exercici.

## Les dades

Hi ha una segona versió dels notebooks de la UT1 amb els **pingüins de
l'arxipèlag Palmer** (344 mesures de camp), pensada per a una primera sessió on
les dades es puguin mirar senceres. El detall és a
[docs/DATASETS.md](docs/DATASETS.md).

El conjunt principal del curs són **mesures meteorològiques diàries de l'estació
B278 (aeroport de Palma)**, publicades per l'AEMET: 4.017 dies, del gener de 2015
al desembre de 2025.

Serveix per als dos grans problemes supervisats sobre les mateixes files:

- **Regressió** — predir `tmax_dema`, la temperatura màxima de demà.
- **Classificació** — predir `plou_dema`, si demà plou (només un 13,5% dels dies).

Són dades **mesurades**, no imputades ni ponderades, i el desbalanç de classes és
real. El detall de per què es va triar aquest conjunt, quins altres es fan servir
i quins es van descartar és a [docs/DATASETS.md](docs/DATASETS.md).

## Unitats

| UT | Títol | Aval | Hores | Estat |
|---|---|---|---|---|
| 1 | [Entorn de treball i primer model de principi a fi](UT01-Entorn_de_treball_primer_model) | 1a | 8 | NB 1.1 i 1.2, amb AEMET i amb pingüins |
| 2 | Regressió lineal i polinòmica | 1a | 18 | pendent |
| 3 | Correlacions i preparació de variables | 1a | 12 | pendent |
| 4 | Classificació: regressió logística i k-NN. Mètriques | 1a | 18 | pendent |
| 5 | Arbres de decisió i mètodes d'ensemble | 1a | 18 | pendent |
| 6 | Màquines de suport vectorial (SVM) | 1a | 12 | pendent |
| 7 | Aprenentatge no supervisat: k-means i mixtures gaussianes | 2a | 15 | pendent |
| 8 | Reducció de la dimensió i representació gràfica | 2a | 12 | pendent |
| 9 | Primer contacte amb xarxes neuronals (MLP) | 2a | 15 | pendent |
| 10 | Validació creuada, ajust d'hiperparàmetres i robustesa | 2a | 15 | pendent |
| 11 | Projecte integrador i informe d'avaluació | 2a | 22 | pendent |
| 12 | FEMPO | 3a | 55 | pendent |

A la UT2 s'aparta el **20% de les dades com a test segellat**, que no s'obre fins
a la UT11. És el fil que cus el curs sencer.

## Organització del repositori

```
UTnn-Nom_de_la_unitat/
  <dataset>/
    NB_u_n_titol.ipynb     els notebooks de la unitat
    dades.csv              les dades que carreguen
docs/                      planificació, convencions i datasets
```

## Documentació

| | |
|---|---|
| [docs/PLANIFICACIO.md](docs/PLANIFICACIO.md) | Programació didàctica: resultats d'aprenentatge, competències i la fitxa de cada UT amb continguts, activitats i criteris d'avaluació |
| [docs/CONVENCIONS.md](docs/CONVENCIONS.md) | Com s'escriu el material: enfocament, entorn, redacció i estructura dels notebooks |
| [docs/DATASETS.md](docs/DATASETS.md) | Conjunts de dades del curs, amb el motiu de cada tria i de cada descart |

---

Docent: Pere Prohens Galmés · Departament d'Informàtica · Politècnic Llevant
