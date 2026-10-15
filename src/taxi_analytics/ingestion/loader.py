import logging
from pathlib import Path
import pandas as pd
import seaborn as sns
logger = logging.getLogger(__name__)

def load_taxi_dataset(cache_path: Path, refresh=False):
    cache_path.parent.mkdir(parents=True, exist_ok=True)
    if cache_path.exists() and not refresh:
        logger.info("Loading cached data: %s", cache_path)
        return pd.read_csv(cache_path)
    logger.info("Fetching Seaborn dataset taxis")
    try:
        df = sns.load_dataset("taxis")
    except Exception as exc:
        raise RuntimeError("Could not fetch Seaborn taxis dataset. Connect to the internet for the first run or provide data/raw/taxis.csv.") from exc
    df.to_csv(cache_path, index=False)
    return df
