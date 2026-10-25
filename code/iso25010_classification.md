# ISO/IEC 25010 Quality Model Classification for MedBook NFRs

**Lab 06 — Member 1: System Analyst & Simulation Engineer**  
**Author:** Hồ Điền Hùng (Leader)  
**Project Case Study:** MedBook – Online Medical Appointment Booking System  
**Dataset:** `datasets/nonfunctional_requirements.csv`

---

## 1. Overview of ISO/IEC 25010 System and Software Quality Model

The ISO/IEC 25010 standard defines a software product quality model comprising **8 primary quality characteristics** (Performance Efficiency, Compatibility, Usability, Reliability, Security, Maintainability, Flexibility/Portability, and Functional Suitability), each subdivided into rigorous sub-characteristics. 

In the MedBook clinical appointment platform, non-functional requirements (NFRs) are specified using **SMART** criteria (Specific, Measurable, Achievable, Relevant, Time-bound). Below is the systematic mapping of all 10 project requirements to their corresponding primary characteristics and sub-characteristics under ISO/IEC 25010, along with their engineering justification.

---

## 2. Complete Classification Table

| NFR ID | Attribute Name | SMART Measurement Criterion | ISO/IEC 25010 Primary Characteristic | ISO/IEC 25010 Sub-characteristic | Verification Method | Priority | Architectural / Engineering Justification |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **NFR-001** | Performance | Doctor-search page response time $\le 2\text{s}$ with 500 concurrent users. | **Performance Efficiency** | **Time Behaviour** | Load testing | High | Evaluates degree to which response times meet clinical browsing requirements under peak concurrent user loads. |
| **NFR-002** | Availability | The system shall achieve $\ge 99.5\%$ monthly uptime (excluding scheduled maintenance). | **Reliability** | **Availability** | 30-day uptime monitoring / Simulation | High | Measures the proportion of operational time where MedBook is accessible and ready to process appointment reservations. |
| **NFR-003** | Security | Medical record data shall be encrypted with AES-256 at rest and TLS 1.2+ in transit. | **Security** | **Confidentiality** | Configuration review + penetration test | High | Guarantees patient electronic health records (EHR) remain inaccessible to unauthorized eavesdroppers and attackers. |
| **NFR-004** | Data privacy | The system shall follow data-minimization principles for personal data. | **Security** *(Compliance / Operational Context)* | **Confidentiality** / **Accountability** | Compliance checklist review | High | Ensures collection and retention of patient identifiable data is strictly confined to what is legally and medically necessary. |
| **NFR-005** | Scalability | The system shall handle 3x booking volume growth over 12 months without architecture changes. | **Performance Efficiency** | **Capacity** | Incremental load testing | Medium | Assesses the upper limit of transaction volume and concurrent appointments sustainable by existing database and server nodes. |
| **NFR-006** | Usability | A first-time user shall complete their first booking in $\le 3$ minutes without guidance. | **Usability** | **Learnability** / **Operability** | Usability testing | Medium | Validates how readily new patients can navigate appointment workflows independently without errors or cognitive strain. |
| **NFR-007** | Safety | The system shall raise a conflict warning within $\le 1$ second when a doctor double-booking is detected. | **Reliability** / **Functional Safety** | **Fault Tolerance** / **Time Behaviour** | Booking-conflict scenario testing | High | Assures system resilience against concurrent appointment race conditions, preserving clinic schedule integrity without scheduling conflicts. |
| **NFR-008** | Recoverability | The system shall recover booking data within 15 minutes after an incident (RPO $\le 5\text{min}$, RTO $\le 15\text{min}$). | **Reliability** | **Recoverability** | Disaster-recovery drill | High | Quantifies recovery time objective (RTO) and recovery point objective (RPO) to minimize clinical booking loss during server outages. |
| **NFR-009** | Maintainability | Source code shall achieve $\ge 80\%$ unit-test coverage for the booking module. | **Maintainability** | **Testability** / **Modifiability** | CI coverage report | Medium | Guarantees test suite rigor, enabling agile refactoring and low regression probability across core reservation business logic. |
| **NFR-010** | Compatibility | The UI shall work correctly on Chrome, Safari, Edge versions released in the last 2 years. | **Compatibility** | **Interoperability** / **Co-existence** | Cross-browser testing | Low | Ensures uniform front-end rendering and client-side script execution across standard browser runtimes and operating platforms. |

---

## 3. Structural Summary by ISO/IEC 25010 Quality Characteristics

```
ISO/IEC 25010 System Quality Model (MedBook Scope)
│
├── 1. Performance Efficiency
│   ├── Time Behaviour: NFR-001 (Doctor search latency <= 2s at 500 users)
│   └── Capacity: NFR-005 (3x booking volume scaling)
│
├── 2. Reliability
│   ├── Availability: NFR-002 (>= 99.5% monthly uptime)
│   ├── Fault Tolerance / Safety: NFR-007 (Conflict detection <= 1s)
│   └── Recoverability: NFR-008 (RPO <= 5 min, RTO <= 15 min)
│
├── 3. Security
│   ├── Confidentiality: NFR-003 (AES-256 rest, TLS 1.2+ transit)
│   └── Confidentiality & Compliance: NFR-004 (Data minimization principles)
│
├── 4. Usability
│   └── Learnability & Operability: NFR-006 (First booking <= 3 min without guidance)
│
├── 5. Maintainability
│   └── Testability: NFR-009 (>= 80% booking unit test coverage)
│
└── 6. Compatibility
    └── Interoperability / Multi-browser Support: NFR-010 (Chrome, Safari, Edge modern versions)
```

---

## 4. Verification & Validation Summary

1. **Quantification Rigor:** Every NFR translates broad qualitative intentions into measurable numbers (percentiles $p50, p95, p99$, percentages $\%$, timeouts in seconds/minutes).
2. **Automated Verification:** Critical high-priority NFRs (NFR-001, NFR-007, and self-chosen NFR-002) are integrated into automated verification via Python simulation in `code/nfr_validator.py`.
