# Documentazione del Progetto
Questo branch contiene i sorgenti in formato `.tex` della documentazione di progetto.
## Dettagli
- È possibile consultare il file [README](https://github.com/NaN1fy/docs/tree/main) nel branch `main` per ulteriori dettagli.
- La compilazione dei sorgenti avviene tramite [GitHub Action](https://docs.github.com/en/actions).
## Guida all'azione di compilazione LaTeX
### Cos'è questa azione?
Questa GitHub Action, chiamata "compile LaTeX documents", permette di compilare automaticamente i sorgenti LaTeX presenti nella branch `sources`.
### Come funziona?
L'azione può essere attivata in due modi:
- Automaticamente tramite push: Quando si effettua un push di modifiche alla branch `sources`, l'azione viene eseguita automaticamente.
- Manualmente nel repository GitHub: È possibile attivare manualmente l'azione tramite la scheda `Actions` > `compile LaTeX documents` > `Run workflow`.
### Directory di lavoro
Affinché l'azione funzioni correttamente, i sorgenti LaTeX principali devono essere posizionati nella directory `documents/**/*.tex`. Ecco una rappresentazione grafica della struttura delle cartelle:
```
documents
└── documentazione1
    └── documentazione1.tex
    └──  sections
        └──  section1.tex
        └──  section2.tex
        ...
└── documentazione2
    └── documentazione2.tex
...
```
I file `.pdf` compilati saranno generati nella stessa cartella del file sorgente LaTeX principale, ma saranno presenti nella branch `main` .

### Versionamento dei file
Possiamo versionare i documenti compilati anche per nome del file , per farlo è necessario aggiungere un commento nel `.tex` principale secondo il seguente formato:
```
% changelog: "X.X, YYYY-MM-DD, Autore, Descrizione della modifica"
```
Il nome del file `.pdf` sarà modificato aggiungendo `_vX.X` alla fine del nome del file.
