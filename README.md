
# VizCraft — Personal Python Visualization Library

## Overview

**VizCraft** is a personal Python visualization library built on top of **Matplotlib** and **Bokeh**.
It provides reusable plotting functions with a **consistent custom visual style** and supports
both **static** and **interactive** visualizations.

The library was developed as part of an academic project to demonstrate:
- clean visualization logic,
- reusable design,
- and the ability to reproduce the **same analytical logic** using different visualization tools.

---

## Features

- Unified visual theme (colors, fonts, grid, axes, line width)
- Clean and simple API
- Modular code structure
- Standard Python packaging
- Reusable across projects
- Interactive maps with **Bokeh** (zoom + hover)

### Available Charts (Matplotlib)

- `styled_line` — Line plot
- `styled_scatter` — Scatter plot
- `styled_bar` — Bar chart
- `styled_hist` — Histogram
- `styled_pie` — Pie chart

### Interactive Visualization (Bokeh)

- `election_map_bokeh` — Interactive choropleth election map
  
  - Fixed color scale
  - Hover tooltips
  - Zoom and pan
  - HTML output

---

## Project Structure

```text
vizcraft/
├── README.md
├── pyproject.toml
├── src/
│   └── vizcraft/
│       ├── __init__.py
│       ├── style.py         # Global visual theme
│       ├── plots.py         # Matplotlib charts
│       └── bokeh_maps.py    # Bokeh interactive maps
└── examples/
    ├── demo.py
    └── election_map_bokeh.py
````

---

## Step-by-Step Setup

### Step 1 — Clone the repository

```bash
git clone https://github.com/SidiElvaly/vizcraft.git
cd vizcraft
```

---

### Step 2 — Create and activate a virtual environment

```bash
python -m venv .venv
```

**Windows**

```bash
.venv\Scripts\activate
```

**Linux / macOS**

```bash
source .venv/bin/activate
```

---

### Step 3 — Install dependencies and the library

```bash
pip install --upgrade pip
pip install -e .
```

This installs the library in editable mode.

---

## Basic Usage (Matplotlib)

Once installed, the library can be used from any Python script.

```python
import vizcraft as vc

vc.styled_line(
    x=[1, 2, 3],
    y=[4, 2, 5],
    title="My styled plot",
    xlabel="X",
    ylabel="Y"
)
```

---

## Interactive Election Map (Bokeh)



### Example

```python
import pandas as pd
import vizcraft as vc

df = pd.read_csv("results_elections_rim_2019-2024.csv")
df_2024 = df[df["year"] == 2024]

df_agg = (
    df_2024.groupby(["candidate", "moughataa"], as_index=False)["nb_votes"]
    .sum()
)

vc.election_map_bokeh(
    shapefile_path="mrt_admbnda_adm2.shp",
    data_df=df_agg,
    region_col_shape="ADM2_EN",
    region_col_data="moughataa",
    value_col="nb_votes",
    output_html="election_2024.html",
    title="Mauritania Presidential Election 2024",
)
```

### Features

* Zoom and pan
* Hover tooltips (region + number of votes)
* Same color scale as GeoPandas version
* Missing regions shown in grey
* Output as interactive **HTML**

---

## Demo Scripts

### Matplotlib Demo

```bash
python examples/demo.py
```

### Bokeh Election Map Demo

```bash
python examples/election_map_bokeh.py
```


## Custom Theme

The library exposes a `Theme` class to customize the visual identity.

```python
from vizcraft import Theme, apply_style

custom_theme = Theme(
    primary="#7C3AED",
    secondary="#22C55E",
    accent="#F97316"
)

apply_style(custom_theme)
```

All subsequent Matplotlib plots automatically use the custom theme.

---

## Packaging Details

The project uses a modern Python packaging standard defined in `pyproject.toml`.

Key points:

* Source code is located in `src/`
* The package is installable via `pip`
* Dependencies are automatically resolved
* Compatible with academic and production workflows


