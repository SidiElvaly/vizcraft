from __future__ import annotations

from typing import Optional

import pandas as pd
import geopandas as gpd
from bokeh.io import output_file, save
from bokeh.models import GeoJSONDataSource, LinearColorMapper, ColorBar, HoverTool
from bokeh.palettes import brewer, linear_palette, Viridis256
from bokeh.plotting import figure


def election_map_bokeh(
    shapefile_path: str,
    data_df: pd.DataFrame,
    region_col_shape: str,
    region_col_data: str,
    value_col: str,
    output_html: str = "election_map.html",
    title: str = "Election Map",
    *,
    width: int = 1100,
    height: int = 650,
    fill_alpha: float = 0.85,
    line_color: str = "black",
    line_width: float = 0.6,
    palette_name: str = "OrRd",
    palette_steps: int = 9,
    low: Optional[float] = None,
    high: Optional[float] = None,
    nan_color: str = "lightgrey",
    legend_label: str = "Nombre de voix",
):
    gdf = gpd.read_file(shapefile_path)

    if region_col_shape not in gdf.columns:
        raise ValueError(f"'{region_col_shape}' not found in shapefile columns: {gdf.columns.tolist()}")
    if region_col_data not in data_df.columns:
        raise ValueError(f"'{region_col_data}' not found in data_df columns: {data_df.columns.tolist()}")
    if value_col not in data_df.columns:
        raise ValueError(f"'{value_col}' not found in data_df columns: {data_df.columns.tolist()}")

    gdf = gdf.copy()
    data_df = data_df.copy()

    gdf[region_col_shape] = gdf[region_col_shape].astype(str).str.strip().str.lower()
    data_df[region_col_data] = data_df[region_col_data].astype(str).str.strip().str.lower()

    data_df[value_col] = pd.to_numeric(data_df[value_col], errors="coerce")

    gdf = gdf.merge(
        data_df[[region_col_data, value_col]],
        left_on=region_col_shape,
        right_on=region_col_data,
        how="left",
    )

    gdf = gdf[[region_col_shape, value_col, "geometry"]]

    if gdf.crs is not None:
        try:
            gdf = gdf.to_crs(epsg=3857)
        except Exception:
            pass

    vmin = float(gdf[value_col].min()) if low is None else float(low)
    vmax = float(gdf[value_col].max()) if high is None else float(high)
    if vmax == vmin:
        vmax = vmin + 1.0

    try:
        base = brewer[palette_name][palette_steps]
        pal = linear_palette(base, 256)
    except Exception:
        pal = Viridis256

    color_mapper = LinearColorMapper(palette=pal, low=vmin, high=vmax, nan_color=nan_color)

    geo_source = GeoJSONDataSource(geojson=gdf.to_json())

    p = figure(
        title=title,
        tools="pan,wheel_zoom,reset,hover,save",
        x_axis_location=None,
        y_axis_location=None,
        width=width,
        height=height,
        active_scroll="wheel_zoom",
    )
    p.grid.grid_line_color = None

    p.patches(
        "xs",
        "ys",
        source=geo_source,
        fill_color={"field": value_col, "transform": color_mapper},
        fill_alpha=fill_alpha,
        line_color=line_color,
        line_width=line_width,
    )

    hover = p.select_one(HoverTool)
    hover.tooltips = [
        ("Moughataa", f"@{region_col_shape}"),
        (legend_label, f"@{value_col}{{0,0}}"),
    ]

    p.add_layout(ColorBar(color_mapper=color_mapper, label_standoff=10, title=legend_label), "right")

    output_file(output_html, title=title)
    save(p)
    return p
