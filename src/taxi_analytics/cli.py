import argparse
import logging
from taxi_analytics.pipeline import execute_pipeline, run_profile, run_validation

def main():
    parser=argparse.ArgumentParser(prog="taxi-analytics",description="Seaborn taxi NumPy/pandas analytics")
    parser.add_argument("--config",default=None,help="Optional YAML config file")
    sub=parser.add_subparsers(dest="command",required=True)
    run=sub.add_parser("run",help="Run complete analytics pipeline")
    run.add_argument("--no-charts",action="store_true")
    run.add_argument("--refresh",action="store_true")
    sub.add_parser("profile",help="Profile the source dataset")
    sub.add_parser("validate",help="Run data-quality checks")
    args=parser.parse_args()
    try:
        if args.command=="run":
            result=execute_pipeline(args.config,False if args.no_charts else None,args.refresh)
            print(f"Pipeline complete: {result['summary']['raw_rows']} source rows.")
        elif args.command=="profile": run_profile(args.config)
        else: run_validation(args.config)
    except Exception:
        logging.exception("Command failed")
        raise

if __name__=="__main__": main()
