# Programació didàctica — MP 5134

> **Font de veritat.** Aquest document és el bolcat de la programació didàctica
> oficial del centre (full de càlcul de Google, vegeu [Enllaços](#enllaços)).
> Si el full i aquest document divergeixen, mana el full: actualitzeu aquí.
> Bolcat fet el 2026-09-08. Actualitzat el 2026-09-14: s'elimina la UT de xarxes
> neuronals (passa al mòdul 5149) i la validació creuada s'avança a la UT7.
> Totes les UT lectives tenen hores múltiples de 3 (sessions de 3 h).
> Actualitzat el 2026-09-14: competències avaluables per bloc, avaluació,
> metodologia i fitxes completes de les UT1-UT11.

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

## 4. Competències avaluables i mapa amb les UT

La programació s'organitza en **vuit competències avaluables**, una per bloc
tècnic. Totes es tornen a avaluar al projecte de la UT10. El pes és el de la
pestanya Avaluació.

| Competència avaluable | Comp. BOE | RA | UT | Pes |
|---|---|---|---|---|
| Entrenar i avaluar models de regressió lineal i polinòmica i les seves mètriques | i | 3, 4, 5 | 1, 2, 10 | 15% |
| Detectar i interpretar i preparar correlacions entre variables per a l'entrenament de models | g | 1, 3 | 3, 10 | 10% |
| Entrenar i avaluar models de classificació: regressió logística i k-NN i les seves mètriques | i | 3, 4, 5 | 4, 10 | 15% |
| Entrenar i avaluar Arbres de decisió i mètodes d'ensemble, com els Random Forests i veure'n les seves mètriques. | i | 3, 4, 5 | 5, 10 | 15% |
| Entrenar i avaluar Màquines de suport vectorial (SVM) | i | 3, 4, 5 | 6, 10 | 15% |
| Validar de forma creuada els models en entrenament i ajustar els seus hiperparàmetres per mesurar la robustesa | j | 4, 5 | 7, 10 | 10% |
| Entrenar models d'aprenentatge no supervisat: k-means i mixtures gaussianes | i | 3, 4, 5 | 8, 10 | 15% |
| Reduir la dimensió de les mostres per a millorar els models de ML i representar gràficament les dades | h | 2 | 9, 10 | 5% |

**Competències professionals del BOE** a què es vinculen:

- g) Cercar, amb anterioritat a l'entrenament, correlacions entre les variables mitjançant eines estadístiques i d'aprenentatge automàtic.
- h) Reduir la dimensió de les mostres dels conjunts de dades, mitjançant programació o eines de programari, visualitzant-les mitjançant eines gràfiques, amb la finalitat de corroborar les correlacions trobades i verificant la reducció.
- i) Dissenyar models basats en aprenentatge automàtic (machine learning, ML) per aplicar-los sobre el conjunt de dades amb l'objecte d'abordar el problema plantejat segons el seu tipus, de regressió o de classificació.
- j) Avaluar els models dissenyats mitjançant subconjunts de test, creant noves particions de validació i entrenament.

Aplicables a totes les files:

- k) Adaptar-se a les noves situacions laborals originades per canvis tecnològics i organitzatius en la seva activitat laboral.
- l) Complir les tasques pròpies del seu nivell amb autonomia i responsabilitat, efectuant-les de manera individual o com a membre d'un equip de treball.
- m) Comunicar-se eficaçment, respectant l'autonomia i la competència de les persones que intervenen al seu àmbit de treball.
- n) Complir les normes de qualitat, accessibilitat universal i disseny per a totes les persones que afecten la seva activitat professional.
- ñ) Actuar amb esperit emprenedor i iniciativa personal en l'elecció o l'aplicació dels procediments de la seua activitat professional.
- o) Exercir els seus drets i complir les obligacions derivades de la seva activitat professional, d'acord amb allò establert a la legislació vigent, participant activament a la vida econòmica, social i cultural.

**Competències transversals**

- **CS1.** Comunicar-se eficaçment i treballar en equip respectant l'autonomia i la competència de les persones
- **CS2.** Complir les normes de qualitat, accessibilitat universal i la normativa de protecció de dades i propietat intel·lectual
- **CPe1.** Actuar amb autonomia, responsabilitat, iniciativa i esperit emprenedor en la resolució de problemes
- **CPe2.** Adaptar-se als canvis tecnològics i organitzatius mitjançant l'aprenentatge continu

