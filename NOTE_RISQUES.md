# Note de risques



**Binôme :** Alexandre - Hamza · **Date :** 25/11/2026

## Réponse en trois lignes

Non. Sur les réservations de septembre à décembre 2016, 74 % des clients portugais déclenchent une alerte, contre 22 % des clients des autres pays.
Une partie de cet écart correspond à un fait réel : les clients portugais annulent à 62 %, les autres à 26 %.
Mais l'écart subsiste chez ceux qui viennent quand même : 44 % des Portugais sont signalés à tort, contre 12 % des autres.

## Risques, du plus grave au moins grave

| Risque | Usage concerné | Chiffre à l'appui | Personnes touchées | Mesure proposée | Risque restant |
|---|---|---|---|---|---|
| Si l'alerte sert à exiger un acompte, le modèle subordonne une condition de paiement au pays du client | Annulation : acompte | 74 % des réservations portugaises déclenchent une alerte, contre 22 % des autres | Les 5 076 réservations portugaises alertées sur quatre mois | Ne pas piloter l'acompte par le score : acompte uniforme, ou décision humaine motivée | Le pays se retrouve sans la colonne : AUC 0,838, et « Non Refund » est portugais à 100 % |
| La relance traite comme suspect un client portugais sur deux qui vient pourtant honorer sa réservation | Annulation : relance | 44 % d'alertes à tort côté portugais, contre 12 % pour les autres pays | 1 136 clients portugais venus quand même sur quatre mois | Message et procédure identiques pour tous, pays non affiché à l'agent, information du client qu'un score existe | Le taux reste inégal tant que le modèle sert à prioriser |
| Retirer `country` pour corriger déplace le préjudice sur les clients étrangers au lieu de le supprimer | Les deux usages | Alertes à tort côté étranger : 12 % aujourd'hui, 35 % sans la variable, et précision globale de 72 % à 60 % | 2 206 clients étrangers supplémentaires alertés à tort sur quatre mois | Ne retirer aucune variable sans mesurer par groupe avant et après | Aucune version du modèle ne supprime l'écart : il faut encadrer l'usage, pas la variable |

## Cadre réglementaire

| Usage | Base légale envisagée | Principe en tension | Niveau AI Act et justification |
|---|---|---|---|
| Annulation : relance | Finalité : réduire les annulations tardives en recontactant les réservations à risque. Intérêt légitime (art. 6), avec la mise en balance que suppose cette base. | Minimisation (art. 5) : `country` est-il nécessaire à cette finalité ? Puis information (art. 13-14) : le client ignore qu'un score est calculé sur sa réservation. | Risque minimal : la relance ne figure dans aucun des usages listés en haut risque (recrutement, solvabilité, éducation, biométrie) ni dans les pratiques interdites. Obligation : art. 4, maîtrise de l'IA par les équipes qui exploitent les alertes. |
| Annulation : acompte | Finalité : couvrir le risque financier d'une annulation. Contrat (art. 6) si l'acompte est une condition annoncée avant la réservation, sinon intérêt légitime et mise en balance. | Décision automatisée (art. 22) : exiger un acompte affecte la personne de façon significative, donc intervention humaine. Puis analyse d'impact (art. 35). | Risque minimal au regard de la liste, mais la fiche rappelle que la non-discrimination s'apprécie indépendamment de l'IA : code pénal 225-1 et 225-2 sur la subordination d'un service, et règlement 2018/302 sur la nationalité et la résidence. Obligation : art. 22 et art. 35. |
| Motifs d'avis | Finalité : classer les motifs d'insatisfaction à partir du flux brut d'avis. Intérêt légitime (art. 6), avec mise en balance. | Minimisation (art. 5) : les noms, numéros de chambre et e-mails du flux brut ne servent pas à cette finalité. Puis conservation (art. 5) : quelle durée, et pourquoi. | Risque minimal, sauf si un contenu est généré ou un agent conversationnel intervient, auquel cas art. 50 sur la transparence. Obligation : masquer avant stockage, et documenter que le résultat reste pseudonymisé tant que l'individualisation, la corrélation ou l'inférence restent possibles. |

## Désaccord au sein du binôme

Le point discuté : faut-il traiter la relance comme l'acompte, c'est-à-dire comme une différence de traitement à proscrire, ou comme un geste commercial sans effet significatif ?

Hamza : les deux usages reposent sur le même score et le même écart. Un client portugais sur deux qui vient honorer sa réservation reçoit un message qu'un client étranger comparable ne reçoit pas. Un préjudice faible n'est pas un préjudice nul, et l'article 22 parle d'effet significatif, pas d'effet financier.

Alexandre : un message de rappel ne modifie ni le prix, ni les conditions, ni l'accès au service. Il ne subordonne rien à la nationalité, contrairement à un acompte. L'écart de traitement existe, mais il reste dans le registre commercial.

Décision : le binôme retient la distinction, en la fondant sur ce que l'alerte déclenche et non sur l'écart lui-même. La relance est maintenue sous conditions, message et procédure identiques, pays non affiché à l'agent, et suivi de l'écart de fausses alertes à chaque version du modèle. L'acompte piloté par le score est refusé en l'état.

## Recommandation, usage par usage

**Relance : continuer, en modifiant la procédure.** Quatre conditions : message et procédure identiques quel que soit le pays, `country` non affiché à l'agent qui appelle, mention au client qu'un score est calculé sur sa réservation, et suivi de l'écart de fausses alertes par groupe à chaque version du modèle, avec un seuil au-delà duquel l'usage est suspendu.

**Acompte : ne pas mettre en place.** Le score ne doit pas conditionner une exigence de paiement. Si le besoin commercial est réel, deux voies restent ouvertes : un acompte uniforme annoncé avant la réservation, ou une décision humaine motivée, assortie du droit de contester.

**Point transversal.** Ne pas retirer `country` pour corriger l'écart : la mesure déplace le préjudice sur les clients étrangers et coûte 12 points de précision. Le correctif porte sur ce que l'alerte déclenche, pas sur la liste des variables.
