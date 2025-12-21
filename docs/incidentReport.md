# Incident Postmortem: Voting App Connection Failure

**Date:** 20 December 2025
**Severity:** HIGH (Service Disruption)
**Author:** fxthur, Jr.Cloud.E

## 1. Issue Summary
Users reported receiving an **"Internal Server Error (500)"** when accessing the Voting App.
The Frontend service was running, but could not process votes.

## 2. Root Cause Analysis (RCA)
Upon investigating the logs using `kubectl logs`, we found recurring errors:
> "ConnectionError: Error -2 connecting to redis:6379. Name or service not known."

The root cause was a **Service Name Mismatch**:
* **Application Code:** Hardcoded to look for a hostname named `redis`.
* **Kubernetes Cluster:** The database service was named `redis-svc`.
* **Result:** The application could not resolve the DNS for the database.

## 3. Resolution
We applied a fix at the Infrastructure level to avoid modifying the legacy codebase:
1.  Deleted the incorrectly named service (`redis-svc`).
2.  Redeployed the Redis Service with the name `redis`.
3.  Restarted the Frontend pods to refresh DNS caching.

## 4. Lessons Learned
* Always check application default configurations (environment variables) before deployment.
* Do not assume application code will respect `ENV` overrides in legacy images.
* Kubernetes Service names must match the application's expected hostname.
