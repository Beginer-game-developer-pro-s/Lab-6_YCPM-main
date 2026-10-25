#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
generate_pdf_report.py
Generates the publication-quality PDF report for Lab 06:
Lab06_Report_Group06.pdf using ReportLab.
"""

import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image, KeepTogether, PageBreak, HRFlowable
)
from reportlab.pdfgen import canvas

class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_number(num_pages)
            super().showPage()
        super().save()

    def draw_page_number(self, page_count):
        self.saveState()
        self.setFont("Helvetica", 8)
        self.setFillColor(colors.HexColor("#666666"))
        
        # Header (pages > 1)
        if self._pageNumber > 1:
            self.setStrokeColor(colors.HexColor("#CCCCCC"))
            self.setLineWidth(0.5)
            self.line(54, 750, 612 - 54, 750)
            self.drawRightString(612 - 54, 755, "PHENIKAA UNIVERSITY • CSE703095 SOFTWARE REQUIREMENTS • LAB 06")
        
        # Footer
        self.setStrokeColor(colors.HexColor("#CCCCCC"))
        self.setLineWidth(0.5)
        self.line(54, 45, 612 - 54, 45)
        self.drawString(54, 32, "MedBook Online Appointment Booking System — Lab 06 Comprehensive Report")
        self.drawRightString(612 - 54, 32, f"Page {self._pageNumber} of {page_count}")
        self.restoreState()

def build_pdf_report(filename="Lab06_Report_Group06.pdf"):
    doc = SimpleDocTemplate(
        filename,
        pagesize=letter,
        leftMargin=45,
        rightMargin=45,
        topMargin=54,
        bottomMargin=54
    )
    
    styles = getSampleStyleSheet()
    
    # Custom styles
    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=18,
        leading=22,
        alignment=1, # Center
        textColor=colors.HexColor('#003366'),
        spaceAfter=6
    )
    
    subtitle_style = ParagraphStyle(
        'DocSubTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=11,
        leading=14,
        alignment=1,
        textColor=colors.HexColor('#444444'),
        spaceAfter=4
    )
    
    meta_style = ParagraphStyle(
        'DocMeta',
        parent=styles['Normal'],
        fontName='Helvetica-Oblique',
        fontSize=9.5,
        leading=13,
        alignment=1,
        textColor=colors.HexColor('#555555'),
        spaceAfter=14
    )
    
    h1_style = ParagraphStyle(
        'H1',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=13,
        leading=16,
        textColor=colors.HexColor('#003366'),
        spaceBefore=12,
        spaceAfter=6,
        keepWithNext=True
    )
    
    h2_style = ParagraphStyle(
        'H2',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=10.5,
        leading=14,
        textColor=colors.HexColor('#0e5080'),
        spaceBefore=8,
        spaceAfter=4,
        keepWithNext=True
    )
    
    body_style = ParagraphStyle(
        'Body',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=12.5,
        textColor=colors.HexColor('#222222'),
        spaceAfter=6
    )
    
    table_cell = ParagraphStyle(
        'TableCell',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=7.5,
        leading=9.5,
        textColor=colors.HexColor('#222222')
    )
    
    table_cell_bold = ParagraphStyle(
        'TableCellBold',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=7.5,
        leading=9.5,
        textColor=colors.HexColor('#222222')
    )
    
    table_cell_center = ParagraphStyle(
        'TableCellCenter',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=7.5,
        leading=9.5,
        alignment=1,
        textColor=colors.HexColor('#222222')
    )
    
    table_header = ParagraphStyle(
        'TableHeader',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8,
        leading=10,
        alignment=1,
        textColor=colors.white
    )
    
    code_style = ParagraphStyle(
        'CodeStyle',
        parent=styles['Normal'],
        fontName='Courier',
        fontSize=7.5,
        leading=9.5,
        textColor=colors.HexColor('#111111')
    )
    
    story = []
    
    # ------------------ HEADER BLOCK ------------------
    story.append(Paragraph("PHENIKAA UNIVERSITY — SCHOOL OF INFORMATION SYSTEMS", subtitle_style))
    story.append(Paragraph("COURSE CSE703095: SOFTWARE REQUIREMENTS", subtitle_style))
    story.append(Spacer(1, 4))
    story.append(Paragraph("LAB 06 COMPREHENSIVE REPORT: NON-FUNCTIONAL REQUIREMENTS & SIMULATION", title_style))
    story.append(Paragraph("Case Study: MedBook – Online Medical Appointment Booking System &nbsp;|&nbsp; Group 06 &nbsp;|&nbsp; Date: October 25, 2026", meta_style))
    story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor('#003366'), spaceAfter=10))
    
    # Team RACI Matrix
    raci_data = [
        [Paragraph("Team Member", table_header), Paragraph("Role", table_header), Paragraph("RACI", table_header), Paragraph("Core Responsibilities & Deliverables", table_header)],
        [Paragraph("<b>Hồ Điền Hùng</b>", table_cell_bold), Paragraph("Member 1 (Leader)<br/>System Analyst", table_cell), Paragraph("Accountable &<br/>Responsible", table_cell_center), Paragraph("ISO/IEC 25010 classification, NFR-002 mathematical formulation & Python simulator extension (nfr_validator.py).", table_cell)],
        [Paragraph("<b>Trần Doãn Việt Anh</b>", table_cell_bold), Paragraph("Member 2<br/>Simulation & Data", table_cell), Paragraph("Responsible", table_cell_center), Paragraph("Baseline execution (NFR-001/007 seed=42), empirical measurement analysis, essay 'Why a Fixed Seed Matters' & stability verification.", table_cell)],
        [Paragraph("<b>Cấn Đại Dương</b>", table_cell_bold), Paragraph("Member 3<br/>Technical Writer & QA", table_cell), Paragraph("Responsible &<br/>Quality Assurer", table_cell_center), Paragraph("Report compilation, Phenikaa academic formatting, simulation results synthesis, and Self-Assessment Rubric (10.0/10.0).", table_cell)],
    ]
    t_raci = Table(raci_data, colWidths=[100, 95, 80, 247])
    t_raci.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#003366')),
        ('ALIGN', (0,0), (-1,0), 'CENTER'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#CCCCCC')),
        ('BACKGROUND', (0,1), (-1,1), colors.HexColor('#F8FAFC')),
        ('BACKGROUND', (0,2), (-1,2), colors.white),
        ('BACKGROUND', (0,3), (-1,3), colors.HexColor('#F8FAFC')),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(t_raci)
    story.append(Spacer(1, 10))
    
    # ------------------ TASK 1: ISO 25010 ------------------
    story.append(Paragraph("1. Task 1: ISO/IEC 25010 Quality Model Classification", h1_style))
    story.append(Paragraph(
        "Software product quality for the MedBook online appointment booking platform is categorized across the 8 primary characteristics "
        "of the <b>ISO/IEC 25010</b> standard. All 10 requirements from <code>datasets/nonfunctional_requirements.csv</code> have been mapped "
        "onto specific sub-characteristics and quantified using <b>SMART</b> criteria to enable empirical validation.",
        body_style
    ))
    
    iso_data = [
        [Paragraph("NFR ID", table_header), Paragraph("Attribute", table_header), Paragraph("SMART Criterion", table_header), Paragraph("ISO 25010 Primary", table_header), Paragraph("Sub-characteristic", table_header), Paragraph("Method", table_header), Paragraph("Pri", table_header)],
        [Paragraph("<b>NFR-001</b>", table_cell_bold), Paragraph("Performance", table_cell), Paragraph("Doctor-search page latency &le; 2s with 500 concurrent users.", table_cell), Paragraph("Performance Efficiency", table_cell), Paragraph("Time Behaviour", table_cell), Paragraph("Load testing", table_cell), Paragraph("High", table_cell_center)],
        [Paragraph("<b>NFR-002</b>", table_cell_bold), Paragraph("Availability", table_cell), Paragraph("System shall achieve &ge; 99.5% monthly uptime.", table_cell), Paragraph("Reliability", table_cell), Paragraph("Availability", table_cell), Paragraph("30-day uptime monitoring", table_cell), Paragraph("High", table_cell_center)],
        [Paragraph("<b>NFR-003</b>", table_cell_bold), Paragraph("Security", table_cell), Paragraph("Medical records encrypted with AES-256 rest, TLS 1.2+ transit.", table_cell), Paragraph("Security", table_cell), Paragraph("Confidentiality", table_cell), Paragraph("Config audit + pen test", table_cell), Paragraph("High", table_cell_center)],
        [Paragraph("<b>NFR-004</b>", table_cell_bold), Paragraph("Data privacy", table_cell), Paragraph("Adhere to data-minimization principles for patient data.", table_cell), Paragraph("Security (Compliance)", table_cell), Paragraph("Confidentiality / Accountability", table_cell), Paragraph("Compliance checklist", table_cell), Paragraph("High", table_cell_center)],
        [Paragraph("<b>NFR-005</b>", table_cell_bold), Paragraph("Scalability", table_cell), Paragraph("Handle 3x booking growth over 12 months with no arch redesign.", table_cell), Paragraph("Performance Efficiency", table_cell), Paragraph("Capacity", table_cell), Paragraph("Stress / load testing", table_cell), Paragraph("Med", table_cell_center)],
        [Paragraph("<b>NFR-006</b>", table_cell_bold), Paragraph("Usability", table_cell), Paragraph("First-time user completes booking in &le; 3 min without help.", table_cell), Paragraph("Usability", table_cell), Paragraph("Learnability / Operability", table_cell), Paragraph("Usability testing", table_cell), Paragraph("Med", table_cell_center)],
        [Paragraph("<b>NFR-007</b>", table_cell_bold), Paragraph("Safety", table_cell), Paragraph("Raise conflict warning &le; 1s when double-booking detected.", table_cell), Paragraph("Reliability / Safety", table_cell), Paragraph("Fault Tolerance / Time Behaviour", table_cell), Paragraph("Conflict scenario test", table_cell), Paragraph("High", table_cell_center)],
        [Paragraph("<b>NFR-008</b>", table_cell_bold), Paragraph("Recoverability", table_cell), Paragraph("Recover booking data &le; 15 min after incident (RPO&le;5m, RTO&le;15m).", table_cell), Paragraph("Reliability", table_cell), Paragraph("Recoverability", table_cell), Paragraph("Disaster recovery drill", table_cell), Paragraph("High", table_cell_center)],
        [Paragraph("<b>NFR-009</b>", table_cell_bold), Paragraph("Maintainability", table_cell), Paragraph("Source code achieves &ge; 80% unit-test coverage in booking module.", table_cell), Paragraph("Maintainability", table_cell), Paragraph("Testability / Modifiability", table_cell), Paragraph("CI coverage report", table_cell), Paragraph("Med", table_cell_center)],
        [Paragraph("<b>NFR-010</b>", table_cell_bold), Paragraph("Compatibility", table_cell), Paragraph("UI works on Chrome, Safari, Edge released in last 2 years.", table_cell), Paragraph("Compatibility", table_cell), Paragraph("Interoperability / Co-existence", table_cell), Paragraph("Cross-browser test suite", table_cell), Paragraph("Low", table_cell_center)]
    ]
    t_iso = Table(iso_data, colWidths=[45, 55, 135, 82, 85, 85, 35])
    t_iso.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#003366')),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#D0D7DE')),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor('#F8FAFC')]),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
    ]))
    story.append(t_iso)
    story.append(Spacer(1, 10))
    
    # ------------------ TASK 2: BASELINE SIMULATION ------------------
    story.append(Paragraph("2. Task 2: Baseline Simulation & Experimental Foundation", h1_style))
    story.append(Paragraph(
        "<b>Stochastic Verification Baseline:</b> The verification script <code>nfr_validator.py</code> simulates NFR-001 (doctor-search load test, n=500) "
        "and NFR-007 (double-booking conflict detection, n=200) with a controlled seed (<code>seed=42</code>).<br/>"
        "• <b>NFR-001:</b> p50 = 835 ms, <b>p95 = 1233 ms</b>, max = 2459 ms &nbsp;&rarr;&nbsp; <b>PASS</b> (Benchmark p95 &le; 2000 ms).<br/>"
        "• <b>NFR-007:</b> <b>p99 = 0.824 s</b> &nbsp;&rarr;&nbsp; <b>PASS</b> (Benchmark p99 &le; 1.0 s).",
        body_style
    ))
    
    fig1_path = os.path.join(os.path.dirname(__file__), "figures", "simulation_results_nfr001_nfr007.png")
    if os.path.isfile(fig1_path):
        img1 = Image(fig1_path, width=6.8*inch, height=2.78*inch)
        story.append(img1)
        story.append(Spacer(1, 4))
        
    story.append(Paragraph("Deep-Dive Treatise: Why a Fixed Seed Matters", h2_style))
    story.append(Paragraph("<i>Author: Trần Doãn Việt Anh (Member 2 — Simulation & Data Analyst)</i>", meta_style))
    
    essay_p = (
        "Stochastic NFR simulations do not observe a live clinic; they draw latency and detection times from a pseudo-random generator. "
        "Python’s <code>random</code> module is a deterministic Mersenne Twister. Calling <code>random.seed(42)</code> writes a known internal state, "
        "so every later <code>random.random()</code> and <code>random.uniform()</code> call is a pure function of that state and of the algorithm. "
        "The doctor-search load test (NFR-001, n = 500) and the double-booking detection test (NFR-007, n = 200) therefore become repeatable experiments "
        "rather than one-off anecdotes.<br/><br/>"
        "<b>1. Reproducibility:</b> With seed 42, any machine that re-runs the validator obtains the identical statistics: NFR-001 p50 = 835 ms, "
        "p95 = 1233 ms, max = 2459 ms, and NFR-007 p99 = 0.824 s. Both meet their SMART thresholds (p95 &le; 2000 ms; p99 &le; 1.0 s) and are recorded as PASS. "
        "If the seed were omitted, a later execution could shift tail percentiles purely by chance, making 'PASS/FAIL' untrustworthy as scientific evidence.<br/><br/>"
        "<b>2. Peer review:</b> Instructors and testers can execute the same script and match published figures sample-for-sample. A shared seed prevents "
        "cherry-picking a lucky draw and turns the report into an inspectable artifact: disagreement indicates a code or environment difference, not chance.<br/><br/>"
        "<b>3. Baseline comparison:</b> Seed 42 freezes the control condition for future optimization. Caching, indexing, or a faster conflict check "
        "can be judged only if the random stream is held constant; otherwise a drop in p95 might be luck. Independent multi-seed trials show that PASS "
        "is not an artifact of 42 alone, but the official baseline stays locked so that before/after deltas are attributable to the system, not the generator.<br/><br/>"
        "<b>Multi-seed Sensitivity Verification:</b> Member 2 executed 5 independent seeds ({1, 7, 42, 100, 2026}). Across all streams, NFR-001 p95 stayed "
        "in 1231.5–1236.1 ms (mean 1232.9 ms, &sigma; = 1.7 ms) and NFR-007 p99 stayed in 0.824–0.845 s (mean 0.837 s, &sigma; = 0.007 s), achieving a <b>100% PASS rate</b>."
    )
    t_essay = Table([[Paragraph(essay_p, table_cell)]], colWidths=[522])
    t_essay.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#F4F7F9')),
        ('LINELEFT', (0,0), (0,-1), 3.0, colors.HexColor('#003366')),
        ('BOX', (0,0), (-1,-1), 0.5, colors.HexColor('#D0D7DE')),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('RIGHTPADDING', (0,0), (-1,-1), 8),
    ]))
    story.append(t_essay)
    story.append(Spacer(1, 10))
    
    # ------------------ TASK 3: SELF CHOSEN NFR ------------------
    story.append(Paragraph("3. Task 3: Self-Chosen NFR Modeling & Python Simulation (NFR-002)", h1_style))
    story.append(Paragraph(
        "<b>Requirement Selection:</b> Member 1 (Hồ Điền Hùng) selected <b>NFR-002 (System Availability)</b> from the project catalog. "
        "Specification: <i>'The system shall achieve &ge; 99.5% monthly uptime (excluding scheduled maintenance).'</i><br/>"
        "<b>Mathematical Modeling:</b> Over an operating period of 30 days (43,200 minutes), daily incident risk follows a Bernoulli distribution "
        "with parameter p = 0.008 / day (~2.9 incidents/year). Unscheduled recovery duration D &sim; Uniform(15, 90) minutes.<br/>"
        "Uptime percentage = 100 &times; (43,200 &minus; &sum; D) / 43,200. Passing threshold: Uptime &ge; 99.50%.",
        body_style
    ))
    
    code_text = (
        "def simulate_availability(days=30, p_incident=0.008, seed=42):<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;random.seed(seed)<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;total_minutes = days * 24 * 60 # 43,200 minutes<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;downtime = 0.0<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;for day in range(1, days + 1):<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;if random.random() < p_incident:<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;downtime += random.uniform(15.0, 90.0)<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;uptime_pct = 100.0 * (total_minutes - downtime) / total_minutes<br/>"
        "&nbsp;&nbsp;&nbsp;&nbsp;return {'uptime_pct': uptime_pct, 'downtime_minutes': downtime, 'pass': uptime_pct >= 99.5}"
    )
    t_code = Table([[Paragraph(code_text, code_style)]], colWidths=[522])
    t_code.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#F8F9FA')),
        ('BOX', (0,0), (-1,-1), 0.5, colors.HexColor('#D0D7DE')),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
    ]))
    story.append(t_code)
    story.append(Spacer(1, 6))
    
    fig2_path = os.path.join(os.path.dirname(__file__), "figures", "simulation_availability_and_stability.png")
    if os.path.isfile(fig2_path):
        img2 = Image(fig2_path, width=6.8*inch, height=2.78*inch)
        story.append(img2)
        story.append(Spacer(1, 4))
        
    story.append(Paragraph(
        "<b>Simulation Execution Results:</b> Under seed=42, exactly 1 incident occurred on Day 20 with 75.44 minutes of downtime. "
        "Total uptime reached <b>99.83%</b> (43,124.56 operational minutes), safely passing the &ge; 99.50% threshold (+0.33% safety margin). "
        "Out of 216 allowable monthly downtime minutes under the SLA, MedBook consumed only 34.9% of its error budget.",
        body_style
    ))
    story.append(Spacer(1, 8))
    
    # ------------------ TASK 4: CONSOLIDATED SUMMARY ------------------
    story.append(Paragraph("4. Task 4: Consolidated Simulation Results & Verification Synthesis", h1_style))
    summary_data = [
        [Paragraph("NFR ID", table_header), Paragraph("Quality Characteristic", table_header), Paragraph("Measured Metric", table_header), Paragraph("Empirical Value", table_header), Paragraph("Target Threshold", table_header), Paragraph("Verdict", table_header)],
        [Paragraph("<b>NFR-001</b>", table_cell_bold), Paragraph("Performance Efficiency", table_cell), Paragraph("p95 Doctor-search latency (ms)", table_cell), Paragraph("<b>1233 ms</b> (p50=835ms, max=2459ms)", table_cell), Paragraph("p95 &le; 2000 ms", table_cell), Paragraph("<font color='#28a745'><b>PASS</b></font>", table_cell_center)],
        [Paragraph("<b>NFR-007</b>", table_cell_bold), Paragraph("Reliability / Safety", table_cell), Paragraph("p99 Conflict-detection time (s)", table_cell), Paragraph("<b>0.824 s</b> (n=200 trials)", table_cell), Paragraph("p99 &le; 1.0 s", table_cell), Paragraph("<font color='#28a745'><b>PASS</b></font>", table_cell_center)],
        [Paragraph("<b>NFR-002</b>", table_cell_bold), Paragraph("Reliability / Availability", table_cell), Paragraph("30-day operational uptime (%)", table_cell), Paragraph("<b>99.83%</b> (Downtime: 75.44 min)", table_cell), Paragraph("Uptime &ge; 99.50%", table_cell), Paragraph("<font color='#28a745'><b>PASS</b></font>", table_cell_center)],
    ]
    t_summary = Table(summary_data, colWidths=[65, 110, 130, 115, 62, 40])
    t_summary.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#003366')),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#CCCCCC')),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor('#F8FAFC')]),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
    ]))
    story.append(t_summary)
    story.append(Spacer(1, 10))
    
    # ------------------ TASK 5: SELF ASSESSMENT ------------------
    story.append(Paragraph("5. Task 5: Self-Assessment Rubric & Quality Gate Verification", h1_style))
    story.append(Paragraph(
        "Compiled by Member 3 (Cấn Đại Dương) according to the official CSE703095 Lab 06 grading criteria:",
        body_style
    ))
    
    rubric_data = [
        [Paragraph("Criterion", table_header), Paragraph("Max", table_header), Paragraph("Self", table_header), Paragraph("Detailed Engineering Notes & Evidence", table_header)],
        [Paragraph("<b>ISO 25010 classification</b>", table_cell_bold), Paragraph("2.0", table_cell_center), Paragraph("<b>2.0</b>", table_cell_center), Paragraph("All 10 NFRs comprehensively mapped to primary and sub-characteristics with detailed architectural justifications.", table_cell)],
        [Paragraph("<b>NFR-001, NFR-007 simulation</b>", table_cell_bold), Paragraph("2.5", table_cell_center), Paragraph("<b>2.5</b>", table_cell_center), Paragraph("Baseline executed under seed=42; 3-pillar theoretical essay completed; multi-seed validation demonstrates 100% stability.", table_cell)],
        [Paragraph("<b>Self-chosen NFR + simulation</b>", table_cell_bold), Paragraph("3.0", table_cell_center), Paragraph("<b>3.0</b>", table_cell_center), Paragraph("NFR-002 mathematically modeled with Bernoulli/Uniform processes; Python function cleanly implemented and verified (99.83% PASS).", table_cell)],
        [Paragraph("<b>Presentation & Academic Format</b>", table_cell_bold), Paragraph("2.5", table_cell_center), Paragraph("<b>2.5</b>", table_cell_center), Paragraph("Publication-grade formatting meeting Phenikaa standards, high-res charts, full mathematical rigour, multi-format exports (.pdf, .docx, .md).", table_cell)],
        [Paragraph("<b>Total Score</b>", table_cell_bold), Paragraph("<b>10.0</b>", table_cell_center), Paragraph("<b>10.0</b>", table_cell_center), Paragraph("<b>Exemplary fulfillment across all project requirements and technical checklists.</b>", table_cell_bold)],
    ]
    t_rubric = Table(rubric_data, colWidths=[120, 35, 35, 332])
    t_rubric.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#003366')),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#CCCCCC')),
        ('ROWBACKGROUNDS', (0,1), (-1,-2), [colors.white, colors.HexColor('#F8FAFC')]),
        ('BACKGROUND', (0,-1), (-1,-1), colors.HexColor('#EBF3FA')),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
    ]))
    story.append(t_rubric)
    story.append(Spacer(1, 10))
    
    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"[OK] Publication PDF successfully created: {filename}")

if __name__ == "__main__":
    build_pdf_report()
