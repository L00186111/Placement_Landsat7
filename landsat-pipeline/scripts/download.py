import os
import requests

def download_landsat_data():
    # Placeholder example: downloading a test file
    url = "https://example.com/sample_landsat7_file.tif"
    output_path = os.path.join("data", "raw", "sample_landsat7_file.tif")

    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    print(f"Downloading Landsat-7 data from {url} ...")
    try:
        response = requests.get(url)
        response.raise_for_status()
        with open(output_path, "wb") as f:
            f.write(response.content)
        print(f"Download complete: {output_path}")
    except Exception as e:
        print(f"Error downloading data: {e}")

if __name__ == "__main__":
    download_landsat_data()
