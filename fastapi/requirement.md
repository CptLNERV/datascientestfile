1. Réception de données CSV via post("/question")
    i. Sélectionner une utilisation et plusieurs sujets. Sélectionner 5, 10 ou 20.
    ii. Les mêmes paramètres peuvent générer des problèmes différents de manière aléatoire à chaque fois.
    
Avant d'envoyer les données, demandez au front-end de valider la dépendance des données.

**Exemple de valeur :**
```json
{
  "use": "string",
  "subject": [
    "string"
  ],
  "number": 0
}

Test curl:
curl -X 'POST' -i 'http://127.0.0.1:8000/question' -H 'Content-Type: application/json'   -d '{ "use":"Test de positionnement","subject":["BDD", "Docker"],"number": 2}'

Le front end doit valider les données envoyées, par exemple. Ici il s'agit de "test de validation". Il ne peut donc pas choisir "BDD ou docker" dans le sujet.
Sinon, il retournera une table vide et provoquera une erreur. Je fais raise comme une erreur dans le programme

2. Vérification de l'utilisateur via post("/login")
    i. Vérification de l'utilisateur et du mot de passe

**Exemple de valeur :**
```json
{
  "username": "string",
  "password": "string"
}

test url:
 curl -X 'POST' -i 'http://127.0.0.1:8000/login' -H 'Content-Type: application/json'   -d '{"username":"alice","password":"wonderland"}'

3. admin ("/add_question")
    i. Vérifier la connexion de l'administrateur avec le mot de passe de l'administrateur
    ii. l'administrateur peut ajouter une question et les réponses

**Exemple de valeur :**
```json
{
  "user": {
    "username": "string",
    "password": "string"
  },
  "question": {
    "question": "string",
    "subject": "string",
    "use": "string",
    "correct": "string",
    "responseA": "string",
    "responseB": "string",
    "responseC": "string",
    "responseD": "string",
    "remark": "string"
  }
}

Test url
curl -X 'POST' -i 'http://127.0.0.1:8000/add_question' -H 'Content-Type: application/json'   -d '{"user":{"username":"Admin","password":"4dm1N"},"question":{"question":"add_question","subject":"add_subject","use":"add_use","correct":"add_correct","responseA":"add_responseA","responseB":"add_responseB","responseC":"add_responseC","responseD":"add_responseD","remark":"add_remark"} }'