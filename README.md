# Chest X-Ray Classification with Transfer Learning



## Overview

Welcome to the Chest X-Ray Classification with Transfer Learning project! This repository contains code for classifying chest X-rays using transfer learning. Transfer learning is employed to leverage pre-trained models, enhancing the performance of the model on a specific task, particularly when there is limited labeled data available.

## Dataset

The dataset utilized for this project is the Chest X-Ray Images (Pneumonia) sourced from Kaggle. It comprises over 500 chest X-ray images, annotated with five different classes.

## Model Architecture

The model architecture is based on a pre-trained convolutional neural network (CNN) commonly employed in medical image classification tasks. The top layers of the pre-trained model were removed, and new fully connected layers were added to tailor the model to the specific chest X-ray classification task.

## Project Structure

```
|-- data/
|   |-- chest_xray/
|       |-- train/
|       |-- test/
|       |-- val/
|-- notebooks/
|   |-- Chest_XRay_Classification.ipynb
|-- src/
|   |-- data_preprocessing.py
|   |-- model.py
|-- .gitignore
|-- README.md
|-- requirements.txt
```

## Getting Started

1. Clone the repository:

   ```bash
   git clone https://github.com/amed-et/Chest-X-Ray-Classification.git
   ```



2. Explore the provided Jupyter notebook:

   ```bash
   jupyter notebook notebooks/Chest_XRay_Classification.ipynb
   ```

## Usage

Adjust the notebook and scripts to suit your specific use case. Experiment with hyperparameters, try different pre-trained models, and fine-tune the network based on your dataset.

## Acknowledgments

- Kaggle for providing the Chest X-Ray Images (Pneumonia) dataset.
- 

## License

This project is licensed under the [MIT License](LICENSE).
 
---

**Author:** Amdebirhan Abebe
