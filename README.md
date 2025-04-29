# Health App Calculator Microservice

Un microservice Python (Flask) pour calculer le BMI et BMR, déployé sur Azure avec CI/CD.

## 📌 Fonctionnalités

- **BMI** : Calcul d'Indice de Masse Corporelle
- **BMR** : Calcul du Métabolisme de Base (Harris-Benedict)
- Déploiement automatisé via GitHub Actions

## 🔧 Prérequis

- Python 3.9+
- Docker (pour le build local)
- Compte Azure (pour le déploiement)

## 🚀 Installation et Démarrage

### Avec Docker
```bash
docker build -t health-calculator .
docker run -dp 5000:5000 --name health-app health-calculator
```

### Sans Docker
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
pip install -r requirements.txt
python app.py
```

## 🌐 API Endpoints

### POST /bmi
```json
# Test BMI pour une personne de 1.75m et 70kg
curl -X POST https://health-app-cddfbebjheergufc.canadacentral-01.azurewebsites.net/bmi \
-H "Content-Type: application/json" \
-d '{
    "height": 1.75,
    "weight": 70
}'

# Résultat attendu
{"bmi": 22.86}

# Test BMI pour une personne de 1.80m et 75kg
curl -X POST https://health-app-cddfbebjheergufc.canadacentral-01.azurewebsites.net/bmi \
-H "Content-Type: application/json" \
-d '{
    "height": 1.80,
    "weight": 75
}'

# Résultat attendu
{"bmi": 23.15}

```

### POST /bmr
```json
# Test BMR pour un homme
curl -X POST https://health-app-cddfbebjheergufc.canadacentral-01.azurewebsites.net/bmr \
-H "Content-Type: application/json" \
-d '{
    "height": 175,
    "weight": 70,
    "age": 30,
    "gender": "male"
}'

# Résultat attendu
{"bmr": 1723.46}

# Test BMR pour une femme
curl -X POST https://health-app-cddfbebjheergufc.canadacentral-01.azurewebsites.net/bmr \
-H "Content-Type: application/json" \
-d '{
    "height": 165,
    "weight": 60,
    "age": 25,
    "gender": "female"
}'

# Résultat attendu
{"bmr": 1382.29}

```

### POST /Health
```json

curl https://health-app-cddfbebjheergufc.canadacentral-01.azurewebsites.net/health

```
## 🔄 Pipeline CI/CD

Le workflow GitHub Actions est déclenché à chaque push sur main :

1. **Build**
   - Installation de Python 3.9
   - Configuration de l'environnement
   - Installation des dépendances
   - Exécution des tests

2. **Deploy**
   - Déploiement sur Azure App Service
   - URL de production : `http://pythonsdv-a0cmccbbgag2a3de.francecentral-01.azurewebsites.net/`

## ⚙️ Structure du Projet
```
.
├── app.py                # Application Flask
├── health_utils.py       # Fonctions de calcul
├── requirements.txt      # Dépendances
├── Dockerfile           
├── Makefile             # Commandes d'automatisation
├── .github/workflows/   
│   └── ci-cd.yml        # Configuration CI/CD
└── tests/               # Tests unitaires
```

## 🧪 Tests

```bash
make test
# ou
python -m pytest tests/
```

## 📋 Commandes Make

```bash
make init    # Installation des dépendances
make run     # Démarrage local
make test    # Exécution des tests
make build   # Build Docker
make clean   # Nettoyage
```

## 🔒 Sécurité

- HTTPS activé
- Variables d'environnement sécurisées
- Secrets stockés dans GitHub Secrets

## 📊 Formules de Calcul

### BMI
```
BMI = weight (kg) / (height (m))²
```

### BMR (Harris-Benedict)
```
Hommes:
BMR = 88.362 + (13.397 × weight) + (4.799 × height) - (5.677 × age)

Femmes:
BMR = 447.593 + (9.247 × weight) + (3.098 × height) - (4.330 × age)
```