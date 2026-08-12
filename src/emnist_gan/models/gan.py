"""TensorFlow/Keras model builders for the baseline dense GAN."""

from __future__ import annotations

from collections.abc import Sequence

import numpy as np


def _require_tensorflow():
    try:
        import tensorflow as tf
    except ImportError as exc:
        raise ImportError(
            "TensorFlow is required for model construction. "
            "Install the ML extras with: pip install -e '.[ml]'"
        ) from exc
    return tf


def build_dense_generator(
    latent_dim: int = 100,
    units: int = 256,
    output_shape: Sequence[int] = (28, 28, 1),
):
    """Build the original notebook's fully connected GAN generator."""
    if latent_dim <= 0:
        raise ValueError("latent_dim must be positive")
    if units <= 0:
        raise ValueError("units must be positive")

    tf = _require_tensorflow()
    model = tf.keras.Sequential(name="dense_generator")
    model.add(tf.keras.layers.Input(shape=(latent_dim,)))
    model.add(tf.keras.layers.Dense(units, activation="relu"))
    model.add(tf.keras.layers.BatchNormalization())
    model.add(tf.keras.layers.Dense(units * 2, activation="relu"))
    model.add(tf.keras.layers.BatchNormalization())
    model.add(tf.keras.layers.Dense(int(np.prod(output_shape)), activation="tanh"))
    model.add(tf.keras.layers.Reshape(tuple(output_shape)))
    return model


def build_dense_discriminator(input_shape: Sequence[int] = (28, 28, 1), units: int = 256):
    """Build the original notebook's fully connected GAN discriminator."""
    if units <= 1:
        raise ValueError("units must be greater than 1")

    tf = _require_tensorflow()
    model = tf.keras.Sequential(name="dense_discriminator")
    model.add(tf.keras.layers.Input(shape=tuple(input_shape)))
    model.add(tf.keras.layers.Flatten())
    model.add(tf.keras.layers.Dense(units))
    model.add(tf.keras.layers.LeakyReLU(negative_slope=0.2))
    model.add(tf.keras.layers.Dense(units // 2))
    model.add(tf.keras.layers.LeakyReLU(negative_slope=0.2))
    model.add(tf.keras.layers.Dense(1, activation="sigmoid"))
    return model


def generator_loss(fake_output):
    """Binary cross-entropy generator objective."""
    tf = _require_tensorflow()
    cross_entropy = tf.keras.losses.BinaryCrossentropy(from_logits=False)
    return cross_entropy(tf.ones_like(fake_output), fake_output)


def discriminator_loss(real_output, fake_output):
    """Binary cross-entropy discriminator objective."""
    tf = _require_tensorflow()
    cross_entropy = tf.keras.losses.BinaryCrossentropy(from_logits=False)
    real_loss = cross_entropy(tf.ones_like(real_output), real_output)
    fake_loss = cross_entropy(tf.zeros_like(fake_output), fake_output)
    return real_loss + fake_loss
