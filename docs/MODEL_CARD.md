# Model Card

## Overview

This project studies generative modeling for selected EMNIST letter classes. The original notebook includes VAE/CVAE experimentation and multiple GAN variants:

- Vanilla GAN
- DCGAN
- WGAN
- WGAN-GP
- LSGAN
- DRAGAN
- InfoGAN
- SAGAN
- cDRAGAN

## Intended Use

The project is intended for deep-learning coursework, experimentation, and learning how generative models behave on small grayscale character images.

## Out Of Scope

This project is not intended for:

- Identity verification.
- High-stakes document recognition.
- Production OCR pipelines.
- Synthetic data generation without downstream quality checks.

## Evaluation

The notebook uses a combination of:

- Visual sample grids.
- Generator and discriminator loss curves.
- FID.
- KID.
- t-SNE spread and projection plots.
- Mode-collapse checks.
- Perceptual path length.

## Limitations And Risks

- FID/KID on small grayscale letter images should be interpreted carefully because feature extractors are usually trained on natural RGB images.
- GAN training is sensitive to random seeds, optimizer settings, and data balancing.
- A single run does not establish model robustness.
- Generated samples may amplify class imbalance or ambiguity if preprocessing is inconsistent.

## Reproducibility

Use the `.env.example` defaults, fixed random seeds, versioned dependencies, and saved experiment logs when running new experiments.
