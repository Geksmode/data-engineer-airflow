# 🛠️ Data Engineer Portfolio — Airflow ETL Pipeline

Bienvenue sur mon projet portfolio de Data Engineer. Ce projet démontre mes compétences en orchestration de données avec **Apache Airflow**, **Docker**, et une pipeline **CI/CD GitHub Actions**.

---

## 🚀 Objectif du projet

Ce pipeline simule une ingestion de données météo, leur transformation, puis leur stockage local. Il illustre un cycle complet de type **ETL** :  
**Extract → Transform → Load** orchestré par Apache Airflow.

---

## 🔧 Technologies utilisées

| Outil          | Rôle                                       |
|----------------|---------------------------------------------|
| 🐍 Python       | Développement des tâches et transformation |
| 📦 Docker       | Conteneurisation d'Airflow et PostgreSQL   |
| ⏰ Apache Airflow | Orchestration des tâches ETL               |
| 🔁 GitHub Actions | Déploiement continu des DAGs               |
| 📄 Pandas       | Manipulation de données                     |

---

## 📂 Structure du projet
data-engineer-airflow/
├── dags/ # Fichiers DAGs Airflow
│ └── weather_etl.py # DAG principal (simulé, sans API)
├── output/ # CSVs générés par le DAG
├── plugins/ # Plugins Airflow (vide ici)
├── logs/ # Logs Airflow (non versionnés)
├── .github/workflows/ # CI/CD GitHub Actions
│ └── deploy.yaml # Pipeline de déploiement
├── docker-compose.yaml # Stack Docker Airflow
├── .env # Variables Docker (non versionné)
├── .gitignore
└── README.md

---

## 🧪 Exemple de pipeline ETL

Le DAG `weather_etl.py` contient trois tâches :
1. **`extract_weather`** : génère aléatoirement des données météo (ville, température, humidité)
2. **`transform_data`** : calcule la température en °F
3. **`load_data`** : sauvegarde les résultats dans un fichier CSV local

---

## ⚙️ Lancer le projet localement

```bash
# 1. Cloner le repo
git clone https://github.com/Geksmode/data-engineer-airflow.git
cd data-engineer-airflow

# 2. Initialiser Airflow et Docker
mkdir -p dags logs plugins output
echo "AIRFLOW_UID=$(id -u)" > .env
docker-compose up airflow-webserver  # puis Ctrl+C
docker-compose run airflow-webserver airflow db init
docker-compose up -d

# 3. Accéder à l’interface Airflow
# http://localhost:8080 (admin / admin)

