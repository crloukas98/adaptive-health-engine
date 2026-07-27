# Adaptive Health Engine

An open-source AI framework for discovering health behavior phenotypes, generating personalized intervention profiles, and building explainable lifestyle recommendations using machine learning and public health datasets.

---

## Overview

Adaptive Health Engine is an open-source machine learning platform designed to explore how physiological, behavioral, and lifestyle factors influence health behavior patterns.

The system uses unsupervised learning to discover population-level health phenotypes and provides individualized recommendations based on the identified profile.

The project combines:

- Public health datasets
- Feature engineering
- Unsupervised machine learning
- Explainable recommendations
- API-based inference
- Automated testing and deployment workflows

---

# Research Question

Can machine learning identify meaningful health behavior profiles and generate personalized intervention strategies that improve the likelihood of sustainable lifestyle change?

---

# Architecture


Public Health Dataset
|
↓
Feature Engineering
|
↓
Behavioral Phenotype Discovery
|
↓
Clustering Model
|
↓
Individual Phenotype Prediction
|
↓
Recommendation Engine
|
↓
FastAPI Health Profile API


---

# Machine Learning Pipeline

## 1. Data Processing

The pipeline integrates public health data and transforms raw variables into structured behavioral and physiological features.

Current features include:

- Age
- Weight
- Height
- BMI
- Activity patterns
- Sedentary behavior
- Moderate activity
- Vigorous activity
- Work-related activity

---

## 2. Phenotype Discovery

Adaptive Health Engine currently uses unsupervised clustering to identify health behavior profiles.

The model discovers patterns without predefined labels.

Example discovered phenotypes:

| Phenotype | Description |
|---|---|
| High adiposity phenotype | Higher BMI patterns requiring sustainable weight reduction strategies |
| Low activity lifestyle phenotype | Reduced activity patterns benefiting from increased movement |
| Higher activity phenotype | More favorable movement profiles |

---

## 3. Individual Prediction

Given a new individual's:

- Age
- Weight
- Height
- Activity score

the engine predicts their phenotype and generates personalized recommendations.

Example:

```json
{
  "phenotype_name": "Low activity lifestyle phenotype",
  "recommendations": [
    "Prioritize sustainable weight reduction and metabolic health.",
    "Preserve muscle mass through resistance training.",
    "Gradually increase daily movement."
  ]
}
API Usage

The project exposes a FastAPI inference API.

Start locally:

uvicorn src.api.app:app --reload

API documentation:

http://localhost:8000/docs

Example request:

curl -X POST \
http://localhost:8000/predict \
-H "Content-Type: application/json" \
-d '{
  "age":28,
  "weight_kg":122,
  "height_cm":183,
  "activity_score":5
}'
Docker Support

The project can run as a portable container.

Build:

docker build -t adaptive-health-engine .

Run:

docker run -p 8000:8000 adaptive-health-engine
Testing

Automated testing is implemented with pytest.

Current tests verify:

Model artifact loading
Phenotype prediction
API endpoint functionality

Run:

pytest -vv
Continuous Integration

GitHub Actions automatically runs:

Dependency installation
Automated tests
Docker image build

on every push to the main branch.

Project Structure
adaptive-health-engine/

├── src/
│   ├── api/
│   ├── inference/
│   ├── models/
│   └── recommendations/
│
├── tests/
├── notebooks/
├── research/
├── Dockerfile
├── requirements.txt
└── README.md
Current Status

Active research and development project.

Implemented:

✅ Health phenotype discovery
✅ Machine learning inference pipeline
✅ Explainable recommendation engine
✅ FastAPI deployment
✅ Docker containerization
✅ Automated testing
✅ Continuous integration

Future Directions

Potential future developments:

Larger longitudinal datasets
Deep learning approaches
Reinforcement learning for intervention optimization
Personalized adherence modeling
Integration with wearable health data
Prospective validation studies
Disclaimer

Adaptive Health Engine is a research prototype.

It is not a medical diagnostic system and does not provide medical advice or treatment recommendations.

License

MIT License