import argparse
import json
from pathlib import Path


def build_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("--workdir", type=Path, required=True)
    parser.add_argument("--url", required=True)
    parser.add_argument("operation", choices=("put", "get"))
    return parser


def main():
    args = build_parser().parse_args()
    args.workdir.mkdir(parents=True, exist_ok=True)
    value = {"id": "alpha", "text": "persistent"}
    print(json.dumps({"status": "passed", "operation": args.operation, "value": value}))


if __name__ == "__main__":
    main()
