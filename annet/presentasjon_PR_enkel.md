<!-- page_number: true -->
<!-- $size: 16:9 -->

:bulb: vgs_eksamener - Hvordan lage PR.
=======================================

## En enkel introduksjon


- Hva er en Pull Request (PR), og hvorfor lage PR?
- Installer LaTeX
- Installer Git og GitHub
- Last ned, gjør endringer, og last opp til prosjektet

----

# Hva er en Pull Request (PR), og hvorfor lage PR?


- En PR er et endringsforslag til prosjektet, eksempelvis:
  - En rettet skrivefeil.
  - En oppgave gjort på en bedre måte.
  - Et nytt løsningsforslag.
- Lag en PR for å :
  - Bidra effektivt til prosjektet.
  - Hjelpe fremtidens elever.

----

# Installer LaTeX 


LaTeX genererer pene `.pdf` filer fra `.tex` filer. 
Vi også en editor som lar deg åpne og redigere `.tex` filer effektivt. 

Her er forslag til oppsett for vanlige operativsystemer:

- **Windows**
  * LaTeX-distribusjon: [MiKTeX](https://miktex.org/), Editor: [TeXStudio](http://texstudio.sourceforge.net/)
- **Mac**
  * LaTeX-distribusjon: [MacTeX](https://tug.org/mactex/mactex-download.html), Editor: [TeXStudio](http://texstudio.sourceforge.net/)
- **Ubuntu**
  * LaTeX-distribusjon: [TeX Live](https://tug.org/texlive/). Skriv `sudo apt-get install texlive-full` i terminalen.
  * Editor: [TeXStudio](http://texstudio.sourceforge.net/). Skriv `sudo apt-get install texstudio` i terminalen.
  
----

# Installer Git og GitHub

Du trenger både [Git](https://git-scm.com/downloads) og en [GitHub-konto](https://github.com/join) for å bidra.
- *Git* er et program for versjonskontroll av filer, og kjøres fra terminalen. 
- *GitHub* er en nettside som gjør at folk kan samarbeide om prosjekter som er versjonskontrollert ved hjelp av Git. 

----

# Last ned, gjør endringer, og last opp til prosjektet

1. Fork GitHub prosjektet.
2. Klon (last ned) filene til din PC.
3. Gjør endringer, lagre med `git add` og `git commit -m "Melding"`.
4. Last opp endringer med `git push` og lag pull request.

----

# Forking, pulling og pushing av prosjekter
```text                                                                     
                                                                        GitHub  
+------------------------------------------------------------------------------+
|   upstream                                       origin                      |
|  +------------------------+        fork         +-------------------------+  |
|  |matematikk/vgs_eksamener| ------------------> |<ditt navn>/vgs_eksamener|  |
|  +------------------------+                     +-------------------------+  |
|             -\                                         ^         |           |
+-----------------\--------------------------------------|---------|-----------+
                   --\                                   |         |            
                      --\                       git push |         | git pull   
                         --\                             |         |            
       git fetch upstream   --\                          |         |            
                               --\                       |         |            
                                  --\                    |         |      Din PC
+--------------------------------------\-----------------|---------|-----------+
|                                       --\              |         v           |
|                                          --\    +-------------------------+  |
|                                             ->  |       vgs_eksamener     |  |
|                                                 +-------------------------+  |
|                                                                              |
+------------------------------------------------------------------------------+
```

----

# Commits

```text                                                       
 +--------+     +--------+     +--------+     +--------+     +--------+
 |Commit 1|---->|Commit 2|---->|Commit 3|---->|Commit 4|---->|Commit 5|
 +--------+     +--------+     +--------+     +--------+     +--------+
                               
```



