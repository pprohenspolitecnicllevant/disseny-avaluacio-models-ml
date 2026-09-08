# Convencions del material del MP 5134

## 1. Enfocament

**Es prioritza construir i avaluar models, no la formulació matemàtica.**

L'alumnat ve de programació (POO) i el que ha de saber fer és muntar el flux
complet i decidir amb criteri, no derivar fórmules. La programació ho recull
explícitament: el perceptró s'explica «de manera visual i sense desenvolupament
matemàtic» i el gradient boosting «sense entrar en la formulació matemàtica».

Conseqüències pràctiques:

- Els hiperparàmetres s'expliquen **empíricament i visualment**: dibuixar la
  frontera, escombrar valors i mirar què passa.
- La fórmula, si apareix, arriba **després** de la intuïció i mai com a requisit
  per entendre la cel·la següent.
- Referència de fons del docent: Aurélien Géron, *Hands-On Machine Learning with
  Scikit-Learn and PyTorch*. El curs en segueix l'esperit pràctic.

## 2. Entorn

- **Google Colab.** Res d'instal·lacions locals ni d'entorns virtuals.
- Les dades es carreguen sempre **per URL raw de GitHub**, mai amb fitxers
  locals ni `files.upload()`. L'alumnat no toca claus d'API ni fitxers.
- Cada notebook declara la font en una constant a la primera cel·la de codi:

  ```python
  URL_DADES = "https://raw.githubusercontent.com/.../meteo_palma.csv"
  ```

  Així, si canvia la ubicació de les dades, només cal tocar una línia per
  notebook.

## 3. Redacció

- **En català.**
- To explicatiu i **prosa contínua**, no llistes de passos. Els notebooks han de
  poder fer de guió de les explicacions de classe.
- **Cada cel·la de codi va acompanyada d'una cel·la de text que l'explica.** La
  càrrega de markdown és alta a propòsit.
- **Referències creuades explícites a altres UT** («hi tornarem a la UT3»,
  «això és exactament la UT10»), per donar continuïtat al curs i perquè
  l'alumnat sàpiga que un fil obert es tancarà.
- Els conceptes s'introdueixen **al punt on fan falta**, no en un bloc de
  vocabulari inicial.

## 4. Estructura d'un notebook

1. Capçalera: codi i nom del notebook, mòdul, UT.
2. **Què farem avui** i, si escau, les preguntes que s'han de saber respondre en
   acabar.
3. Desenvolupament: codi + explicació, alternats.
4. **Exercicis.**
5. **Per al debat de classe**, quan la unitat s'hi presta.

## 5. Nomenclatura

- Carpetes: `UTnn-Nom_de_la_unitat` (p. ex. `UT01-Entorn_de_treball_primer_model`).
- Notebooks: `NB_u_n_titol_curt.ipynb`, on `u.n` és la numeració que fixa la
  programació (NB 1.1, NB 1.2, NB 2.1…).
- Dins de cada UT, una subcarpeta per dataset quan n'hi hagi més d'un.

## 6. Criteris pedagògics recurrents

- **Executar primer, entendre després.** El NB «primer model» arrenca amb un
  bloc complet que l'alumnat executa sense entendre, i després es desmunta.
- **Sempre un model de referència.** `DummyRegressor` i `DummyClassifier`
  apareixen ja a la UT1: un R2 o un percentatge d'encerts no volen dir res sense
  un punt de comparació.
- **Mirar casos concrets abans que el número global.** Taula de real contra
  predit abans de la mètrica.
- **Dades mesurades, no imputades.** Vegeu [DATASETS.md](DATASETS.md).
