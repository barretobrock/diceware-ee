# diceware-ee
Eestikeelsete sõnade loend parooli loomiseks diceware meetodiga.

*Diceware*-i kirjeldus:  
http://world.std.com/~reinhold/diceware.html

Esialgse sõnaloendi allikas:  
http://www.eki.ee/tarkvara/wordlist/

Loendi filtreerimine:  
`cat lemmad.txt | egrep "^[aeh-pr-st-võäöü][abd-pr-võäöü]{3,5}$" | egrep -v "ma$" > lihtsad-lemmad.txt`  

Filtreeritud loendist indekseeritud nimekirja tegemine:  
`python3 sonad.py lihtsad-lemmad.txt > diceware-ee.txt`

Tulemus: [diceware-ee.txt](https://github.com/barretobrock/diceware-ee/blob/master/diceware-ee.txt)

_NB! Et parool saaks isegi tugevamaks, kasuta `horcruxing` meetodit - [rohkem infot siit](https://kaizoku.dev/double-blind-passwords-aka-horcruxing) (ingl.)_