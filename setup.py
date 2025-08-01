from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="Digital-twin",  # Replace with your own username
    author="Jelle Degen",
    author_email="jelledegen@gmail.com",
    description="Satellite object recognition models",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Jelle-Degen/Digital-twin",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=[
        "earthpy==0.9.4",
        "scikit-learn==1.4.0",
        "GDAL==3.4.1",
        "fiona==1.9.5",
        "rasterio==1.3.9",
        "shapely==2.0.1",
        "geopandas==1.0.1",
        "pyarrow==15.0.0",
        "fastparquet==2024.2.0",
        "imblearn==0.0",
        "mlflow==2.10.2" ,
        "satellite_images_nso==1.2.5",
    ],
)
