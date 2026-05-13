#!/usr/bin/env python3
"""
DBA Skills: Doctorate of Business Administration Research Skills
=================================================================
Skills and knowledge areas for a DBA thesis at University of Bordeaux.
Covers: Research Methods, Academic Writing, Business Analysis,
Statistical Tools, Literature Review, and Doctoral Competencies.
"""

RESEARCH_METHODOLOGY_SKILLS = {
    "Philosophical_Foundations": [
        "Ontology: Understanding the nature of reality in business research (realism vs. constructivism)",
        "Epistemology: Positivism, interpretivism, and pragmatism paradigms",
        "Research Philosophy: Choosing between positivist, interpretivist, and critical realism stances",
        "Axiology: Understanding the role of values in research design",
        "Abductive Reasoning: Inference to the best explanation for business phenomena",
        "Inductive vs. Deductive Logic: Building theory from data vs. testing existing theory",
        "Mixed-Methods Philosophy: Combining qualitative and quantitative worldviews",
    ],
    "Quantitative_Methods": [
        "Survey Design: Constructing valid and reliable questionnaires (Likert scales, semantic differential)",
        "Structural Equation Modeling (SEM): SmartPLS, AMOS, R lavaan for testing causal models",
        "Regression Analysis: OLS, logistic, hierarchical, and panel data regression",
        "Factor Analysis: EFA and CFA for construct validation",
        "Hypothesis Testing: t-tests, ANOVA, MANOVA, chi-square, Mann-Whitney U",
        "Mediation and Moderation Analysis: Baron and Kenny, PROCESS macro (Hayes)",
        "Longitudinal Data Analysis: Fixed effects, random effects, difference-in-differences",
        "Cluster Analysis: K-means, hierarchical clustering for market segmentation",
        "Partial Least Squares (PLS-SEM): For small samples and exploratory research",
        "Common Method Bias (CMB) Tests: Harman single factor, marker variable approach",
        "Reliability and Validity: Cronbach alpha, composite reliability, AVE, discriminant validity",
        "Power Analysis: G*Power for determining sample size requirements",
    ],
    "Qualitative_Methods": [
        "Case Study Research: Yin methodology for single and multiple case designs",
        "Grounded Theory: Open, axial, selective coding (Strauss and Corbin; Glaser)",
        "Phenomenology: Lived experience research for management and leadership studies",
        "Ethnography: Organizational culture and behavior observation",
        "Action Research: Practitioner-researcher collaboration for organizational change",
        "Narrative Research: Story-based inquiry in entrepreneurship and leadership",
        "Discourse Analysis: Language and power in organizational communication",
        "Delphi Method: Expert consensus for future business scenario planning",
        "Focus Groups: Moderation techniques for business insight gathering",
        "In-depth Interviews: Semi-structured and unstructured interview design",
        "Document Analysis: Annual reports, policy documents, corporate governance texts",
        "Thematic Analysis: Braun and Clarke six-phase approach",
        "Content Analysis: Qualitative and quantitative analysis of textual data",
        "NVivo Software: Qualitative data management and coding",
        "Atlas.ti: Qualitative analysis alternative to NVivo",
    ],
    "Mixed_Methods": [
        "Convergent Parallel Design: Simultaneous qual+quant with equal weight",
        "Explanatory Sequential Design: Quantitative first, then qualitative to explain",
        "Exploratory Sequential Design: Qualitative first, then quantitative to generalize",
        "Embedded Design: One method nested within another",
        "Triangulation: Strengthening findings through multiple data sources",
        "Integration Strategies: Merging, connecting, and embedding mixed data",
    ],
    "Data_Collection": [
        "Primary Data: Surveys, interviews, observations, experiments",
        "Secondary Data: Databases, company reports, government statistics",
        "Sampling Theory: Probability (random, stratified, cluster) vs. non-probability (purposive, snowball)",
        "Sample Size Determination: Rules of thumb for SEM, regression, and qualitative saturation",
        "Non-Response Bias: Wave analysis and comparison of early vs. late respondents",
        "Ethical Data Collection: IRB/ethics committee approval, informed consent",
        "Online Survey Platforms: Qualtrics, SurveyMonkey, Google Forms, LimeSurvey",
        "Pilot Testing: Pre-testing instruments for clarity and reliability",
    ],
}

