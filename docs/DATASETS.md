# Datasets del MP 5134

## Criteri de tria

Es busquen conjunts amb **dades mesurades, no imputades ni ponderades**, prou
grans per entrenar, i amb variables que l'alumnat pugui interpretar sense
context extern. Un conjunt on la variable objectiu s'ha calculat amb una fórmula
a partir de les altres columnes no serveix per aprendre: qualsevol model
n'obté un ajust perfecte que no significa res.

## Els triats

### Principal (UT1-UT9) — AEMET, estació B278 (aeroport de Palma)

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

### El test segellat (des de la UT2)

Al NB 2.2 s'aparten **els anys 2024 i 2025** (730 dies, un 18%) com a test
segellat. No s'obren fins a la UT10. Tots els notebooks que fan servir AEMET a
partir de la UT2 comencen filtrant `fecha < "2024-01-01"`.

El NB 2.2 fa el tall i l'anuncia en quatre línies; **el perquè de fons s'explica
al final del NB 2.3** (secció 8), un cop l'alumnat ha triat el grau del polinomi
mirant la validació i pot entendre que cada decisió presa així fa la validació
una mica optimista. Explicar-ho abans, al primer contacte amb les dades, era
massa abstracte.

Es talla **per dates i no a l'atzar** per dos motius: el model s'ha de fer servir
per predir dies futurs, i dos dies seguits s'assemblen tant que una partició
aleatòria posaria a l'entrenament el dia abans de cada dia de prova. Per
comparar models abans de la UT7 es fa servir **2015-2021 per entrenar i 2022-2023
per validar**.

### Ús a la UT2

- **NB 2.1 (regressió simple): pingüins**, llargada de l'aleta contra massa. Amb
  342 punts la recta es veu sobre el núvol i el pendent es llegeix en veu alta
  (uns 50 g per mm).
