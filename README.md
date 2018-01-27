
# matte_eksamener_VGS
Eksamener med løsningsforslag for matematikkfag på VGS.

## Rask introduksjon

- **Formål:** Effektivt samarbeid om å lage gode løsningsforslag til eksamener i matematikk.
- **Open-source:** Alle kan bidra. **Du** kan komme med løsningsforslag, rette feil, etc.
- **Kildefiler:** Vi tar vare på kildekode i `.tex` filer for fremtiden, istedet for å kun ta vare på `.pdf`.
- **Kvalitet:** Ved effektiv bruk av LaTeX får vi veldig høy kvalitet på løsningsforslagene.
- **Alle kan bidra:** Både lærere, elever og andre kan bidra. Alle bidrag mottas med takk.


## Hvor finner jeg eksamener og løsningsforslag?

I dette prosjektet samarbeider vi om å lage løsningsforslag, distribusjon er nok enklest gjennom [matematikk.net](https://matematikk.net/). 
Se [Eksamensoppgaver](https://matematikk.net/side/Eksamensoppgaver)-siden på [matematikk.net](https://matematikk.net/).

## Hvordan kan jeg bidra?
Finner du **skrivefeil**, **matematiske feil**, **uklare setninger** eller har **andre forbedringsforslag**? 
Du kan bidra til å øke kvaliteten på løsningsforslagene, og både små og store bidrag mottas med stor takk. 
Du har to muligheter når du skal bidra: du kan lage **Issue** eller sende **Pull Request**.

### Lag *Issue*
Lag en [konto på GitHub](https://github.com/join). Gå til [Issues](https://github.com/tommyod/matte_eksamener_VGS/issues) og skriv en detaljert beskrivelse om hva du mener er feil. 
Det beste er om du skriver hvilken linje i hvilken ´.tex´ fil feilen ligger i, og hva feilen er.

### Fiks feil eller bidra selv ved å lage en *Pull Request*
Git og GitHub er et kraftig system med bratt læringskurve, så det kan virke vanskelig å komme i gang. 
Dersom du allikevel har muligheten til å lære litt om Git/GitHub og rette opp i feil selv, så settes det veldig pris på, og du får lært hvordan du kan bidra til open-source prosjekter. 
Jeg har skrevet en detaljert guide til hvordan du kan bidra. 
Dersom du støter på problemer kan du lage *Issue*, så skal du få hjelp.

#### (1) Installer LaTeX
Du trenger programvaren LaTeX for å generere pene `.pdf` filer fra `.tex` filer. 
Du trenger også en editor som lar deg åpne og redigere `.tex` filer. 
Her er forslag til oppsett for vanlige operativsystemer:

- **Windows**
  * LaTeX-distribusjon: [MiKTeX](https://miktex.org/), Editor: [TeXStudio](http://texstudio.sourceforge.net/)
- **Mac**
  * LaTeX-distribusjon: [MacTeX](https://tug.org/mactex/mactex-download.html), Editor: [TeXStudio](http://texstudio.sourceforge.net/)
- **Ubuntu**
  * LaTeX-distribusjon: [TeX Live](https://tug.org/texlive/). Skriv `sudo apt-get install texlive-full` i terminalen.
  * Editor: [TeXStudio](http://texstudio.sourceforge.net/). Skriv `sudo apt-get install texstudio` i terminalen.
  
#### (2) Installer Git og GitHub
Du både Git og en GitHub-konto for å bidra til GitHub prosjekter. 
*Git* er et program for versjonskontroll av filer, og kjøres fra terminalen. 
*GitHub* er en nettside som gjør at folk kan samarbeide om prosjekter som er versjonskontrollert av Git. 
Med andre ord: vi bruker Git for å holde styr på alle endringer i filene (hvem/hva/når/hvorfor), og vi kan også gå tilbake i historikken til filene om nødvendig; vi bruker GitHub for å samarbeide.

* Last ned [Git](https://git-scm.com/downloads) og installer. 
  På Windows får du et program som heter "Git Bash". 
  Det er et terminal-program som du kan kjøre Git kommandoer fra. 
  På Mac og Ubuntu åpner du terminalen ved å søke etter "*terminal*".
* Lag en gratis konto på [GitHub](https://github.com/join).

#### (3) Last ned, gjør endringer, og last opp til prosjektet
Dersom du har følgt stegene ovenfor så har du nå LaTeX installert, slik at du kan åpne og endre `.tex` filer. 
Du har også Git installert, og en GitHub-konto, så du kan ta kopi av prosjektet. 
Her kommer en detaljert forklaring på hvordan du gjør en endring i prosjektet.

1. **Fork GitHub prosjektet:** 
  Øverst på [denne siden](https://github.com/tommyod/matte_eksamener_VGS) er det en knapp som heter "*Fork*". 
  Trykk på denne for å ta en kopi av prosjektet til din GitHub konto. 
  Du har nå tatt en kopi av `tommyod/matte_eksamener_VGS` til `<ditt navn>/matte_eksamener_VGS` på GitHub. 
  Du finner din egen kopi av prosjektet på `https://github.com/<ditt navn>/matte_eksamener_VGS`.
2. **Klon (last ned) filene til din PC:** 
  Åpne terminalen på Mac/Ubuntu, eller Git Bash på Windows.
  Åpne terminalen i en mappe der du vil ta en kopi av prosjektet. 
  Du kan enten åpne terminalen i en mappe ved å finne mappen først, høyreklikke og åpne terminalen der, eller du kan bruke terminalkommandoene `ls` (*list directory contents*) og `cd` (*change directory*) for å navigere filsystemet ditt. 
  Skriv så `git clone https://github.com/<ditt navn>/matte_eksamener_VGS.git`. 
  Prosjektet blir lastet ned i en mappe, som blir kalt `matte_eksamener_VGS`. 
  Du har nå en lokal kopi av filene.
3. **Lag en branch og gjør endringer:** 
  Åpne terminalen, eller Git Bash på Windows, i mappen `matte_eksamener_VGS` som ble laget i forrige steg. 
  Skriv så følgende kommandoer (uten `$`):
  ```
  $ git remote add upstream https://github.com/tommyod/matte_eksamener_VGS.git
  $ git fetch upstream
  $ git branch <navn på endring> upstream/master
  $ git checkout <navn på endring>
  ```
Du har nå tatt en kopi prosjektet og du kan gjøre endringer. Når du har gjort en endring, f.eks. rettet en skrivefeil, skrevet et nytt løsningsforslag, eller noe annet, skriver du følgende:
```
$ git add -A
$ git commit -m "<Beskrivelse av endringer>"
```
Dette kan du gjøre flere ganger. 
Én *commit* samler endringer som hører sammen. 
Når du har gjort alle endringene som du vil gjøre, og *add*et og *commit*et disse, skriver du følgende for å lagre endringene på GitHub profilen din.
```
$ git push origin -f
```
Nå er endringene lagret på `https://github.com/<ditt navn>/matte_eksamener_VGS`. 
Besøk siden, der vil du se en knapp der det står "*Compare & pull request*". 
En *pull request* er en forespørsel om at jeg skal ta inn dine foreslåtte endringer i prosjektet. 
Trykk på knappen, skriv en tittel for dine endringer, og en beskrivelse av hva endringene innebærer. 
Trykk så på "*Create pull request*". 
Gratulerer! 
Du har foreslått en endring på et open-source prosjekt!

#### Oppsummering i ett eksempel - med full terminalutskrift
Her er en oppsummering av "*(3) Last ned, gjør endringer, og last opp for review*".
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
Setter opp en *branch* for endringer.
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
<< Gjør endringer i en eller flere filer>>
bruker@home ~/Desktop/matte_eksamener_VGS$ git add -A                   
bruker@home ~/Desktop/matte_eksamener_VGS$ git commit -m "Endret skrivefeil i S2_V15"
   [endring e5ea83e] Endret skrivefeil i S2_V15
    1 file changed, 1 insertion(+), 1 deletion(-)
<< Gjør flere endringer i en eller flere filer>>
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
Gå til `https://github.com/<ditt navn>/matte_eksamener_VGS`. 
Trykk på "Compare & pull request". 
Skriv en forklaring og trykk på "*Create pull request*".




