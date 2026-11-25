"""Variables calculées du modèle d'annulation v2.

Ce module DOIT être importable partout où le modèle est chargé (notebooks, train.py,
et plus tard l'API) : joblib enregistre une référence à `ajouter_variables`, pas son code.

Toutes les variables sont calculées à partir des 15 champs déjà reçus par l'API de M0-B1,
connus au moment de la réservation : la v2 peut donc remplacer la v1 sans changer le contrat de l'API.
"""

import numpy as np
import pandas as pd

CATEGORICAL_FEATURES = [
    "hotel",
    "arrival_date_month",
    "market_segment",
    "deposit_type",
    "customer_type",
    "country",
]
RAW_NUMERICAL_FEATURES = [
    "lead_time",
    "stays_in_weekend_nights",
    "stays_in_week_nights",
    "adults",
    "children",
    "adr",
    "previous_cancellations",
    "total_of_special_requests",
    "required_car_parking_spaces",
]
# Champs bruts attendus en entrée du pipeline (= le contrat de l'API)
INPUT_FEATURES = CATEGORICAL_FEATURES + RAW_NUMERICAL_FEATURES

NEW_FEATURES = [
    "total_nights",          # durée totale du séjour
    "weekend_share",         # part des nuits en week-end : séjour loisir ou professionnel
    "has_children",          # séjour en famille
    "guests",                # taille du groupe
    "adr_per_guest",         # prix par personne et par nuit
    "has_special_requests",  # un client qui formule des demandes s'est projeté dans son séjour
]
NUMERICAL_FEATURES = RAW_NUMERICAL_FEATURES + NEW_FEATURES


def ajouter_variables(df: pd.DataFrame) -> pd.DataFrame:
    """Ajoute les variables calculées. Ne modifie pas le DataFrame reçu."""
    df = df.copy()
    children = df["children"].fillna(0)
    df["total_nights"] = df["stays_in_weekend_nights"] + df["stays_in_week_nights"]
    df["weekend_share"] = np.where(
        df["total_nights"] > 0, df["stays_in_weekend_nights"] / df["total_nights"].clip(lower=1), 0.0
    )
    df["has_children"] = (children > 0).astype(int)
    df["guests"] = df["adults"] + children
    df["adr_per_guest"] = np.where(df["guests"] > 0, df["adr"] / df["guests"].clip(lower=1), df["adr"])
    df["has_special_requests"] = (df["total_of_special_requests"] > 0).astype(int)
    return df
