# 🌊 Landsat-7 Marine Research Pipeline

This repository demonstrates a simplified DevOps pipeline to preprocess Landsat-7 images for marine research.

## Features

- ✅ Automatic AOI clipping
- ✅ Simple cloud masking
- ✅ Dockerized and reproducible
- ✅ Automated CI/CD on GitHub Actions
- ✅ Easy visualization via Jupyter Notebook

## Usage

### 1️⃣ Add your Landsat-7 image

Place your Landsat-7 file into:

```
data/raw/landsat7_example.tif
```

### 2️⃣ Run locally

```
docker build -t landsat7-pipeline .
docker run landsat7-pipeline
```

### 3️⃣ Run on GitHub

Push to `main` branch — GitHub Actions will build and run automatically.

### 4️⃣ Visualize

```
cd notebooks
jupyter notebook
```

## AOI Example

Longitude: 120.0–121.0  
Latitude: –10.0 to –9.0

## Credits

Built with ❤️ using GDAL, Rasterio, and Docker.
