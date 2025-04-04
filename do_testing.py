#!/usr/bin/env python3
import subprocess
import sys

def run_static_eraser(args):
    try:
        if args[2] != "Y" and args[2] != "y":
            subprocess.run(["cp", "eraser_cpy.db", "eraser.db"], check=True)

        subprocess.run(["./static_eraser"] + args, check=True)
        with open("timing_output.txt", "r") as f:
            output = f.read()

        print("Raw file contents:")
        print(output)

        return [int(num) for num in output.split(" ")]

    except subprocess.CalledProcessError as e:
        print(f"Error running script: {e}")
        exit(1)
    except FileNotFoundError as e:
        print(f"Timing file not found: {e}")
        exit(1)
    
def perform_testing(args):
    names = ["Parsing Time", "Phase 1 Time", "Phase 2 Time", "Phase 3 Time", "Overall Time", "Memory Usage"]
    results = [run_static_eraser(args) for _ in range(10)]
    for i in range(6):
        average_result = sum(result[i] for result in results) / len(results)
        print(f"{names[i]} Average: {average_result}")
        standard_deviation = (sum((result[i] - average_result) ** 2 for result in results) / len(results)) ** 0.5
        print(f"{names[i]} Standard Deviation: {standard_deviation}")

if __name__ == "__main__":
    perform_testing(sys.argv[1:])