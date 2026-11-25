# M2-B2, partie 1 — Biais et réglementation (binôme)

Squelette de la partie synchrone.

```
data/reservations_train.csv   58 199 réservations nettoyées, juillet 2015 à août 2016
data/reservations_test.csv    19 694 réservations nettoyées, septembre à décembre 2016
model/                        modèle v2.1.0 et sa fiche (M2-B1)
features.py                   variables calculées, nécessaires au chargement du modèle
modele.py                     entrainer() et mesures_par_groupe(), fournies
notebooks/01_biais.ipynb      notebook de travail
FICHE_REGLEMENTAIRE.md        repères RGPD et AI Act
NOTE_RISQUES.md               gabarit de la note
```

Pas de base de données ni de Docker. Installation :

```bash
python -m venv .venv
```

```bash
.venv\Scripts\Activate.ps1
```

```bash
pip install -r requirements.txt
```

Ouvrir le notebook avec le noyau `.venv`. La première cellule affiche `(58199, 19694)`.

Données : extrait nettoyé de *Hotel Booking Demand*, Antonio, de Almeida, Nunes (2019), CC BY 4.0. Les noms d'établissements sont fictifs.