ACADEMIC_WRITING_SKILLS = {
    "Thesis_Structure": [
        "Chapter 1 - Introduction: Problem statement, research gap, objectives, questions, significance",
        "Chapter 2 - Literature Review: Theoretical frameworks, systematic review, bibliometric analysis",
        "Chapter 3 - Methodology: Paradigm, design, sample, instruments, analysis plan",
        "Chapter 4 - Results: Data presentation, statistical output, qualitative findings",
        "Chapter 5 - Discussion: Theoretical and managerial implications, comparison with literature",
        "Chapter 6 - Conclusion: Contributions, limitations, future research directions",
        "Abstract Writing: 250-300 word structured abstract (background, methods, results, conclusion)",
        "Executive Summary: Practitioner-focused synthesis of key findings",
        "Appendices: Survey instruments, interview guides, additional statistical output",
    ],
    "Literature_Review_Skills": [
        "Systematic Literature Review (SLR): PRISMA protocol for reproducible reviews",
        "Bibliometric Analysis: VOSviewer and Bibliometrix R package for mapping research fields",
        "Citation Analysis: Identifying seminal papers and research clusters",
        "Research Gap Identification: Theoretical, methodological, and empirical gaps",
        "Theoretical Framework Construction: Adapting and combining existing theories",
        "Conceptual Model Development: Building visual representations of variable relationships",
        "Snowballing Method: Forward and backward citation tracking",
        "Google Scholar: Advanced search, citation alerts, and author profiles",
        "Scopus Database: Field-specific advanced search and bibliometric export",
        "Web of Science: Impact factor, h-index, and journal ranking analysis",
        "EBSCO Business Source: Harvard Business Review and management journal access",
        "JSTOR: Classic management and organizational behavior literature",
        "ProQuest Dissertations: Finding existing doctoral theses for gap analysis",
        "ResearchGate: Networking and accessing working papers",
        "SSRN: Social Science Research Network for management preprints",
    ],
    "Citation_Management": [
        "Zotero: Free reference manager with browser extension and Word plugin",
        "Mendeley: Reference manager with PDF annotation and social features",
        "EndNote: Advanced citation manager for large reference libraries",
        "APA 7th Edition: American Psychological Association format (most common in DBA)",
        "Harvard Referencing: Author-date system widely used in European business schools",
        "Chicago Author-Date: Alternative citation style for business research",
        "DOI Management: Digital Object Identifiers for stable citation links",
        "Citation Tracing: Using Google Scholar Cited-by for forward citation tracking",
    ],
    "Academic_Writing_Style": [
        "Hedging Language: Using cautious claims (suggests, indicates, appears to)",
        "Passive vs. Active Voice: Appropriate use in academic business writing",
        "Avoiding Plagiarism: Paraphrasing techniques and proper attribution",
        "Concision and Clarity: Removing wordiness from academic prose",
        "Academic Vocabulary: Using field-specific terminology accurately",
        "Paragraph Structure: Topic sentence, evidence, analysis, transition",
        "Signposting: Linking phrases to guide reader through argument",
        "Tables and Figures: APA-compliant formatting and labeling",
        "French Academic Writing (Bordeaux): French thesis conventions and norms",
        "English Academic Writing: Anglo-Saxon thesis writing standards",
        "Turnitin/iThenticate: Plagiarism detection tools used by universities",
        "Grammarly: AI grammar and style assistant for academic writing",
    ],
}

