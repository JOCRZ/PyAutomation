import os
import re
import subprocess
import requests
from pathlib import Path

def get_chrome_version():
    """Return the installed Google Chrome major version (e.g., 131)."""
    try:
        output = subprocess.check_output(["google-chrome", "--version"]).decode("utf-8")
        match = re.search(r"(\d+)\.", output)
        if match:
            return match.group(1)
        else:
            raise ValueError("Could not parse Chrome version.")
    except FileNotFoundError:
        raise SystemExit("❌ Google Chrome not found. Please install it first or ensure it's in PATH.")

def get_latest_driver_version(major_version):
    """Fetch the latest ChromeDriver version for the given major Chrome version."""
    url = f"https://googlechromelabs.github.io/chrome-for-testing/LATEST_RELEASE_{major_version}"
    response = requests.get(url)
    if response.status_code != 200:
        raise SystemExit(f"❌ Failed to fetch driver version for Chrome {major_version}.")
    return response.text.strip()

def download_chromedriver(version, download_dir):
    """Download the ChromeDriver ZIP into the Downloads folder."""
    url = f"https://storage.googleapis.com/chrome-for-testing-public/{version}/linux64/chromedriver-linux64.zip"
    output_path = Path(download_dir) / f"chromedriver-linux64-{version}.zip"

    print(f"⬇️  Downloading ChromeDriver {version}...")
    response = requests.get(url, stream=True)
    if response.status_code != 200:
        raise SystemExit(f"❌ Failed to download ChromeDriver from {url}")

    with open(output_path, "wb") as f:
        for chunk in response.iter_content(chunk_size=8192):
            if chunk:
                f.write(chunk)

    print(f"✅ Download complete: {output_path}")

def main():
    print("🚀 ChromeDriver Downloader for Linux (no install)\n")

    download_dir = Path.home() / "Downloads"
    download_dir.mkdir(exist_ok=True)

    chrome_major_version = get_chrome_version()
    print(f"🔍 Detected Chrome major version: {chrome_major_version}")

    driver_version = get_latest_driver_version(chrome_major_version)
    print(f"📦 Matching ChromeDriver version: {driver_version}")

    download_chromedriver(driver_version, download_dir)
    print("\n🎉 Done! File saved in your Downloads folder.")

if __name__ == "__main__":
    main()
