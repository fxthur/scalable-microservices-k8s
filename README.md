## Scalable Microservices Voting App (Kubernetes)

![Kubernetes](https://img.shields.io/badge/kubernetes-%23326ce5.svg?style=for-the-badge&logo=kubernetes&logoColor=white)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![Redis](https://img.shields.io/badge/redis-%23DD0031.svg?style=for-the-badge&logo=redis&logoColor=white)
![Nginx](https://img.shields.io/badge/nginx-%23009639.svg?style=for-the-badge&logo=nginx&logoColor=white)

A production-grade cloud-native voting application deployed on **DigitalOcean Kubernetes (DOKS)**. This project demonstrates advanced **Traffic Management (Layer 7)**, **Microservices Architecture**, and **Auto-Scaling capabilities**.

## rchitecture Design

The system uses **Ingress NGINX** as a single entry point to save LoadBalancer costs and manage routing efficiently.


## 🌟 Key Features Implemented

1.  **Layer 7 Load Balancing (Ingress):**
    * Single Entry Point for multiple applications.
    * **Host-based Routing** configured to serve `voting` and `db-admin` on the same IP.
2.  **Database Observability:**
    * Integrated **Redis Commander** GUI to monitor database keys in real-time.
3.  **Microservices Communication:**
    * Frontend connects to Redis via K8s DNS Service Discovery.
4.  **Auto-Scaling (HPA):**
    * System automatically scales from **2 to 10 replicas** when CPU > 20%.
    * Tested with traffic spike simulation.
5.  **Incident Management:**
    * [Report 001: Redis Connection Failure](./docs/incidentReport.md)
    * [Report 002: Ingress Protocol Mismatch](./docs/incidentReport-002.md)

## 🌐 Live Demo Access (Development)

| Application | URL | Description |
| :--- | :--- | :--- |
| **Voting App** | [http://voting.188.166.206.178.nip.io](http://voting.188.166.206.178.nip.io) | Frontend interface. |
| **Redis Admin** | [http://db-admin.188.166.206.178.nip.io](http://db-admin.188.166.206.178.nip.io) | Redis GUI. |

