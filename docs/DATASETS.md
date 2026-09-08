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
