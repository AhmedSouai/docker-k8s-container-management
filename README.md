# TODO App - Docker & Kubernetes Project

Ce projet personnel a pour but de concevoir, conteneuriser, et orchestrer une application de type TODO list composée de trois services :

- Un **frontend** (interface utilisateur),
- Un **backend** (API REST),
- Une **base de données** (optionnelle).

Le tout est déployé dans un environnement local simulé avec **Vagrant** et **Minikube**.

---

## 🧱 Architecture du projet

my-app/
  ├── backend/ # API REST en Node.js (ou autre) 
  
  ├── frontend/ # Application web en React/Vue/Angular (par exemple)
  
  ├── k8s/ # Manifests Kubernetes (Deployments, Services) 

  ├── .github/

  
  └── README.md


> 📌 **La base de données est déployée via des fichiers YAML Kubernetes**

---

## 🧰 Technologies utilisées

- 🐳 **Docker** : Conteneurisation des services frontend et backend  
- ☁️ **Docker Hub** : Registry pour stocker les images Docker (`ahmed92clmb`)  
- ☸️ **Kubernetes (Minikube)** : Orchestration des conteneurs  
- 🧪 **kubectl** : Commande pour interagir avec Kubernetes  
- 📦 **Vagrant** : Environnement VM local reproductible

---

## 🚀 Lancer le projet

### 1️⃣ Cloner le dépôt
```bash
git clone https://github.com/AhmedSouai/projet_perso?git
cd projet_perso.git/docker-k8s-container-management
```

### 2️⃣  Construire et push les images Docker
```bash

# Backend
docker build -t ahmed92clmb/todo-backend ./backend
docker push ahmed92clmb/todo-backend

# Frontend
docker build -t ahmed92clmb/todo-frontend ./frontend
docker push ahmed92clmb/todo-frontend
```
3️⃣ Déployer les services Kubernetes

```bash
cd k8s
kubectl apply -f db.yaml         # 🛢️ Déploie la base de données
kubectl apply -f backend.yaml    # 🔧 Déploie l'API backend
kubectl apply -f frontend.yaml   # 🖥️ Déploie le frontend
```
4️⃣ Vérifier les ressources
```bash
kubectl get pods
kubectl get deployments
kubectl get services
```

