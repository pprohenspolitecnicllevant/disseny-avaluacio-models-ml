# Programació didàctica — MP 5134

> **Font de veritat.** Aquest document és el bolcat de la programació didàctica
> oficial del centre (full de càlcul de Google, vegeu [Enllaços](#enllaços)).
> Si el full i aquest document divergeixen, mana el full: actualitzeu aquí.
> Bolcat fet el 2026-09-08.

## 1. Dades del mòdul

| | |
|---|---|
| **Mòdul** | 5134. Disseny i avaluació de models basats en aprenentatge automàtic |
| **Codi** | 5134 |
| **Hores** | 220 |
| **Cicle** | Aprenentatge automàtic, gestió de dades i entrenament |
| **Sigles** | IAD41 |
| **Nivell** | Especialització |
| **Curs** | Primer |
| **Any acadèmic** | 2026-27 |
| **Departament** | Informàtica |
| **Docent** | Pere Prohens Galmés |
| **Grup** | A |
| **Normativa** | BOE-A-2026-5869 |

**Unitat de competència acreditable:** `ECP2493_3` — Entrenar models en sistemes
d'Intel·ligència Artificial basats en aprenentatge automàtic.

## 2. Calendari

- Classe presencial del **21 de setembre de 2026 al 10 de maig de 2027**.
  Després, FCT a empresa.
- **6 hores setmanals** repartides en **2 sessions de 3 hores**.

## 3. Resultats d'aprenentatge (RA)

1. **Col·labora en la cerca de correlacions entre les variables**, utilitzant
   eines que incorporen tècniques de l'estadística i l'aprenentatge automàtic,
   amb anterioritat al disseny i entrenament de models.
2. **Aplica la reducció de la dimensió** de les mostres dels conjunts de dades,
   usant la programació o eines de programari, per obtenir-ne una representació
   mitjançant variables latents.
3. **Representa les dades gràficament**, per corroborar visualment les
   correlacions trobades, verificant la reducció de la dimensió aplicada.
4. **Col·labora en el disseny de models basats en ML**, seleccionant, assajant i
   avaluant tècniques, models, paràmetres i mètriques, per abordar el problema
   plantejat segons el seu tipus, de regressió o de classificació.
5. **Avalua els models dissenyats**, definint un subconjunt de test quan el
   conjunt de dades no el tingués prèviament definit, i creant noves particions
   de validació i entrenament un cop separat el subconjunt de test.

> El BOE no especifica objectius per a aquest mòdul.

## 4. Competències professionals i mapa amb les UT

| Comp. | Descripció | RA | UT |
|---|---|---|---|
| **g** | Cercar, amb anterioritat a l'entrenament, correlacions entre les variables mitjançant eines estadístiques i d'aprenentatge automàtic. | 1 | 3 |
| **h** | Reduir la dimensió de les mostres dels conjunts de dades, mitjançant programació o eines de programari, visualitzant-les mitjançant eines gràfiques, amb la finalitat de corroborar les correlacions trobades i verificant la reducció. | 2 i 3 | 8 |
| **i** | Dissenyar models basats en aprenentatge automàtic (ML) per aplicar-los sobre el conjunt de dades amb l'objecte d'abordar el problema plantejat segons el seu tipus, de regressió o de classificació. | 4 | 1, 2, 4, 5, 6, 7, 9 |
| **j** | Avaluar els models dissenyats mitjançant subconjunts de test, creant noves particions de validació i entrenament. | 5 | 10, 11 |

**Competències transversals**

- **SOC** — Presenta bona disposició a l'hora de cooperar i col·laborar en la
  realització de les tasques dins d'un equip, entenent que es treballa per a un
  objectiu comú.
- **PER** — Segueix les normes de classe, comunicació clara i assertiva,
  puntualitat i assistència.

## 5. Distribució de les unitats de treball

| UT | Títol | Aval | Hores | Comp. |
|---|---|---|---|---|
| 1 | Entorn de treball i primer model de principi a fi | 1a | 8 | i |
| 2 | Regressió lineal i polinòmica | 1a | 18 | i |
| 3 | Correlacions i preparació de variables | 1a | 12 | g |
| 4 | Classificació: regressió logística i k-NN. Mètriques | 1a | 18 | i |
| 5 | Arbres de decisió i mètodes d'ensemble | 1a | 18 | i |
| 6 | Màquines de suport vectorial (SVM) | 1a | 12 | i |
| 7 | Aprenentatge no supervisat: k-means i mixtures gaussianes | 2a | 15 | i |
| 8 | Reducció de la dimensió i representació gràfica | 2a | 12 | h |
| 9 | Primer contacte amb xarxes neuronals (MLP) | 2a | 15 | i |
| 10 | Validació creuada, ajust d'hiperparàmetres i robustesa | 2a | 15 | j |
| 11 | Projecte integrador i informe d'avaluació | 2a | 22 | j |
| 12 | FEMPO | 3a | 55 | — |
| | **Total** | | **220** | |

Lectives (UT1-UT11): 165 h. FEMPO: 55 h.

## 6. Fils que travessen tot el mòdul

- **El test segellat.** A la **UT2** s'aparta el 20% de les dades com a test i no
  s'obre fins a la **UT11**, en classe, comparant l'estimació de validació amb el
  resultat real.
- **La fuga d'informació.** Se sembra a la UT1 (per què predim demà i no avui),
  es formalitza a la UT8 (ajustar transformacions només amb entrenament,
  `Pipeline`) i té el seu cas trampa a la UT10.
- **La desconfiança de les mètriques.** El model de referència (`Dummy*`) apareix
  ja a la UT1 i el desbalanç de classes es tanca a la UT4.
- **Pont amb el mòdul 5149.** Els autocodificadors i PyTorch són del 5149. Aquí
  les xarxes es fan amb `MLPClassifier`/`MLPRegressor` de scikit-learn.

## 7. Sistema d'avaluació

**Instruments i pesos** (pendents de tancar al full; ara mateix hi consta):

| Instrument | % |
|---|---|
| Exàmens | 40 |
| Pràctiques | 25 |
| Treballs | 25 |
| Altres | 10 |

> **Pendent.** Al full, el bloc de pesos per competència dona `Pes total 0` i
> arrossega un `#REF!`. Cal revisar-lo.

**Apartats encara sense redactar al full:** procediments d'avaluació i criteris
de qualificació · recuperació · notes d'avaluacions no ordinàries · observacions
· metodologia i dinàmica general de les sessions · recursos i materials · atenció
a la diversitat · temes transversals · activitats extraescolars · normes ·
bibliografia.

## 8. Fitxes de les unitats de treball

Cada fitxa recull els continguts, les activitats d'aula i els criteris
d'avaluació tal com són al full.

---

### UT1 — Entorn de treball i primer model de principi a fi
**Aval.** 1a · **Hores.** 8 · **Competència.** i

**Continguts**

1. **L'entorn de treball** — Jupyter i Colab. Repàs pràctic de NumPy, Pandas i Matplotlib. Càrrega de fitxers CSV.
2. **El flux d'un projecte d'aprenentatge automàtic** — Tipus de problema: regressió, classificació i no supervisat. Mostres, característiques i variable objectiu.
3. **L'API de scikit-learn** — Els estimadors com a objectes: `fit`, `predict` i `score`. Relació amb la POO ja coneguda per l'alumnat.
4. **Primer model complet de principi a fi** — Entrenament sobre un conjunt petit, predicció i primera partició en entrenament i test.

**Activitats d'aula**

- **NB 1.1.** Presa de contacte: càrrega d'un CSV, inspecció amb Pandas i primeres gràfiques.
- **NB 1.2.** Un model complet en poques línies, executat sencer abans d'explicar-ne cap peça.
- Lectura de codi: localitzar `fit`, `predict` i `score` i explicar què fa cadascun.
- Debat: quins problemes del vostre entorn són de regressió i quins de classificació.

**Criteris d'avaluació**

- RA4.a (inici) Es distingeix el tipus de problema plantejat i s'hi associa una tècnica adequada.
- S'executa i es modifica un notebook sense errors, identificant el paper de `fit`, `predict` i `score`.
- *Unitat introductòria: avaluació formativa, sense pes en la qualificació.*

---

### UT2 — Regressió lineal i polinòmica
**Aval.** 1a · **Hores.** 18 · **Competència.** i

**Continguts**

1. **Regressió lineal simple** — Recta d'ajust, pendent i ordenada a l'origen. Lectura del model entrenat.
2. **Regressió lineal múltiple** — Diverses variables d'entrada. Efecte d'afegir o llevar variables sobre l'ajust.
3. **Regressió polinòmica** — Generació de característiques polinòmiques i elecció del grau.
4. **Sobreajust i infraajust** — Grau 1 contra grau 15 amb poques mostres. Comportament davant dades noves.
5. **Mètriques de regressió** — MAE, RMSE, R2 i desviació percentual entre valors predits i reals.

**Activitats d'aula**

- **NB 2.1.** Regressió lineal sobre una variable, amb la recta dibuixada sobre el núvol de punts.
- **NB 2.2.** Regressió múltiple: comparar l'ajust afegint variables d'una en una.
- **NB 2.3.** Escombrada de graus polinòmics per veure el sobreajust amb els ulls.
- **Es reserva el 20% de les dades com a test segellat, que no s'obrirà fins a la UT11.**
- Exercici: triar la mètrica adequada per a una predicció de vendes setmanals i justificar-la.

**Criteris d'avaluació**

- RA4.a S'han triat les tècniques d'aprenentatge automàtic en base a l'anàlisi previ de les dades.
- RA4.b S'assagen els models programant codi per entrenar-los i comparant configuracions.
- RA4.e S'identifica la desviació percentual entre valors predits i reals en problemes de regressió.
- Es reconeix el sobreajust a partir de la diferència de rendiment entre entrenament i validació.

---

### UT3 — Correlacions i preparació de variables
**Aval.** 1a · **Hores.** 12 · **Competència.** g

**Continguts**

1. **Correlació lineal i no lineal** — Pearson i Spearman. Correlació contra causalitat. Correlacions espúries.
2. **Matriu de correlació i mapa de calor** — Lectura del mapa de calor. Detecció de colinealitat entre variables.
3. **Codificació de variables categòriques** — One-hot, codificació ordinal i agrupació de categories minoritàries.
4. **Transformacions i escalat** — Logaritme, arrel i estandardització segons la distribució dels valors.
5. **Selecció de variables d'entrada** — Variables amb més correlació amb la variable objectiu. Document de decisions de disseny.

**Activitats d'aula**

- **NB 3.1.** Matriu de correlació del conjunt del projecte, amb mapa de calor.
- **NB 3.2.** Pearson contra Spearman sobre una relació monòtona no lineal.
- **NB 3.3.** Codificació i escalat, ajustats només amb el subconjunt d'entrenament.
- Exercici de detecció: conjunt amb dues variables quasi idèntiques i una correlació espúria induïda.
- Redacció del document de variables d'entrada, de sortida i correlacions trobades.

**Criteris d'avaluació**

- RA1.a S'han cercat correlacions entre variables, tant lineals com no lineals.
- RA1.b S'apliquen procediments de categorització i codificació de variables, com els one-hot vectors.
- RA1.c S'apliquen les transformacions matemàtiques adequades a la distribució de cada variable.
- RA1.d Se seleccionen les variables d'entrada amb més correlació amb la variable objectiu.
- RA1.e Es redacta un document amb les variables d'entrada i sortida i les correlacions trobades.

---

### UT4 — Classificació: regressió logística i k-NN. Mètriques
**Aval.** 1a · **Hores.** 18 · **Competència.** i

**Continguts**

1. **El problema de classificació** — Diferència amb la regressió. Classes, frontera de decisió i probabilitat de pertinença.
2. **Regressió logística** — Funció logística, llindar de decisió i lectura dels coeficients. El paràmetre C.
3. **K veïns més propers (k-NN)** — Distància, elecció de k i efecte de l'escalat de les variables. Cost de la predicció.
4. **Matriu de confusió i mètriques** — Vertaders i falsos positius i negatius. Accuracy, precision, recall i specificity.
5. **Corba ROC i classes desbalancejades** — Corba ROC i àrea sota la corba. Per què l'accuracy engana amb classes desbalancejades.

**Activitats d'aula**

- **NB 4.1.** Regressió logística sobre dues variables, amb la frontera de decisió dibuixada.
- **NB 4.2.** k-NN amb i sense escalat de variables, per veure'n l'efecte sobre el resultat.
- **NB 4.3.** Taller de mètriques: calcular-les a mà des de la matriu de confusió i comparar amb scikit-learn.
- Cas de classes desbalancejades: un model trivial encerta el 97% i no serveix. Justificar quina mètrica cal.

**Criteris d'avaluació**

- RA4.d Se seleccionen les mètriques adequades a la tècnica aplicada i al problema a resoldre.
- RA4.e S'identifiquen la ràtio de falsos positius i negatius, accuracy, precision, recall, specificity i l'àrea sota la corba ROC.
- RA4.f S'avaluen els models dissenyats en base a les mètriques seleccionades.
- Es justifica per escrit l'elecció de la mètrica en un cas de classes desbalancejades.

---

### UT5 — Arbres de decisió i mètodes d'ensemble
**Aval.** 1a · **Hores.** 18 · **Competència.** i

**Continguts**

1. **L'arbre de decisió** — Divisions successives, lectura de l'arbre dibuixat i interpretabilitat del model.
2. **Hiperparàmetres de l'arbre** — Profunditat màxima i mostres mínimes per fulla. Efecte sobre el sobreajust.
3. **Boscos aleatoris (random forest)** — Combinació de molts arbres. Nombre d'arbres a generar i paper de l'aleatorietat.
4. **Importància de les variables** — Comparació de la importància obtinguda amb les correlacions trobades a la UT3.
5. **Introducció al gradient boosting** — Idea general i quan val la pena, sense entrar en la formulació matemàtica.

**Activitats d'aula**

- **NB 5.1.** Arbre entrenat i dibuixat, llegit en veu alta pel grup.
- **NB 5.2.** Efecte de la profunditat màxima sobre entrenament i validació.
- **NB 5.3.** Random forest contra arbre únic sobre el mateix conjunt.
- Exercici: comparar la importància de variables amb la matriu de correlació de la UT3 i explicar les diferències.

**Criteris d'avaluació**

- RA4.a S'han triat tècniques com els arbres de decisió i els random forests en base a l'anàlisi previ.
- RA4.c S'identifiquen combinacions de paràmetres com el nombre d'arbres a generar.
- RA4.g S'inclouen comentaris al codi per poder reutilitzar-lo en problemes similars.
- Es justifica la tria entre un model interpretable i un altre de més precís.

---

### UT6 — Màquines de suport vectorial (SVM)
**Aval.** 1a · **Hores.** 12 · **Competència.** i

**Continguts**

1. **La idea de marge màxim** — Frontera que separa amb el marge més ample. Els vectors de suport.
2. **SVM lineal** — Aplicació sobre dades separables i quasi separables.
3. **Nuclis (kernels)** — Nucli RBF de manera visual: dades que no se separen amb una recta.
4. **Els paràmetres C i gamma** — Efecte de C i de gamma sobre la frontera, provat de manera empírica.
5. **Quan triar un SVM** — Comparació amb arbres: poques mostres i moltes variables contra dades tabulars grans.

**Activitats d'aula**

- **NB 6.1.** SVM lineal amb els vectors de suport marcats sobre la gràfica.
- **NB 6.2.** Dades en cercles concèntrics: nucli lineal contra RBF.
- **NB 6.3.** Graella de valors de C i gamma, amb les fronteres dibuixades.
- Exercici comparatiu: el mateix problema amb SVM, arbre i random forest, amb taula de resultats.

**Criteris d'avaluació**

- RA4.a S'han triat tècniques com les màquines de suport vectorial en base a l'anàlisi previ.
- RA4.b S'assagen els models fent experiments amb distintes combinacions de paràmetres.
- RA4.f S'avaluen els models i es decideix si cal redissenyar-los.
- Es justifica en quins escenaris un SVM és preferible a un model basat en arbres.

---

### UT7 — Aprenentatge no supervisat: k-means i mixtures gaussianes
**Aval.** 2a · **Hores.** 15 · **Competència.** i

**Continguts**

1. **Agrupament sense variable objectiu** — Diferència amb l'aprenentatge supervisat. Casos d'ús reals.
2. **K-means** — Centroides, assignació de mostres i iteracions de l'algorisme.
3. **Elecció del nombre de grups** — Mètode del colze i coeficient de silueta.
4. **Mixtures de gaussianes** — Assignació probabilística contra assignació dura. Grups de forma no esfèrica.
5. **Altres enfocaments d'agrupament** — DBSCAN i agrupament per densitat, a nivell introductori.

**Activitats d'aula**

- **NB 7.1.** K-means en dues dimensions, amb els centroides dibuixats a cada iteració.
- **NB 7.2.** Colze i silueta per decidir el nombre de grups.
- **NB 7.3.** Mixtures de gaussianes sobre grups allargats on k-means falla.
- Exercici de segmentació: agrupar un conjunt real i descriure amb paraules cada grup obtingut.

**Criteris d'avaluació**

- RA4.a S'han triat tècniques com els models de mixtures de gaussianes en base a l'anàlisi previ.
- RA4.c S'identifica el nombre de grups (clusters) adequat per a l'algorisme k-means.
- RA4.h Es genera documentació amb els models dissenyats i les seves variants.
- Es descriuen amb llenguatge natural els grups obtinguts i la seva utilitat.

---

### UT8 — Reducció de la dimensió i representació gràfica
**Aval.** 2a · **Hores.** 12 · **Competència.** h

**Continguts**

1. **El problema de les moltes dimensions** — Variables latents i per què convé reduir. Cost i pèrdua d'informació.
2. **Anàlisi de components principals (PCA)** — Variància explicada, nombre de components i lectura dels loadings.
3. **Reducció no lineal amb t-SNE** — Perplexitat, caràcter no determinista i ús només exploratori.
4. **Representació gràfica dels resultats** — Histogrames, mapes de dispersió i gràfiques de components acolorides per la classe.
5. **Pipelines i fuita d'informació** — Ajust de la transformació només amb entrenament. Encapsulat amb `Pipeline`.

**Activitats d'aula**

- **NB 8.1.** PCA amb corba de variància acumulada i tria del nombre de components.
- **NB 8.2.** PCA contra t-SNE sobre el mateix conjunt, amb les dues projeccions comparades.
- **NB 8.3.** Repetir t-SNE amb distintes perplexitats i dues execucions per valor.
- Exercici d'error induït: notebook amb el PCA ajustat abans de partir les dades; localitzar-lo i corregir-lo.
- *Els autocodificadors es tracten al mòdul 5149.*

**Criteris d'avaluació**

- RA2.a S'utilitzen tècniques de reducció de la dimensió com PCA i t-SNE.
- RA2.b Es programen procediments que creen una còpia del conjunt amb les transformacions aplicades.
- RA2.d Es documenten les tècniques aplicades, els paràmetres i els resultats obtinguts.
- RA3.a Es generen gràfiques que verifiquen les correlacions i les transformacions aplicades.
- RA3.c Es recullen les gràfiques en un informe amb histogrames i mapes de dispersió.

---

### UT9 — Primer contacte amb xarxes neuronals (MLP)
**Aval.** 2a · **Hores.** 15 · **Competència.** i

**Continguts**

1. **La neurona i el perceptró** — Entrada, pesos i sortida, de manera visual i sense desenvolupament matemàtic.
2. **El perceptró multicapa** — Capes ocultes i problemes que no són linealment separables.
3. **Hiperparàmetres de la xarxa** — Coeficient d'aprenentatge, nombre de capes, neurones per capa i funcions d'activació.
4. **MLP amb scikit-learn** — `MLPClassifier` i `MLPRegressor` com un estimador més, amb la mateixa API ja coneguda.
5. **Pont cap al mòdul 5149** — Limitacions de scikit-learn i per què el 5149 fa servir PyTorch.

**Activitats d'aula**

- **NB 9.1.** Un perceptró resolent AND i OR, i fracassant amb XOR.
- **NB 9.2.** MLP resolent XOR, amb la frontera de decisió dibuixada.
- **NB 9.3.** Escombrada d'hiperparàmetres: capes, neurones, activació i coeficient d'aprenentatge.
- Exercici comparatiu: el mateix problema amb MLP, random forest i SVM, amb resultats i temps d'entrenament.

**Criteris d'avaluació**

- RA4.a S'han triat les xarxes neuronals com a tècnica en base a l'anàlisi previ de les dades.
- RA4.c S'identifiquen el coeficient d'aprenentatge, el nombre de capes, les neurones per capa i els tipus d'activació.
- RA4.b S'assagen els models fent experiments amb distintes configuracions.
- Es justifica quan una xarxa neuronal aporta avantatge sobre models més simples.

---

### UT10 — Validació creuada, ajust d'hiperparàmetres i robustesa
**Aval.** 2a · **Hores.** 15 · **Competència.** j

**Continguts**

1. **Particions d'entrenament, validació i test** — Test entre el 10% i el 30% del conjunt. Partició estratificada que conserva la distribució de classes.
2. **Validació creuada** — K iteracions i variant estratificada. Repetició del procés complet per partició.
3. **Cerca d'hiperparàmetres** — Cerca en graella i cerca aleatòria. En quina iteració es desa la versió del model.
4. **Corbes d'aprenentatge** — Diagnòstic de si convé més dades o bé un model distint.
5. **Mitjana, variància i robustesa** — Mitjana aritmètica i variància de les mètriques entre particions com a mesura de robustesa.

**Activitats d'aula**

- **NB 10.1.** Partició estratificada i comprovació que es manté la distribució de classes.
- **NB 10.2.** Validació creuada sobre els models de les UT anteriors, amb taula de mitjana i variància.
- **NB 10.3.** Cerca d'hiperparàmetres amb graella sobre el millor model fins ara.
- Exercici de robustesa: triar entre un model amb millor mitjana i pitjor variància i un altre més estable.

**Criteris d'avaluació**

- RA5.a Es divideix el conjunt en entrenament i test, amb el test entre el 10% i el 30%.
- RA5.b Es torna a dividir en entrenament i validació conservant la mateixa distribució de classes.
- RA5.c Es duu a terme la validació creuada generant distintes particions.
- RA5.d Es decideix en quina iteració es desa la versió del model a avaluar amb el test.
- RA5.e S'avalua amb el subconjunt de test mostrant mitjana i variància de les mètriques.

---

### UT11 — Projecte integrador i informe d'avaluació
**Aval.** 2a · **Hores.** 22 · **Competència.** j

**Continguts**

1. **Plantejament del projecte** — Elecció del conjunt de dades i definició del problema, de regressió o de classificació.
2. **Desenvolupament del flux complet** — Exploració, preparació, reducció si escau, entrenament de diversos models i validació creuada.
3. **Obertura del test segellat** — Comparació entre l'estimació de validació i el resultat real sobre el test reservat des de la UT2.
4. **Informe d'avaluació** — Gràfiques i taules amb les mètriques triades, comparant rendiment i robustesa de cada model.
5. **Presentació al grup** — Exposició oral breu i conclusions col·lectives.

**Activitats d'aula**

- Projecte en parelles amb repartiment de rols registrat, per poder avaluar l'aportació individual.
- Seguiment amb dues entregues parcials abans de l'entrega final.
- Obertura conjunta del subconjunt de test a l'aula, comparant l'estimació prèvia amb el resultat.
- Exposició de 10 minuts per parella i torn de preguntes del grup.

**Criteris d'avaluació**

- RA5.f Es crea un informe d'avaluació amb gràfiques i taules que comparen rendiment i robustesa.
- RA4.h Es genera la documentació dels models dissenyats amb totes les seves variants.
- RA3.b S'elabora el material de presentació per exposar-lo a l'equip de treball.
- RA3.d S'explica l'obtenció de les gràfiques aportant una valoració de cadascuna.
- Es valora la coherència entre les decisions preses i els resultats obtinguts.

---

### UT12 — FEMPO
**Aval.** 3a · **Hores.** 55

Fitxa pendent d'emplenar al full.

## Enllaços

- Programació didàctica (full de càlcul): <https://docs.google.com/spreadsheets/d/1kRky2w5RGnG40Qe27uaFpq4O2stqnw7iQXRHhwESrek/edit>
- Normativa: BOE-A-2026-5869
