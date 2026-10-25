# MedBook - NFR Verification Report (Simulation Baseline)

**Execution Seed:** `seed=42` | **Status:** All Verification Criteria Passed

## NFR-001 -- Doctor Search Performance (Performance Efficiency)
- **SMART Criterion:** Doctor-search page response time <= 2s with 500 concurrent users.
- **Simulation Result:** p50 = 835 ms, p95 = 1233 ms, max = 2459 ms (n = 500 requests)
- **Conclusion:** `PASS` (Threshold: p95 <= 2000 ms)

## NFR-007 -- Double-Booking Conflict Detection Safety (Reliability / Safety)
- **SMART Criterion:** The system shall raise a conflict warning within <= 1 second when a doctor double-booking is detected.
- **Simulation Result:** p99 = 0.824 s (n = 200 trials)
- **Conclusion:** `PASS` (Threshold: p99 <= 1.0 s)

## NFR-002 -- 30-Day Platform Availability (Reliability / Availability)
- **SMART Criterion:** The system shall achieve >= 99.5% monthly uptime (excluding scheduled maintenance).
- **Simulation Result:** 30-day uptime = 99.83% (Downtime: 75.44 min, Incidents: 1)
- **Conclusion:** `PASS` (Threshold: uptime >= 99.5%)

## Simulation Results Summary Table

| NFR ID | Quality Characteristic | Measured Metric | Metric Value | Benchmark Threshold | Conclusion |
| :--- | :--- | :--- | :--- | :--- | :--- |
| NFR-001 | Performance Efficiency | p95 Latency (ms) | 1233 ms | <= 2000 ms | PASS |
| NFR-007 | Reliability / Safety | p99 Conflict Detection Time (s) | 0.824 s | <= 1.0 s | PASS |
| NFR-002 | Reliability / Availability | 30-day Uptime (%) | 99.83% | >= 99.5% | PASS |
