# Install Streamlit if not already installed
!pip install streamlit -q

import streamlit as st
import pandas as pd
import json
from pathlib import Path

# ----------------------------
# Page Config
# ----------------------------
st.set_page_config(page_title="Store Intelligence Dashboard", layout="wide")

st.title("🛍️ Store Intelligence System Dashboard")
st.markdown("Real-time analytics for retail CCTV + event pipeline")

# ----------------------------
# Load Data
# ----------------------------
DATA_PATH = Path("events_all.jsonl")

def load_data():
    if not DATA_PATH.exists():
        return pd.DataFrame()

    records = []
    with open(DATA_PATH, "r") as f:
        for line in f:
            try:
                records.append(json.loads(line))
            except:
                pass

    return pd.DataFrame(records)

df = load_data()

# ----------------------------
# Refresh Button
# ----------------------------
if st.button("🔄 Refresh Data"):
    df = load_data()

# ----------------------------
# Empty State
# ----------------------------
if df.empty:
    st.warning("No event data found. Run the pipeline first.")
    st.stop()

# ----------------------------
# Metrics Section
# ----------------------------
st.subheader("📊 Key Metrics")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Events", len(df))

with col2:
    entry_count = len(df[df["event_type"] == "entry"]) if "event_type" in df else 0
    st.metric("Entries (Footfall)", entry_count)

with col3:
    exit_count = len(df[df["event_type"] == "exit"]) if "event_type" in df else 0
    st.metric("Exits", exit_count)

# Conversion Rate
st.subheader("📈 Conversion Rate")

conversion = (exit_count / entry_count * 100) if entry_count > 0 else 0
st.metric("Conversion %", round(conversion, 2))

# ----------------------------
# Event Type Distribution
# ----------------------------
st.bar_chart(df["event_type"].value_counts())

# ----------------------------
# Timeline Analysis
# ----------------------------
st.subheader("⏱️ Event Timeline")

if "timestamp" in df.columns:
    df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")
    timeline = df.groupby(df["timestamp"].dt.floor("min")).size()
    st.line_chart(timeline)

# ----------------------------
# Anomaly Detection (simple logic)
# ----------------------------
st.subheader("⚠️ Anomaly Detection")

if len(df) > 10:
    grouped = df.groupby(df.index // 10).size()
    threshold = grouped.mean() + 2 * grouped.std()

    anomalies = grouped[grouped > threshold]

    if len(anomalies) > 0:
        st.error("Anomaly detected (spike in activity)")
        st.write(anomalies)
    else:
        st.success("No anomalies detected")

# ----------------------------
# Raw Data Viewer
# ----------------------------
st.subheader("📄 Raw Event Data")
st.dataframe(df, use_container_width=True)
