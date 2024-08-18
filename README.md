# Documentazione del Progetto
Questo branch contiene i sorgenti in formato `.tex` della documentazione di progetto.
## Dettagli
- È possibile consultare il file [README](https://github.com/NaN1fy/docs/tree/main) nel branch `main` per ulteriori dettagli.
- La compilazione dei sorgenti avviene tramite [GitHub Action](https://docs.github.com/en/actions).
## Guida all'azione di compilazione LaTeX
### Cos'è questa azione?
[![Build LaTeX document](https://github.com/NaN1fy/docs/actions/workflows/compile.yml/badge.svg?branch=sources&event=push)](https://github.com/NaN1fy/docs/actions/workflows/compile.yml)

Questa GitHub Action, chiamata "compile LaTeX documents", permette di compilare automaticamente i sorgenti LaTeX presenti nella branch `sources`.
### Come funziona?
L'azione può essere attivata automaticamente tramite push: Quando si effettua un push di modifiche alla cartella `documents` nella branch `sources`, l'azione viene eseguita automaticamente.
### Directory di lavoro
Affinché l'azione funzioni correttamente, i file LaTeX  devono essere posizionati nelle directory `documents/**/*.tex`. Ecco una rappresentazione grafica della struttura delle cartelle:

> [!IMPORTANT]  
> I documenti deveno essere contenuti per intero in un singolo file `.tex`.


```
/documents
├── /candidatura
│   ├── /verbali
│   │   ├── /interni
│   │   │   └── *.tex
│   │   │       
│   │   └── /esterni                       
│   │       
│   ├── *.tex 
│   ├── *.tex
│   └── *.tex
│
...     ...
```
I file `.pdf` compilati saranno generati nella stessa cartella del file sorgente LaTeX principale, ma nella branch `main` .

### Versionamento dei file
Possiamo versionare i documenti compilati anche per nome del file (non obbligatorio ma altamente consigliato), per farlo è necessario aggiungere un commento nel `.tex` principale secondo il seguente formato:
```
% changelog: "X.X.X, YYYY-MM-DD, Autore, Descrizione della modifica"
```
Il nome del file `.pdf` sarà modificato aggiungendo `_vX.X.X` alla fine del nome del file.
