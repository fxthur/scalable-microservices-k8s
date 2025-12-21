# Scalable Voting App (Microservices)

![Kubernetes](https://img.shields.io/badge/kubernetes-%23326ce5.svg?style=for-the-badge&logo=kubernetes&logoColor=white)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![Redis](https://img.shields.io/badge/redis-%23DD0031.svg?style=for-the-badge&logo=redis&logoColor=white)
![Nginx](https://img.shields.io/badge/nginx-%23009639.svg?style=for-the-badge&logo=nginx&logoColor=white)

A cloud-native voting application deployed on **DigitalOcean Kubernetes (DOKS)**. This project demonstrates **Layer 7 Traffic Management**, **Microservices Architecture**, **Service Discovery**, and **Auto-Scaling capabilities**.

## Architecture
* **Frontend:** Python/Flask voting interface (Served via Ingress).
* **Backend:** Redis (In-memory data store).
* **Management:** Redis Commander (Web GUI for Database).
* **Orchestration:** Kubernetes (K8s) with Horizontal Pod Autoscaler (HPA).

## Key Features Implemented
1.  **Ingress Routing (Layer 7):**
    * Single Entry Point configured to serve multiple apps on one IP.
    * Host-based routing: `voting` (App) and `db-admin` (Redis GUI).
2.  **Microservices Communication:** Frontend connects to Redis via K8s DNS.
3.  **High Availability:** Self-healing pods managed by Deployment Controllers.
4.  **Auto-Scaling (HPA):**
    * System automatically scales from **2 to 10 replicas** when CPU > 20%.
    * Traffic spike simulation performed using `busybox`.
5.  **Incident Management:**
    * See [Incident Report 001](./docs/incidentReport.md) regarding Redis connection fix.

## Live Demo Access (Development) | The live demo can go down at any time :D
| App | URL | Description |
| :--- | :--- | :--- |
| **Voting** | [http://voting.188.166.206.178.nip.io](http://voting.188.166.206.178.nip.io) | Frontend Interface |
| **Admin** | [http://db-admin.188.166.206.178.nip.io](http://db-admin.188.166.206.178.nip.io) | Redis DB GUI |

## How to Deploy

### Steps
1.  **Install Ingress Controller**
    ```bash
    kubectl apply -f [https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-v1.8.2/deploy/static/provider/do/deploy.yaml](https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-v1.8.2/deploy/static/provider/do/deploy.yaml)
    ```

2.  **Deploy All Microservices**
    ```bash
    kubectl apply -f k8s/
    ```

3.  **Check Ingress IP**
    ```bash
    kubectl get ingress
    ```
    *(Update `k8s/ingress.yaml` with your new IP)*.

---
**Author:** fxthur