STATISTICAL_SOFTWARE_SKILLS = {
    "R_Statistical_Computing": [
        "R Base: Data import, manipulation, and basic statistics",
        "tidyverse: dplyr, ggplot2, tidyr, readr for data science workflow",
        "lavaan: Structural equation modeling and CFA in R",
        "psych: Reliability analysis, EFA, and descriptive statistics",
        "lme4: Multilevel and mixed-effects modeling",
        "stargazer and modelsummary: Publication-ready regression output tables",
        "ggplot2: Publication-quality charts and visualizations",
        "Bibliometrix: Bibliometric analysis and science mapping",
        "semTools: SEM comparison tests and reliability for latent variables",
        "mediation: Causal mediation analysis",
        "car: Companion to Applied Regression (VIF, Levene tests)",
        "RMarkdown: Reproducible research reports combining code and text",
        "Quarto: Next-generation academic manuscript preparation",
    ],
    "SPSS_Statistics": [
        "Descriptive Statistics: Frequencies, means, standard deviations",
        "Reliability Analysis: Cronbach alpha via Analyze > Scale > Reliability",
        "Correlation Matrix: Pearson, Spearman, Kendall correlation tables",
        "Regression: Linear, binary logistic, multinomial logistic regression",
        "Factor Analysis: EFA via Analyze > Dimension Reduction > Factor",
        "ANOVA and MANOVA: Group mean comparison with post-hoc tests",
        "Non-parametric Tests: Mann-Whitney, Kruskal-Wallis, Wilcoxon",
        "Data Management: Variable recoding, computing new variables, filtering",
        "Output Viewer: Copying tables to Word for thesis formatting",
    ],
    "SmartPLS": [
        "PLS-SEM: Partial least squares structural equation modeling",
        "Measurement Model Assessment: Loadings, AVE, CR, HTMT criterion",
        "Structural Model Assessment: Path coefficients, R-squared, Q-squared, f-squared",
        "Bootstrapping: 5000 subsamples for significance testing",
        "Mediation Analysis: Direct, indirect, and total effects",
        "Moderation and Interaction Effects: Product indicator approach",
        "Multigroup Analysis (MGA): Testing model differences across groups",
        "IPMA: Importance-Performance Map Analysis",
        "Common Method Bias: Marker variable technique in SmartPLS",
    ],
    "Python_for_Research": [
        "pandas: Data loading, cleaning, and manipulation",
        "numpy: Numerical computation and array operations",
        "scipy.stats: Statistical tests (t-test, ANOVA, chi-square, correlation)",
        "scikit-learn: Machine learning for business classification and prediction",
        "matplotlib and seaborn: Data visualization for research papers",
        "statsmodels: OLS regression, time series, panel data models",
        "pingouin: Easy ANOVA, correlation, and reliability in Python",
        "nltk and spaCy: Natural language processing for text and content analysis",
        "Jupyter Notebook: Interactive research and data analysis environment",
    ],
    "Microsoft_Excel_for_Research": [
        "Data Cleaning: Remove duplicates, handle missing values, text to columns",
        "Descriptive Stats: AVERAGE, STDEV, MEDIAN, MIN, MAX, PERCENTILE",
        "PivotTables: Cross-tabulation and group comparison",
        "Charts: Bar, scatter, box plots for preliminary data visualization",
        "Data Analysis Toolpak: Regression, ANOVA, correlation, t-tests in Excel",
        "VLOOKUP and INDEX-MATCH: Merging datasets from multiple sources",
        "Conditional Formatting: Visual flagging of outliers and missing data",
    ],
}

