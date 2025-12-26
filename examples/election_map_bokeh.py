import pandas as pd
import vizcraft as vc

CSV_URL = "https://raw.githubusercontent.com/binorassocies/rimdata/refs/heads/main/data/results_elections_rim_2019-2024.csv"
SHAPEFILE = "/home/sidi/vizcraft/src/vizcraft/mrshape/mrt_admbnda_adm2_ansade_20240327.shp"

df = pd.read_csv(CSV_URL)

df_2024 = df[df["year"] == 2024].copy()

df_agg_2024 = (
    df_2024
    .groupby(["candidate", "moughataa"], as_index=False)["nb_votes"]
    .sum()
)

global_low = float(df_agg_2024["nb_votes"].min())
global_high = float(df_agg_2024["nb_votes"].max())

candidates = sorted(df_agg_2024["candidate"].unique())

for cand in candidates:
    df_c = df_agg_2024[df_agg_2024["candidate"] == cand].copy()

    vc.election_map_bokeh(
        shapefile_path=SHAPEFILE,
        data_df=df_c,
        region_col_shape="ADM2_EN",
        region_col_data="moughataa",
        value_col="nb_votes",
        output_html=f"election_2024_{cand.replace(' ', '_')}.html",
        title=f"Résultats {cand} - Élection 2024 (ADM2)",
        palette_name="OrRd",
        legend_label="Nombre de voix",
        nan_color="lightgrey",
        low=global_low,
        high=global_high,
    )

print("HTML maps generated for all candidates (same scale).")
