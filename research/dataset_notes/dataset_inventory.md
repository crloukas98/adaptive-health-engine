# Dataset Inventory

## Project Goal

Build an explainable AI system that models health behavior and recommends sustainable interventions based on physiological and behavioral profiles.

---

# Dataset 1: NHANES

## Purpose

Physiological and lifestyle foundation.

## Source

National Health and Nutrition Examination Survey.

## Role in model

Provides:
- body measurements
- metabolic markers
- dietary information
- physical activity
- demographics

## Expected Variables

### Demographics
- age
- sex
- education
- socioeconomic factors

### Body composition
- height
- weight
- BMI
- waist circumference

### Metabolic health
- glucose
- insulin-related variables
- cholesterol
- blood pressure

### Lifestyle
- dietary intake
- physical activity
- smoking
- sleep

## Model Features Generated

- metabolic risk index
- activity capacity index
- nutrition profile
- baseline health state

---

# Dataset 2: ADHD / Executive Function Dataset

## Purpose

Behavioral and cognitive profile.

## Role in model

Provides:
- ADHD traits
- executive dysfunction
- impulsivity
- attention regulation

## Model Features Generated

- executive function index
- impulsivity index
- attention regulation profile

---

# Dataset 3: Activity / Wearable Dataset

## Purpose

Real-world behavior patterns.

## Role in model

Provides:
- activity patterns
- sedentary behavior
- sleep patterns

## Model Features Generated

- activity consistency
- routine stability
- daily variability

---

# Dataset 4: Intervention Knowledge Base

## Purpose

Defines possible recommendations.

## Examples

Nutrition:
- low preparation diet
- structured meal plan
- flexible calorie approach

Training:
- resistance training
- walking program
- short frequent workouts

## Model Role

Maps person profiles to intervention compatibility.

---

# Integration Strategy

Raw datasets
        |
        ↓
Feature engineering
        |
        ↓
Unified person representation
        |
        ↓
Behavioral profiles
        |
        ↓
Recommendation engine