## 5. Distribució de les unitats de treball

| UT | Títol | Aval | Hores |
|---|---|---|---|
| 1 | Entorn de treball i primer model de principi a fi | 1a | 9 |
| 2 | Regressió lineal i polinòmica | 1a | 18 |
| 3 | Correlacions i preparació de variables | 1a | 15 |
| 4 | Classificació: regressió logística i k-NN. Mètriques | 1a | 18 |
| 5 | Arbres de decisió i mètodes d'ensemble. Random Forests | 1a | 18 |
| 6 | Màquines de suport vectorial (SVM) | 1a | 12 |
| 7 | Validació creuada, ajust d'hiperparàmetres i robustesa | 2a | 18 |
| 8 | Aprenentatge no supervisat: k-means i mixtures gaussianes | 2a | 15 |
| 9 | Reducció de la dimensió i representació gràfica | 2a | 15 |
| 10 | Projecte transversal d'inici a fi | 2a | 27 |
| 11 | FEMPO | 3a | 55 |
| | **Total** | | **220** |

Lectives (UT1-UT10): 165 h. FEMPO: 55 h.

## 6. Fils que travessen tot el mòdul

- **El test segellat.** A la **UT2** (NB 2.2) s'aparten els anys 2024 i 2025 de les
  dades d'AEMET (un 18%) com a test i no
  s'obre fins a la **UT10**, en classe, comparant l'estimació de validació amb el
  resultat real.
- **La fuga d'informació.** Se sembra a la UT1 (per què predim demà i no avui),
  té el seu cas trampa a la UT7 (validació creuada) i es formalitza a la UT9
  (ajustar transformacions només amb entrenament, `Pipeline`).
- **La desconfiança de les mètriques.** El model de referència (`Dummy*`) apareix
  ja a la UT1 i el desbalanç de classes es tanca a la UT4.
- **Pont amb el mòdul 5149.** Les xarxes neuronals (MLP inclòs), els
  autocodificadors i PyTorch són del 5149. Aquest mòdul no en fa cap UT.

## 7. Sistema d'avaluació

**Instruments** (iguals per a cada competència):

| Instrument | % |
|---|---|
| Exàmens o proves específiques (teòrics o pràctics) | 40 |
| Pràctiques individuals o en grup | 50 |
| Exercicis (dels que siguin avaluables) | 10 |

**Procediments d'avaluació i criteris de qualificació**

La primera convocatòria s'avaluarà amb els següents instruments de qualificació:

- Exàmens: 40%
- Pràctiques puntuables: 50%
- Exercicis de seguiment: 10%

És necessari aprovar els exàmens amb una nota de 5 o superior per poder fer mitjana i, per tant, superar el mòdul. Aquesta condició és independent de que s'aprovin les pràctiques i els exercisis. Si no s'han aprovat tots els exàmens la nota màxima a la que s'aspirarà serà un 4.

Es farà un mínim d'un examen per trimestre.

Les pràctiques entregades fora de plaç només aspiraran a un 5 com a màxim.

L'avaluació dels exercicis de seguiment és la d'entregat (10), entregat parcialment (5) fora de plaç o no entregat (0).

Cada competència té un pes percentual sobre el total del mòdul i la seva puntuació es calcula a partir dels percentatges dels seus instruments d'avaluació, com es mostra en la taula.

**Recuperació**

Durant l'avaluació ordinària es té dret a recuperar cada competència avaluable un sol cop mitjançant la recuperació la prova específica, exàmen o pràctica. L'alumne amb la competència aprovada pot presentar-se de nou amb el risc de baixar nota si la qualificació es menor.

**Avaluacions no ordinàries**

La nota de l'avaluació extraordinària sorgirà de l'examen global que qualificarà totes les competències descrites (90%) i la realització d'una bateria de tasques entregades prèviament (10%). Les dues parts han de ser superades amb mínim un 5 per poder superar la recuperació extraordinària.

> **Pendent al full.** A la pestanya Avaluació, la cel·la O40 (columna oculta i
> protegida) conté `=H40+#REF!`, restes de la plantilla. Només la pot corregir qui
> tingui permís sobre l'interval protegit.

## 7b. Metodologia