BUSINESS_THEORY_SKILLS = {
    "Strategic_Management_Theories": [
        "Resource-Based View (RBV): Barney 1991 - VRIN resources and competitive advantage",
        "Dynamic Capabilities Theory: Teece 2007 - Sensing, seizing, reconfiguring",
        "Porters Five Forces: Industry structure analysis framework",
        "Transaction Cost Economics (TCE): Williamsons governance structures",
        "Institutional Theory: DiMaggio and Powell - Isomorphism and legitimacy",
        "Agency Theory: Jensen and Meckling - Principal-agent relationships",
        "Stakeholder Theory: Freemans model of stakeholder management",
        "Upper Echelons Theory: CEO and TMT characteristics on firm strategy",
        "Blue Ocean Strategy: Kim and Mauborgne - Creating uncontested market space",
        "Ambidexterity Theory: Exploiting current and exploring new capabilities",
        "Absorptive Capacity: Cohen and Levinthal - Learning and innovation",
        "Knowledge-Based View (KBV): Grants model of organizational knowledge",
    ],
    "Organizational_Behavior_Theories": [
        "Organizational Learning Theory: Single-loop vs. double-loop learning (Argyris)",
        "Social Capital Theory: Nahapiet and Ghoshal - Structural, relational, cognitive",
        "Social Exchange Theory: Blaus reciprocity norms in organizations",
        "Self-Determination Theory (SDT): Intrinsic vs. extrinsic motivation",
        "Job Demands-Resources Model (JD-R): Burnout and engagement",
        "Transformational Leadership Theory: Bass and Avolio",
        "Leader-Member Exchange (LMX): Dyadic leadership relationships",
        "Organizational Commitment Theory: Meyer and Allen three-component model",
        "Trust Theory: Mayer, Davis and Schoorman trust model",
        "Psychological Capital (PsyCap): Luthans - HERO model",
        "Person-Organization Fit Theory: Value congruence and retention",
    ],
    "Innovation_Entrepreneurship_Theories": [
        "Diffusion of Innovations: Rogers adoption curve",
        "Technology Acceptance Model (TAM): Davis - Perceived usefulness and ease of use",
        "Disruptive Innovation Theory: Christensen - Sustaining vs. disruptive technologies",
        "Lean Startup: Eric Ries - Build-measure-learn feedback loop",
        "Opportunity Recognition Theory: Shane and Venkataraman entrepreneurship model",
        "Bricolage Theory: Baker and Nelson - Making do with available resources",
        "Entrepreneurial Orientation (EO): Miller/Covin and Slevin - Innovativeness, risk-taking, proactiveness",
        "Business Model Innovation: Osterwalders Business Model Canvas",
        "Open Innovation: Chesbrough - Internal and external knowledge flows",
    ],
    "Finance_Accounting_Frameworks": [
        "Financial Statement Analysis: Ratio analysis (liquidity, leverage, profitability, efficiency)",
        "Corporate Governance Frameworks: OECD Principles of Corporate Governance",
        "ESG Integration: Environmental, Social, and Governance metrics in valuation",
        "Capital Structure Theory: Modigliani-Miller theorem and trade-off theory",
        "Behavioral Finance: Kahneman and Tversky - Prospect theory and cognitive biases",
        "Agency Cost Framework: Monitoring and bonding costs in principal-agent",
        "Value Creation Theory: Shareholder vs. stakeholder value models",
        "Real Options Theory: Flexibility value in strategic investment decisions",
        "Balanced Scorecard: Kaplan and Norton - Financial, customer, process, learning perspectives",
    ],
    "Marketing_Consumer_Theories": [
        "Consumer Behavior Theory: Engel-Kollat-Blackwell (EKB) model",
        "Theory of Planned Behavior (TPB): Ajzen - Attitudes, norms, perceived control",
        "Service-Dominant Logic: Vargo and Lusch - Value co-creation",
        "Customer Lifetime Value (CLV): Predictive modeling of customer profitability",
        "Brand Equity Theory: Kellers CBBE pyramid model",
        "Relationship Marketing Theory: Morgan and Hunt commitment-trust model",
        "Market Orientation Theory: Kohli and Jaworski - Customer intelligence dissemination",
        "Customer Journey Mapping: Touchpoint analysis and experience design",
        "Segmentation-Targeting-Positioning (STP): Kotlers strategic marketing framework",
    ],
}

