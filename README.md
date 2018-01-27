
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
Finner du **skrivefeil**, **matematiske feil**, eller har **andre forbedringsforslag**? Du kan bidra til å øke kvaliteten på løsningsforslagene. Alle bidrag mottas med stor takk. 

### Lag "Issue"

Gå til [Issues](https://github.com/tommyod/matte_eksamener_VGS/issues) og skriv en detaljert beskrivelse om hva du mener er feil. Det beste er om du skrive hvilken linje i hvilken ´.tex´ fil feilen ligger i, og hva feilen er. Før du kan lage Issue må du lage en [konto på GitHub](https://github.com/join).

### Fiks feilen selv ved å lage en "Pull Request"
Git og GitHub er et kraftig system, og det kan virke vanskelig å komme i gang. Dersom du har muligheten til å rette opp i feil selv, så settes det veldig pris på, og du får lært hvordan du kan bidra til open source prosjekter som dette. Jeg har skrevet en detaljert guide til hvordan du kan bidra.

#### (1) Installer LaTeX
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
  
#### (2) Installer Git og GitHub
Du trenger Git og GitHub for å gjøre bidrag til et GitHub prosjekt. Git er et program for versjonskontroll av filer, og kjøres fra terminalen. GitHub er en nettside som gjør at folk kan samarbeide om prosjekter som er versjonskontrollert av Git. Vi bruker Git for å holde styr på alle endringer i filene (hvem/hva/når/hvorfor), og vi kan også gå tilbake i historikken til filene om nødvendig. Vi bruker GitHub for å samarbeide.
* Last ned [Git](https://git-scm.com/downloads) og installer på PCen. På Windows får du et program som heter "Git Bash". Det er et terminal-program som du kan kjøre Git kommandoer fra.
* Lag en gratis konto på [GitHub](https://github.com/join).

#### (3) Last ned, gjør endringer, og last opp for review
Nå har du LaTeX, så du kan åpne og endre `.tex` filer. Du har Git og GitHub, så du kan ta kopi av prosjektet. Her kommer en detaljert forklaring på hvordan du kan bidrag.

1. **Fork GitHub prosjektet:** Øverst på [denne siden](https://github.com/tommyod/matte_eksamener_VGS) er det en knapp som heter "Fork". Trykk på denne for å ta en kopi av prosjektet til din GitHub konto. Du har nå tatt en kopi av `tommyod/matte_eksamener_VGS` til `<ditt navn>/matte_eksamener_VGS`.
2. **Klon filene til din PC:** Gå til `https://github.com/<ditt navn>/matte_eksamener_VGS`, trykk "Clone or download", kopier linken `https://github.com/<ditt navn>/matte_eksamener_VGS.git`. Åpne terminalen på Mac/Ubuntu, eller Git Bash på Windows. Åpne terminalen i en mappe der du vil ta en kopi av prosjektet. Du kan enten åpne terminalen i en mappe ved å finne mappen først, høyreklikke og åpne terminalen der, eller du kan bruke terminalkommandoene `ls` (*list directory contents*) og `cd` (*change directory*) for å navigere filsystemet. Skriv så `git clone https://github.com/<ditt navn>/matte_eksamener_VGS.git`. Prosjektet blir lastet ned i en mappe, som blir kalt `matte_eksamener_VGS`. Du har nå en lokal kopi av filene.
3. **Lag en branch og gjør endringer:** Åpne terminalen, eller Git Bash på Windows, i mappen    `matte_eksamener_VGS` som ble laget i forrige skritt. Skriv 
  ```
  $ git remote add upstream https://github.com/tommyod/matte_eksamener_VGS.git
  $ git fetch upstream
  $ git branch <navn på endring> upstream/master
  $ git checkout <navn på endring>
  ```
  Du har nå tatt en kopi prosjektet og du kan gjøre endringer. Når du har gjort en endring, f.eks. rettet en skrivefeil, skrevet et nytt løsningsforslag, eller noe annet, skriver du følgende.
```
$ git add -A
$ git commit -m "<Beskrivelse av endringer>"
```
Dette kan du gjøre flere ganger. Én enkelt *commit* samler endringer som hører sammen. Når du har gjort alle endringene som du vil gjøre, og addet og commitet disse, skriver du følgende for å lagre endringene på din GitHub profil.
```
$ git push origin -f
```
Nå er endringene lagret på `https://github.com/<ditt navn>/matte_eksamener_VGS`. Besøk siden, og vil du se en knapp der det står "Compare & pull request". En *pull request* er en forespørsel om å ta inn dine foreslåtte endringer. Trykk på kanppen, skriv en tittel for dine endringer, og en beskrivelse av hva endringene innebærer. Trykk så på "*Create pull request*". Gratulerer! Du har foreslått en endring på et open-source prosjekt!

#### Oppsummering i ett eksempel
Her er en oppsummering av "*(3) Last ned, gjør endringer, og last opp for review*". Vi kloner fra GitHub til PCen.
```
bruker@home ~$ cd Desktop
bruker@home ~/Desktop$ git clone https://github.com/<ditt navn>/matte_eksamener_VGS.git
   Cloning into 'matte_eksamener_VGS'...
   remote: Counting objects: 9, done.
   remote: Compressing objects: 100% (8/8), done.
   Unpacking objects: 100% (9/9), done.
   remote: Total 9 (delta 1), reused 5 (delta 1), pack-reused 0
   Checking connectivity... done.
```
Setter opp en branch for endringer.
```
bruker@home ~/Desktop$ cd matte_eksamener_VGS                                  
bruker@home ~/Desktop/matte_eksamener_VGS$ git remote add upstream https://github.com/tommyod/matte_eksamener_VGS.git
bruker@home ~/Desktop/matte_eksamener_VGS$ git fetch upstream
   From https://github.com/tommyod/matte_eksamener_VGS
    * [new branch]      master     -> upstream/master
bruker@home ~/Desktop/matte_eksamener_VGS$ git branch endring upstream/master
   Branch endring set up to track remote branch master from upstream.
bruker@home ~/Desktop/matte_eksamener_VGS$ git checkout endring
   Switched to branch 'endring'
   Your branch is up-to-date with 'upstream/master'.
```
Gjør en, eller flere, endringer.
```
<< Gjør en endring >>
bruker@home ~/Desktop/matte_eksamener_VGS$ git add -A                   
bruker@home ~/Desktop/matte_eksamener_VGS$ git commit -m "Endret skrivefeil i S2_V15"
   [endring e5ea83e] Endret skrivefeil i S2_V15
    1 file changed, 1 insertion(+), 1 deletion(-)
<< Gjør enda en endring >>
bruker@home ~/Desktop/matte_eksamener_VGS$ git add -A                   
bruker@home ~/Desktop/matte_eksamener_VGS$ git commit -m "Endret skrivefeil i S2_V16"
   [endring e5ea83e] Endret skrivefeil i S2_V16
    1 file changed, 1 insertion(+), 1 deletion(-)
```
Dytt endringene opp til GitHub med "*push*" kommandoen.
```
bruker@home ~/Desktop/matte_eksamener_VGS$ git push origin -f              
   Counting objects: 3, done.
   Delta compression using up to 4 threads.
   Compressing objects: 100% (3/3), done.
   Writing objects: 100% (3/3), 284 bytes | 0 bytes/s, done.
   Total 3 (delta 2), reused 0 (delta 0)
   remote: Resolving deltas: 100% (2/2), completed with 2 local objects.
   To https://github.com/<ditt navn>/matte_eksamener_VGS.git
    * [new branch]      endring -> endring            
```
Gå til `https://github.com/<ditt navn>/matte_eksamener_VGS`. Trykk på "Compare & pull request". Skriv en forklaring og trykk på "*Create pull request*".




