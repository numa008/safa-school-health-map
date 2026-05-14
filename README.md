# Safa School Health Map
Safa School Health Map is an open-source AI-assisted planning tool that maps schools near landfills, dumping corridors, and unmanaged waste zones, generates child-centered climate-health vulnerability scores, and recommends practical interventions for schools, municipalities, and collection networks.
## Problem
Children studying near landfills and unmanaged waste zones in Nepal may face daily exposure to waste burning, polluted surroundings, foul odor, vectors, and unsafe environmental conditions. However, schools and municipalities often lack localized, child-sensitive data to identify exposure hotspots, compare risk across schools, and prioritize preventive action.
## Solution
The project builds a school-level risk-scoring and mapping system that combines:
- GIS/location data
- school survey data
- community hotspot reports
- waste-flow and collection data
- landfill, dumping, and open-burning proximity indicators
The tool classifies schools into exposure categories and provides practical recommendations for local action.
## Technology Approach
The prototype uses AI and data science methods including:
- geospatial analysis to assess school proximity to waste-risk zones
- structured data collection from schools and communities
- a vulnerability scoring model for school-level exposure
- hotspot mapping for landfill, dumping, and open-burning risks
- recommendation logic for preventive waste-management interventions
The solution does not diagnose health conditions. It focuses on identifying and reducing environmental exposure risks affecting children.
## Current Status
The project is at concept and early prototype stage. It builds on Khaalisisi’s existing waste-flow operations, school engagement experience, and recyclable collection network in Nepal. The next stage is to develop the scoring framework, sample dataset, dashboard interface, and pilot implementation with selected landfill-affected and waste-risk schools.
## Planned Pilot
The pilot will focus on selected schools near landfill and unmanaged waste-risk zones in Nepal. The pilot will test:
- school vulnerability scoring
- waste-risk hotspot mapping
- school and community data collection
- dashboard visualization
- practical intervention recommendations
## Open Source Commitment
The core methodology, scoring framework, data templates, documentation, and prototype code will be made open source. Sensitive child, school, community, and operational data will be anonymized, aggregated, or excluded to protect privacy and safety.
## Repository Structure
```text
safa-school-health-map/
├── README.md
├── LICENSE
├── data/
│   └── sample_school_risk_data.csv
├── docs/
│   └── methodology.md
├── src/
│   └── risk_scoring.py
└── dashboard/
    └── dashboard_mockup.md
