3 Dataset Description

The dataset used in this project consists of certificate images categorized into two classes: genuine certificates and forged certificates. These certificates are used to train and evaluate the deep learning model for fake certificate detection.

3.1 Dataset Categories

The dataset is organized into two folders:

dataset/
   real/
   fake/

Real Certificates: Authentic certificates collected from publicly available samples or generated templates.

Fake Certificates: Manipulated versions of certificates created by editing the original documents.

3.2 Data Format

Certificates may be provided in different formats such as:

PDF documents

JPEG images

PNG images

PDF files are converted into images using the pdf2image library so that they can be processed by the deep learning model.

3.3 Data Preprocessing

Before training the model, the dataset undergoes several preprocessing steps:

PDF certificates are converted to images.

Images are resized to 224 × 224 pixels to match the MobileNetV2 input size.

Pixel values are normalized to improve model performance.

The dataset is divided into training and validation sets.

3.4 Purpose of the Dataset

The dataset helps the model learn the difference between genuine and fake certificates by identifying visual patterns such as:

Layout inconsistencies

Font irregularities

Altered logos or seals

Modified text or signatures

This dataset enables the deep learning model to effectively classify certificates as real or fake.
