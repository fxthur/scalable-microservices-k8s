# Scalable Voting App (Microservices)

![Kubernetes](https://img.shields.io/badge/kubernetes-%23326ce5.svg?style=for-the-badge&logo=kubernetes&logoColor=white)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![Redis](https://img.shields.io/badge/redis-%23DD0031.svg?style=for-the-badge&logo=redis&logoColor=white)

A cloud-native voting application deployed on **DigitalOcean Kubernetes (DOKS)** using modern DevOps practices. This project demonstrates **Microservices Architecture**, **Service Discovery**, **Infrastructure as Code**, and **Auto-Scaling capabilities**.

## Architecture
* **Frontend:** Python/Flask-based voting interface (LoadBalanced).
* **Backend:** Redis (In-memory data store).
* **Orchestration:** Kubernetes (K8s) with Horizontal Pod Autoscaler (HPA).

## Key Features Implemented
1.  **Microservices Communication:** Frontend connects to Redis via K8s DNS Service Discovery.
2.  **High Availability:** Self-healing pods managed by Deployment Controllers.
3.  **Auto-Scaling (HPA):**
    * Traffic spike simulation performed using `busybox`.
    * System automatically scales from **2 replicas to 10 replicas** when CPU > 20%.
4.  **Incident Management:**
    * See [Incident Report 001](./docs/incidentReport.md) regarding Redis connection failure fix.

## How to Deploy

### Steps
1.  **Deploy Database (Redis)**
    ```bash
    kubectl apply -f k8s/redis-db.yaml
    ```

2.  **Deploy Frontend (Voting App)**
    ```bash
    kubectl apply -f k8s/voting-app.yaml
    ```

3.  **Enable Auto-Scaling**
    ```bash
    kubectl autoscale deployment voting-app-deployment --cpu-percent=20 --min=2 --max=10
    ```

---
**Author:** fxthur
