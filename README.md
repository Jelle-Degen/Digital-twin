# Introduction

please refer to the repository for the basis of the code

[Here](https://github.com/Provincie-Zuid-Holland/satellite_images_nso_tif_model_iterator).

# Installation

When starting up and working with 64x Windows and Anaconda for your python environment management execute the following terminal commands in order one by one:

```sh
conda create -n satellite-images-nso-datascience python=3.12 -y
conda activate satellite-images-nso-datascience
pip install -r requirements.txt
pip install -e .
```
Then in VS code go to your file, download the ipykernel package when prompted, and run the first line 

```sh
pip install .
```

# How to train a new model

1. Retrieve images using the [satellite_images_nso_extractor](https://github.com/Provincie-Zuid-Holland/satellite_images_nso_extractor) repository.
2. Use QGis to set up annotations for each of the images. Make polygons for each area of a specific label and add the following columns, before exporting as a geojson:
   - 'name': this is the name of the tif file (extension excluded)
   - 'Label': this is the label of the selected polygon.
3. Next run the 'data/annotations/transform_polygon_annotations_to_pixels.ipynb' with the appropriate variables.
4. Finally run 'annotations_models/train_random_forest_classifier_model.ipynb' notebook with the appropriate variables. This notebook trains a scaler & model, resulting in:
   - A pickle file containing the cross-validation models, scalers & metrics
   - A pickle file containing the model & scaler trained on all annotated data
5. See the model results by running 'mlflow ui' in the annotations_models folder

