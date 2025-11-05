# E-handel: snabbrapport & GitHub-samarbete

Syftet med detta projekt var att analysera och visualisera data från en fiktiv e-handelsverksamhet och träna på att använda GitHub. 

## Beskrivning

Den påhittade ledningen vill ha ett snabbt beslutsunderlag inför nästa kampanjperiod. 

Projektet har analyserat försäljningsdata från första halvåret 2024 och ger genom nyckeltal och diagram svar på ledningens frågor:

* Vad säljer? - Vilka kategorier driver mest intäkt?
* Var säljer vi? - Vilka städer står för störst intäkt?
* När säljer vi? - Finns tidsmönster/säsong i försäljningen?
* Hur ser en typisk order ut? - AOV (Average Order Value) och spridning
* Vilka är topp-3 kategorierna? (baserat på intäkt)
* Eventuella avikelser - finns det något oväntat mönster som sticker ut?

I slutet av rapporten presenteras projektgruppens rekommendationer. 

Projektgruppens medlemmar var:

* Josefin
* Sayed
* Jonas
* Henry
* Shara
* Alma
* Jazdan
* Elias

Då antalet gruppmedlemmar var många i förhållande till projektets storlek delade vi upp oss två och två: 

* Josefin & Sayed
* Jonas & Henry
* Shara & Alma 
* Jazdan & Elias 

Varje par ansvarade för en viss del av projektet och skrev koden till det. Vilket par som gjorde vad står i avsnitt Funktioner. 

Under projektets gång hade vi ett flertal gruppmöten där vi bl.a. gick igenom den färdiga koden, gjorde ändringar och sen merge:ade vi tillsammans. 

Så alla medlemmar kunde hänga med på vilken kod som skrevs och varför. Vi fick även gemensamt uppleva vad som kan gå snett när olika PR:s ska merge:as (:sweat_smile:)

Alma sammanställde rekommendationerna och Josefin skrev README:n.

## Funktioner 

### io_utils.py

Här ligger två funktioner. Den första läser in innehållet från en fil och returnerar innehållet som en DataFrame. 

Den andra funktionen tar en DataFrame och "städar" den genom att att ändra datatyperna till de korrekta varianterna. 

Den här filen och dessa funktioner ansvarade Shara och Alma för. 

### metrics.py 

Här ligger alla funktioner som definierar hur olika nyckeltal beräknas:

* Antal ordrar (Elias & Jazdan)
* Summan av valfri kolumn (Elias & Jazdan)
* AOV (Elias & Jazdan)
* Antal ordrar per månad (Josefin & Sayed)
* Antal ordrar per veckodag (Josefin & Sayed)
* Total intäkt per stad (Jonas & Henry)
* Antal, medelvärde och summa per kategori (Shara & Alma)

### viz.py

Här ligger alla funktioner som definierar hur olika diagram skapas: 

* Histogram som visar fördelningen av antal ordrar i relation till intäkten per order (Jonas & Henry)
* Stapeldiagram över total intäkt per stad (Jonas & Henry)
* Linjediagram över totalt antal ordrar per månad (Josefin & Sayed)
* Linjediagram över totalt antal ordrar per veckodag (Josefin & Sayed)
* En mall för stapeldiagram (Shara & Alma)
* En mall för låddiagram (Shara & Alma)

Samtliga plot-funktioner - förutom mallarna för stapeldiagram och låddiagram - anropar "beräkningsfunktionerna" från metrics.py

### ecommerce.py

Här ligger det en klass vars metod anropar funktioner från metrics.py för att beräkna AOV, totalt antal ordrar, total intäkt och totalt antal enheter.

Den här filen och den här klassen ansvarade Elias och Jazdan för. 

### Report.ipynb

Detta är själva rapporten. Den läser in data och anropar sedan funktioner från src/-mappen för att beräkna statistik och skapa diagram. 

## Installation 

1. Klona projeket från GitHub:

git clone https://github.com/eliasstalfreelancer/GruppArbete.git

2. Gå in i projektmappen:

cd GruppArbete

3. Installera nödvändiga paket:

pip install -r requirements.txt

## Hur man kör

När du har installerat alla paket enligt Installationsavsnittet:

1. Öppna Report.ipynb i VS Code 
2. Klicka på "Run All"
3. Voilà

## Teknikstack 

* Dataanalys: Pandas
* Visualisering: Matplotlib
* Rapport: Jupyter Notebook 
