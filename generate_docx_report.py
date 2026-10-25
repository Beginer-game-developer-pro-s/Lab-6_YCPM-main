#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
generate_docx_report.py
Generates the professional Word document (.docx) for Lab 06:
Lab06_Report_Group06.docx
"""

import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn
import os

def set_cell_background(cell, fill_hex):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>')
    tcPr.append(shd)

def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = parse_xml(
        f'<w:tcMar {nsdecls("w")}>'
        f'<w:top w:w="{top}" w:type="dxa"/>'
        f'<w:bottom w:w="{bottom}" w:type="dxa"/>'
        f'<w:left w:w="{left}" w:type="dxa"/>'
        f'<w:right w:w="{right}" w:type="dxa"/>'
        f'</w:tcMar>'
    )
    tcPr.append(tcMar)

def add_callout(doc, text, title=""):
    table = doc.add_table(rows=1, cols=1)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = False
    table.columns[0].width = Inches(6.5)
    cell = table.cell(0, 0)
    set_cell_background(cell, "F0F4F8")
    set_cell_margins(cell, top=140, bottom=140, left=200, right=200)
    
    # Left border highlight
    tcPr = cell._tc.get_or_add_tcPr()
    borders = parse_xml(
        f'<w:tcBorders {nsdecls("w")}>'
        f'<w:top w:val="none"/>'
        f'<w:left w:val="single" w:sz="24" w:space="0" w:color="003366"/>'
        f'<w:bottom w:val="none"/>'
        f'<w:right w:val="none"/>'
        f'</w:tcBorders>'
    )
    tcPr.append(borders)
    
    p = cell.paragraphs[0]
    p.paragraph_format.space_before = Pt(2)
    p.paragraph_format.space_after = Pt(2)
    p.paragraph_format.line_spacing = 1.15
    if title:
        run_t = p.add_run(f"{title}\n")
        run_t.font.bold = True
        run_t.font.color.rgb = RGBColor(0, 51, 102)
        run_t.font.size = Pt(10)
    run = p.add_run(text)
    run.font.size = Pt(9.5)
    run.font.color.rgb = RGBColor(33, 37, 41)
    doc.add_paragraph()

def build_word_report(output_path="Lab06_Report_Group06.docx"):
    doc = docx.Document()
    
    # Page Margins: 1 inch (72 pt)
    sections = doc.sections
    for section in sections:
        section.top_margin = Inches(1.0)
        section.bottom_margin = Inches(1.0)
        section.left_margin = Inches(1.0)
        section.right_margin = Inches(1.0)
        
        # Header & Footer
        header = section.header
        hp = header.paragraphs[0]
        hp.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        hrun = hp.add_run("PHENIKAA UNIVERSITY • CSE703095 SOFTWARE REQUIREMENTS • LAB 06")
        hrun.font.name = "Calibri"
        hrun.font.size = Pt(8.5)
        hrun.font.color.rgb = RGBColor(120, 120, 120)
        
        footer = section.footer
        fp = footer.paragraphs[0]
        fp.alignment = WD_ALIGN_PARAGRAPH.CENTER
        frun = fp.add_run("MedBook Online Appointment Booking System — Lab 06 Comprehensive Report")
        frun.font.name = "Calibri"
        frun.font.size = Pt(8.5)
        frun.font.color.rgb = RGBColor(120, 120, 120)

    # Base Styles
    normal_style = doc.styles['Normal']
    normal_style.font.name = 'Calibri'
    normal_style.font.size = Pt(11)
    normal_style.font.color.rgb = RGBColor(40, 40, 40)
    
    # ------------------ COVER / TITLE SECTION ------------------
    p_uni = doc.add_paragraph()
    p_uni.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_uni = p_uni.add_run("PHENIKAA UNIVERSITY\nSCHOOL OF INFORMATION SYSTEMS")
    r_uni.font.bold = True
    r_uni.font.size = Pt(13)
    r_uni.font.color.rgb = RGBColor(0, 51, 102)
    p_uni.paragraph_format.space_after = Pt(4)
    
    p_course = doc.add_paragraph()
    p_course.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_course = p_course.add_run("COURSE: CSE703095 — SOFTWARE REQUIREMENTS")
    r_course.font.bold = True
    r_course.font.size = Pt(11)
    r_course.font.color.rgb = RGBColor(70, 70, 70)
    p_course.paragraph_format.space_after = Pt(18)
    
    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_title = p_title.add_run("LAB 06: NON-FUNCTIONAL REQUIREMENTS &\nSTOCHASTIC SIMULATION REPORT")
    r_title.font.bold = True
    r_title.font.size = Pt(18)
    r_title.font.color.rgb = RGBColor(0, 51, 102)
    p_title.paragraph_format.space_after = Pt(8)
    
    p_case = doc.add_paragraph()
    p_case.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_case = p_case.add_run("Case Study: MedBook – Online Medical Appointment Booking System\nGroup: Group 06 | Date of Submission: October 25, 2026")
    r_case.font.italic = True
    r_case.font.size = Pt(10.5)
    r_case.font.color.rgb = RGBColor(90, 90, 90)
    p_case.paragraph_format.space_after = Pt(24)
    
    # Group Members Table
    doc.add_heading("Project Team & RACI Assignment Matrix", level=2)
    p_t = doc.add_paragraph("The project tasks were formally allocated according to the RACI governance model:")
    p_t.paragraph_format.space_after = Pt(8)
    
    raci_table = doc.add_table(rows=4, cols=4)
    raci_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    raci_headers = ["Member Name", "Assigned Role", "RACI Responsibility", "Core Deliverables & Focus"]
    for j, h in enumerate(raci_headers):
        cell = raci_table.cell(0, j)
        cell.text = h
        set_cell_background(cell, "003366")
        set_cell_margins(cell, top=120, bottom=120, left=120, right=120)
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        for r in p.runs:
            r.font.bold = True
            r.font.color.rgb = RGBColor(255, 255, 255)
            r.font.size = Pt(9.5)
            
    members_data = [
        ("Hồ Điền Hùng", "Member 1 (Leader)\nSystem Analyst & Dev", "Accountable &\nResponsible", "ISO/IEC 25010 Classification, Self-chosen NFR-002 mathematical modeling & Python simulator extension (nfr_validator.py)."),
        ("Trần Doãn Việt Anh", "Member 2\nSimulation & Data Analyst", "Responsible", "Baseline execution (NFR-001/007, seed=42), empirical measurement analysis, theoretical essay 'Why a Fixed Seed Matters' & multi-seed verification."),
        ("Cấn Đại Dương", "Member 3\nTechnical Writer & QA", "Responsible &\nQuality Assurer", "Report integration, academic formatting, results consolidation, Self-Assessment Rubric scoring (10.0/10.0) & deliverable verification.")
    ]
    
    for i, data in enumerate(members_data, start=1):
        bg = "F9FBFD" if i % 2 == 1 else "FFFFFF"
        for j, val in enumerate(data):
            cell = raci_table.cell(i, j)
            cell.text = val
            set_cell_background(cell, bg)
            set_cell_margins(cell, top=100, bottom=100, left=120, right=120)
            p = cell.paragraphs[0]
            if j in (0, 1, 2):
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            for r in p.runs:
                r.font.size = Pt(9)
                if j == 0:
                    r.font.bold = True
                    
    doc.add_paragraph().paragraph_format.space_after = Pt(12)
    
    # ------------------ SECTION 1 ------------------
    h1 = doc.add_heading("1. Task 1: ISO/IEC 25010 Quality Model Classification", level=1)
    h1.paragraph_format.space_before = Pt(14)
    h1.paragraph_format.space_after = Pt(6)
    
    p = doc.add_paragraph(
        "The ISO/IEC 25010 standard defines a software product quality model comprising 8 primary characteristics: "
        "Performance Efficiency, Compatibility, Usability, Reliability, Security, Maintainability, Flexibility/Portability, "
        "and Functional Suitability. In medical scheduling architectures such as MedBook, ambiguous non-functional statements "
        "create severe engineering risks. Therefore, each requirement from the project dataset (datasets/nonfunctional_requirements.csv) "
        "is mapped onto the ISO/IEC 25010 taxonomy and quantified via SMART (Specific, Measurable, Achievable, Relevant, Time-bound) criteria."
    )
    p.paragraph_format.line_spacing = 1.15
    p.paragraph_format.space_after = Pt(8)
    
    # ISO Table
    iso_headers = ["NFR ID", "Attribute", "SMART Measurement Criterion", "ISO 25010 Primary", "Sub-characteristic", "Method", "Pri", "Engineering Justification"]
    nfr_rows = [
        ("NFR-001", "Performance", "Doctor-search page response time <= 2s with 500 concurrent users.", "Performance Efficiency", "Time Behaviour", "Load testing", "High", "Guarantees search response latency stays sub-second under peak clinic booking hours."),
        ("NFR-002", "Availability", "The system shall achieve >= 99.5% monthly uptime (excluding scheduled maintenance).", "Reliability", "Availability", "30-day uptime monitoring", "High", "Assures continuous patient booking readiness around the clock without unhandled outages."),
        ("NFR-003", "Security", "Medical record data shall be encrypted with AES-256 at rest and TLS 1.2+ in transit.", "Security", "Confidentiality", "Config review + pen test", "High", "Guarantees patient electronic medical records remain invulnerable to packet eavesdropping."),
        ("NFR-004", "Data privacy", "The system shall follow data-minimization principles for personal data.", "Security", "Confidentiality / Accountability", "Compliance checklist review", "High", "Strictly confines patient identifiable data to what is legally and clinically required."),
        ("NFR-005", "Scalability", "The system shall handle 3x booking volume growth over 12 months without architecture changes.", "Performance Efficiency", "Capacity", "Incremental load testing", "Med", "Assesses horizontal database indexing and server cluster capacity during business growth."),
        ("NFR-006", "Usability", "A first-time user shall complete their first booking in <= 3 minutes without guidance.", "Usability", "Learnability / Operability", "Usability user testing", "Med", "Validates intuitive patient navigation across booking wizard steps without cognitive friction."),
        ("NFR-007", "Safety", "The system shall raise a conflict warning within <= 1 second when a doctor double-booking is detected.", "Reliability / Safety", "Fault Tolerance / Time Behaviour", "Conflict scenario testing", "High", "Prevents concurrent double-booking race conditions through rapid transactional validation."),
        ("NFR-008", "Recoverability", "The system shall recover booking data within 15 minutes after an incident (RPO <= 5min, RTO <= 15min).", "Reliability", "Recoverability", "Disaster-recovery drill", "High", "Enforces automated database replica failover with minimal transaction data loss."),
        ("NFR-009", "Maintainability", "Source code shall achieve >= 80% unit-test coverage for the booking module.", "Maintainability", "Testability / Modifiability", "CI coverage report", "Med", "Guarantees high test harness coverage, enabling safe agile refactoring in core booking code."),
        ("NFR-010", "Compatibility", "The UI shall work correctly on Chrome, Safari, Edge versions released in the last 2 years.", "Compatibility", "Interoperability / Co-existence", "Cross-browser testing", "Low", "Ensures front-end layout fidelity and client script execution across major browser runtimes.")
    ]
    
    iso_table = doc.add_table(rows=len(nfr_rows) + 1, cols=len(iso_headers))
    iso_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    for j, h in enumerate(iso_headers):
        c = iso_table.cell(0, j)
        c.text = h
        set_cell_background(c, "003366")
        set_cell_margins(c, top=100, bottom=100, left=80, right=80)
        p = c.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        for r in p.runs:
            r.font.bold = True
            r.font.color.rgb = RGBColor(255, 255, 255)
            r.font.size = Pt(8.5)
            
    for i, row_data in enumerate(nfr_rows, start=1):
        bg = "F9FBFD" if i % 2 == 1 else "FFFFFF"
        for j, val in enumerate(row_data):
            c = iso_table.cell(i, j)
            c.text = val
            set_cell_background(c, bg)
            set_cell_margins(c, top=80, bottom=80, left=80, right=80)
            p = c.paragraphs[0]
            if j in (0, 3, 5, 6):
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            for r in p.runs:
                r.font.size = Pt(8)
                if j == 0:
                    r.font.bold = True

    doc.add_paragraph().paragraph_format.space_after = Pt(12)
    
    # ------------------ SECTION 2 ------------------
    h2 = doc.add_heading("2. Task 2: Baseline Simulation & Experimental Foundation", level=1)
    h2.paragraph_format.space_before = Pt(14)
    h2.paragraph_format.space_after = Pt(6)
    
    p = doc.add_paragraph(
        "To empirically validate high-priority NFRs, stochastic simulation was implemented in Python using a fixed seed (seed=42). "
        "The baseline verification script evaluates two critical operational thresholds:\n"
        "• NFR-001 (Doctor search latency under 500 concurrent users): p95 <= 2000 ms.\n"
        "• NFR-007 (Double-booking conflict detection safety): p99 <= 1.0 s."
    )
    p.paragraph_format.line_spacing = 1.15
    p.paragraph_format.space_after = Pt(8)
    
    # Insert Figure 1 if exists
    fig1_path = os.path.join(os.path.dirname(__file__), "figures", "simulation_results_nfr001_nfr007.png")
    if os.path.isfile(fig1_path):
        p_img = doc.add_paragraph()
        p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_img.paragraph_format.space_before = Pt(6)
        p_img.paragraph_format.space_after = Pt(4)
        run_img = p_img.add_run()
        run_img.add_picture(fig1_path, width=Inches(6.2))
        p_cap = doc.add_paragraph("Figure 1: Stochastic Simulation Distributions for NFR-001 (p95=1233ms) and NFR-007 (p99=0.824s)")
        p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_cap.runs[0].font.size = Pt(8.5)
        p_cap.runs[0].font.italic = True
        p_cap.paragraph_format.space_after = Pt(10)
        
    doc.add_heading("Deep-Dive Treatise: Why a Fixed Seed Matters", level=2)
    p_auth = doc.add_paragraph("Author: Trần Doãn Việt Anh (Member 2 — Simulation & Data Analyst)")
    p_auth.runs[0].font.italic = True
    p_auth.runs[0].font.size = Pt(9.5)
    p_auth.runs[0].font.color.rgb = RGBColor(90, 90, 90)
    
    essay_text = (
        "Stochastic NFR simulations do not observe a live clinic; they draw latency and detection times from a pseudo-random generator. "
        "Python’s random module is a deterministic Mersenne Twister. Calling random.seed(42) writes a known internal state, so every "
        "later random.random() and random.uniform() call is a pure function of that state and of the algorithm. The doctor-search load test "
        "(NFR-001, n = 500) and the double-booking detection test (NFR-007, n = 200) therefore become repeatable experiments rather than one-off anecdotes.\n\n"
        "1. Reproducibility: With seed 42, any machine that re-runs the validator obtains the identical statistics: NFR-001 p50 = 835 ms, "
        "p95 = 1233 ms, max = 2459 ms, and NFR-007 p99 = 0.824 s. Both meet their SMART thresholds (p95 <= 2000 ms; p99 <= 1.0 s) and are "
        "recorded as PASS. If the seed were omitted, a later execution could shift tail percentiles purely by chance, making 'PASS/FAIL' untrustworthy.\n\n"
        "2. Peer Review: Instructors and testers can execute the same script and match published figures sample-for-sample. A shared seed prevents "
        "cherry-picking a lucky draw and turns the report into an inspectable artifact: disagreement indicates a code or environment difference, not chance.\n\n"
        "3. Baseline Comparison: Seed 42 freezes the control condition for future optimization. Caching, indexing, or a faster conflict check can "
        "be judged only if the random stream is held constant; otherwise a drop in p95 might be luck. Independent multi-seed trials show that PASS "
        "is not an artifact of 42 alone, but the official baseline stays locked so that before/after deltas are attributable to the system, not the generator."
    )
    add_callout(doc, essay_text, title="Treatise: Scientific and Engineering Significance of Fixed Seed (random.seed(42))")
    
    doc.add_heading("Multi-Seed Sensitivity and Stability Analysis", level=2)
    p = doc.add_paragraph(
        "To confirm that the PASS verdict is robust and not an artifact of seed 42, Member 2 evaluated 5 diverse seeds "
        "(seeds ∈ {1, 7, 42, 100, 2026}). Across all runs, NFR-001 p95 remained tightly bounded between 1231.5 ms and 1236.1 ms "
        "(mean 1232.9 ms, σ = 1.7 ms), while NFR-007 p99 ranged from 0.824 s to 0.845 s (mean 0.837 s, σ = 0.007 s). "
        "Both achieved a 100% PASS rate across all random streams."
    )
    p.paragraph_format.line_spacing = 1.15
    p.paragraph_format.space_after = Pt(12)
    
    # ------------------ SECTION 3 ------------------
    h3 = doc.add_heading("3. Task 3: Self-Chosen NFR Modeling & Simulation (NFR-002)", level=1)
    h3.paragraph_format.space_before = Pt(14)
    h3.paragraph_format.space_after = Pt(6)
    
    p = doc.add_paragraph(
        "Requirement Selection: NFR-002 (System Availability) was chosen by Member 1 (Hồ Điền Hùng) for comprehensive mathematical "
        "modeling and simulation extension. The SMART criterion dictates: 'The system shall achieve >= 99.5% monthly uptime (excluding scheduled maintenance).'\n\n"
        "Mathematical Scenario Formulation:\n"
        "• Operating Window: 30 continuous operational days (T_total = 30 * 24 * 60 = 43,200 minutes).\n"
        "• Incident Process: Each day d ∈ {1..30} faces an unhandled service incident modeled as a Bernoulli random variable with p_incident = 0.008 (approx. 0.8% failure probability per day).\n"
        "• Downtime Distribution: Unscheduled incident downtime duration D_i is sampled from Uniform(15, 90) minutes, representing container restarts and database replica promotions.\n"
        "• Uptime Percentage: Computed as 100 * (43,200 - ∑ D_i) / 43,200. Target threshold >= 99.50%."
    )
    p.paragraph_format.line_spacing = 1.15
    p.paragraph_format.space_after = Pt(8)
    
    code_snippet = (
        "def simulate_availability(days=30, p_incident=0.008, seed=42):\n"
        "    random.seed(seed)\n"
        "    total_minutes = days * 24 * 60  # 43,200 minutes\n"
        "    downtime = 0.0\n"
        "    incident_log = []\n"
        "    for day in range(1, days + 1):\n"
        "        if random.random() < p_incident:\n"
        "            duration = random.uniform(15.0, 90.0)\n"
        "            downtime += duration\n"
        "            incident_log.append({'day': day, 'duration_min': round(duration, 2)})\n"
        "    uptime_pct = 100.0 * (total_minutes - downtime) / total_minutes\n"
        "    return {'uptime_pct': uptime_pct, 'downtime_minutes': downtime, 'pass': uptime_pct >= 99.5}"
    )
    add_callout(doc, code_snippet, title="Listing 1: Python Simulation Algorithm for NFR-002 (simulate_availability)")
    
    # Insert Figure 2 if exists
    fig2_path = os.path.join(os.path.dirname(__file__), "figures", "simulation_availability_and_stability.png")
    if os.path.isfile(fig2_path):
        p_img = doc.add_paragraph()
        p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_img.paragraph_format.space_before = Pt(6)
        p_img.paragraph_format.space_after = Pt(4)
        run_img = p_img.add_run()
        run_img.add_picture(fig2_path, width=Inches(6.2))
        p_cap = doc.add_paragraph("Figure 2: 30-Day Platform Uptime Breakdown (99.83% PASS) and Multi-Seed Stability Verification")
        p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_cap.runs[0].font.size = Pt(8.5)
        p_cap.runs[0].font.italic = True
        p_cap.paragraph_format.space_after = Pt(10)
        
    p_res = doc.add_paragraph(
        "Simulation Execution Result: Under the baseline seed 42, exactly one incident occurred on Day 20 with a duration of 75.44 minutes. "
        "Total operational uptime reached 99.83% (43,124.56 minutes operational), safely exceeding the 99.50% requirement by +0.33%. "
        "The allowable monthly error budget is 216 minutes; consuming only 75.44 minutes leaves 65.1% of the safety buffer intact."
    )
    p_res.paragraph_format.line_spacing = 1.15
    p_res.paragraph_format.space_after = Pt(12)
    
    # ------------------ SECTION 4 ------------------
    h4 = doc.add_heading("4. Task 4: Consolidated Simulation Results & Verification Synthesis", level=1)
    h4.paragraph_format.space_before = Pt(14)
    h4.paragraph_format.space_after = Pt(6)
    
    p = doc.add_paragraph(
        "The table below consolidates all empirical simulation findings across the MedBook non-functional requirement test harness. "
        "All three evaluated NFRs have achieved 100% compliance with established benchmarks."
    )
    p.paragraph_format.line_spacing = 1.15
    p.paragraph_format.space_after = Pt(8)
    
    summary_headers = ["NFR ID", "Quality Characteristic", "Measured Metric", "Empirical Value", "Target Benchmark", "Verdict"]
    summary_data = [
        ("NFR-001", "Performance Efficiency (Time Behaviour)", "Doctor search p95 latency", "1233 ms (p50=835ms, max=2459ms)", "p95 <= 2000 ms", "PASS"),
        ("NFR-007", "Reliability / Safety (Fault Tolerance)", "Conflict detection p99 time", "0.824 s (n=200 trials)", "p99 <= 1.0 s", "PASS"),
        ("NFR-002", "Reliability (Availability)", "30-day operational uptime", "99.83% (downtime=75.44 min)", "Uptime >= 99.50%", "PASS")
    ]
    
    sum_table = doc.add_table(rows=len(summary_data) + 1, cols=len(summary_headers))
    sum_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    for j, h in enumerate(summary_headers):
        c = sum_table.cell(0, j)
        c.text = h
        set_cell_background(c, "003366")
        set_cell_margins(c, top=110, bottom=110, left=100, right=100)
        p = c.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        for r in p.runs:
            r.font.bold = True
            r.font.color.rgb = RGBColor(255, 255, 255)
            r.font.size = Pt(9)
            
    for i, row_data in enumerate(summary_data, start=1):
        bg = "F9FBFD" if i % 2 == 1 else "FFFFFF"
        for j, val in enumerate(row_data):
            c = sum_table.cell(i, j)
            c.text = val
            set_cell_background(c, bg)
            set_cell_margins(c, top=90, bottom=90, left=100, right=100)
            p = c.paragraphs[0]
            if j in (0, 3, 4, 5):
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            for r in p.runs:
                r.font.size = Pt(8.5)
                if j == 0:
                    r.font.bold = True
                if j == 5:
                    r.font.bold = True
                    r.font.color.rgb = RGBColor(40, 167, 69)

    doc.add_paragraph().paragraph_format.space_after = Pt(12)
    
    # ------------------ SECTION 5 ------------------
    h5 = doc.add_heading("5. Task 5: Self-Assessment Rubric & Quality Gate Verification", level=1)
    h5.paragraph_format.space_before = Pt(14)
    h5.paragraph_format.space_after = Pt(6)
    
    p = doc.add_paragraph(
        "In accordance with course grading guidelines, Group 06 has conducted a rigorous self-assessment across all four rubric criteria. "
        "The project has achieved an exemplary score of 10.0 / 10.0."
    )
    p.paragraph_format.line_spacing = 1.15
    p.paragraph_format.space_after = Pt(8)
    
    rubric_headers = ["Criterion", "Max Score", "Self Score", "Detailed Engineering Notes & Evidence"]
    rubric_data = [
        ("ISO 25010 classification", "2.0", "2.0", "All 10 NFRs comprehensively mapped onto primary & sub-characteristics with detailed architectural rationales."),
        ("NFR-001, NFR-007 simulation", "2.5", "2.5", "Baseline executed with seed=42; 3-pillar theoretical essay completed; multi-seed validation demonstrates 100% stability."),
        ("Self-chosen NFR + simulation", "3.0", "3.0", "NFR-002 mathematically modeled using Bernoulli & Uniform processes; Python function implemented and verified (99.83% PASS)."),
        ("Presentation & Formatting", "2.5", "2.5", "Report strictly adheres to Phenikaa University academic format, including data visualizations, math notation, and multi-format exports."),
        ("Total Score", "10.0", "10.0 / 10.0", "Exemplary fulfillment across all technical, analytical, and documentation requirements.")
    ]
    
    rub_table = doc.add_table(rows=len(rubric_data) + 1, cols=len(rubric_headers))
    rub_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    for j, h in enumerate(rubric_headers):
        c = rub_table.cell(0, j)
        c.text = h
        set_cell_background(c, "003366")
        set_cell_margins(c, top=110, bottom=110, left=100, right=100)
        p = c.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        for r in p.runs:
            r.font.bold = True
            r.font.color.rgb = RGBColor(255, 255, 255)
            r.font.size = Pt(9)
            
    for i, row_data in enumerate(rubric_data, start=1):
        bg = "EBF3FA" if i == len(rubric_data) else ("F9FBFD" if i % 2 == 1 else "FFFFFF")
        for j, val in enumerate(row_data):
            c = rub_table.cell(i, j)
            c.text = val
            set_cell_background(c, bg)
            set_cell_margins(c, top=90, bottom=90, left=100, right=100)
            p = c.paragraphs[0]
            if j in (1, 2):
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            for r in p.runs:
                r.font.size = Pt(8.5)
                if i == len(rubric_data):
                    r.font.bold = True
                    if j == 2:
                        r.font.color.rgb = RGBColor(0, 51, 102)

    doc.add_paragraph().paragraph_format.space_after = Pt(14)
    
    # Save document
    doc.save(output_path)
    print(f"[OK] Word report successfully created: {output_path}")

if __name__ == "__main__":
    build_word_report()
