4 Results

The proposed fake certificate detection system was implemented using a MobileNetV2 deep learning model. The model was trained on a dataset containing both genuine and forged certificate images.

4.1 Model Training

The dataset was divided into training and validation sets. During training, MobileNetV2 extracted visual features from certificate images such as layout structure, fonts, logos, and seals.

The model was trained using the following configuration:

Model Architecture: MobileNetV2

Input Image Size: 224 × 224 pixels

Loss Function: Binary Cross-Entropy

Optimizer: Adam

Training Epochs: 10

4.2 Performance Evaluation

The trained model was evaluated using standard classification metrics:

Accuracy

Precision

Recall

F1-score

These metrics help measure the ability of the model to correctly classify certificates as genuine or fake.

4.3 Prediction Results

After training, the model was tested with new certificate images. The system successfully predicted whether the certificate was real or fake based on the learned visual features.

Example output:

Prediction: REAL Certificate

or

Prediction: FAKE Certificate
4.4 Observations

The MobileNetV2 model efficiently extracted visual features from certificate images.

The model showed good performance in distinguishing genuine certificates from manipulated ones.

The system can process both scanned certificates and mobile-captured images.

4.5 Conclusion of Results

The experimental results demonstrate that deep learning models such as MobileNetV2 can effectively detect forged certificates. The proposed system provides an automated solution for certificate verification and reduces the need for manual document inspection.
