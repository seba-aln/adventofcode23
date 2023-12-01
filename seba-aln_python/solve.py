import argparse
import importlib
import os


def main():
    parser = argparse.ArgumentParser(description="Argument Parser Example")
    parser.add_argument("--day", type=int, help="Specify a day (integer)")
    parser.add_argument("--set", choices=["test1", "test2", "1", "2"],
                        help="Specify a set (test1/test2/1/2)")
    args = parser.parse_args()

    day_value = args.day
    set_value = args.set

    solution = importlib.import_module(f"day_{day_value}.day_{day_value}")
    solve = getattr(solution, "solve")

    cwd = os.getcwd()
    try:
        with open(f"{cwd}/day_{day_value}/{set_value}.txt", "r") as input_file:
            data = input_file.readlines()
            print(solve(data, 1 if set_value.endswith('1') else 2))
    except FileNotFoundError as e:
        print(e)


if __name__ == "__main__":
    main()
