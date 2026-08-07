import subprocess
import sys


def print_step(message: str):
    print("\n" + "=" * 50)
    print(message)
    print("=" * 50)


def main():
    try:
        print_step("Step 1/2: Scraping quotes...")

        subprocess.run(
            ["scrapy", "crawl", "quotes"],
            check=True,
        )

        print_step("Step 2/2: Loading data into MongoDB...")

        subprocess.run(
            [sys.executable, "seed.py"],
            check=True,
        )

        print_step("Project completed successfully!")

    except subprocess.CalledProcessError as error:
        print(f"\n❌ Project execution failed. Exit code: {error.returncode}")


if __name__ == "__main__":
    main()
