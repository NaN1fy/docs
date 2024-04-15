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

## Guida all'azione di controllo dei termini del glossario nei file sorgenti LaTeX
### Cos'è questa azione?
[![check glossary terms in latex source files](https://github.com/NaN1fy/docs/actions/workflows/check_glossary.yml/badge.svg)](https://github.com/NaN1fy/docs/actions/workflows/check_glossary.yml)
Questa GitHub Action, denominata "check glossary terms in latex source files", controlla automaticamente la presenza di termini del glossario all'interno dei file sorgenti LaTeX presenti nella cartella `documents` nei branch diversi da `main` e `sources`. Se trova dei termini mancanti o non aggiornati rispetto al glossario, notifica l'utente.
### Come funziona?
Prima di procedere, è importante tenere presente: non è pensato per ottenere un tasso di successo del 100%, poiché
- Considererà anche i termini all'interno delle tabelle (come le intestazioni);
- Non tiene conto dei duplicati, se ci sono due termini uguali nel documento (che sono presenti nel glossario) e solo uno è contrassegnato, il termine non sarà considerato come mancante.

Pertanto, funge da strumento aggiuntivo e **non dovrebbe sostituire la verifica manuale**. Aggiornamenti futuri potrebbero risolvere questa limitazione.
