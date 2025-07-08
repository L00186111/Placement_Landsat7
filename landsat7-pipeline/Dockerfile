FROM osgeo/gdal:alpine-small-latest

RUN apk add --no-cache python3 py3-pip
RUN pip3 install rasterio numpy

WORKDIR /app
COPY . /app

CMD ["python3", "scripts/main_preprocess.py"]
