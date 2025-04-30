# Image Encryption Tool

**Lightweight Python utility for pixel-level image encryption and decryption.**

---

## Features

- **XOR Cipher**: Byte‑wise reversible XOR on RGB channels.
- **Pixel Shuffle**: Deterministic permutation using a seed‑based PRNG.
- **Lossless Decryption**: Inverse shuffle + XOR restores original.
- **Customizable**: `--key` and `--seed` via CLI.
- **Dependencies**: Pillow & NumPy.

## Installation

```bash
git clone https://github.com/your-username/image-encryption-tool.git
cd image-encryption-tool
pip install pillow numpy
```

## Usage

**Encrypt:**
```bash
python image_encryption_tool.py encrypt \
  path/to/input.jpg \
  path/to/encrypted.png \
  --key 42 \
  --seed 2025
```

**Decrypt:**
```bash
python image_encryption_tool.py decrypt \
  path/to/encrypted.png \
  path/to/output.jpg \
  --key 42 \
  --seed 2025
```

## How It Works

1. **Load Image**: Converts the file into a NumPy array `(H, W, C)`.
2. **XOR Cipher**: Applies `value = value XOR key`; reversible by reapplying.
3. **Pixel Shuffle**: Flattens and permutes pixels via a seed‑based PRNG.
4. **Save**: Writes the scrambled array as an encrypted image.
5. **Decrypt**: Unshuffle using the same seed, then XOR again.

## Customization & Extensions

- **Block Shuffling**: Shuffle regions or blocks for stronger security.
- **Multiple Rounds**: Chain XOR + shuffle with different keys/seeds.
- **GUI Frontend**: Integrate with PySimpleGUI, Tkinter, or web.
- **Additional Formats**: Support grayscale, RGBA, or raw streams.

---

© 2025 Jebin