- **NB 2.2 (regressió múltiple): AEMET**, `tmax_dema`. És el primer contacte de
  l'alumnat amb AEMET (la UT1 es fa amb pingüins), així que el notebook presenta
  el fitxer, les columnes i per què es prediu *demà* i no *avui* (primera
  aparició de la fuga d'informació). La primera variable fa
  gairebé tota la feina (MAE de 5,8 °C amb la mitjana, 1,61 °C amb `tmax`) i les
  nou següents només baixen set centèsimes. La persistència (*demà igual que
  avui*, 1,64 °C) fa de referència exigent.
- **NB 2.3 (polinòmica i sobreajust): AEMET**, `tmed` contra la fracció de l'any.
  Amb 15 dies de mostra, el grau 4 dóna 2,7 °C a validació i el grau 15, més de
  70 °C (arriba a predir més de 3.000 °C al desembre). Amb tots els dies
  d'entrenament, el grau 15 torna a ser raonable.

### Secundari (UT3 i UT8) — Directori d'empreses amb activitat econòmica (IBESTAT)

Desenes de milers de registres reals amb sector CNAE, municipi, tram
d'assalariats i forma jurídica.

**Per què.** El fitxer meteorològic és gairebé tot numèric, i això deixa la
**UT3 coixa en codificació de variables categòriques i one-hot**, que són
criteris avaluables (RA1.b). El directori d'empreses és exactament el contrari:
tot categòric. Es complementen. A més serveix per al clustering de la **UT8**,
on agrupar municipis o sectors dona grups que l'alumnat pot interpretar.

**El fitxer.** `UT03-Correlacions_preparacio_variables/ibestat_empreses/empreses_balears.csv`,
fet amb `generar_empreses_balears.py` (a la mateixa carpeta) a partir del
**DIRCE-IB de 2024** que l'IBESTAT publica amb llicència CC-BY al seu catàleg de
dades obertes. 48.326 empreses i cinc columnes de text: `illa`, `municipi` (67),
`sector` (les 19 seccions de la CNAE-2009 amb nom català), `forma_juridica` (16,
deduïda de la lletra inicial del NIF) i `assalariats` (5 trams ordenats). El script
**treu el NIF i la raó social**: no calen, i serveixen per parlar de minimització de
dades al NB 3.3. El directori només inclou persones jurídiques; els autònoms no hi
surten. Al NB 3.3, la UT3 en fa servir el tram com a variable ordinal i el municipi
(de Palma, amb 14.483 empreses a l'entrenament, a Estellencs, amb 8) per agrupar
categories minoritàries.

L'antiga fitxa de datos.gob.es (`a04003003-empreses-amb-activitat-economica-illes-balears`)
dona 404 (octubre de 2026); el fitxer es troba cercant «dirceib» al catàleg de dades
obertes del Govern.

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
   0,730 en comptes de 0,959. És un accident real i molt bo per a la UT7.
2. **Amb 344 files, la mesura balla.** Sobre 200 particions distintes, el R2 de
   la regressió va de 0,579 a 0,846 (desviació 0,043); amb AEMET, de 0,877 a
   0,911 (desviació 0,007). La corba d'aprenentatge, però, s'aplana a partir de
   120 mostres: **el model no necessita més dades, la mesura sí**. És l'argument
   de la validació creuada de la UT7, i el NB 1.2 ja el deixa plantat.

**Descartada la versió "extended" de Kaggle.** Circula una ampliació a ~3.400
files amb columnes de dieta, etapa vital i estat de salut. És **artificial**: la
generà un notebook, els anys són 2021-2025 (l'estudi real és de 2007-2009) i les
mesures no respecten la biologia — hi ha Adelie de 6.800 g amb aletes de 270 mm
quan els reals no passen de 4.775 g ni de 210 mm. A més, `health_metrics` es
calcula a partir de la massa, l'etapa i l'espècie, o sigui el mateix problema de
columna derivada que els creuers. Serviria, com a molt, com a exercici de
detecció de dades falses.

### Cas trampa (UT7) — Despesa dels creuers (IBESTAT)

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

### UT10 — Elecció lliure

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

A `UT02-Regressio_lineal_polinomica/california_housing/` hi ha també la versió
California Housing del NB 2.2 i del NB 2.3. Diferències respecte a AEMET que
convé tenir presents:

- **Test segellat a l'atzar, no per dates.** No hi ha dates (és una fotografia
  del cens de 1990), així que el segell és `train_test_split(df, test_size=0.2,
  random_state=42)`. Aquest `random_state` és el pany: no es pot tocar mai. Els
  207 buits de `total_bedrooms` cauen tots al test segellat, cosa que tornarà a
  sortir a la UT10.
- **Referència de sentit comú:** el preu mitjà de cada `ocean_proximity`, en lloc
  de la persistència.
- **El NB 2.3 no prediu el preu.** Amb una sola entrada, el preu és massa sorollós
  per veure l'infraajust i el sobreajust (la latitud només baixa l'error d'un
  11%). Es fa servir el percentatge de dormitoris a partir de les habitacions per
  llar, una corba neta; la latitud contra el preu queda per a l'exercici 5.

## Demanda elèctrica de les Balears (versió alternativa del NB 2.3)

`UT02-Regressio_lineal_polinomica/demanda_electrica/demanda_balears.csv`

Demanda elèctrica diària del sistema balear (Mallorca-Menorca i
Eivissa-Formentera), publicada per **Red Eléctrica** a l'API pública REData, que
no demana clau. Cada dia porta, com a columnes, el temps que va fer a l'estació
B278 (aeroport de Palma). El genera `generar_demanda_balears.py`, a la mateixa
carpeta, que consulta l'API i llegeix `meteo_palma.csv`.

**És el NB 2.3 del camí pingüins → California Housing.** L'alumnat no ha treballat
mai amb AEMET, així que el notebook és un problema aïllat: no cita el fitxer AEMET
ni els seus notebooks, i quan fa referència a la regressió lineal ho fa al NB 2.2
de California Housing (les dues muntanyes de la latitud, les vuit variables, el
20% de districtes segellat). L'AEMET només surt com a font de les columnes del
temps.

- **4.017 files**, del 2015-01-01 al 2025-12-30. Una fila = un dia.
- Columnes: `fecha`, `any`, `mes`, `dia_any`, `cap_de_setmana` (1 dissabte i
  diumenge), `tmed`, `tmax`, `tmin` (°C), `prec` (mm), `sol` (h), `velmedia` (m/s)
  i `demanda` (GWh, de 9,6 a 27,5; uns 16 de mitjana).
- Buits: `sol` (4 dies) i `velmedia` (5 dies). Només afecten la secció 8, que els
  treu amb `dropna`.
- **Test segellat propi: 2024 i 2025**, per dates. Entrenament 2015-2021, validació
  2022-2023.

**Per què.** Per al NB 2.3 es buscava una relació on la recta fallés de debò, el
polinomi l'arreglés i el sobreajust sortís amb qualsevol mostra. La demanda contra
la temperatura dibuixa una **U**: les calefaccions a l'hivern i l'aire condicionat
i els turistes a l'estiu. El consum mínim és entre 13 i 16 °C.

| Model (demanda ~ `tmed`) | MAE validació | R2 validació |
|---|---|---|
| Consum mitjà | 3,02 GWh | — |
| Recta | 2,11 GWh | 0,53 |
| Grau 2 | 1,20 GWh | 0,84 |

Amb 15 dies (`random_state=2`, cap dia per sota dels 10 °C) la vall de validació
cau al grau 2 (1,54 GWh) i el grau 15 dóna més de 40.000 GWh d'error. Sobre 40
mostres de 15 dies, el millor grau va del 2 al 6. El grau 12 es desboca sempre
(com a mínim 13 GWh d'error) i el grau 8, gairebé sempre (31 GWh de mediana).

**La secció 8, amb totes les variables** (`tmed`, `tmax`, `tmin`, `prec`, `sol`,
`velmedia`, `cap_de_setmana`, `dia_any`):

| Model | Columnes | MAE validació | R2 validació |
|---|---|---|---|
| Vuit variables, lineal | 8 | 2,00 GWh | 0,58 |
| + corba de la temperatura (grau 2) | 10 | 1,10 GWh | 0,86 |
| `PolynomialFeatures` grau 2 | 44 | 1,03 GWh | 0,88 |
| Grau 3 | 164 | 0,95 GWh | 0,89 |
| Grau 4 | 494 | 1,44 GWh | −4,36 |

El grau 4 sobreajusta amb i sense escalar les variables (comprovat amb
`MinMaxScaler`): no és un problema numèric. El R2 s'enfonsa per cinc dies amb
errors de més de 10 GWh, sobretot el 24 de maig del 2022 (52 mm de pluja amb gairebé
11 hores de sol, una combinació que no surt a l'entrenament), on prediu −220 GWh.
El notebook ho fa servir per explicar per què convé mirar el MAE i el R2 alhora.

**Advertències, totes aprofitades al notebook:**

- **El 2020** (confinament i estiu sense turistes) fa una franja de punts baixos.
  Es manté a l'entrenament i surt al debat. És també el motiu que, en gairebé tots
  els models, la validació surti millor que l'entrenament; el notebook ho explica
  a la secció 8.
- **La U només demana grau 2.** El grau 4 no millora la validació (1,18 GWh). Per
  veure que una forma més complexa demana més grau hi ha l'exercici 5: la demanda
  contra el dia de l'any necessita grau 6 (1,38 GWh).
- **Calor i turistes van junts** a l'estiu i el model no els pot separar. Es
  planteja al debat i enllaça amb la UT3.

**Diapositives.** La carpeta té també el deck de la UT2 per a aquest camí
(`UT2_regressio_lineal_REE.html` i el seu PDF). És el deck AEMET amb les
diapositives 3, 6, 8, 11 i 12 passades a California Housing (els exemples del
NB 2.2, la referència del preu mitjà de la zona, els trossos 60/20/20) i les 7, 9
i 10 refetes amb la demanda elèctrica.

**Candidats provats i descartats** amb el mateix protocol (R2 de validació de la
recta contra el millor polinomi, i sobreajust amb 15 mostres i 6 llavors):

- **Resistència dels iots** (UCI, canal de Delft): el salt més espectacular
  (0,59 → 0,99), però gairebé sense soroll i amb només 14 velocitats diferents. El
  grau 8 amb 15 mostres encara dóna 0,97: no hi ha sobreajust per ensenyar. El
  número de Froude, a més, és abstracte.
- **Gapminder** (esperança de vida contra PIB): millora fins al grau 6, però la
  forma és logarítmica i la pregunta *per què no `log(PIB)`?* és inevitable.
- **Peixos de Laengelmavesi** (pes contra llargada): la recta ja dóna 0,89-0,90.
- **Diamants** (preu contra quirats) i **Auto MPG**: el polinomi millora poc
  (0,85 → 0,87 i 0,63 → 0,73).
- **Bike Sharing** (Washington i Seül): massa soroll, i la tendència entre anys
  trenca una validació per dates.

## Picaporta (exercicis de consolidació UT1-UT2)

`UT02-Regressio_lineal_polinomica/consolidacio_picaporta/repartiments_manacor.csv`

Comandes del 2025 de **Picaporta**, una app de repartiment **inventada** que porta
menjar del centre de Manacor a Manacor, Son Macià, Porto Cristo, s'Illot i Cala
Murada. L'objectiu és `minuts_entrega`. Es fa servir als exercicis de consolidació de
la UT1 i la UT2, una sessió de pràctica autònoma a prop del format de l'examen.

**És l'única excepció al criteri de dades mesurades**, i és deliberada. Per a un
exercici d'examen calia un fitxer que l'alumnat no hagués vist, que s'entengués sense
context i on cada concepte de la UT1 i la UT2 tingués el seu lloc. El temps d'entrega
porta prou soroll perquè cap model no l'endevini: el millor model raonable es queda en
uns 3,5 minuts d'error. El notebook diu clarament que les dades són simulades.

- **3.000 comandes, 14 columnes.** Errors sembrats a propòsit perquè l'alumnat els
  trobi: buits, distàncies impossibles i temps d'entrega impossibles. Netejant-los
  queden 2.895 comandes.
- **Partició amb `train_test_split`**, com al NB 2.2: un 20% de test i la resta,
  75% d'entrenament i 25% de validació, tot amb `random_state=42` (1.737, 579 i 579
  comandes). El temps no hi té cap paper (no hi ha tendència ni estacionalitat que
  afecti els minuts), així que partir a l'atzar és legítim. Es va provar també de
  partir per dates, i es va descartar per no despistar l'alumnat.
- **La neteja és obligatòria i igual per a tothom** (eliminar les files amb buits o
  valors impossibles), perquè la partició es fa després de netejar. Qui imputés en
  lloc d'eliminar tindria un altre nombre de files, i amb això una altra partició: el
  MAE del model lineal passaria de 5,77 a 5,21 minuts i el repte deixaria de ser
  comparable.
- **El generador no és aquí.** `generar_repartiments.py` és al repositori de
  solucions, a la mateixa ruta, perquè conté la fórmula que l'alumnat ha de
  descobrir. Amb la llavor fixada torna a fer el CSV idèntic, byte a byte.


## Ca Nostra Lloguers (exercicis de consolidació UT3)

`UT03-Correlacions_preparacio_variables/consolidacio_lloguers/lloguers_llevant.csv`

1.600 anuncis **inventats** de lloguer de llarga durada a la comarca de Llevant
(Manacor, Porto Cristo, Cala Millor, Felanitx, Artà, Petra…), per a la sessió de
consolidació de la UT3. L'objectiu és `lloguer_mensual`. Com Picaporta, és una
excepció deliberada al criteri de dades mesurades, i el notebook ho diu.

Hi ha sembrat el que la UT3 ha d'ensenyar a trobar:

- **Una parella que diu el mateix**: `peus_quadrats` és la superfície de
  `metres_quadrats` en una altra unitat (correlació 0,999).
- **Una correlació espúria**: `id_anunci` té 0,36 de correlació amb el lloguer
  perquè el portal va exportar primer l'interior i després la costa (−0,73 amb la
  distància al mar). Amb les categòriques al model, no hi aporta res.
- **Una corba**: el preu per m² baixa de pressa el primer quilòmetre de costa i
  després s'aplana, i el logaritme de la distància l'adreça.
- **Categòriques dels tres tipus**: `estat` (amb ordre), `tipus` i `localitat`
  (sense ordre; Ariany, Sant Joan i Vilafranca tenen pocs anuncis i s'agrupen).
- **103 buits** a `any_construccio`, per a un `SimpleImputer`.

Partició com a Picaporta (`random_state=42`, 960 / 320 / 320). El repte es
calibra amb el solucionari: només numèriques 202 €; amb les categòriques, 130 €
(bronze < 140); amb el logaritme de la distància, 125 € (plata < 127); amb els metres
multiplicats pel one-hot, 105 € (or < 110). El generador, `generar_lloguers.py`, és
al repositori de solucions, a la mateixa ruta, perquè conté la fórmula.
