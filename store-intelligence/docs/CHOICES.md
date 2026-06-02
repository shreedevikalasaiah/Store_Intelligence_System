

```md
# Key Design Choices

## 1. Event-based architecture
We chose event-based logging (JSONL) instead of direct DB writes because:
- scalable
- easy replay/debugging
- decouples pipeline from analytics

## 2. Lightweight FastAPI backend
FastAPI was chosen due to:
- high performance
- async support
- easy API generation for metrics layer

## 3. Rule-based anomaly detection
Instead of heavy ML models, we used statistical rules:
- moving average spikes
- threshold-based detection
Reason: reduces compute cost and improves interpretability
