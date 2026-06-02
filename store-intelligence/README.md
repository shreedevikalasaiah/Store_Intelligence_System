# Store Intelligence System

## Overview
This project is a real-time retail analytics system that processes CCTV feeds and generates store intelligence metrics like:

- Footfall tracking
- Conversion rate estimation
- Customer journey funnel
- Anomaly detection (sudden crowd spikes or drops)
- Session tracking

## Architecture

- **Pipeline Layer**: Object detection + tracking from CCTV videos
- **Backend (FastAPI)**: Metrics computation and API exposure
- **Analytics Engine**: Funnel + anomaly detection
- **Event Store**: JSONL-based event logging
- **Dockerized Deployment**

## Tech Stack
- Python
- FastAPI
- OpenCV (assumed in pipeline)
- Docker
- Pandas / NumPy

## Modules

### pipeline/
Handles video processing and event generation.

### app/
Handles API, metrics, ingestion, anomalies, funnel logic.

### tests/
Unit tests for pipeline and analytics.

### docs/
Design decisions and trade-offs.

## How to Run

```bash
docker-compose up --build