La dinàmica general serà la de introduïr la UT mitjançant una presentació de slides per plantejar un problema o una situació que el Machine Learning pot superar.
Llavors es treballarà sobretot amb Jupyter Notebooks disponibles en GitHub o google drive. Aquests serviran tant per les explicacions dels conceptes, l'execució de codi i el plantejament d'exercicis i reflexions.
Seguidament els alumnes podran treballar en els exercicis proposats en el mateix ecosisitema usat per la classe magistral.
Els jupyter notebooks es podran executar en Googe Colab (on les llibreries de python, pandas, numpy, matplotlib, scikitlearn, etc... estan pre-instal·lades) o en un entorn local o en el servidor del centre amb Jupyter Lab.

**Recursos i materials**

HARDWARE:
- Ordinador de sobretaula (o portàtil si l'alumne disposa d'ell) equipat amb tarja gràfica suficient per poder executar certs algorismes i llibreries de processament gràfic.

SOFTWARE:
- Accés a Google Classroom i tot el material proporcionat pel professor.
- Accés a Goolge Colab
- Python y les seves llibreries
- Jupyter Lab
- Accés al servidor del centre proporcionat per a l'entrenament de models o execució d'ells.

**Normes**

- Assistència i puntualitat: es registren a cada sessió; les faltes injustificades poden comportar la pèrdua del dret a l'avaluació contínua segons el ROF del centre.
- Ús de dispositius: els equips de l'aula i els portàtils propis s'usen exclusivament per a les tasques del mòdul; el mòbil roman guardat, excepte per a l'autenticació de dos factors.
- Lliuraments: al repositori Git i a l'aula virtual abans de la data límit..
- IA generativa: ús permès com a assistent i declarat en cada lliurament; prohibit en les proves individuals; l'alumnat ha de poder explicar tot el codi que lliura.
- Respecte i col·laboració: llenguatge respectuós a l'aula i en els comentaris de revisió de codi; els conflictes dins les parelles es comuniquen al professorat.
- Seguretat i dades: no es pugen credencials ni dades personals als repositoris; s'usen fitxers .env i .gitignore i dades anonimitzades.

L'apartat d'atenció a la diversitat és al full (pestanya Metodologia).

## 7c. Bibliografia

**Llibres**

- Géron, A. (2025). *Hands-On Machine Learning with Scikit-Learn and PyTorch: Concepts, Tools, and Techniques to Build Intelligent Systems*. O'Reilly Media.
- James, G., Witten, D., Hastie, T., Tibshirani, R. i Taylor, J. (2023). *An Introduction to Statistical Learning with Applications in Python*. Springer.
- Torres Viñals, J. (2020). *Python Deep Learning: Introducción práctica con Keras y TensorFlow 2*. Marcombo.
- Nielsen, M. A. (2015). *Neural Networks and Deep Learning*. Determination Press.

**Pàgines web**

- Neural Networks and Deep Learning (M. A. Nielsen), llibre en línia: <http://neuralnetworksanddeeplearning.com/>
- An Introduction to Statistical Learning, edició en Python amb el llibre i els laboratoris: <https://www.statlearning.com/>

**Altres**

- Documentació oficial de scikit-learn (User Guide): <https://scikit-learn.org/stable/user_guide.html>
- Notebooks del llibre Python Deep Learning (J. Torres): <https://github.com/jorditorresBCN/python-deep-learning>

## 8. Fitxes de les unitats de treball

Cada fitxa recull la competència avaluable, els continguts, les activitats
d'aula, els criteris d'avaluació (amb la lletra del BOE), les activitats
complementàries i les observacions, tal com són al full.

---

### UT1 — Entorn de treball i primer model de principi a fi
**Aval.** 1a · **Hores.** 9 · **Competència.** Entrenar i avaluar models de regressió lineal i polinòmica i les seves mètriques

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

- RA4.a (inici) Es distingeix el tipus de problema plantejat (regressió, classificació o no supervisat) i s'hi associa una tècnica d'aprenentatge automàtic adequada.
- RA4.b (inici) S'entrena un primer model programant el codi amb `fit`, `predict` i `score`.
- RA5.a (inici) Es divideix el conjunt en entrenament i test i el test s'usa només per avaluar el model.
- RA3.a (inici) Es generen les primeres gràfiques de les dades per comprovar-ne el comportament abans d'entrenar.
- Es compara el model amb un model de referència (`Dummy`) abans de donar-lo per bo.

