
# matte_eksamener_VGS
Eksamener med løsningsforslag for matematikkeksamener på VGS.

## Rask introduksjon

- **Formål**: Samarbeid om å lage gode løsningsforslag til tidliger eksamenere i matematikk.
- **Open-source**: Vi bruker GitHub og open-sourcer dokumentene, alle kan komme med endringsforslag.
- **Kildefiler**: Vi tar bare på kildekode i `.tex` filer for fremtiden, istedet for å kun ta vare på `.pdf`.
- **Kvalitet**: Ved effektiv bruk av LaTeX får vi høy kvalitet på løsningsforslagene.
- **Alle kan bidra**: Både lærere, elever og andre kan bidra. Alle bidrag mottas med takk.


## Hvor finner jeg eksamener og løsningsforslag?
Dersom du er elev er den beste kilden til tidligere eksamensoppgaver [Eksamensoppgaver](https://matematikk.net/side/Eksamensoppgaver)-siden på [matematikk.net](https://matematikk.net/). I dette prosjektet samarbeider vi om å lage løsningsforslag, distribusjon er nok enklest gjennom [matematikk.net](https://matematikk.net/).

## Hvordan kan jeg bidra?
Finner du **skrivefeil**, **matematiske feil**, eller har **andre forbedringsforslag**? Du kan bidra til å øke kvaliteten på løsningsforslagene. Alle bidrag mottas med stor takk. Det kan virke vanskelig å komme i gang, så jeg har skrevet en detaljert guide.

### (1) Installer LaTeX
Du trenger programvaren LaTeX for å generere pene `.pdf` filer fra `.tex` filer. Du trenger også en editor som lar deg åpne og redigere `.tex` filer. Her er forslag til oppsett for vanlige operativsystemer:

- **Windows**
  * LaTeX-distribusjon: [MiKTeX](https://miktex.org/)
  * Editor: [TeXStudio](http://texstudio.sourceforge.net/)
- **Mac**
  * LaTeX-distribusjon: [MacTeX](https://tug.org/mactex/mactex-download.html)
  * Editor: [TeXStudio](http://texstudio.sourceforge.net/)
- **Ubuntu**
  * LaTeX-distribusjon: [TeX Live](https://tug.org/texlive/). Skriv `sudo apt-get install texlive-full` i terminalen.
  * Editor: [TeXStudio](http://texstudio.sourceforge.net/). Skriv `sudo apt-get install texstudio` i terminalen.
  
### (2) Installer Git og GitHub
Du trenger Git og GitHub for å gjøre bidrag til et GitHub prosjekt. Git er et program for versjonskontroll av filer, og kjøres fra terminalen. GitHub er en nettside som gjør at folk kan samarbeide om prosjekter som er versjonskontrollert av Git. Vi bruker Git for å holde styr på alle endringer i filene (hvem/hva/når/hvorfor), og vi kan også gå tilbake i historikken til filene om nødvendig. Vi bruker GitHub for å samarbeide.
* Last ned [Git](https://git-scm.com/downloads) og installer på PCen. På Windows får du et program som heter "Git Bash". Det er et terminal-program som du kan kjøre Git kommandoer fra.
* Lag en gratis konto på [GitHub](https://github.com/join).

### (3) Last ned, gjør endringer, og last opp for review
Nå har du LaTeX, så du kan åpne og endre `.tex` filer. Du har Git og GitHub, så du kan ta kopi av prosjektet. Her kommer en detaljert forklaring på hvordan du kan bidrag.

1. **Fork GitHub prosjektet:** Øverst på [denne siden](https://github.com/tommyod/matte_eksamener_VGS) er det en knapp som heter "Fork". Trykk på denne for å ta en kopi av prosjektet til din GitHub konto. Du har nå tatt en kopi av `tommyod/matte_eksamener_VGS` til `<ditt navn>/matte_eksamener_VGS`.
2. **Klon filene til din PC:** Gå til `https://github.com/<ditt navn>/matte_eksamener_VGS`, trykk "Clone or download", kopier linken `https://github.com/<ditt navn>/matte_eksamener_VGS.git`. Åpne terminalen på Mac/Ubuntu, eller Git Bash på Windows. Åpne terminalen i en mappe der du vil ta en kopi av prosjektet. Du kan enten åpne terminalen i en mappe ved å finne mappen først, høyreklikke og åpne terminalen der, eller du kan bruke terminalkommandoene `ls` (*list directory contents*) og `cd` (*change directory*) for å navigere filsystemet. Skriv så `git clone https://github.com/<ditt navn>/matte_eksamener_VGS.git`. Prosjektet blir lastet ned i en mappe, som blir kalt `matte_eksamener_VGS`. Du har nå en lokal kopi av filene.
3. **Lag en branch og gjør endringer:** Åpne terminalen, eller Git Bash på Windows, i mappen `matte_eksamener_VGS` som ble laget i forrige skritt. Skriv 
```
git add remote upstream https://github.com/tommyod/matte_eksamener_VGS.git
git branch <navn på endring>
git checkout <navn på endring>
```



