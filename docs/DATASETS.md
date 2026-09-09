# Datasets del MP 5134

## Criteri de tria

Es busquen conjunts amb **dades mesurades, no imputades ni ponderades**, prou
grans per entrenar, i amb variables que l'alumnat pugui interpretar sense
context extern. Un conjunt on la variable objectiu s'ha calculat amb una fórmula
a partir de les altres columnes no serveix per aprendre: qualsevol model
n'obté un ajust perfecte que no significa res.

## Els triats

### Principal (UT1-UT10) — AEMET, estació B278 (aeroport de Palma)

`UT01-Entorn_de_treball_primer_model/aemet/meteo_palma.csv`

Mesures diàries reals publicades per l'AEMET. Generat amb un script propi que
consulta l'API d'AEMET (cal una clau gratuïta; l'alumnat no la necessita, ja que
carrega el CSV per URL).

- **4.017 files**, del 2015-01-01 al 2025-12-30. Una fila = un dia.
- **16 columnes.**
- Valors absents: pràcticament cap — `velmedia` (5), `sol` (4), `racha` (2).
  4.006 files completes.

| Columna | Què és |
|---|---|
| `fecha` | data del dia |
| `any`, `mes`, `dia_any` | variables de calendari |
| `tmed`, `tmin`, `tmax` | temperatura mitjana, mínima i màxima (°C) |
| `prec` | precipitació (mm) |
| `velmedia`, `racha` | vent mitjà i ratxa màxima (m/s) |
| `sol` | hores de sol |
| `presMax`, `presMin` | pressió màxima i mínima (hPa) |
| `tmax_dema` | **objectiu de regressió**: temperatura màxima del dia següent |
| `prec_dema` | precipitació del dia següent |
| `plou_dema` | **objectiu de classificació**: 1 si demà plou, 0 si no |

**Per què aquest.** És l'únic candidat que dona **regressió i classificació sobre
les mateixes files** amb dades mesurades. El desbalanç de classes és real
(**13,47% de dies de pluja**, 86,53% de dies sense) i serveix de material per a
la UT4. I les correlacions són intuïtives per a qualsevol que visqui aquí.

**Decisió de disseny important:** les variables objectiu són **del dia següent**.
Predir la `tmax` d'avui a partir de la `tmed` i la `tmin` d'avui seria un
exercici buit — estan lligades gairebé per definició — i qualsevol model
encertaria sempre. Amb l'objectiu desplaçat un dia hi ha senyal, però no és
perfecta: exactament el que cal per poder comparar algorismes.

### Secundari (UT3 i UT7) — Directori d'empreses amb activitat econòmica (IBESTAT)

Desenes de milers de registres reals amb sector CNAE, municipi, tram
d'assalariats i forma jurídica.

**Per què.** El fitxer meteorològic és gairebé tot numèric, i això deixa la
**UT3 coixa en codificació de variables categòriques i one-hot**, que són
criteris avaluables (RA1.b). El directori d'empreses és exactament el contrari:
tot categòric. Es complementen. A més serveix per al clustering de la **UT7**,
on agrupar municipis o sectors dona grups que l'alumnat pot interpretar.

### Alternativa per a la UT1 — Palmer Penguins

`UT01-Entorn_de_treball_primer_model/penguins/penguins.csv`