DOCTORAL_COMPETENCY_SKILLS = {
    "Research_Design": [
        "Problem Statement Formulation: Identifying the so-what of your research",
        "Research Questions: Crafting specific, measurable, and achievable questions",
        "Research Objectives: SMART objectives aligned with research questions",
        "Conceptual Framework: Linking theories, constructs, and hypotheses visually",
        "Theoretical Framework vs. Conceptual Framework: Understanding the distinction",
        "Operationalization: Moving from abstract constructs to measurable variables",
        "Construct Validity: Face, content, convergent, discriminant validity",
        "Internal Validity: Controlling for confounds in causal research",
        "External Validity: Generalizability beyond the sample",
        "Pilot Study Design: Pre-testing instruments and procedures",
        "Ethics Approval Process: Writing IRB/ethics committee applications",
        "Research Proposal Writing: Structure and components for DBA proposal",
    ],
    "Critical_Thinking": [
        "Theoretical Critique: Evaluating assumptions and limitations of theories",
        "Methodological Critique: Assessing research design quality",
        "Evidence Synthesis: Weighing conflicting empirical findings",
        "Contribution Identification: Theoretical, methodological, and practical contributions",
        "Reflexivity: Acknowledging researcher positionality and bias",
        "Counterargument Anticipation: Strengthening thesis defense preparation",
        "Competing Hypotheses: Considering alternative explanations",
        "Abductive Reasoning: Moving between theory and data iteratively",
    ],
    "Thesis_Defense_Preparation": [
        "Viva Voce and Soutenance: French DBA oral defense preparation",
        "Jury Committee Preparation: Understanding jury roles (directeur, rapporteurs, examinateurs)",
        "Research Summary Presentation: 20-minute slide presentation best practices",
        "Answering Difficult Questions: Techniques for handling unexpected critiques",
        "Limitations Framing: Presenting limitations constructively, not defensively",
        "Future Research Direction: Linking your thesis to next research steps",
        "University of Bordeaux Regulations: Specific submission and defense requirements",
        "Manuscript Formatting: University-specific formatting and style requirements",
    ],
    "Professional_Skills": [
        "Academic Networking: Conferences (AOM, SMS, EURAM) for DBA candidates",
        "Academic Job Market: CV writing, cover letters, and interview preparation",
        "Grant Writing: Research funding applications (ANR in France, EU Horizon)",
        "Peer Review Process: How to review and respond to manuscript reviews",
        "Academic Collaboration: Co-authoring and multi-site research coordination",
        "Research Impact: h-index, citation count, and journal ranking (FNEGE, HCERES in France)",
        "Practitioner Engagement: Translating research for corporate audiences",
        "LinkedIn for Academics: Building professional visibility as a doctoral candidate",
        "ORCID: Setting up and maintaining academic identity profile",
        "ResearchGate Profile: Sharing papers and tracking readership",
    ],
    "AI_Tools_for_DBA_Research": [
        "Elicit.org: AI-assisted literature search and summarization",
        "Consensus.app: Evidence-based AI search engine for research papers",
        "Connected Papers: Visual map of paper relationships and citation networks",
        "Semantic Scholar: AI-powered academic search with citation analysis",
        "ChatGPT and Claude: Drafting, brainstorming, and feedback on academic writing",
        "Grammarly: Grammar and style checking for academic manuscripts",
        "DeepL: High-quality translation between French and English for bilingual research",
        "Otter.ai: Interview transcription for qualitative data collection",
        "MAXQDA: Qualitative and mixed-methods data analysis platform",
        "Rayyan: Systematic literature review screening and PRISMA compliance",
        "Covidence: Systematic review management and data extraction",
        "Zotero with Better BibTeX: Automated bibliography management in LaTeX or Word",
        "LaTeX and Overleaf: Professional academic typesetting for thesis manuscripts",
    ],
}

