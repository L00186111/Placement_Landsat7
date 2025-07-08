import rasterio
from rasterio.windows import from_bounds
import numpy as np
import os

def clip_aoi(src_path, dst_path, bbox):
    with rasterio.open(src_path) as src:
        window = from_bounds(*bbox, transform=src.transform)
        profile = src.profile
        profile.update({
            'height': window.height,
            'width': window.width,
            'transform': rasterio.windows.transform(window, src.transform)
        })
        data = src.read(window=window)
        os.makedirs(os.path.dirname(dst_path), exist_ok=True)
        with rasterio.open(dst_path, 'w', **profile) as dst:
            dst.write(data)
    print(f"Clipped image saved to {dst_path}")

def simple_cloud_mask(band_array, threshold=0.2):
    return band_array < threshold

if __name__ == "__main__":
    input_file = "data/raw/landsat7_example.tif"
    output_file = "data/processed/landsat7_clipped.tif"
    bbox = (120.0, -10.0, 121.0, -9.0)

    if not os.path.exists(input_file):
        print(f"Input file not found: {input_file}. Please add your Landsat-7 TIFF first.")
        exit(1)

    clip_aoi(input_file, output_file, bbox)

    with rasterio.open(output_file) as src:
        band = src.read(1)
        mask = simple_cloud_mask(band, threshold=0.15)
        masked_band = np.where(mask, band, np.nan)
        np.save("data/processed/cloud_masked_band.npy", masked_band)

    print("Cloud masking completed and saved.")
