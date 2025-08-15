
# Critical Path & Dependencies (AI Architect 10-Day Plan)

Below is a concise dependency map so you always know **what must be done before what**. Use this while following your 10-day plan.

---

## Visual Dependency Graph (Mermaid)

```mermaid
flowchart TD
  %% Core foundations
  Pyth[Python Setup & Basics] --> Flask[Flask API]
  Pyth --> Django[Django + DRF]
  Flask --> Docker[Dockerize Services]
  Django --> Docker

  %% Cloud path
  Docker --> ECR[AWS ECR Push]
  ECR --> DeployAWS[Deploy (Lambda/ECS/EKS)]
  DeployAWS --> Mon[Observability (CloudWatch/Logs)]

  %% AI path
  PyStack[NumPy/Pandas] --> SKL[scikit-learn Model]
  SKL --> Serve[Serve Model via Flask/Django]
  TF[TensorFlow Basics] --> Serve
  PT[PyTorch Basics] --> Serve
  Serve --> Docker

  %% K8s path
  Docker --> K8s[minikube/Kubernetes Deploy]
  K8s --> HPA[Autoscaling (HPA)]

  %% RAG path (optional but valuable)
  LLM[OpenAI + LangChain] --> RAG[Index + Retrieval]
  RAG --> Serve
```

---

## Bottlenecks (Complete these first)

- **Python Setup → Flask/Django → Docker → AWS ECR** (blocks all deployments)
- **scikit-learn/TensorFlow/PyTorch → Serve Model** (blocks AI endpoints & demos)
- **Docker Image → Kubernetes/minikube** (blocks K8s practice & scaling)
- **OpenAI + LangChain → RAG** (blocks LLM/RAG demo)

---

## Minimal Critical Path (Interview-Ready)

1. Python env ready → Flask API with 2 endpoints  
2. Dockerize Flask → Push to AWS ECR → Deploy (Lambda/ECS)  
3. Train tiny **scikit-learn** model → expose `/predict` endpoint in Flask  
4. Add **observability** (CloudWatch logs/screenshots)  
5. Optional: minikube deploy + HPA (adds strong differentiation)

---

## Short Table of Prerequisites (keep concise)

| Topic | Must Have Before |
|---|---|
| Flask API | Python setup |
| Django REST | Python setup |
| Dockerize | Flask/Django API |
| AWS ECR | Docker image |
| Lambda/ECS/EKS | ECR image |
| scikit-learn model | NumPy/Pandas |
| Serve ML via API | scikit-learn / TF / PT |
| Kubernetes (minikube) | Docker image |
| HPA | K8s deploy |
| RAG (LangChain) | OpenAI API setup |

---

## Notes (for quick recall)

- **If Docker isn’t done**, you can’t deploy to **ECR/ECS/EKS** or practice **K8s**.  
- **If no basic ML model**, your AI endpoint demo is blocked — finish **scikit-learn** first.  
- **If Flask/Django isn’t running locally**, **everything else** is blocked.  
- **RAG** is optional, but it strongly boosts **AI Architect** credibility.

---

Tip: Print this page or keep it pinned beside the 10-Day plan in your repo.