Mesures de camp de **344 pingüins** de tres illes de l'arxipèlag Palmer
(Antàrtida), preses entre 2007 i 2009 per la Palmer Station LTER. Dades de
Gorman, Williams i Fraser (2014), distribuïdes al paquet
[palmerpenguins](https://allisonhorst.github.io/palmerpenguins/) amb llicència
CC0. En tenim una còpia al repositori perquè els notebooks no depenguin d'un
projecte extern el dia de classe.

8 columnes: `species`, `island`, `bill_length_mm`, `bill_depth_mm`,
`flipper_length_mm`, `body_mass_g`, `sex`, `year`.

**Què aporta que AEMET no té:**

- **Cap a la pantalla.** 344 files es poden projectar senceres. Per a una unitat
  el lema de la qual és mirar les dades abans de tocar-les, això no és una
  limitació sinó el motiu.
- **Valors absents que es poden comptar amb el dit.** Onze files: dos pingüins
  sense cap mesura i nou als quals no consta el sexe. Es veuen d'un cop amb
  `df[df.isna().any(axis=1)]`.
- **Tres columnes categòriques** (espècie, illa, sexe), que és justament el que
  falta a AEMET, i que deixen sembrat el one-hot de la UT3.
- **La lliçó contrària a la d'AEMET.** L'arbre encerta el 94% contra un
  `DummyClassifier` del 51%: aquí el model sí que guanya la referència. Amb AEMET
  passa el revés. Posar les dues coses seguides és el que fixa la idea que la
  referència és una comparació, no un veredicte.
- **La paradoxa de Simpson servida.** La correlació entre llargada i gruix del
  bec és **−0,235** al conjunt sencer i **positiva dins de cada espècie** (+0,39
  Adelie, +0,65 Chinstrap, +0,64 Gentoo). Material directe per a la UT3.

**Dues advertències, totes dues aprofitables com a material:**

1. **El fitxer està ordenat per espècie** (primer tots els Adelie, després els
   Gentoo, després els Chinstrap). `train_test_split` barreja per defecte i els
   notebooks de la UT1 són segurs, però una validació creuada sense `shuffle=True`
   dona resultats absurds: R2 de **−0,818** en comptes de 0,744, i accuracy de
   0,730 en comptes de 0,959. És un accident real i molt bo per a la UT10.
2. **Amb 344 files, la mesura balla.** Sobre 200 particions distintes, el R2 de
   la regressió va de 0,579 a 0,846 (desviació 0,043); amb AEMET, de 0,877 a
   0,911 (desviació 0,007). La corba d'aprenentatge, però, s'aplana a partir de
   120 mostres: **el model no necessita més dades, la mesura sí**. És l'argument
   de la validació creuada de la UT10, i el NB 1.2 ja el deixa plantat.

**Descartada la versió "extended" de Kaggle.** Circula una ampliació a ~3.400
files amb columnes de dieta, etapa vital i estat de salut. És **artificial**: la
generà un notebook, els anys són 2021-2025 (l'estudi real és de 2007-2009) i les
mesures no respecten la biologia — hi ha Adelie de 6.800 g amb aletes de 270 mm
quan els reals no passen de 4.775 g ni de 210 mm. A més, `health_metrics` es
calcula a partir de la massa, l'etapa i l'espècie, o sigui el mateix problema de
columna derivada que els creuers. Serviria, com a molt, com a exercici de
detecció de dades falses.

### Cas trampa (UT10) — Despesa dels creuers (IBESTAT)

CSV directe i sense clau, quatre anys disponibles.

**No val com a conjunt d'entrenament**, i aquest és precisament el seu valor
didàctic: les columnes `GASTO_TURISTICO_*` **no són respostes reals, són valors
imputats**. Es repeteixen idèntics en centenars de files (`484,10676854` apareix
una vegada i una altra) perquè es calculen amb una fórmula a partir del país de
residència, les nits i el tipus d'allotjament. Un arbre de decisió reconstrueix
la fórmula i dona un R2 de 0,99.

S'entrega **sense avisar** i l'alumnat ha de descobrir per què el resultat és
massa bo per ser cert. És el millor exemple real de fuga d'informació que hem
trobat, i a sobre és local.

### UT11 — Elecció lliure

Cada parella tria el seu conjunt del catàleg d'IBESTAT o de datos.gob.es. Aquí
el rigor el posa el projecte.

## Els descartats, i per què

- **Flux de turistes (FRONTUR, IBESTAT).** Volum de sobres (11 MB el fitxer de
  2018), però només 16 columnes i totes són codis opacs del tipus `A0_7x`,
  `A7_1_2x`. Sense el fitxer de disseny de registre no signifiquen res, i
  descodificar-los es menjaria mitja UT3. Sobretot: **no hi ha cap variable
  contínua que serveixi d'objectiu**. L'única decimal és `Factor`, que és el pes
  mostral de l'enquesta, no una dada del turista; fer-la servir com a objectiu
  seria un error metodològic greu i difícil de detectar.
- **Enquesta modular d'hàbits socials (IBESTAT).** Variables mixtes molt riques,
  però és del 2010 i a l'alumnat li sonarà antiga.
- **Portal de dades obertes de Palma.** L'ajuntament no té un catàleg comparable
  al de Barcelona; no hi ha res aprofitable.

> Sobre el catàleg d'IBESTAT: els 14.338 conjunts enganyen. La immensa majoria
> són taules estadístiques agregades de poques desenes de files, que serveixen
> per fer gràfics però no per entrenar. Els que serveixen són els **microdades**,
> i d'aquests IBESTAT només en publica quatre operacions — les quatre revisades
> aquí.

## California Housing (material alternatiu)

A `UT01-Entorn_de_treball_primer_model/california_housing/` hi ha una versió
paral·lela dels notebooks de la UT1 amb el conjunt clàssic de California
Housing (`ageron/handson-ml2`), com a alternativa al d'AEMET.
