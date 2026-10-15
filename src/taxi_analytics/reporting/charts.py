from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns

def generate_charts(df, output_dir: Path):
    output_dir.mkdir(parents=True, exist_ok=True)
    sns.set_theme(style="whitegrid")
    generated=[]
    plot = df.loc[df["distance"].gt(0) & df["fare"].notna(), ["distance","fare","color"]].dropna()
    if len(plot):
        sample = plot.sample(min(4000,len(plot)), random_state=42)
        fig,ax=plt.subplots(figsize=(9,5))
        sns.scatterplot(data=sample,x="distance",y="fare",hue="color",alpha=.55,ax=ax)
        ax.set_title("Recorded Fare vs Trip Distance (visual sample)")
        fig.tight_layout(); p=output_dir/"fare_vs_distance.png"; fig.savefig(p,dpi=150); plt.close(fig)
        generated.append(str(p))
    hourly=df.groupby("pickup_hour",dropna=True).size().rename("trip_records").reset_index()
    if len(hourly):
        fig,ax=plt.subplots(figsize=(9,5)); sns.barplot(data=hourly,x="pickup_hour",y="trip_records",ax=ax)
        ax.set_title("Trip Records by Pickup Hour"); fig.tight_layout()
        p=output_dir/"trips_by_pickup_hour.png"; fig.savefig(p,dpi=150); plt.close(fig); generated.append(str(p))
    corr=df.select_dtypes(include="number").corr()
    if len(corr.columns):
        fig,ax=plt.subplots(figsize=(8,6)); sns.heatmap(corr,annot=True,fmt=".2f",cmap="vlag",center=0,ax=ax)
        ax.set_title("Numeric Feature Correlations"); fig.tight_layout()
        p=output_dir/"numeric_correlation_heatmap.png"; fig.savefig(p,dpi=150); plt.close(fig); generated.append(str(p))
    return generated
