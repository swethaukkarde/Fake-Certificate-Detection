1.Literature Review

Forgery detection in digital documents has become an important research area due to the increasing use of certificates in education, employment, and professional verification. With the availability of advanced image editing tools, it has become easier to manipulate certificates by altering text, images, seals, or signatures. Researchers have proposed various machine learning and deep learning techniques to detect such document forgeries.

Early approaches relied on traditional image processing techniques combined with machine learning algorithms such as Support Vector Machines (SVM) to detect irregular patterns in document images. For example, studies like Gupta et al. (2019) used preprocessing techniques and compared SVM with Convolutional Neural Networks (CNNs) for certificate verification. Their findings showed that CNN-based methods performed better in identifying subtle visual patterns such as layout inconsistencies and texture anomalies.

With the advancement of deep learning, Convolutional Neural Networks (CNNs) have become widely used for document forgery detection. Research by Afzal et al. (2021) demonstrated that CNN-based models can effectively analyze visual features such as fonts, textures, logos, and document layouts. These models achieved strong performance in identifying manipulated regions within scanned documents.

Another direction explored by researchers is the combination of visual analysis and textual analysis. For instance, Vaidya et al. (2020) proposed a system that integrates CNN-based image analysis with Optical Character Recognition (OCR) to detect tampered text within certificates. This multimodal approach improves detection accuracy because it examines both the visual structure of the document and the textual content extracted from it.

More recent studies have explored transformer-based architectures and multimodal learning frameworks. Hussain et al. (2022) introduced a transformer-based model capable of analyzing both image features and textual content simultaneously. These models demonstrate better generalization across different document formats and provide improved robustness against noise and distortions in scanned images.

Although these approaches have shown promising results, several challenges still remain. Many models require large labeled datasets of genuine and forged certificates, which are difficult to obtain in real-world scenarios. Additionally, high-performing deep learning models often require significant computational resources, making them less suitable for lightweight or real-time applications.

In this project, we address these limitations by implementing a MobileNetV2-based deep learning model, which is lightweight and computationally efficient while still providing strong performance for image classification tasks. By focusing on both visual characteristics and certificate structure, the proposed system aims to effectively distinguish between genuine and fake certificates.

1.1 Observations from the Literature Review

Deep learning models such as CNNs and Transformers show strong performance in document image analysis and forgery detection.

Combining visual features (layout, fonts, seals) with textual features (OCR-extracted content) improves detection accuracy compared to single-modality approaches.

Data augmentation and synthetic forgery generation techniques are often used to overcome the lack of large forged document datasets.

Performance of forgery detection models is typically evaluated using metrics such as Accuracy, Precision, Recall, and F1-score.

Multimodal deep learning approaches provide better generalization across different certificate formats and institutions.

1.2 Limitations from the Literature Review

Many existing approaches require large labeled datasets, but real-world forged certificate datasets are difficult to obtain.

Models trained on a specific dataset often fail to generalize to certificates from different institutions or formats.

High-performance deep learning models such as Transformers and GANs require powerful GPU resources, making deployment difficult in real-time environments.

Several existing systems focus only on visual forgery detection or text-based forgery detection, but not both together in a unified framework.

Many research works lack explainability, making it difficult for human verifiers to understand why a certificate is classified as fake.
