# Infineon Global Distribution Performance Dashboard

An interactive analytical dashboard exploring Infineon Technologies AG's
revenue performance, regional distribution mix, and the global semiconductor
distribution landscape.

Built as a portfolio project to demonstrate applied skills in dashboard
development, KPI tracking, business data consolidation, and competitive
distribution research, mirroring the responsibilities of a Global
Distribution Marketing function.

**Live demo:** https://infineon-distribution-dashboard-va7dmweaoeumzgmo6zt33z.streamlit.app/

---

## What this project demonstrates

This dashboard answers questions a distribution marketing analyst would need
to answer on a typical day:

- How is revenue trending across regions and how has the mix shifted over five years?
- Which business segment drives the most growth, and how is that growth distributed regionally?
- How is the global distributor landscape changing, and what does that mean for channel strategy?
- Which distributor partners are high-performing on revenue and reliability KPIs?

The work covers:

1. **Data consolidation** from multiple public sources into structured CSV files
2. **Interactive dashboard** with reactive filters, KPI metrics, and drill-down views
3. **Trend analysis** across five fiscal years of Infineon revenue
4. **Competitive research** on the top global semiconductor distributors
5. **Partner KPI tracking** including on-time delivery, inventory weeks, and design wins

---

## Key features

- Five-year revenue trend across all regions with reactive filtering
- Regional revenue mix and segment breakdown for any selected period
- Year-over-year growth metrics computed dynamically
- Global distributor leaderboard coloured by year-over-year change
- Performance quadrant scatter plot for distributor partners
- Filterable distributor KPI table with formatted numerical columns

---

## Data sources

**Real, publicly-sourced data:**

- Infineon Financial Data 2020 to 2024, official annual report
  ([Infineon Investor Relations](https://www.infineon.com/cms/en/about-infineon/investor/reports-and-presentations/))
- Top 50 Authorized Distributor Report 2024 (electronics-sourcing.com, ECIA)
- Industry analysis from EE Times China, Easelink Electronics, and WPG Holdings investor materials

**Synthetic data (clearly labelled in the dashboard):**

- Distributor partner KPI table. Real partner-level Infineon data is
  confidential, so realistic illustrative figures are used. Values are
  calibrated against published partner tier structures and known regional
  splits, and are flagged as illustrative throughout the dashboard.

---

## Local setup

Tested on Python 3.10+. If you don't have Python installed, get it from
[python.org](https://www.python.org/downloads/) first.

```bash
# Clone the repository
git clone https://github.com/<your-username>/infineon-distribution-dashboard.git
cd infineon-distribution-dashboard

# Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate     # On Windows use: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the dashboard
streamlit run app.py
```

The dashboard opens automatically in your default browser at
`http://localhost:8501`.

---

## Project structure

```
infineon-distribution-dashboard/
├── app.py                          # Main Streamlit application
├── requirements.txt                # Python dependencies
├── README.md                       # This file
├── .gitignore
└── data/
    ├── infineon_revenue_by_region.csv     # Real, from annual report
    ├── infineon_revenue_by_segment.csv    # Real, from annual report
    ├── top_distributors.csv               # Real, from industry reports
    └── distributor_kpis.csv               # Synthetic, illustrative
```

---

## Why this dashboard, and what it shows about my work

The Global Distribution Marketing function at Infineon tracks revenue
across regions, monitors distributor partner performance, and supports
Go-to-Market decisions with data. This project recreates that workflow
in miniature, end to end:

- Sourcing real data from public filings and industry reports
- Cleaning and consolidating it into analysis-ready tables
- Building an interactive dashboard that surfaces KPIs and supports
  filtered exploration
- Adding written insights at each section to explain what the data shows

All charts respond to a shared filter set in the sidebar so the dashboard
behaves like a real analytical tool, not a static slide deck.

---

## Limitations and honest caveats

- Distributor partner KPIs are illustrative, not real. Real partner data
  would never be public, and substituting fabricated numbers without
  flagging them would be dishonest. The synthetic table is calibrated
  for plausibility but is not based on Infineon internal data.
- Currency mixing exists between Infineon (EUR, fiscal year ending September)
  and global distributor revenues (USD, calendar year). Each chart labels
  its currency clearly.
- Industry source figures vary slightly between reports. Where conflicts
  exist, the official Infineon annual report figures take precedence.

---

## About the author

Built by **Arqam Faiz Siddiqui**, M.Sc. International Information Systems
candidate at Friedrich-Alexander-Universität Erlangen-Nürnberg, with
hands-on experience in distribution data analysis at GSK (55,000 plus pharmacy
outlets) and procurement and supplier KPI tracking at T.M. Enterprises.

This project is not affiliated with or endorsed by Infineon Technologies AG.