**Activitats complementàries**

- Configuració de Google Colab i accés al repositori de GitHub.
- Qüestionari inicial de Python, NumPy i Pandas (sense nota).

**Observacions**

- Unitat introductòria: s'avalua dins la competència de regressió (amb la UT2).
- Dades: AEMET (aeroport de Palma) o, com a alternativa, Palmer Penguins.
- Transversals: CPe2.

---

### UT2 — Regressió lineal i polinòmica
**Aval.** 1a · **Hores.** 18 · **Competència.** Entrenar i avaluar models de regressió lineal i polinòmica i les seves mètriques

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
- Es reserva el 20% de les dades com a test segellat, que no s'obrirà fins a la UT10.
- Exercici: triar la mètrica adequada per a una predicció de vendes setmanals i justificar-la.

**Criteris d'avaluació**

- RA4.a S'han triat les tècniques d'aprenentatge automàtic en base a l'anàlisi exploratòria i visual prèvia de les dades.
- RA4.b S'assagen els models programant codi per entrenar-los i comparant configuracions (variables d'entrada i grau del polinomi).
- RA4.e S'identifica la desviació percentual entre valors predits i reals en problemes de regressió.
- RA4.f S'avaluen els models amb les mètriques triades (MAE, RMSE i R2) i es decideix si cal redissenyar-los.
- RA3.a Es generen gràfiques (recta d'ajust, valors predits contra reals i residus) que verifiquen el comportament del model.
- RA5.a Es reserva un subconjunt de test d'entre el 10% i el 30% del conjunt, que només s'usa per avaluar.

**Activitats complementàries**

- Lectura guiada de la documentació de `LinearRegression`.
- Repte opcional: afegir variables dels dies anteriors.

**Observacions**

- Aquí es reserva el 20% de test segellat, que no s'obre fins a la UT10.
- Dades: AEMET (temperatura màxima de l'endemà).
- Transversals: CPe1.

---

### UT3 — Correlacions i preparació de variables
**Aval.** 1a · **Hores.** 15 · **Competència.** Detectar i interpretar i preparar correlacions entre variables per a l'entrenament de models

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
- Redacció del document de variables d'entrada, de sortida i correlacions trobades, amb histogrames i mapes de dispersió.

**Criteris d'avaluació**

- RA1.a S'han cercat correlacions entre variables, tant lineals com no lineals.
- RA1.b S'apliquen procediments de categorització i codificació de variables, com els one-hot vectors.
- RA1.c S'apliquen les transformacions matemàtiques adequades a la distribució de cada variable.
- RA1.d Se seleccionen les variables d'entrada amb més correlació amb la variable objectiu.
- RA1.e Es redacta un document amb les variables d'entrada i sortida i les correlacions trobades.
- RA3.a Es generen gràfiques (mapa de calor i diagrames de dispersió) que verifiquen les correlacions i les transformacions aplicades.
- RA3.c Es recullen les gràfiques en un informe amb histogrames i mapes de dispersió.

**Activitats complementàries**

- Cerca al catàleg de dades obertes de l'IBESTAT.
- Lectura: correlacions espúries i causalitat.

**Observacions**

- Dades: AEMET (numèric), directori d'empreses IBESTAT (categòric) i pingüins.
- El document de correlacions es reutilitza a la UT5 i a la UT10.
- Transversals: CS2 (llicències de dades obertes i protecció de dades).

---

### UT4 — Classificació: regressió logística i k-NN. Mètriques
**Aval.** 1a · **Hores.** 18 · **Competència.** Entrenar i avaluar models de classificació: regressió logística i k-NN i les seves mètriques

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
- RA3.a Es generen gràfiques (frontera de decisió, matriu de confusió i corba ROC) que verifiquen el comportament dels models.
- RA5.b Es fa una partició estratificada que conserva la distribució de classes entre entrenament i validació.
- Es justifica per escrit l'elecció de la mètrica en un cas de classes desbalancejades.

**Activitats complementàries**

- Debat: quan és pitjor un fals negatiu que un fals positiu (diagnòstic mèdic, frau, correu brossa).

**Observacions**

- Dades: AEMET, «demà plou» (13,47% de dies de pluja, desbalanç real).
- El model `Dummy` de la UT1 desmunta l'accuracy amb classes desbalancejades.
- Transversals: CS1 (debat en grup).

---

### UT5 — Arbres de decisió i mètodes d'ensemble. Random Forests
**Aval.** 1a · **Hores.** 18 · **Competència.** Entrenar i avaluar Arbres de decisió i mètodes d'ensemble, com els Random Forests i veure'n les seves mètriques.

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
- RA4.c S'identifiquen combinacions de paràmetres com la profunditat màxima o el nombre d'arbres a generar.
- RA4.g S'inclouen comentaris al codi per poder reutilitzar-lo en problemes similars.
- RA3.d S'explica la gràfica d'importància de variables i se'n fa una valoració comparant-la amb les correlacions de la UT3.
- RA5.b Es comparen els resultats d'entrenament i validació per detectar el sobreajust en variar la profunditat.
- Es justifica la tria entre un model interpretable i un altre de més precís.

**Activitats complementàries**

- Repte opcional: `HistGradientBoosting` contra el random forest.

**Observacions**

- La importància de variables es contrasta amb les correlacions de la UT3.
- El gradient boosting només com a idea general, sense matemàtiques.
- Transversals: CPe1.

---

### UT6 — Màquines de suport vectorial (SVM)
**Aval.** 1a · **Hores.** 12 · **Competència.** Entrenar i avaluar Màquines de suport vectorial (SVM)

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
- RA4.b S'assagen els models fent experiments amb distintes combinacions de paràmetres (nucli, C i gamma).
- RA4.f S'avaluen els models i es decideix si cal redissenyar-los.
- RA3.a Es generen gràfiques de les fronteres de decisió que verifiquen l'efecte dels paràmetres.
- RA5.b Es fa servir un subconjunt de validació per triar C i gamma sense tocar el test.
- Es justifica en quins escenaris un SVM és preferible a un model basat en arbres.

**Activitats complementàries**

- Taula compartida de resultats: SVM, arbre i random forest (es reprèn a la UT7 amb validació creuada).

**Observacions**

- El SVM és sensible a l'escala: es reprèn l'escalat de la UT3.
- Tanca la 1a avaluació; la cerca de C i gamma es formalitza a la UT7.
- Transversals: CS1 (posada en comú de resultats).

---

### UT7 — Validació creuada, ajust d'hiperparàmetres i robustesa
**Aval.** 2a · **Hores.** 18 · **Competència.** Validar de forma creuada els models en entrenament i ajustar els seus hiperparàmetres per mesurar la robustesa

**Continguts**

1. **Particions d'entrenament, validació i test** — Test entre el 10% i el 30% del conjunt. Partició estratificada que conserva la distribució de classes.
2. **Validació creuada** — K iteracions i variant estratificada. Repetició del procés complet per partició, amb el preprocessat ajustat dins de cada partició.
3. **Cerca d'hiperparàmetres** — Cerca en graella i cerca aleatòria. En quina iteració es desa la versió del model.
4. **Corbes d'aprenentatge** — Diagnòstic de si convé més dades o bé un model distint.
5. **Mitjana, variància i robustesa** — Mitjana aritmètica i variància de les mètriques entre particions com a mesura de robustesa.

**Activitats d'aula**

- **NB 7.1.** Partició estratificada i comprovació que es manté la distribució de classes.
- **NB 7.2.** Validació creuada sobre els models de les UT anteriors, amb taula de mitjana i variància.
- **NB 7.3.** Cerca d'hiperparàmetres amb graella sobre el millor model fins ara.
- Exercici de robustesa: triar entre un model amb millor mitjana i pitjor variància i un altre més estable.
- Cas trampa: un conjunt amb un R2 massa bo per ser cert; localitzar la fuga d'informació.

**Criteris d'avaluació**

- RA5.a Es divideix el conjunt en entrenament i test, amb el test entre el 10% i el 30%.
- RA5.b Es torna a dividir en entrenament i validació conservant la mateixa distribució de classes.
- RA5.c Es duu a terme la validació creuada generant distintes particions i repetint el procés complet per a cadascuna.
- RA5.d Es decideix en quina iteració es desa la versió del model a avaluar amb el test.
- RA5.e S'avalua amb el subconjunt de test mostrant la mitjana i la variància de les mètriques.
- RA4.b S'assagen els models amb cerca en graella i cerca aleatòria d'hiperparàmetres.
- RA4.c S'identifiquen les combinacions de paràmetres que donen millors resultats.

**Activitats complementàries**

- Lectura: guia de scikit-learn de validació creuada i cerca d'hiperparàmetres.

**Observacions**

- S'avança a l'inici de la 2a avaluació: és la base per avaluar la resta de models.
- Cas trampa: despesa dels creuers (IBESTAT). Pingüins: cal `shuffle`.
- Transversals: CPe1 (esperit crític davant resultats massa bons).

---

### UT8 — Aprenentatge no supervisat: k-means i mixtures gaussianes
**Aval.** 2a · **Hores.** 15 · **Competència.** Entrenar models d'aprenentatge no supervisat: k-means i mixtures gaussianes

**Continguts**

1. **Agrupament sense variable objectiu** — Diferència amb l'aprenentatge supervisat. Casos d'ús reals.
2. **K-means** — Centroides, assignació de mostres i iteracions de l'algorisme.
3. **Elecció del nombre de grups** — Mètode del colze i coeficient de silueta.
4. **Mixtures de gaussianes** — Assignació probabilística contra assignació dura. Grups de forma no esfèrica.
5. **Altres enfocaments d'agrupament** — DBSCAN i agrupament per densitat, a nivell introductori.

**Activitats d'aula**

- **NB 8.1.** K-means en dues dimensions, amb els centroides dibuixats a cada iteració.
- **NB 8.2.** Colze i silueta per decidir el nombre de grups.
- **NB 8.3.** Mixtures de gaussianes sobre grups allargats on k-means falla.
- Exercici de segmentació: agrupar un conjunt real i descriure amb paraules cada grup obtingut.
- Exercici d'estabilitat: repetir k-means amb distintes llavors i subconjunts i comparar la silueta.

**Criteris d'avaluació**

- RA4.a S'han triat tècniques com els models de mixtures de gaussianes en base a l'anàlisi previ.
- RA4.c S'identifica el nombre de grups (clusters) adequat per a l'algorisme k-means.
- RA4.h Es genera documentació amb els models dissenyats i les seves variants.
- RA3.a Es generen gràfiques (colze, silueta i grups acolorits) que verifiquen l'agrupament obtingut.
- RA5.e Es mostren la mitjana i la variància de la silueta en repetir l'agrupament amb distintes llavors i particions.
- Es descriuen amb llenguatge natural els grups obtinguts i la seva utilitat.

**Activitats complementàries**

- Posada en comú: cada parella presenta la seva segmentació en dos minuts.

**Observacions**

- Dades: directori d'empreses de l'IBESTAT (municipis o sectors).
- DBSCAN només a nivell introductori.
- Transversals: CS1 (exposició oral breu).

---

### UT9 — Reducció de la dimensió i representació gràfica
**Aval.** 2a · **Hores.** 15 · **Competència.** Reduir la dimensió de les mostres per a millorar els models de ML i representar gràficament les dades

**Continguts**

1. **El problema de les moltes dimensions** — Variables latents i per què convé reduir. Cost i pèrdua d'informació.
2. **Anàlisi de components principals (PCA)** — Variància explicada, nombre de components i lectura dels loadings.
3. **Reducció no lineal amb t-SNE** — Perplexitat, caràcter no determinista i ús només exploratori.
4. **Representació gràfica dels resultats** — Histogrames, mapes de dispersió i gràfiques de components acolorides per la classe.
5. **Pipelines i fuita d'informació** — Ajust de la transformació només amb entrenament. Encapsulat amb `Pipeline`.

**Activitats d'aula**

- **NB 9.1.** PCA amb corba de variància acumulada i tria del nombre de components.
- **NB 9.2.** PCA contra t-SNE sobre el mateix conjunt, amb les dues projeccions comparades.
- **NB 9.3.** Repetir t-SNE amb distintes perplexitats i dues execucions per valor.
- Exercici d'error induït: notebook amb el PCA ajustat abans de partir les dades; localitzar-lo i corregir-lo.
- Els autocodificadors es tracten al mòdul 5149.

**Criteris d'avaluació**

- RA2.a S'utilitzen tècniques de reducció de la dimensió com PCA i t-SNE.
- RA2.b Es programen procediments que creen una còpia del conjunt amb les transformacions aplicades.
- RA2.c S'apliquen les transformacions durant l'entrenament, abans que les mostres entrin al model, encapsulades en un `Pipeline`.
- RA2.d Es documenten les tècniques aplicades, els valors dels paràmetres de configuració i els resultats obtinguts.
- Es comprova amb gràfiques de components acolorides per la classe que la reducció conserva la informació rellevant.

**Activitats complementàries**

- Exploració de projeccions PCA i t-SNE amb l'Embedding Projector de TensorFlow.

**Observacions**

- Els autocodificadors del RA2.a es treballen al mòdul 5149.
- El `Pipeline` connecta amb el preprocessat de la validació creuada (UT7).
- Transversals: CPe2.

---

### UT10 — Projecte transversal d'inici a fi
**Aval.** 2a · **Hores.** 27 · **Competència.** Validar de forma creuada els models en entrenament i ajustar els seus hiperparàmetres per mesurar la robustesa / Detectar i interpretar i preparar correlacions entre variables per a l'entrenament de models / Reduir la dimensió de les mostres per a millorar els models de ML i representar gràficament les dades

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

- RA1.e Es redacta el document de variables d'entrada i sortida i les correlacions trobades.
- RA4.g S'inclouen comentaris al codi que en permeten la reutilització.
- RA4.h Es genera la documentació dels models dissenyats amb totes les seves variants.
- RA5.f Es crea un informe d'avaluació amb gràfiques i taules que comparen rendiment i robustesa.
- RA3.b S'elabora el material de presentació per exposar-lo a l'equip de treball.
- RA3.d S'explica l'obtenció de les gràfiques aportant una valoració de cadascuna.
- Es valora la coherència entre les decisions preses i els resultats obtinguts.

**Activitats complementàries**

- Jornada de presentació dels projectes oberta a l'alumnat del cicle.

**Observacions**

- Avalua totes les competències (totes inclouen la UT10); aquí se'n marquen 3.
- Dades de lliure elecció: IBESTAT o datos.gob.es.
- Transversals: CS1, CS2 i CPe1.

---

### UT11 — FEMPO
**Aval.** 3a · **Hores.** 55

**Continguts**

1. **Incorporació a l'empresa** — Acollida, normes de funcionament, seguretat i protecció de dades de l'entitat.
2. **Pla de formació** — Activitats formatives acordades entre el centre i l'empresa i vinculades als RA del mòdul.
3. **Preparació de dades en un entorn real** — Exploració, neteja i anàlisi de correlacions sobre dades de l'empresa, respectant la confidencialitat.
4. **Entrenament i avaluació de models** — Participació en el disseny, l'entrenament i la validació de models dins dels projectes de l'empresa.
5. **Documentació i comunicació** — Registre del treball fet i presentació de resultats a l'equip de l'empresa.

**Activitats d'aula**

- Estada a l'empresa segons el calendari de la formació en empresa (55 h).
- Quadern de seguiment setmanal amb les tasques realitzades i les dificultats trobades.
- Reunions de seguiment entre la persona tutora del centre, la persona tutora de l'empresa i l'alumne.
- Memòria final de l'estada amb un cas de model entrenat o avaluat a l'empresa.

**Criteris d'avaluació**

- Les activitats a l'empresa s'avaluen conjuntament amb la persona tutora de l'empresa, d'acord amb el pla de formació.
- Es valoren la preparació de dades i l'entrenament i l'avaluació de models en un context real (RA1, RA4 i RA5, segons les tasques assignades).
- Es compleixen les normes de l'empresa, de seguretat i de protecció de dades (CS2).
- Es mostra autonomia, responsabilitat i capacitat d'adaptació als canvis tecnològics i organitzatius (CPe1 i CPe2).

**Activitats complementàries**

- Sessió prèvia al centre: normes, confidencialitat i quadern de seguiment.

**Observacions**

- 3a avaluació, un cop acabada la formació al centre (a partir del 10/05/2027).
- Cap competència de la pestanya Competències inclou la UT11: els RA avaluats els fixa el pla de formació de cada alumne.

## Enllaços

- Programació didàctica (full de càlcul): <https://docs.google.com/spreadsheets/d/1kRky2w5RGnG40Qe27uaFpq4O2stqnw7iQXRHhwESrek/edit>
- Normativa: BOE-A-2026-5869
