import os
import random
import pandas as pd
import plotly.graph_objects as go

DATA_DIR = os.path.join(os.path.dirname(__file__), "data")
SITES_DIR = os.path.join(os.path.dirname(__file__), "sites")

csv_files = [f for f in os.listdir(DATA_DIR) if f.endswith(".csv")]
if not csv_files:
    raise FileNotFoundError(f"No CSV files found in {DATA_DIR}")
chosen = random.choice(csv_files)
csv_path = os.path.join(DATA_DIR, chosen)

df = pd.read_csv(csv_path)

x_col = "Timestamp" if "Timestamp" in df.columns else df.columns[0]

fig = go.Figure()
for col in df.columns:
    if col == x_col:
        continue
    fig.add_trace(go.Scatter(x=df[x_col], y=df[col], mode="lines", name=col))

fig.update_layout(
    title=f"Thermal data: {chosen}",
    xaxis_title="Timestamp",
    yaxis_title="Value",
    xaxis=dict(tickangle=-45),
    template="plotly_dark",
)

os.makedirs(SITES_DIR, exist_ok=True)
output_path = os.path.join(SITES_DIR, "index.html")
fig.write_html(output_path)
print(f"Visualised {chosen} -> {output_path}")