BORDEAUX_DBA_RESOURCES = {
    "French_Academic_System": [
        "HDR (Habilitation a Diriger des Recherches): Post-doctoral qualification in France",
        "CNU (Conseil National des Universites): French academic qualification body",
        "HCERES: French research evaluation agency - journal and lab rankings",
        "FNEGE: French management journal ranking list (equivalent to ABS in UK)",
        "AERES: Conference and journal ranking system in France",
        "ANR (Agence Nationale de la Recherche): French national research funding agency",
        "CIFRE Convention: Industry-funded PhD/DBA in partnership with companies",
        "Ecole Doctorale: Doctoral school structure at University of Bordeaux",
        "ADUM: French doctoral management platform for registration and thesis submission",
        "HAL (Hyper Articles en Ligne): French open-access repository for academic publications",
        "TEL (These en Ligne): French platform for electronic thesis submission",
    ],
    "Key_Journals_for_DBA": [
        "Strategic Management Journal (SMJ): Top strategy research - Wiley",
        "Academy of Management Journal (AMJ): Empirical organizational research",
        "Academy of Management Review (AMR): Theoretical and conceptual management research",
        "Journal of Management (JOM): Broad management research - SAGE",
        "Organization Science: Complex organizational systems and theory",
        "Administrative Science Quarterly (ASQ): Rigorous organizational research",
        "Journal of Business Research (JBR): Broad applied business research - Elsevier",
        "Journal of Business Venturing: Entrepreneurship and innovation research",
        "European Management Journal (EMJ): European context management research",
        "Revue Francaise de Gestion: Leading French management journal",
        "Management International: Bilingual French and English management research",
        "Finance Controle Strategie: French journal for finance and strategy research",
        "M@n@gement: Online French management journal (open access)",
    ],
    "Bordeaux_Research_Centers": [
        "IRGO (Institut de Recherche en Gestion des Organisations): IAE Bordeaux research lab",
        "GRETHA (Groupe de Recherche en Economie Theorique et Appliquee): Economics lab",
        "LAPSCO: Psychology and cognition lab relevant to OB research",
        "BEM Bordeaux Business School: Partner institution for management research",
        "IAE Bordeaux: Institut d Administration des Entreprises - DBA host institution",
        "Doctoral School BSE (Business, Society, Environment) at Bordeaux",
    ],
}


def count_total_dba_skills():
    total = 0
    for d in [RESEARCH_METHODOLOGY_SKILLS, ACADEMIC_WRITING_SKILLS,
              STATISTICAL_SOFTWARE_SKILLS, BUSINESS_THEORY_SKILLS,
              DOCTORAL_COMPETENCY_SKILLS, BORDEAUX_DBA_RESOURCES]:
        for v in d.values():
            total += len(v)
    return total


def export_dba_skills_json(filename="dba_skills.json"):
    import json
    data = {
        "source": "Claude AI + University of Bordeaux DBA Research",
        "institution": "University of Bordeaux - IAE Bordeaux",
        "degree": "Doctorate of Business Administration (DBA)",
        "total_skills": count_total_dba_skills(),
        "domains": {
            "research_methodology": RESEARCH_METHODOLOGY_SKILLS,
            "academic_writing": ACADEMIC_WRITING_SKILLS,
            "statistical_software": STATISTICAL_SOFTWARE_SKILLS,
            "business_theory": BUSINESS_THEORY_SKILLS,
            "doctoral_competencies": DOCTORAL_COMPETENCY_SKILLS,
            "bordeaux_resources": BORDEAUX_DBA_RESOURCES,
        }
    }
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"Exported {data['total_skills']} DBA skills to {filename}")


if __name__ == "__main__":
    print(f"Total DBA skills loaded: {count_total_dba_skills()}")
    export_dba_skills_json()
    print("Done.")
