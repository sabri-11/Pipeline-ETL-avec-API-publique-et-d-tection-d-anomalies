# 📦 Projet ETL — Mini Pipeline de Données avec API & Détection d'Anomalies

> Projet personnel de préparation au stage — Niveau Bac+2 / 2ème année école d'ingénieur informatique

---

## 🎯 Objectif du projet

Construire un **pipeline ETL complet** (Extract → Transform → Load) en Python, qui :
- Consomme une **API REST publique** pour récupérer des données réelles
- **Nettoie et transforme** les données brutes
- **Détecte automatiquement des anomalies** dans les données
- **Stocke les résultats** dans une base de données SQL locale
- **Génère un rapport** de synthèse lisible

Ce projet simule exactement ce que l'on fait en entreprise pour automatiser des flux de données et fiabiliser le reporting.

---

## 🌐 Source de données — API Frankfurter

**URL :** `https://api.frankfurter.app`

- Gratuite, sans inscription, sans clé API
- Fournit les **taux de change historiques** entre devises (EUR, USD, GBP, JPY, CHF…)
- Données stables et structurées : idéales pour débuter avec les API REST
- Contexte métier réaliste : une entreprise internationale suit l'évolution des devises

**Exemple d'appel :** `GET https://api.frankfurter.app/2024-01-01..2024-03-31?from=EUR&to=USD,GBP`

---

## 🏗️ Architecture du projet

```
etl_project/
│
├── extract.py        # Étape E : appel API et récupération des données brutes
├── transform.py      # Étape T : nettoyage, typage, enrichissement
├── anomaly.py        # Détection d'anomalies statistiques
├── load.py           # Étape L : insertion en base SQLite + requêtes SQL
├── report.py         # Génération d'un rapport HTML de synthèse
├── pipeline.py       # Orchestrateur : exécute tout le flux dans l'ordre
├── database.db       # Base SQLite générée automatiquement
├── report.html       # Rapport généré automatiquement
└── README.md         # Documentation du projet
```

---

## 🔧 Étapes détaillées & points clés

### Étape 1 — Extract (Appel API)
**Objectif :** Interroger l'API et récupérer les données brutes sous forme de DataFrame.

Points clés à maîtriser :
- Faire une requête HTTP avec des paramètres (`GET`, `params`)
- Gérer les erreurs HTTP (`raise_for_status`)
- Comprendre la structure JSON retournée et la mettre à plat (JSON imbriqué → tableau)
- Stocker les données dans un DataFrame pandas

---

### Étape 2 — Transform (Nettoyage & enrichissement)
**Objectif :** Rendre les données fiables et exploitables.

