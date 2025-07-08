import os
from scripts import process

def test_process_landsat_data(tmp_path):
    raw_file = tmp_path / "sample_landsat7_file.tif"
    raw_file.write_text("dummy data")

    # Patch data/raw path temporarily
    original_raw_dir = os.path.join("data", "raw")
    original_processed_dir = os.path.join("data", "processed")

    os.makedirs(original_raw_dir, exist_ok=True)
    with open(os.path.join(original_raw_dir, "sample_landsat7_file.tif"), "w") as f:
        f.write("dummy data")

    process.process_landsat_data()

    processed_file = os.path.join(original_processed_dir, "processed_output.txt")
    assert os.path.exists(processed_file)

    with open(processed_file, "r") as f:
        content = f.read()
    assert "placeholder" in content
