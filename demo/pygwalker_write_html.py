import pygwalker as pyg
import pandas as pd


df = pd.read_csv("../data/cereal/cereal_data.csv", sep=";")

with open("pyg_report.html", "w", encoding="utf-8") as f:
    html = pyg.to_html(df, spec="./gw_config.json")
    f.write(html)