Points clés à maîtriser :
- Convertir les colonnes au bon type (`datetime`, `float`)
- Gérer les valeurs manquantes (les week-ends n'ont pas de cotation → `forward fill`)
- Calculer de nouvelles colonnes : variation journalière en %, jour de la semaine
- Ajouter un **timestamp de traitement** pour la traçabilité (notion clé en ETL)
- Trier et réindexer le DataFrame

---

### Étape 3 — Détection d'anomalies
**Objectif :** Identifier automatiquement les valeurs aberrantes dans les données.

Points clés à maîtriser :
- Comprendre la méthode **IQR (Interquartile Range)** : méthode statistique simple et robuste
  - Calculer Q1, Q3, et l'IQR
  - Définir des bornes haute et basse
  - Marquer les lignes hors bornes comme anomalies
- Ajouter une colonne `is_anomaly` (booléen) et `anomaly_reason` (description)
- Afficher un résumé dans la console (nombre d'anomalies détectées)

---

### Étape 4 — Load (Chargement en base SQL)
**Objectif :** Persister les données transformées dans une base de données.

Points clés à maîtriser :
- Créer une connexion **SQLite** avec Python (aucune installation serveur nécessaire)
- Insérer un DataFrame directement dans une table SQL (`to_sql`)
- Écrire des **requêtes SQL** pour interroger les données chargées
  - Exemple : récupérer uniquement les lignes anomalies
  - Exemple : calculer la moyenne des taux par mois
- Comprendre les modes `replace` vs `append`

---

### Étape 5 — Rapport HTML
**Objectif :** Produire un fichier de reporting lisible automatiquement.

Points clés à maîtriser :
- Convertir un DataFrame en tableau HTML avec `pandas.to_html()`
- Construire une page HTML simple avec un résumé : nombre de lignes, nombre d'anomalies, plage de dates
- Sauvegarder le fichier `report.html` automatiquement

---

### Étape 6 — Pipeline & orchestration
**Objectif :** Relier toutes les étapes dans un seul script d'exécution.

Points clés à maîtriser :
- Importer les fonctions des modules précédents
- Utiliser le module **`logging`** à la place des `print()` pour tracer l'exécution (bonne pratique professionnelle)
- Structurer le pipeline avec des logs à chaque étape (`INFO`, `WARNING`, `ERROR`)
- Protéger l'exécution avec `if __name__ == "__main__"`

---

## 📚 Bibliothèques à utiliser

| Bibliothèque | Rôle dans le projet | Installation |
|---|---|---|
| `requests` | Appels API REST (HTTP GET) | `pip install requests` |
| `pandas` | Manipulation de données, DataFrames | `pip install pandas` |
| `sqlite3` | Base de données SQL locale | Inclus dans Python (stdlib) |
| `logging` | Logs et traçabilité du pipeline | Inclus dans Python (stdlib) |
| `datetime` | Gestion des dates pour l'API | Inclus dans Python (stdlib) |
| `json` | Parsing des réponses API | Inclus dans Python (stdlib) |

> ✅ Pas besoin de `numpy` ni de librairies complexes : tout se fait avec pandas pour ce niveau de projet.

---

## 🗓️ Timeline estimée

| Étape | Durée estimée | Détail |
|---|---|---|
| **Setup & prise en main de l'API** | ~2h | Créer l'environnement, tester l'API dans un notebook, comprendre le JSON retourné |
| **Étape Extract** | ~2h | Écrire `extract.py`, tester différents paramètres, mettre à plat le JSON |
| **Étape Transform** | ~3h | Nettoyage, typage, valeurs manquantes, nouvelles colonnes |
| **Détection d'anomalies** | ~2h | Comprendre l'IQR, l'implémenter, vérifier les résultats |
| **Étape Load (SQL)** | ~2h | Connexion SQLite, insertion, requêtes SQL de vérification |
| **Rapport HTML** | ~1h | Tableau pandas → HTML, ajout d'un résumé |
| **Pipeline & orchestration** | ~2h | Relier les modules, ajouter le logging, tester le flux complet |
| **README & documentation** | ~1h | Décrire le projet, les choix techniques, comment l'exécuter |
| **Total** | **~15h** | Soit 3 à 4 jours de travail espacé |

---

## 💡 Bonnes pratiques à adopter dès maintenant

- **Séparer les responsabilités** : un fichier = une étape du pipeline (principe de séparation des concerns)
- **Logger, ne pas `print()`** : utiliser `logging.info()` / `logging.warning()` pour toute trace d'exécution
- **Gérer les erreurs** : anticiper les échecs API (`try/except`) et les données manquantes
- **Documenter chaque fonction** : écrire une docstring expliquant ce que fait la fonction, ses paramètres et ce qu'elle retourne
- **Versionner avec Git** : créer un repo GitHub, commiter après chaque étape fonctionnelle

---

## 🚀 Extensions possibles (si le temps le permet)

- Ajouter une **deuxième source de données** (ex : Open-Meteo pour la météo) pour simuler une jointure multi-sources
- Automatiser l'exécution avec le module **`schedule`** (lancement toutes les heures)
- Ajouter des **tests unitaires** avec `pytest` sur les fonctions de transformation
- Remplacer SQLite par **PostgreSQL** (via `psycopg2`) pour se rapprocher d'un vrai environnement professionnel

---

## 💬 Ce que tu pourras dire en entretien

> *"J'ai développé un pipeline ETL en Python qui interroge une API REST, transforme et nettoie les données avec pandas, détecte automatiquement des anomalies par la méthode IQR, puis charge les résultats dans une base SQLite. J'ai structuré le projet en modules indépendants avec un orchestrateur central et un système de logs pour assurer la traçabilité du flux."*
