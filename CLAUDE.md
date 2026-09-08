# Context del projecte

Aquest repositori és **material docent**, no programari. Conté els notebooks de
Google Colab del mòdul professional **5134 — Disseny i avaluació de models basats
en aprenentatge automàtic** (cicle IAD41, especialització en IA i Big Data,
Politècnic Llevant, curs 2026-27).

Abans de tocar res, llegeix:

- **[docs/PLANIFICACIO.md](docs/PLANIFICACIO.md)** — programació didàctica:
  220 h, 12 UT, resultats d'aprenentatge, criteris d'avaluació de cada unitat i
  quins notebooks li toquen. És el bolcat del full de càlcul oficial del centre.
- **[docs/CONVENCIONS.md](docs/CONVENCIONS.md)** — com s'escriu el material:
  enfocament pràctic (no matemàtic), català, Colab, estructura de cada notebook.
- **[docs/DATASETS.md](docs/DATASETS.md)** — quins conjunts de dades es fan
  servir a cada unitat i per què es van descartar els altres.

## Regles ràpides

- El material es redacta **en català**.
- **L'enfocament és pràctic**: construir i avaluar models, no derivar fórmules.
- Els notebooks s'executen a **Colab** i carreguen les dades **per URL raw de
  GitHub**, mai amb fitxers locals.
- **Cada cel·la de codi porta la seva cel·la d'explicació.** Els notebooks fan de
  guió de classe, així que la càrrega de markdown és alta a propòsit.
- Si canvies la planificació, **actualitza també el full de càlcul** — la font de
  veritat administrativa és aquell, i `docs/PLANIFICACIO.md` n'és el reflex.

## Estructura

```
UTnn-Nom_de_la_unitat/
  <dataset>/
    NB_u_n_titol.ipynb
    dades.csv
docs/
```
