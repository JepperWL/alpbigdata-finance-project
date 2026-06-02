import os
import random
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import streamlit as st
import plotly.express as px
import time
from datetime import datetime, timedelta


# Page Congiguration
APP_TITLE = "Yahoo Finance Stock Market"
DATASET_PERIOD = "2018-2023"
CSV_PATH = "/app/data/stock_data.csv"

st.set_page_config(
    page_title=APP_TITLE,
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

# CSS
st.markdown(
    """
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500;700&family=Syne:wght@700;800&display=swap');

[data-testid="stIconMaterial"] {
        display: none !important;
    }
    section[data-testid="stSidebar"] {
        transform: none !important;
        width: 275px !important;
    }

:root {
    --bg: #050805;
    --panel: #08110C;
    --panel-2: #0B1710;
    --panel-3: #0E1E15;
    --line: #173524;
    --line-hot: rgba(0, 255, 148, .32);
    --text: #EAFBF1;
    --muted: #73947E;
    --muted-2: #4D705A;
    --green: #00FF94;
    --green-2: #00D17A;
    --cyan: #00E5FF;
    --red: #FF4B6E;
    --amber: #F7C948;
}

*, html, body, [class*="css"] {
    font-family: 'Space Grotesk', sans-serif !important;
    letter-spacing: 0 !important;
}

.stApp {
    color: var(--text);
    background:
        radial-gradient(circle at 12% 0%, rgba(0,255,148,.09), transparent 34%),
        linear-gradient(180deg, #050805 0%, #071009 42%, #030503 100%);
}

#MainMenu, footer, header { visibility: hidden; }
.block-container { padding: 1rem 1.55rem 2rem !important; max-width: 1500px; }

section[data-testid="stSidebar"] {
    background:
        linear-gradient(180deg, rgba(0,255,148,.055), transparent 24%),
        #07100B !important;
    border-right: 1px solid var(--line);
    min-width: 275px !important;
}
section[data-testid="stSidebar"] * { color: #CDEDD8 !important; }
div[data-testid="stSidebarUserContent"] { padding-top: 1.3rem; }

.sidebar-logo {
    font-family: 'Syne', sans-serif !important;
    font-size: 24px;
    line-height: 1.02;
    font-weight: 800;
    color: var(--text);
    margin-bottom: 6px;
}
.sidebar-logo span {
    color: var(--green);
    text-shadow: 0 0 20px rgba(0,255,148,.2);
}
.sidebar-tagline {
    font-family: 'JetBrains Mono', monospace !important;
    color: var(--muted-2);
    font-size: 11px;
    letter-spacing: .8px !important;
    margin-bottom: 18px;
}
.side-chip {
    border: 1px solid var(--line);
    background: rgba(0,255,148,.045);
    border-radius: 8px;
    padding: 10px 12px;
    margin: 10px 0 16px;
    font-size: 12px;
    color: #B6DAC0;
}

.stRadio [role="radiogroup"] {
    gap: 7px;
}
.stRadio label {
    background: #0B1510;
    border: 1px solid #142D1F;
    border-radius: 8px;
    padding: 8px 10px;
}
.stSelectbox div[data-baseweb="select"] > div {
    background: #0B1510;
    border-color: #183725;
    border-radius: 8px;
}

.hero-shell {
    position: relative;
    border: 1px solid var(--line-hot);
    border-radius: 12px;
    padding: 20px 22px;
    margin-bottom: 18px;
    overflow: hidden;
    background:
        linear-gradient(90deg, rgba(0,255,148,.105), rgba(0,229,255,.035) 45%, rgba(255,255,255,.015)),
        repeating-linear-gradient(90deg, rgba(255,255,255,.025) 0 1px, transparent 1px 72px),
        #07100B;
    box-shadow: 0 18px 70px rgba(0,0,0,.42), inset 0 1px 0 rgba(255,255,255,.03);
}
.hero-shell::after {
    content: '';
    position: absolute;
    inset: 0;
    pointer-events: none;
    background: linear-gradient(180deg, transparent, rgba(0,0,0,.18));
}
.hero-title {
    position: relative;
    z-index: 1;
    font-family: 'Syne', sans-serif !important;
    font-weight: 800;
    font-size: 38px;
    line-height: 1.02;
    color: var(--text);
}
.hero-title span { color: var(--green); }
.hero-sub {
    position: relative;
    z-index: 1;
    color: var(--muted);
    font-size: 13px;
    margin-top: 8px;
}
.hero-metrics {
    position: relative;
    z-index: 1;
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
    margin-top: 14px;
}
.pill {
    display: inline-flex;
    align-items: center;
    gap: 7px;
    height: 28px;
    padding: 0 10px;
    border-radius: 999px;
    border: 1px solid rgba(0,255,148,.25);
    background: rgba(0,255,148,.07);
    color: #BFFFF0;
    font-family: 'JetBrains Mono', monospace !important;
    font-size: 10px;
    font-weight: 700;
}
.pulse-dot {
    width: 7px;
    height: 7px;
    border-radius: 50%;
    background: var(--green);
    box-shadow: 0 0 0 rgba(0,255,148,.7);
    animation: pulse 1.4s infinite;
}
@keyframes pulse {
    0% { box-shadow: 0 0 0 0 rgba(0,255,148,.6); }
    70% { box-shadow: 0 0 0 8px rgba(0,255,148,0); }
    100% { box-shadow: 0 0 0 0 rgba(0,255,148,0); }
}

.index-bar {
    background: rgba(7,16,11,.92);
    border: 1px solid var(--line);
    border-radius: 10px;
    padding: 10px 14px;
    display: flex;
    gap: 22px;
    align-items: center;
    margin-bottom: 14px;
    overflow-x: auto;
    box-shadow: inset 0 1px 0 rgba(255,255,255,.03);
}
.index-item { min-width: fit-content; }
.index-name {
    font-family: 'JetBrains Mono', monospace !important;
    font-size: 10px;
    color: var(--muted-2);
    text-transform: uppercase;
}
.index-val {
    font-family: 'JetBrains Mono', monospace !important;
    font-size: 15px;
    color: var(--text);
    font-weight: 700;
}
.index-chg-up, .index-chg-dn {
    font-family: 'JetBrains Mono', monospace !important;
    font-size: 11px;
    font-weight: 700;
}
.index-chg-up { color: var(--green); }
.index-chg-dn { color: var(--red); }

.ticker-bar {
    background: #030704;
    border-top: 1px solid var(--line);
    border-bottom: 1px solid var(--line);
    padding: 10px 0;
    margin-bottom: 18px;
}

.kpi-card {
    min-height: 118px;
    background:
        linear-gradient(180deg, rgba(0,255,148,.055), rgba(255,255,255,.012)),
        var(--panel);
    border: 1px solid var(--line);
    border-radius: 10px;
    padding: 18px 18px;
    position: relative;
    overflow: hidden;
    transition: .2s ease;
}
.kpi-card::before {
    content: '';
    position: absolute;
    inset: 0 auto 0 0;
    width: 3px;
    background: linear-gradient(180deg, var(--green), var(--cyan));
    opacity: .65;
}
.kpi-card:hover {
    transform: translateY(-2px);
    border-color: var(--line-hot);
    box-shadow: 0 16px 42px rgba(0,0,0,.35), 0 0 24px rgba(0,255,148,.055);
}
.kpi-label {
    font-size: 11px;
    color: var(--muted);
    text-transform: uppercase;
    font-weight: 700;
    margin-bottom: 9px;
}
.kpi-val {
    font-family: 'JetBrains Mono', monospace !important;
    font-size: 27px;
    font-weight: 800;
    color: var(--text);
    line-height: 1;
}
.kpi-sub { color: var(--green); font-size: 11px; margin-top: 8px; font-weight: 600; }
.kpi-sub-neutral { color: var(--muted-2); font-size: 11px; margin-top: 8px; }

.section-header {
    font-family: 'Syne', sans-serif !important;
    font-size: 18px;
    font-weight: 800;
    color: var(--text);
    margin: 10px 0 8px;
}
.section-divider {
    width: 42px;
    height: 3px;
    background: linear-gradient(90deg, var(--green), var(--cyan));
    border-radius: 999px;
    margin: 0 0 14px;
}
.glass-panel {
    background: rgba(8,17,12,.78);
    border: 1px solid var(--line);
    border-radius: 10px;
    padding: 14px;
    box-shadow: inset 0 1px 0 rgba(255,255,255,.03);
}

.gl-row {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 10px 0;
    border-bottom: 1px solid #12281C;
}
.gl-ticker {
    font-family: 'JetBrains Mono', monospace !important;
    font-weight: 800;
    color: var(--text);
    font-size: 14px;
}
.gl-vol {
    color: var(--muted-2);
    font-family: 'JetBrains Mono', monospace !important;
    font-size: 10px;
}

.info-box-green {
    background: rgba(0,255,148,.055);
    border: 1px solid rgba(0,255,148,.18);
    border-left: 3px solid var(--green);
    border-radius: 8px;
    padding: 13px 15px;
    color: #BDF7D6;
    font-size: 13px;
    margin: 8px 0 16px;
    line-height: 1.55;
}
.feed-item {
    background: linear-gradient(90deg, rgba(0,255,148,.045), rgba(255,255,255,.012));
    border: 1px solid var(--line);
    border-radius: 9px;
    padding: 12px 15px;
    margin-bottom: 9px;
    display: grid;
    grid-template-columns: 90px 1fr 110px 96px;
    gap: 14px;
    align-items: center;
    transition: all .18s ease;
}
.feed-item:hover {
    border-color: var(--line-hot);
    background: #0B1710;
}
.feed-ticker {
    font-family: 'JetBrains Mono', monospace !important;
    font-weight: 800;
    font-size: 15px;
    color: var(--text);
}
.feed-time {
    font-family: 'JetBrains Mono', monospace !important;
    font-size: 10px;
    color: var(--muted-2);
}
.feed-change-up, .feed-change-dn {
    font-family: 'JetBrains Mono', monospace !important;
    font-size: 12px;
    font-weight: 800;
    padding: 4px 8px;
    border-radius: 6px;
    text-align: center;
}
.feed-change-up {
    color: var(--green);
    background: rgba(0,255,148,.09);
}
.feed-change-dn {
    color: var(--red);
    background: rgba(255,75,110,.09);
}

.rank-grid {
    display: grid;
    grid-template-columns: repeat(4, minmax(0, 1fr));
    gap: 10px;
    margin-bottom: 14px;
}
.rank-card {
    border: 1px solid var(--line);
    border-radius: 9px;
    padding: 12px;
    background: var(--panel);
}
.rank-label {
    font-size: 10px;
    color: var(--muted-2);
    text-transform: uppercase;
    font-weight: 700;
}
.rank-value {
    font-family: 'JetBrains Mono', monospace !important;
    font-size: 20px;
    color: var(--text);
    font-weight: 800;
    margin-top: 5px;
}

div[data-testid="stDataFrame"] {
    border: 1px solid var(--line);
    border-radius: 10px;
    overflow: hidden;
}
::-webkit-scrollbar { width: 6px; height: 6px; }
::-webkit-scrollbar-track { background: #050805; }
::-webkit-scrollbar-thumb { background: #1D422D; border-radius: 4px; }

@media (max-width: 900px) {
    .hero-title { font-size: 28px; }
    .feed-item { grid-template-columns: 1fr; }
    .rank-grid { grid-template-columns: repeat(2, minmax(0, 1fr)); }
}
</style>
""",
    unsafe_allow_html=True,
)

# Utils
def fmt_vol(num):
    try:
        num = float(num)
        if num >= 1_000_000_000:
            return f"{num / 1_000_000_000:.2f}B"
        if num >= 1_000_000:
            return f"{num / 1_000_000:.1f}M"
        if num >= 1_000:
            return f"{num / 1_000:.0f}K"
        return str(int(num))
    except (TypeError, ValueError):
        return str(num)


def delta_color(val):
    return "#00FF94" if val >= 0 else "#FF4B6E"


def delta_icon(val):
    return "▲" if val >= 0 else "▼"


def sector_for_ticker(ticker):
    sector_map = {
        "AAPL": "Consumer Tech", "MSFT": "Cloud", "GOOGL": "Internet", "META": "Internet",
        "AMZN": "Commerce", "NVDA": "Semiconductors", "AMD": "Semiconductors",
        "TSLA": "EV", "RIVN": "EV", "LCID": "EV", "JPM": "Banking", "BAC": "Banking",
        "GS": "Banking", "V": "Payments", "MA": "Payments", "XOM": "Energy",
        "CVX": "Energy", "PFE": "Healthcare", "JNJ": "Healthcare", "UNH": "Healthcare",
    }
    return sector_map.get(ticker, "Growth")

@st.cache_data(show_spinner="⏳ Memuat data historis dari HDFS...")
def load_batch_data():
    df = pd.read_csv(CSV_PATH)
    df["Date"] = pd.to_datetime(
        df["Date"],
        utc=True
    )
    df = df.rename(
        columns={"Company": "Ticker"}
    )
    df["Change_Pct"] = (
        (
            df["Close"] - df["Open"]
        )
        / df["Open"]
        * 100
    ).round(2)
    return df

ALL_TICKERS = [
    "AAPL", "TSLA", "MSFT", "GOOGL", "NVDA", "META", "AMZN", "NFLX", "AMD", "INTC",
    "BABA", "ORCL", "IBM", "UBER", "SPOT", "PYPL", "SHOP", "SNAP", "CRM", "ADBE",
    "QCOM", "AVGO", "SONY", "DIS", "NKE", "PINS", "SQ", "COIN", "PLTR", "ARM",
    "SAP", "ZM", "ROKU", "EBAY", "CSCO", "HPQ", "DELL", "V", "MA", "JPM",
    "BAC", "GS", "WMT", "COST", "PEP", "KO", "T", "VZ", "XOM", "CVX",
    "ABNB", "LYFT", "PANW", "NET", "DDOG", "SNOW", "MDB", "TEAM", "DOCU", "OKTA",
    "CRWD", "ZS", "ASML", "TSM", "MU", "F", "GM", "RIVN", "LCID", "AI",
    "UPST", "AFRM", "HOOD", "SOFI", "DKNG", "UAL", "DAL", "AAL", "BA", "CAT",
    "MCD", "SBUX", "YUM", "WFC", "C", "MS", "BLK", "TGT", "LOW", "HD",
    "RTX", "LMT", "GE", "JNJ", "PFE", "MRNA", "CVS", "UNH", "ABBV", "BMY",
]


batch_csv = load_batch_data()
dataset_start = batch_csv["Date"].min()
dataset_end = batch_csv["Date"].max()

DATASET_PERIOD = (
    f"{dataset_start.year}-{dataset_end.year}"
)
batch_date_range = DATASET_PERIOD
batch_tickers = sorted(batch_csv["Ticker"].unique().tolist()) if not batch_csv.empty else []
ticker_opts = batch_tickers if batch_tickers else sorted(ALL_TICKERS)

# Sidebar
with st.sidebar:
    st.markdown(
        f"<div class='sidebar-logo'>Yahoo Finance<br><span>Stock Market</span></div>",
        unsafe_allow_html=True,
    )
    st.markdown("<div class='sidebar-tagline'>FINANCIAL TERMINAL </div>", unsafe_allow_html=True)
    st.markdown(
        f"<div class='side-chip'>Batch Dataset Period locked to <b>{DATASET_PERIOD}</b></div>",
        unsafe_allow_html=True,
    )

    page = st.radio(
        "Navigation",
        ["📊 Overview", "📈 Analytics", "⚡ Live Feed", "⭐ Smart Watchlist"],
        label_visibility="collapsed",
    )

    st.divider()
    st.markdown("**🔍 Filter Emiten / Company**")
    selected_stock = st.selectbox("Select Ticker", ["All"] + ticker_opts, label_visibility="collapsed")

    st.markdown("**⚙️ Terminal Settings**")
    rows_to_show = st.sidebar.slider(
    "Rows shown",
    min_value=10,
    max_value=100,
    value=50,
    step=10
    )

    st.markdown("**📅 Historical Replay**")

    replay_mode = st.radio(
        "Replay Mode",
        ["Manual", "Auto Replay"]
    )

    available_dates = sorted(
        batch_csv["Date"].dt.date.unique()
    )

    if "date_index" not in st.session_state:
        st.session_state.date_index = len(available_dates) - 1

    if replay_mode == "Manual":

        selected_date = st.selectbox(
            "Select Trading Date",
            available_dates,
            index=st.session_state.date_index
        )

    else:

        selected_date = available_dates[
            st.session_state.date_index
        ]

        st.info(
            f"▶ Replay Date: {selected_date}"
        )

    if replay_mode == "Auto Replay":

        if st.button("Next Day ▶"):

            st.session_state.date_index += 1

            if st.session_state.date_index >= len(available_dates):
               st.session_state.date_index = 0

            st.rerun()

# Static Top Bar
st.markdown(
    f"""
<div class="hero-shell">
    <div class="hero-title">Yahoo Finance <span>Stock Market</span></div>
    <div class="hero-sub">
        Enterprise financial intelligence platform • Historical Dataset:
        <b style="color:#00FF94">{DATASET_PERIOD}</b> • Historical Market Replay
    </div>
    <div class="hero-metrics">
        <div class="pill"><span class="pulse-dot"></span> MARKET REPLAY  ACTIVE</div>
        <div class="pill">APACHE SPARK ANALYTICS</div>
        <div class="pill">HDFS READY</div>
    </div>
</div>
""",
    unsafe_allow_html=True,
)
  
st.markdown(
    """
<div class="index-bar">
    <div class="index-item"><div class="index-name">NASDAQ</div><div class="index-val">18,432.14</div><div class="index-chg-up">▲ +1.24%</div></div>
    <div class="index-item"><div class="index-name">S&P 500</div><div class="index-val">5,234.82</div><div class="index-chg-up">▲ +0.87%</div></div>
    <div class="index-item"><div class="index-name">DOW JONES</div><div class="index-val">39,127.56</div><div class="index-chg-dn">▼ -0.12%</div></div>
    <div class="index-item"><div class="index-name">BTC/USD</div><div class="index-val">67,432.10</div><div class="index-chg-up">▲ +2.11%</div></div>
    <div class="index-item"><div class="index-name">ETH/USD</div><div class="index-val">3,512.44</div><div class="index-chg-up">▲ +1.02%</div></div>
    <div class="index-item"><div class="index-name">CRUDE OIL</div><div class="index-val">81.24</div><div class="index-chg-dn">▼ -0.44%</div></div>
    <div class="index-item"><div class="index-name">GOLD</div><div class="index-val">2,312.80</div><div class="index-chg-up">▲ +0.92%</div></div>
    <div style="margin-left:auto;text-align:right;min-width:fit-content">
        <div style="font-family:'JetBrains Mono',monospace;font-size:18px;font-weight:800;color:#EAFBF1">MARKET SIMULATION</div>
        <div style="font-size:11px;color:#4D705A">Historical Financial Dataset</div>
    </div>
</div>
""",
    unsafe_allow_html=True,
)

st.markdown(
    """
<div class="ticker-bar">
<marquee behavior="scroll" direction="left" scrollamount="5"
style="font-family:'JetBrains Mono',monospace;font-size:12px;color:#73947E;font-weight:700;">
🟢 NVDA <span style="color:#00FF94">▲ +4.2%</span> &nbsp;│&nbsp;
🟢 AAPL <span style="color:#00FF94">▲ +2.1%</span> &nbsp;│&nbsp;
🔴 TSLA <span style="color:#FF4B6E">▼ -1.3%</span> &nbsp;│&nbsp;
🟢 MSFT <span style="color:#00FF94">▲ +1.9%</span> &nbsp;│&nbsp;
🟢 META <span style="color:#00FF94">▲ +3.1%</span> &nbsp;│&nbsp;
🟢 AMZN <span style="color:#00FF94">▲ +2.4%</span> &nbsp;│&nbsp;
🔴 NFLX <span style="color:#FF4B6E">▼ -0.7%</span> &nbsp;│&nbsp;
🟢 AMD <span style="color:#00FF94">▲ +2.8%</span> &nbsp;│&nbsp;
🟢 COIN <span style="color:#00FF94">▲ +5.2%</span> &nbsp;│&nbsp;
🔴 INTC <span style="color:#FF4B6E">▼ -0.4%</span> &nbsp;│&nbsp;
🟢 GOOGL <span style="color:#00FF94">▲ +1.1%</span> &nbsp;│&nbsp;
🟢 PLTR <span style="color:#00FF94">▲ +3.7%</span>
</marquee>
</div>
""",
    unsafe_allow_html=True,
)

# Main Loop
placeholder = st.empty()

for _ in range(1):
    current_time = datetime.now()

    historical_timestamp = dataset_end.strftime(
    "%Y-%m-%d 16:00:00"
    )

    current_stream_date = pd.to_datetime(selected_date)

    rt_df = batch_csv[
        batch_csv["Date"].dt.date == current_stream_date.date()
    ].copy()

    rt_df["Price"] = rt_df["Close"]

    rt_df["Sector"] = rt_df["Ticker"].apply(
        sector_for_ticker
    )

    rt_df["Spread"] = (
        rt_df["High"] - rt_df["Low"]
    ).round(2)

    rt_df["Timestamp"] = (
        rt_df["Date"]
        .dt.strftime("%Y-%m-%d")
    )

    rt_df["Signal"] = np.select(
    [
        rt_df["Change_Pct"] >= 3,
        rt_df["Change_Pct"] <= -3
    ],
    [
        "STRONG BUY",
        "RISK OFF"
    ],
    default="WATCH"
    )

    display_rt = rt_df.head(rows_to_show).copy()

    st.info(
        f"""
    📅 Current Trading Session

    Date:
    {selected_date}

    Mode:
    {replay_mode}

    Data Source:
    Historical Replay Dataset
    """
    )

    if selected_stock != "All":
        display_rt = rt_df[rt_df["Ticker"] == selected_stock]

        if display_rt.empty:
            display_rt = rt_df

    if selected_stock != "All":
        
        st.info(
            f"""
    📌 Single Stock Analysis Mode

    Currently analysing:
    {selected_stock}
    
    Sector-wide analytics are hidden because
    only one company is selected.
    """
    )

    total_vol = display_rt["Volume"].sum()
    market_avg = round(display_rt["Price"].mean(), 2)
    gainers_df = display_rt.sort_values("Change_Pct", ascending=False).head(5)
    losers_df = display_rt.sort_values("Change_Pct").head(5)
    top_gainer = gainers_df.iloc[0]
    top_loser = losers_df.iloc[0]
    up_count = len(display_rt[display_rt["Change_Pct"] > 0])
    dn_count = len(display_rt[display_rt["Change_Pct"] < 0])
    up_pct_rt = round(up_count / len(display_rt) * 100, 1)

    with placeholder.container():
        c1, c2, c3, c4, c5 = st.columns(5)
        with c1:
            st.markdown(
                f"""<div class="kpi-card">
                    <div class="kpi-label">📊 Total Volume</div>
                    <div class="kpi-val">{fmt_vol(total_vol)}</div>
                    <div class="kpi-sub">Across {len(display_rt)} emiten</div>
                </div>""",
                unsafe_allow_html=True,
            )
        with c2:
            st.markdown(
                f"""<div class="kpi-card">
                    <div class="kpi-label">💵 Avg Price</div>
                    <div class="kpi-val">${market_avg}</div>
                    <div class="kpi-sub-neutral">Realtime simulation</div>
                </div>""",
                unsafe_allow_html=True,
            )
        with c3:
            st.markdown(
                f"""<div class="kpi-card">
                    <div class="kpi-label">🚀 Top Gainer</div>
                    <div class="kpi-val" style="font-size:24px">{top_gainer["Ticker"]}</div>
                    <div style="color:{delta_color(top_gainer["Change_Pct"])};font-size:12px;font-weight:800;margin-top:7px;font-family:'JetBrains Mono',monospace">
                        {delta_icon(top_gainer["Change_Pct"])} {top_gainer["Change_Pct"]}%
                    </div>
                </div>""",
                unsafe_allow_html=True,
            )
        with c4:
            st.markdown(
                f"""<div class="kpi-card">
                    <div class="kpi-label">📉 Top Loser</div>
                    <div class="kpi-val" style="font-size:24px">{top_loser["Ticker"]}</div>
                    <div style="color:{delta_color(top_loser["Change_Pct"])};font-size:12px;font-weight:800;margin-top:7px;font-family:'JetBrains Mono',monospace">
                        {delta_icon(top_loser["Change_Pct"])} {top_loser["Change_Pct"]}%
                    </div>
                </div>""",
                unsafe_allow_html=True,
            )
        with c5:
            st.markdown(
                f"""<div class="kpi-card">
                    <div class="kpi-label">⚡ Market Breadth</div>
                    <div style="display:flex;gap:15px;align-items:center;margin-top:8px">
                        <div><div style="font-family:'JetBrains Mono',monospace;font-size:22px;font-weight:800;color:#00FF94">{up_count}</div><div style="font-size:10px;color:#00FF94;font-weight:800">▲ UP</div></div>
                        <div style="color:#173524;font-size:20px">│</div>
                        <div><div style="font-family:'JetBrains Mono',monospace;font-size:22px;font-weight:800;color:#FF4B6E">{dn_count}</div><div style="font-size:10px;color:#FF4B6E;font-weight:800">▼ DOWN</div></div>
                    </div>
                </div>""",
                unsafe_allow_html=True,
            )

        st.markdown("<br>", unsafe_allow_html=True)

        if page == "📊 Overview":
            st.markdown("<div class='section-header'>📡 Historical Streaming Replay</div><div class='section-divider'></div>", unsafe_allow_html=True)
            col_chart, col_gl = st.columns([2, 1])
            st.success(""" 🟢 REALTIME DATA Source:
                       Kafka Producer → Kafka Topic → Spark Streaming
            Mode:
                       Live Market Simulation
                       """)

            with col_chart:
                st.markdown("<div class='section-header'>📈 Price Performance — Top Emiten</div>", unsafe_allow_html=True)
                chart_df = display_rt.head(rows_to_show).copy()
                colors = ["#00FF94" if c >= 0 else "#FF4B6E" for c in chart_df["Change_Pct"]]
                fig = go.Figure()
                fig.add_trace(
                    go.Scatter(
                        x=chart_df["Ticker"],
                        y=chart_df["Price"],
                        mode="lines+markers",
                        line=dict(color="#00FF94", width=2),
                        marker=dict(color=colors, size=9, line=dict(color="#050805", width=2)),
                        fill="tozeroy",
                        fillcolor="rgba(0,255,148,0.06)",
                        hovertemplate="<b>%{x}</b><br>Price: $%{y}<extra></extra>",
                    )
                )
                fig.update_layout(
                    paper_bgcolor="rgba(0,0,0,0)",
                    plot_bgcolor="rgba(0,0,0,0)",
                    font=dict(color="#8DB79A", family="JetBrains Mono"),
                    height=370,
                    margin=dict(l=10, r=10, t=10, b=10),
                    xaxis=dict(gridcolor="#12281C"),
                    yaxis=dict(gridcolor="#12281C", tickprefix="$"),
                )
                st.plotly_chart(fig,use_container_width=True,config={"displayModeBar": False}
)

            with col_gl:
                st.markdown(f"<div class='section-header'>🚀 Top Gainers Dataset Period <span style='font-size:10px;color:#4D705A;font-family:JetBrains Mono'>{DATASET_PERIOD}</span></div>", unsafe_allow_html=True)
                for _, row in gainers_df.iterrows():
                    st.markdown(
                        f"""<div class="gl-row">
                            <div><div class="gl-ticker">{row["Ticker"]}</div><div class="gl-vol">Vol: {fmt_vol(row["Volume"])}</div></div>
                            <div style="text-align:right"><div style="font-family:'JetBrains Mono',monospace;font-weight:800;color:#EAFBF1;font-size:13px">${row["Price"]}</div><div style="color:#00FF94;font-family:'JetBrains Mono',monospace;font-size:12px;font-weight:800">▲ {row["Change_Pct"]}%</div></div>
                        </div>""",
                        unsafe_allow_html=True,
                    )
                st.markdown(f"<div class='section-header'>📉 Top Losers Dataset Period <span style='font-size:10px;color:#4D705A;font-family:JetBrains Mono'>{DATASET_PERIOD}</span></div>", unsafe_allow_html=True)
                for _, row in losers_df.iterrows():
                    st.markdown(
                        f"""<div class="gl-row">
                            <div><div class="gl-ticker">{row["Ticker"]}</div><div class="gl-vol">Vol: {fmt_vol(row["Volume"])}</div></div>
                            <div style="text-align:right"><div style="font-family:'JetBrains Mono',monospace;font-weight:800;color:#EAFBF1;font-size:13px">${row["Price"]}</div><div style="color:#FF4B6E;font-family:'JetBrains Mono',monospace;font-size:12px;font-weight:800">▼ {row["Change_Pct"]}%</div></div>
                        </div>""",
                        unsafe_allow_html=True,
                    )
                st.markdown("</div>", unsafe_allow_html=True)

            st.markdown("<div class='section-header'>📊 Volume per Emiten (Realtime)</div>", unsafe_allow_html=True)
            st.info("""
                Volume Analytics Purpose

            Visualisasi ini menunjukkan emiten dengan aktivitas transaksi tertinggi.

            Semakin besar volume perdagangan,
            semakin tinggi minat pasar terhadap saham tersebut.

            Digunakan untuk mengidentifikasi:

            • Saham paling aktif
            • Lonjakan aktivitas pasar
            • Potensi momentum trading
            """, icon="ℹ️")
            vol_sorted = display_rt.sort_values("Volume", ascending=False).head(rows_to_show)
            fig_vol = go.Figure(
                go.Bar(
                    x=vol_sorted["Ticker"],
                    y=vol_sorted["Volume"],
                    marker=dict(
                        color=vol_sorted["Change_Pct"],
                        colorscale=[[0, "#FF4B6E"], [0.5, "#173524"], [1, "#00FF94"]],
                        showscale=True,
                        colorbar=dict(title="Change%", tickfont=dict(color="#8DB79A"), thickness=12),
                    ),
                    text=vol_sorted["Volume"].apply(fmt_vol),
                    textposition="outside",
                    textfont=dict(color="#8DB79A", size=10, family="JetBrains Mono"),
                    hovertemplate="<b>%{x}</b><br>Volume: %{text}<extra></extra>",
                )
            )
            fig_vol.update_layout(
                paper_bgcolor="rgba(0,0,0,0)",
                plot_bgcolor="rgba(0,0,0,0)",
                font=dict(color="#8DB79A", family="JetBrains Mono"),
                height=320,
                margin=dict(l=10, r=10, t=30, b=10),
                xaxis=dict(gridcolor="#12281C"),
                yaxis=dict(gridcolor="#12281C", showticklabels=False),
                bargap=0.3,
            )
            st.plotly_chart(fig_vol,use_container_width=True,config={"displayModeBar": False}
)

        elif page == "📈 Analytics":
            st.warning("""
                       🟡 BATCH DATA
                       Source:
                       CSV Dataset → HDFS → Spark Batch Processing
                       Mode:
                       Historical Analysis
                       """)
            # Company Detail
            if selected_stock != "All" and not display_rt.empty:
                company_data = display_rt.iloc[0]
                
                st.markdown(
                    f"### 📈 Company Detail — {selected_stock}"
                )
                d1, d2, d3, d4, d5 = st.columns(5)

                with d1:
                    st.metric(
                        "Price",
                        f"${company_data['Price']:.2f}"
                    )
   
                with d2:
                    st.metric(
                        "Volume",
                        fmt_vol(company_data["Volume"])
                    )

                with d3:
                    st.metric(
                        "Change %",
                        f"{company_data['Change_Pct']:.2f}%"
                    )
        
                with d4:
                    st.metric(
                        "Sector",
                        company_data["Sector"]
                    )
                
                with d5:
                    st.metric(
                        "Signal",
                        company_data["Signal"]
                    )

                last_hist_date = "N/A"
        
                if not batch_csv.empty:
                    hist_company = batch_csv[batch_csv["Ticker"] == selected_stock
                ]

                if not hist_company.empty:
                    last_hist_date = (
                    hist_company["Date"]
                    .max()
                    .strftime("%Y-%m-%d")
                )

                st.info(
                    f"""
                Historical Data Until : {last_hist_date}

                High : ${company_data['High']:.2f}

                Low : ${company_data['Low']:.2f}

                Ticker : {company_data['Ticker']}
"""
)
                hist_company = batch_csv[batch_csv["Ticker"] == selected_stock
                ].sort_values("Date")

                history = hist_company["Close"]

                x=hist_company["Date"]
                y=history

                fig_detail = go.Figure()

                fig_detail.add_trace(
                    go.Scatter(
                        x=x,
                        y=history,
                        mode="lines",
                        line=dict(color="#00FF94", width=3)
                    )
                )   

                fig_detail.update_layout(
                    title=f"{selected_stock} Price Trend",
                height=250,
                paper_bgcolor="rgba(0,0,0,0)",
                plot_bgcolor="rgba(0,0,0,0)"
                )

                st.plotly_chart(
                    fig_detail,
                use_container_width=True
                )

            if selected_stock == "All":    
                st.markdown(
                    "<div class='section-header'>🏢 Sector Performance</div>",unsafe_allow_html=True,
                )

                sector_perf = (
                    display_rt
                    .groupby("Sector")["Change_Pct"]
                    .mean()
                    .reset_index()
                )

                top3_sector = (
                    sector_perf
                    .sort_values(
                    "Change_Pct",
                    ascending=False
                    )
                    .head(3)
                )

                sector_text = ""
            
                for idx, row in top3_sector.iterrows():
                    medal = {
                        0: "🥇",
                        1: "🥈",
                        2: "🥉"
                    }.get(idx, "🏅")
                
                    sector_text += (
                            f"{medal} {row['Sector']} "
                        f"({row['Change_Pct']:.2f}%)\n"
                    )   

                st.success(
                    f"""
                    🏆 Top Performing Sectors

                {sector_text}
                    """
                )    

                fig_sector = px.bar(
                    sector_perf,
                    x="Sector",
                    y="Change_Pct",
                    text="Change_Pct"
                )

                fig_sector.update_layout(
                    paper_bgcolor="rgba(0,0,0,0)",
                    plot_bgcolor="rgba(0,0,0,0)",font=dict(color="#8DB79A"),height=350,
                    )

                st.plotly_chart(
                    fig_sector,use_container_width=True
                )
            
                st.markdown(
                    "<div class='section-header'>🎯 Signal Distribution</div>",
                        unsafe_allow_html=True,
                )

                signal_dist = (
                    display_rt["Signal"]
                    .value_counts()
                    .reset_index()
                )

                signal_dist.columns = [
                    "Signal",
                    "Count"
                ]

                fig_signal = px.pie(
                    signal_dist,
                    names="Signal",
                    values="Count",
                )

                fig_signal.update_layout(
                    paper_bgcolor="rgba(0,0,0,0)",
                    font=dict(color="#8DB79A"),height=350,
                )

                st.plotly_chart(
                    fig_signal,
                    use_container_width=True
                )
            
            st.markdown("<div class='section-header'>🗄️ Historical Batch Analytics</div><div class='section-divider'></div>", unsafe_allow_html=True)

            if not batch_csv.empty:
                b_df = batch_csv.copy()
                if selected_stock != "All":
                    b_df = batch_csv[batch_csv["Ticker"] == selected_stock]
                    if b_df.empty:
                        b_df = batch_csv
            
                b1, b2, b3, b4 = st.columns(4)
                with b1:
                    st.markdown(f"""<div class="kpi-card"><div class="kpi-label">📦 Total Volume Batch</div><div class="kpi-val">{fmt_vol(b_df["Volume"].sum())}</div><div class="kpi-sub-neutral">{DATASET_PERIOD}</div></div>""", unsafe_allow_html=True)
                with b2:
                    st.markdown(f"""<div class="kpi-card"><div class="kpi-label">💵 Avg Close (Batch)</div><div class="kpi-val">${round(b_df["Close"].mean(), 2)}</div><div class="kpi-sub-neutral">Historical average</div></div>""", unsafe_allow_html=True)
                with b3:
                    avg_change = b_df.groupby("Ticker")["Change_Pct"].mean()
                    best_ticker = avg_change.idxmax()
                    best_val = round(avg_change.max(), 2)
                    st.markdown(f"""<div class="kpi-card"><div class="kpi-label">🏆 Best Avg Return</div><div class="kpi-val" style="font-size:22px">{best_ticker}</div><div class="kpi-sub">▲ {best_val}% avg</div></div>""", unsafe_allow_html=True)
                with b4:
                    st.markdown(f"""<div class="kpi-card"><div class="kpi-label">📅 Data Period</div><div class="kpi-val" style="font-size:18px">{DATASET_PERIOD}</div><div class="kpi-sub-neutral">{len(b_df):,} records</div></div>""", unsafe_allow_html=True)

                st.markdown("<br>", unsafe_allow_html=True)
                hist_agg = (
                    b_df.groupby("Ticker")
                    .agg(Avg_Close=("Close", "mean"), Total_Volume=("Volume", "sum"), Avg_Change=("Change_Pct", "mean"))
                    .reset_index()
                    .sort_values("Avg_Close", ascending=False).head(rows_to_show)
                )
                st.markdown(f"<div class='section-header'>📈 Historical Avg Close Price — Top {rows_to_show} Emiten (Batch)</div>", unsafe_allow_html=True)
                fig_hist = go.Figure(
                    go.Bar(
                        x=hist_agg["Ticker"],
                        y=hist_agg["Avg_Close"],
                        marker=dict(
                            color=hist_agg["Avg_Change"],
                            colorscale=[[0, "#FF4B6E"], [0.5, "#173524"], [1, "#00FF94"]],
                            showscale=True,
                            colorbar=dict(title="Avg Change%", tickfont=dict(color="#8DB79A"), thickness=12),
                        ),
                        text=[f"${v:.0f}" for v in hist_agg["Avg_Close"]],
                        textposition="outside",
                        textfont=dict(color="#8DB79A", size=10, family="JetBrains Mono"),
                    )
                )
                fig_hist.update_layout(
                    paper_bgcolor="rgba(0,0,0,0)",
                    plot_bgcolor="rgba(0,0,0,0)",
                    font=dict(color="#8DB79A", family="JetBrains Mono"),
                    height=390,
                    margin=dict(l=10, r=10, t=30, b=10),
                    xaxis=dict(gridcolor="#12281C"),
                    yaxis=dict(gridcolor="#12281C", tickprefix="$"),
                )
                st.plotly_chart(fig_hist,use_container_width=True,config={"displayModeBar": False}
                )

            else:
                st.markdown(
                    f"""<div class="info-box-green">
                    No CSV found at <b>data/stock_data.csv</b>. The dashboard still runs using realtime simulation,
                    while the displayed dataset period remains locked to <b>{DATASET_PERIOD}</b>.
                    </div>""",
                    unsafe_allow_html=True,
                )

            st.markdown(
                   "<div class='section-header'>🔥 Market Sentiment Heatmap</div>",
                    unsafe_allow_html=True
)

            st.markdown("""
                    <div class="info-box">
                    <b>📖 Heatmap Purpose</b><br><br>

                    Heatmap digunakan untuk membaca kondisi pasar secara cepat berdasarkan perubahan harga (Change %).

                    🟢 <b>Hijau</b> = saham mengalami kenaikan harga<br>
                    🔴 <b>Merah</b> = saham mengalami penurunan harga<br>

                    Semakin pekat warnanya,
                    semakin besar perubahan harga yang terjadi.

                    Heatmap membantu investor mengidentifikasi:

                    <ul>
                    <li>Sektor atau emiten yang sedang bullish</li>
                    <li>Sektor atau emiten yang sedang bearish</li>
                    <li>Pergerakan pasar secara keseluruhan</li>
                    </ul>

                    </div>
                    """, unsafe_allow_html=True)

            hm_df = display_rt.copy()
            hm = go.Figure(
                data=go.Heatmap(
                    z=[hm_df["Change_Pct"].tolist()],
                    x=hm_df["Ticker"].tolist(),
                    y=["Sentiment"],
                    colorscale=[[0, "#7F1D1D"], [0.28, "#FF4B6E"], [0.5, "#173524"], [0.72, "#00D17A"], [1, "#00FF94"]],
                    zmid=0,
                    text=[[f"{v:+.1f}%" for v in hm_df["Change_Pct"].tolist()]],
                    texttemplate="%{text}",
                    textfont=dict(size=10, color="white", family="JetBrains Mono"),
                )
            )
            hm.update_layout(
                paper_bgcolor="rgba(0,0,0,0)",
                font_color="#8DB79A",
                height=150,
                margin=dict(l=10, r=10, t=10, b=10),
                font=dict(family="JetBrains Mono"),
            )
            st.plotly_chart(hm,use_container_width=True,config={"displayModeBar": False})
            bullish = len(hm_df[hm_df["Change_Pct"] > 0])
            bearish = len(hm_df[hm_df["Change_Pct"] < 0])
            total_stocks = len(hm_df)
            st.success(
                  f"""
                     Heatmap Summary

                        Bullish Stocks : {bullish}
                        Bearish Stocks : {bearish}
                        Total Stocks Analysed : {total_stocks}

                    Current market sentiment is dominated by
                    {'bullish' if bullish > bearish else 'bearish'} movement.
                  """,
                  icon="📈" if bullish > bearish else "📉",
                  )

            st.markdown(
                "<div class='section-header'>🤖 AI Market Intelligence </div>",
                unsafe_allow_html=True,
                )

            signal_buy = len(
                display_rt[
                    display_rt["Signal"] == "STRONG BUY"
                ]
            )

            signal_risk = len(
                display_rt[
                    display_rt["Signal"] == "RISK OFF"
                ]
            )

            avg_change = display_rt["Change_Pct"].mean()

            market_status = (
                "Bullish"
                if up_count > dn_count
                else "Bearish"
            )

            sector_perf = (
                display_rt
                .groupby("Sector")["Change_Pct"]
                .mean()
                .reset_index()
            )

            best_sector = (
                sector_perf
                .sort_values(
                    "Change_Pct",
                    ascending=False
                )
                .iloc[0]
            )

            market_score = (
                (up_count - dn_count)
                / len(display_rt)
            ) * 100

            if market_score > 20:
                market_grade = "🟢 Strong Bullish"
            elif market_score > 0:
                market_grade = "🟡 Mild Bullish"
            elif market_score > -20:
                market_grade = "🟠 Mild Bearish"
            else:
                market_grade = "🔴 Strong Bearish"

            confidence = min(
                100,
                round(
                    (
                        signal_buy /
                        max(signal_buy + signal_risk, 1)
                    ) * 100
                )
            )

            st.progress(confidence)

            st.caption(
                f"AI Confidence Score: {confidence}%"
            )

            st.success(
                f"""
            🤖 AI MARKET INTELLIGENCE REPORT

            Market Regime:
            {market_grade}

            Market Score:
            {market_score:.1f}%

            Average Return:
            {avg_change:.2f}%

            Top Performing Sector:
            {best_sector['Sector']}
            ({best_sector['Change_Pct']:.2f}%)

            Top Gainer:
            {top_gainer['Ticker']}
            (+{top_gainer['Change_Pct']:.2f}%)

            Top Loser:
            {top_loser['Ticker']}
            ({top_loser['Change_Pct']:.2f}%)

            Strong Buy Signals:
            {signal_buy}

            Risk-Off Signals:
            {signal_risk}

            Conclusion:
            The market is currently operating under a
            {market_status.lower()} regime.

            Sector rotation is favoring{best_sector['Sector']} stocks.

            Current market breadth shows{up_count} advancing stocks and{dn_count} declining stocks.

            Based on signal distribution,
            the short-term market outlook remains{'positive' if signal_buy > signal_risk else 'cautious'}.
            """
            )

            if top_gainer["Change_Pct"] > 5:
                st.success(
                    f"🚀 Momentum Alert: {top_gainer['Ticker']} is experiencing unusually strong bullish momentum."
                )

            if top_loser["Change_Pct"] < -5:
                st.error(
                    f"⚠️ Risk Alert: {top_loser['Ticker']} is under significant selling pressure."
                )

            if signal_buy > signal_risk:
                st.success(
                    "📈 AI Recommendation: Focus on momentum-based opportunities and strong sectors."
                )
        
            else:
                st.warning(
                    "📉 AI Recommendation: Defensive positioning is advised until sentiment improves."
                )    

        elif page == "⚡ Live Feed":
            st.markdown("<div class='section-header'>⚡ Real-Time Trading Feed</div><div class='section-divider'></div>", unsafe_allow_html=True)
            st.markdown(
                f"""
                <div class="info-box-green">
                    📡 <b>Live Market Simulation</b> — Feed transaksi realtime disimulasikan via <b>Kafka Streaming</b> pipeline.<br>
                    📅 Tahun: 2018-2023
                    🔍 Filter: <b>{selected_stock}</b>
                    &nbsp;|&nbsp; 📦 Batch Period: <b>{DATASET_PERIOD}</b>
                </div>
                """,
                unsafe_allow_html=True,
            )
            feed_tickers = display_rt["Ticker"].tolist()
            if len(feed_tickers) == 0:
                feed_tickers = ALL_TICKERS

            for i in range(min(rows_to_show, len(feed_tickers))):
                tk = feed_tickers[i % len(feed_tickers)]
                filtered_row = rt_df[
                rt_df["Ticker"] == tk
                ]
                if filtered_row.empty:
                    continue
                row = filtered_row.iloc[0]
                chg = round(random.uniform(-5, 5), 2)
                vol_f = fmt_vol(random.randint(100_000, 2_000_000))
                price_f = round(float(row["Price"]) + random.uniform(-2, 2), 2)
                ts = (current_time - timedelta(seconds=random.randint(0, 45))).strftime("%H:%M:%S")

                if chg >= 0:
                    chg_html = f'<div class="feed-change-up">▲ +{chg}%</div>'
                    side_color = "#00FF94"
                    side_label = "BUY"
                else:
                    chg_html = f'<div class="feed-change-dn">▼ {chg}%</div>'
                    side_color = "#FF4B6E"
                    side_label = "SELL"

                st.markdown(
                    f"""
                    <div class="feed-item">
                        <div><div class="feed-ticker">{tk}</div><div class="feed-time">{ts}</div></div>
                        <div><div style="font-size:12px;color:#8DB79A">Vol: <b style="color:#EAFBF1;font-family:'JetBrains Mono',monospace">{vol_f}</b></div><div style="font-size:11px;color:#4D705A">{dataset_end.strftime('%d %b %Y')}</div></div>
                        <div style="font-family:'JetBrains Mono',monospace;font-weight:800;font-size:16px;color:#EAFBF1">${price_f}</div>
                        <div style="display:flex;flex-direction:column;align-items:flex-end;gap:5px">{chg_html}<div style="font-size:10px;color:{side_color};font-family:'JetBrains Mono',monospace;border:1px solid {side_color}55;border-radius:4px;padding:2px 8px;font-weight:800">{side_label}</div></div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

        elif page == "⭐ Smart Watchlist":
            st.markdown("<div class='section-header'>⭐ Smart Watchlist</div><div class='section-divider'></div>", unsafe_allow_html=True)
            watch = display_rt.sort_values(["Change_Pct", "Volume"], ascending=[False, False]).head(12).copy()
            watch["Volume"] = watch["Volume"].apply(fmt_vol)

            st.markdown(
                f"""
                <div class="rank-grid">
                    <div class="rank-card"><div class="rank-label">Bullish Ratio</div><div class="rank-value">{up_pct_rt}%</div></div>
                    <div class="rank-card"><div class="rank-label">Most Active</div><div class="rank-value">{display_rt.sort_values("Volume", ascending=False).iloc[0]["Ticker"]}</div></div>
                    <div class="rank-card"><div class="rank-label">Signal Leader</div><div class="rank-value">{top_gainer["Ticker"]}</div></div>
                    <div class="rank-card"><div class="rank-label">Dataset</div><div class="rank-value" style="font-size:17px">{DATASET_PERIOD}</div></div>
                </div>
                """,
                unsafe_allow_html=True,
            )
            watch = (
                display_rt[
                    display_rt["Signal"] == "STRONG BUY"
                ]
                .sort_values(
                     ["Change_Pct", "Volume"],
                     ascending=[False, False]
                )
            ) 

            if watch.empty:
                watch = (
                    display_rt
                    .sort_values(
                        ["Change_Pct", "Volume"],ascending=[False, False]
                        )
                        .head(12)
                )
            else:
                watch = watch.head(12)
            
            st.success(
                f"""
                ⭐ Smart Watchlist Logic

                Stocks are selected using:

                • Highest Change %
                • Highest Volume
                • STRONG BUY Signal

                Current Candidates:
                {len(watch)} stocks
                """
                )

            best_stock = watch.iloc[0]
            st.info(
                f"""
                🏆 Top Watchlist Candidate

                Ticker : {best_stock['Ticker']}

                Change : {best_stock['Change_Pct']:.2f}%

                Volume : {fmt_vol(best_stock['Volume'])}

                Signal : {best_stock['Signal']}
                """
                )

            fig_watch = px.bar(
            watch,
            x="Ticker",
            y="Change_Pct",
            color="Signal",
            text="Change_Pct"
            )

            fig_watch.update_layout(
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            font=dict(color="#8DB79A"),
            height=350
            )

            st.plotly_chart(
            fig_watch,
            use_container_width=True
            )

            st.dataframe(
                watch[["Ticker", "Sector", "Price", "Change_Pct", "Volume", "Spread", "Signal", "Timestamp"]],
                use_container_width=True,
                height=460,
                hide_index=True,
            )

        st.markdown(
            f"""
            <div style="text-align:center;color:#173524;font-size:11px;
                        font-family:'JetBrains Mono',monospace;padding:16px 0;margin-top:10px;
                        border-top:1px solid #0B1710">
                MarketPulse Terminal v3.0 &nbsp;•&nbsp;
                Batch Data: {DATASET_PERIOD} &nbsp;•&nbsp;
                Dataset End: {dataset_end.strftime('%Y-%m-%d')}
            </div>
            """,
            unsafe_allow_html=True,
        )