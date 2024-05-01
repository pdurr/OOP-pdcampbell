# pragma once
from processor import DataProcessor


def main() -> None:
    """Main function to process input data and analyze cases."""
    processor: DataProcessor = DataProcessor()
    while True:
        try:
            line: str = input().strip()
            if not line:
                break
            n, *data = map(int, line.split())
            processor.add_case(data)
        except EOFError:
            break

    processor.analyze_cases()


if __name__ == "__main__":
    main()
