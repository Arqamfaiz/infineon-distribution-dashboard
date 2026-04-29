"""
Infineon Global Distribution Performance Dashboard
==================================================
A portfolio project demonstrating data-driven distribution marketing analysis.
Built with Streamlit, pandas, and Plotly.

Author: Arqam Faiz Siddiqui
Data sources:
  - Infineon Annual Report 2024 (revenue by region & segment, FY2020-2024)
  - Industry reports on global electronic component distributors (2024)
  - Synthetic distributor-partner KPI data (clearly labelled, for visualization)
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from pathlib import Path

# ---------- Page configuration ----------
st.set_page_config(
    page_title="Infineon Distribution Dashboard",
    page_icon="chip",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ---------- Data loading (cached for performance) ----------
DATA_DIR = Path(__file__).parent / "data"


@st.cache_data
def load_revenue_by_region():
    return pd.read_csv(DATA_DIR / "infineon_revenue_by_region.csv")


@st.cache_data
def load_revenue_by_segment():
    return pd.read_csv(DATA_DIR / "infineon_revenue_by_segment.csv")


@st.cache_data
def load_top_distributors():
    return pd.read_csv(DATA_DIR / "top_distributors.csv")


@st.cache_data
def load_distributor_kpis():
    return pd.read_csv(DATA_DIR / "distributor_kpis.csv")


# ---------- Sidebar ----------
with st.sidebar:
    st.title("Filters")
    st.caption("Adjust filters to explore the data")

    df_region = load_revenue_by_region()
    available_years = sorted(df_region["fiscal_year"].unique())
    selected_years = st.multiselect(
        "Fiscal Year",
        options=available_years,
        default=available_years,
    )

    available_regions = sorted(df_region["region"].unique())
    selected_regions = st.multiselect(
        "Region",
        options=available_regions,
        default=available_regions,
    )

    st.divider()
    st.caption("**About this project**")
    st.write(
        "Portfolio dashboard built to demonstrate skills relevant to "
        "Infineon's Global Distribution Marketing function: "
        "KPI tracking, data consolidation, competitive research, "
        "and Go-to-Market analytics."
    )
    st.caption("Built by Arqam Faiz Siddiqui")

# ---------- Header ----------
st.title("Infineon Global Distribution Performance Dashboard")
st.markdown(
    "An interactive analytical view of Infineon Technologies AG's revenue "
    "performance, regional distribution mix, and the global semiconductor "
    "distribution landscape. Built as a portfolio project to demonstrate "
    "applied skills in dashboard development, KPI tracking, and "
    "competitive distribution research."
)

# Data sources callout
with st.expander("Data sources & methodology"):
    st.markdown(
        """
        **Real data (publicly sourced):**
        - Infineon Financial Data 2020 to 2024, official annual report (Infineon Investor Relations)
        - Top distributor revenue rankings from electronics-sourcing.com Top 50 Distributor Report 2024
        - Industry analysis from EE Times China, Easelink, and ECIA member reports

        **Synthetic data (clearly labelled):**
        - Distributor-partner KPI table: realistic illustrative figures used for
          dashboard visualization since true partner-level data is not public.
          Figures are calibrated against published partner tier structures
          and known regional revenue splits.

        **Methodology:**
        Data was consolidated from public sources into structured CSV files,
        loaded via pandas, and visualized with Plotly. All filters are applied
        reactively across charts to enable scenario-based exploration.
        """
    )

st.divider()

# ---------- Apply filters ----------
df_region_filtered = df_region[
    df_region["fiscal_year"].isin(selected_years)
    & df_region["region"].isin(selected_regions)
]

df_segment = load_revenue_by_segment()
df_segment_filtered = df_segment[df_segment["fiscal_year"].isin(selected_years)]

# ---------- KPI Row ----------
st.subheader("Key Performance Indicators")

if df_region_filtered.empty:
    st.warning("No data matches the current filter selection.")
    st.stop()

latest_year = max(selected_years)
prior_year = latest_year - 1 if (latest_year - 1) in selected_years else None

total_revenue_latest = df_region_filtered[
    df_region_filtered["fiscal_year"] == latest_year
]["revenue_eur_m"].sum()

total_revenue_prior = (
    df_region_filtered[df_region_filtered["fiscal_year"] == prior_year][
        "revenue_eur_m"
    ].sum()
    if prior_year
    else 0
)

revenue_yoy = (
    ((total_revenue_latest - total_revenue_prior) / total_revenue_prior) * 100
    if total_revenue_prior
    else 0
)

top_region = (
    df_region_filtered[df_region_filtered["fiscal_year"] == latest_year]
    .sort_values("revenue_eur_m", ascending=False)
    .iloc[0]
)

num_regions = df_region_filtered["region"].nunique()

col1, col2, col3, col4 = st.columns(4)
col1.metric(
    label=f"Total Revenue (FY{latest_year})",
    value=f"€{total_revenue_latest:,.0f}M",
    delta=f"{revenue_yoy:+.1f}% YoY" if prior_year else None,
)
col2.metric(
    label="Top Revenue Region",
    value=top_region["region"],
    delta=f"€{top_region['revenue_eur_m']:,.0f}M",
    delta_color="off",
)
col3.metric(
    label="Regions in View",
    value=num_regions,
)
col4.metric(
    label="Years in View",
    value=len(selected_years),
)

st.divider()

# ---------- Section 1: Revenue trend by region ----------
st.subheader("Revenue Trend by Region")
st.caption(
    "Tracks Infineon's annual revenue by geographical region. "
    "Useful for identifying growth markets, declining regions, "
    "and the overall regional mix shift."
)

fig_trend = px.line(
    df_region_filtered,
    x="fiscal_year",
    y="revenue_eur_m",
    color="region",
    markers=True,
    labels={
        "fiscal_year": "Fiscal Year",
        "revenue_eur_m": "Revenue (EUR Millions)",
        "region": "Region",
    },
    template="plotly_white",
)
fig_trend.update_layout(
    legend=dict(orientation="h", yanchor="bottom", y=-0.3),
    height=420,
    margin=dict(l=20, r=20, t=20, b=20),
)
st.plotly_chart(fig_trend, use_container_width=True)

# Insight box
top_growth_region = (
    df_region_filtered.groupby("region")["revenue_eur_m"]
    .agg(lambda s: s.iloc[-1] - s.iloc[0])
    .sort_values(ascending=False)
)

st.info(
    f"**Insight:** Across the selected period, **{top_growth_region.index[0]}** "
    f"grew by **€{top_growth_region.iloc[0]:,.0f}M** in absolute terms, "
    f"the strongest regional gain. Greater China consistently represents "
    f"Infineon's largest single market, reflecting the concentration of "
    f"electronics manufacturing and EV supply chains in the region."
)

st.divider()

# ---------- Section 2: Regional mix ----------
col_left, col_right = st.columns(2)

with col_left:
    st.subheader(f"Regional Mix (FY{latest_year})")
    st.caption("Share of total revenue by region for the latest year.")

    df_pie = df_region_filtered[df_region_filtered["fiscal_year"] == latest_year]
    fig_pie = px.pie(
        df_pie,
        values="revenue_eur_m",
        names="region",
        hole=0.45,
        template="plotly_white",
    )
    fig_pie.update_traces(textposition="inside", textinfo="percent+label")
    fig_pie.update_layout(
        height=400,
        margin=dict(l=20, r=20, t=20, b=20),
        showlegend=False,
    )
    st.plotly_chart(fig_pie, use_container_width=True)

with col_right:
    st.subheader("Revenue by Business Segment")
    st.caption(
        "Infineon's four business segments. Automotive is the dominant "
        "segment, driven by EV and ADAS demand."
    )

    fig_seg = px.bar(
        df_segment_filtered,
        x="fiscal_year",
        y="revenue_eur_m",
        color="segment",
        labels={
            "fiscal_year": "Fiscal Year",
            "revenue_eur_m": "Revenue (EUR Millions)",
            "segment": "Segment",
        },
        template="plotly_white",
        barmode="stack",
    )
    fig_seg.update_layout(
        legend=dict(orientation="h", yanchor="bottom", y=-0.4),
        height=400,
        margin=dict(l=20, r=20, t=20, b=20),
    )
    st.plotly_chart(fig_seg, use_container_width=True)

st.divider()

# ---------- Section 3: Competitive distribution landscape ----------
st.subheader("Global Distribution Landscape")
st.caption(
    "The top global electronic component distributors. Understanding the "
    "channel mix is essential for distribution marketing strategy."
)

df_dist = load_top_distributors()
df_dist_sorted = df_dist.sort_values("revenue_2024_usd_b", ascending=True)

fig_dist = go.Figure()
fig_dist.add_trace(
    go.Bar(
        y=df_dist_sorted["distributor"],
        x=df_dist_sorted["revenue_2024_usd_b"],
        orientation="h",
        marker=dict(
            color=df_dist_sorted["yoy_change_pct"],
            colorscale="RdYlGn",
            cmid=0,
            colorbar=dict(title="YoY %"),
        ),
        text=[f"${v:.1f}B" for v in df_dist_sorted["revenue_2024_usd_b"]],
        textposition="outside",
        hovertemplate=(
            "<b>%{y}</b><br>"
            "Revenue 2024: $%{x:.2f}B<br>"
            "YoY Change: %{marker.color:.1f}%<extra></extra>"
        ),
    )
)
fig_dist.update_layout(
    template="plotly_white",
    height=450,
    margin=dict(l=20, r=20, t=20, b=20),
    xaxis_title="Revenue 2024 (USD Billions)",
    yaxis_title="",
)
st.plotly_chart(fig_dist, use_container_width=True)

st.info(
    "**Insight:** WPG Holdings and WT Microelectronics overtook the historical "
    "leaders Arrow and Avnet in 2024, driven by Asia-Pacific recovery and "
    "WT's acquisition of Future Electronics. This realignment has direct "
    "implications for Infineon's Go-to-Market strategy: the distributor "
    "weight has shifted toward Asia-Pacific channels."
)

st.divider()

# ---------- Section 4: Distributor KPIs (synthetic) ----------
st.subheader("Distributor Partner KPIs (Illustrative)")
st.caption(
    "Synthetic but realistic illustration of how a distribution marketing "
    "team would track partner-level KPIs. Real figures are confidential."
)

df_kpis = load_distributor_kpis()

# Allow region filter for this view
region_filter_kpi = st.selectbox(
    "Filter by region",
    options=["All"] + sorted(df_kpis["region"].unique().tolist()),
)

df_kpis_view = (
    df_kpis if region_filter_kpi == "All" else df_kpis[df_kpis["region"] == region_filter_kpi]
)

# Aggregate to distributor level
df_kpis_agg = (
    df_kpis_view.groupby("distributor")
    .agg(
        quarterly_revenue_eur_m=("quarterly_revenue_eur_m", "sum"),
        avg_inventory_weeks=("inventory_weeks", "mean"),
        avg_on_time_delivery=("on_time_delivery_pct", "mean"),
        total_design_wins=("design_wins_q4", "sum"),
    )
    .round(2)
    .sort_values("quarterly_revenue_eur_m", ascending=False)
    .reset_index()
)

st.dataframe(
    df_kpis_agg,
    use_container_width=True,
    hide_index=True,
    column_config={
        "distributor": "Distributor",
        "quarterly_revenue_eur_m": st.column_config.NumberColumn(
            "Quarterly Revenue (EUR M)", format="€%.1f"
        ),
        "avg_inventory_weeks": st.column_config.NumberColumn(
            "Avg Inventory (weeks)", format="%.1f"
        ),
        "avg_on_time_delivery": st.column_config.NumberColumn(
            "On-Time Delivery %", format="%.1f%%"
        ),
        "total_design_wins": st.column_config.NumberColumn(
            "Design Wins", format="%d"
        ),
    },
)

# Scatter: revenue vs delivery performance
st.subheader("Performance Quadrant: Revenue vs On-Time Delivery")
st.caption(
    "Identifying high-revenue, high-reliability partners. Top-right quadrant "
    "represents strategic distribution partners worth investing in."
)

fig_quad = px.scatter(
    df_kpis_view,
    x="on_time_delivery_pct",
    y="quarterly_revenue_eur_m",
    size="design_wins_q4",
    color="partner_tier",
    hover_data=["distributor", "region", "segment_focus"],
    labels={
        "on_time_delivery_pct": "On-Time Delivery (%)",
        "quarterly_revenue_eur_m": "Quarterly Revenue (EUR M)",
        "partner_tier": "Partner Tier",
    },
    template="plotly_white",
)
fig_quad.update_layout(
    height=450,
    margin=dict(l=20, r=20, t=20, b=20),
)
st.plotly_chart(fig_quad, use_container_width=True)

st.divider()

# ---------- Footer ----------
st.markdown(
    """
    <div style='text-align: center; color: #888; font-size: 0.85em; padding-top: 1em;'>
    Built by Arqam Faiz Siddiqui as a portfolio project demonstrating
    distribution marketing analytics. <br>
    This dashboard is not affiliated with or endorsed by Infineon Technologies AG.
    </div>
    """,
    unsafe_allow_html=True,
)
