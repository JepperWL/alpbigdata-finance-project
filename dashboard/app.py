import streamlit as st
import pandas as pd
import random
import time
from datetime import datetime
import plotly.express as px
import plotly.graph_objects as go

# Page Configuration
st.set_page_config(
    page_title="Yahoo Finance Stocks Market Dashboard",
    page_icon="📈",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>

/* =========================================================
Global Styles
========================================================= */

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
    background-color: #050816;
    color: white;
}

/* =========================================================
Background
========================================================= */

.stApp {
    background:
    radial-gradient(circle at top left,
    rgba(0,255,170,0.14), transparent 25%),

    radial-gradient(circle at bottom right,
    rgba(59,130,246,0.12), transparent 25%),

    linear-gradient(135deg,
    #050816 0%,
    #09111f 100%);
}

/* =========================================================
Remove Streamlit Default 
========================================================= */

#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

/* =========================================================
Sidebar
========================================================= */

section[data-testid="stSidebar"] {
    background: rgba(255,255,255,0.03);
    border-right: 1px solid rgba(255,255,255,0.05);
}

/* =========================================================
Title
========================================================= */

.title {
    font-size: 68px;
    font-weight: 900;
    color: white;
    margin-bottom: 0;
    letter-spacing: -2px;
}

.subtitle {
    color: #9CA3AF;
    font-size: 20px;
    margin-top: -10px;
}

/* =========================================================
Live Status
========================================================= */

.live {
    color: #00FFAA;
    font-weight: 700;
    font-size: 15px;
    margin-top: 10px;
}

/* =========================================================
Glass Card
========================================================= */

.glass {

    background: rgba(255,255,255,0.05);

    backdrop-filter: blur(16px);

    border-radius: 26px;

    padding: 30px;

    border: 1px solid rgba(255,255,255,0.08);

    transition: 0.3s ease;

    box-shadow:
    0px 0px 35px rgba(0,0,0,0.25);
}

.glass:hover {

    transform: translateY(-6px);

    border: 1px solid rgba(0,255,170,0.25);

    box-shadow:
    0px 0px 40px rgba(0,255,170,0.10);
}

/* =========================================================
KPI
========================================================= */

.kpi-title {
    color: #9CA3AF;
    font-size: 15px;
}

.kpi-value {
    color: white;
    font-size: 42px;
    font-weight: 900;
    margin-top: 10px;
}

/* =========================================================
Section
========================================================= */

.section {
    font-size: 28px;
    font-weight: 800;
    margin-bottom: 12px;
}

/* =========================================================
Ticker
========================================================= */

.ticker-wrap {

    overflow: hidden;

    white-space: nowrap;

    background: rgba(255,255,255,0.04);

    border-radius: 18px;

    padding: 16px;

    margin-top: 22px;
    margin-bottom: 25px;

    border: 1px solid rgba(255,255,255,0.05);
}

.ticker {

    display: inline-block;

    padding-left: 100%;

    animation: ticker 28s linear infinite;

    color: #00FFAA;

    font-weight: 700;
}

@keyframes ticker {

    0% {
        transform: translateX(0%);
    }

    100% {
        transform: translateX(-100%);
    }
}

/* =========================================================
Activity Panel
========================================================= */

.activity {

    background: rgba(255,255,255,0.05);

    border-radius: 20px;

    padding: 20px;

    margin-bottom: 16px;

    border: 1px solid rgba(255,255,255,0.05);
}

/* =========================================================
Table
========================================================= */

[data-testid="stDataFrame"] {

    border-radius: 18px;

    overflow: hidden;
}

/* =========================================================
Scrollbar
========================================================= */

::-webkit-scrollbar {
    width: 8px;
}

::-webkit-scrollbar-thumb {
    background: #00FFAA;
    border-radius: 10px;
}

</style>
""", unsafe_allow_html=True)

# Sidebar
st.sidebar.title("📈 Yahoo Finance Stocks Market Dashboard")

page = st.sidebar.radio(
    "Navigation",
    ["Overview", "Analytics", "Live Feed"]
)

# Header
st.markdown(
    "<div class='title'> Yahoo Finance Stocks Market Dashboard</div>",
    unsafe_allow_html=True
)

st.markdown(
    "<div class='subtitle'>Enterprise Real-Time Financial Intelligence Platform</div>",
    unsafe_allow_html=True
)

current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

st.markdown(
    f"<div class='live'>🟢 LIVE MARKET ACTIVE | {current_time}</div>",
    unsafe_allow_html=True
)

# 50 STOCKS
all_tickers = [
    "AAPL", "TSLA", "MSFT", "GOOGL", "NVDA",
    "META", "AMZN", "NFLX", "AMD", "INTC",
    "BABA", "ORCL", "IBM", "UBER", "SPOT",
    "PYPL", "SHOP", "SNAP", "CRM", "ADBE",
    "QCOM", "AVGO", "SONY", "DIS", "NKE",
    "PINS", "SQ", "COIN", "PLTR", "ARM",
    "SAP", "ZM", "ROKU", "EBAY", "CSCO",
    "HPQ", "DELL", "V", "MA", "JPM",
    "BAC", "GS", "WMT", "COST", "PEP",
    "KO", "T", "VZ", "XOM", "CVX"
]

# Ticker Text
st.markdown("""
<div class="ticker-wrap">
<div class="ticker">

🚀 NVDA +4.2% &nbsp;&nbsp;&nbsp;
📈 AAPL +2.1% &nbsp;&nbsp;&nbsp;
⚠️ TSLA -1.3% &nbsp;&nbsp;&nbsp;
📊 MSFT +1.9% &nbsp;&nbsp;&nbsp;
🔥 META +3.1% &nbsp;&nbsp;&nbsp;
💹 AMZN +2.4% &nbsp;&nbsp;&nbsp;
📉 NFLX -0.7%

</div>
</div>
""", unsafe_allow_html=True)

placeholder = st.empty()

# Market Events Generator
positive_events = [
    "bullish breakout detected",
    "strong buy pressure detected",
    "institutional accumulation spotted",
    "volume surge confirmed",
    "price momentum increasing",
    "new resistance level broken"
]

negative_events = [
    "heavy sell pressure detected",
    "bearish momentum increasing",
    "support level broken",
    "high volatility warning",
    "institutional selling activity",
    "market correction detected"
]

# Realtime Loop
while True:

    tickers = random.sample(all_tickers, 50)

    avg_close = [
        round(random.uniform(100, 350), 2)
        for _ in range(len(tickers))
    ]

    volume = [
        random.randint(1000000, 9000000)
        for _ in range(len(tickers))
    ]

    changes = [
        round(random.uniform(-5, 5), 2)
        for _ in range(len(tickers))
    ]

    df = pd.DataFrame({
        "Ticker": tickers,
        "Average Close": avg_close,
        "Volume": volume,
        "Change %": changes
    })

    # Fixed Top Stocks
    df = df.sort_values(
        by="Average Close",
        ascending=False
    )

    total_volume = sum(volume)

    market_avg = round(
        df["Average Close"].mean(),
        2
    )

    top_stock = df.iloc[0]["Ticker"]

    # Top Gainers / Losers
    gainers = df.sort_values(
        by="Change %",
        ascending=False
    ).head(5)

    losers = df.sort_values(
        by="Change %"
    ).head(5)

    # Top 10 + OTHERS for Donut Chart
    top10 = df.head(10)

    others_volume = df.iloc[10:]["Volume"].sum()

    donut_labels = list(top10["Ticker"]) + ["OTHERS"]

    donut_values = list(top10["Volume"]) + [others_volume]

    with placeholder.container():

        # KPI Row
        k1, k2, k3, k4 = st.columns(4)

        with k1:
            st.markdown(f"""
            <div class="glass">
                <div class="kpi-title">📊 Total Volume</div>
                <div class="kpi-value">{total_volume:,}</div>
            </div>
            """, unsafe_allow_html=True)

        with k2:
            st.markdown(f"""
            <div class="glass">
                <div class="kpi-title">📈 Market Average</div>
                <div class="kpi-value">${market_avg}</div>
            </div>
            """, unsafe_allow_html=True)

        with k3:
            st.markdown(f"""
            <div class="glass">
                <div class="kpi-title">🏆 Top Stock</div>
                <div class="kpi-value">{top_stock}</div>
            </div>
            """, unsafe_allow_html=True)

        with k4:
            st.markdown(f"""
            <div class="glass">
                <div class="kpi-title">⚡ Active Stocks</div>
                <div class="kpi-value">50</div>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        # Overview
        if page == "Overview":

            left, right = st.columns([1.8, 1])

            with left:

                st.markdown(
                    "<div class='section'>📈 Market Performance</div>",
                    unsafe_allow_html=True
                )

                fig_line = px.line(
                    df.head(20),
                    x="Ticker",
                    y="Average Close",
                    color="Change %",
                    markers=True
                )

                fig_line.update_traces(
                    line=dict(width=4)
                )

                fig_line.update_layout(
                    paper_bgcolor='rgba(0,0,0,0)',
                    plot_bgcolor='rgba(0,0,0,0)',
                    font_color='white',
                    height=430
                )

                st.plotly_chart(
                    fig_line,
                    use_container_width=True
                )

            with right:

                st.markdown(
                    "<div class='section'>🔥 Top Gainers</div>",
                    unsafe_allow_html=True
                )

                st.dataframe(
                    gainers,
                    use_container_width=True,
                    height=210
                )

                st.markdown(
                    "<div class='section'>📉 Top Losers</div>",
                    unsafe_allow_html=True
                )

                st.dataframe(
                    losers,
                    use_container_width=True,
                    height=210
                )

            bottom1, bottom2 = st.columns([1.5, 1])

            with bottom1:

                st.markdown(
                    "<div class='section'>📋 Live Market Table</div>",
                    unsafe_allow_html=True
                )

                st.dataframe(
                    df,
                    use_container_width=True,
                    height=500
                )

            with bottom2:

                st.markdown(
                    "<div class='section'>🥧 Market Share</div>",
                    unsafe_allow_html=True
                )

                fig_pie = go.Figure(
                    data=[
                        go.Pie(
                            labels=donut_labels,
                            values=donut_values,
                            hole=.72
                        )
                    ]
                )

                fig_pie.update_layout(
                    paper_bgcolor='rgba(0,0,0,0)',
                    font_color='white',
                    height=450
                )

                st.plotly_chart(
                    fig_pie,
                    use_container_width=True
                )

        # Analytics
        elif page == "Analytics":

            st.markdown(
                "<div class='section'>📊 Volume Analytics</div>",
                unsafe_allow_html=True
            )

            fig_bar = px.bar(
                df.head(25),
                x="Ticker",
                y="Volume",
                color="Change %"
            )

            fig_bar.update_layout(
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)',
                font_color='white',
                height=500
            )

            st.plotly_chart(
                fig_bar,
                use_container_width=True
            )

            st.markdown(
                "<div class='section'>🔥 Market Heatmap</div>",
                unsafe_allow_html=True
            )

            heatmap_df = df.head(20)

            fig_heat = go.Figure(
                data=go.Heatmap(
                    z=[heatmap_df["Change %"]],
                    x=heatmap_df["Ticker"],
                    y=["Market"],
                    colorscale="RdYlGn"
                )
            )

            fig_heat.update_layout(
                paper_bgcolor='rgba(0,0,0,0)',
                font_color='white',
                height=250
            )

            st.plotly_chart(
                fig_heat,
                use_container_width=True
            )

        # Live Feed
        elif page == "Live Feed":

            st.markdown(
                "<div class='section'>⚡ Real-Time Trading Feed</div>",
                unsafe_allow_html=True
            )

            for i in range(25):

                random_stock = random.choice(tickers)

                random_volume = random.randint(
                    100000,
                    900000
                )

                random_change = round(
                    random.uniform(-5, 5),
                    2
                )

                if random_change > 0:

                    color = "#00FFAA"

                    event = random.choice(
                        positive_events
                    )

                    icon = "🚀"

                else:

                    color = "#FF4B4B"

                    event = random.choice(
                        negative_events
                    )

                    icon = "⚠️"

                st.markdown(f"""
                <div class="activity">

                {icon} [{datetime.now().strftime("%H:%M:%S")}]

                <br><br>

                <b>{random_stock}</b>
                {event}

                <br><br>

                Volume activity:
                <b>{random_volume:,}</b>

                <br><br>

                Price Change:
                <span style="color:{color}; font-weight:bold;">
                {random_change}%
                </span>

                </div>
                """, unsafe_allow_html=True)

        st.caption("⚡ Auto-refresh every 3 seconds")

    time.sleep(3)