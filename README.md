# Image Encryption Tool

Lightweight Python script to encrypt/decrypt images by combining an XOR cipher and pixel permutation.

## Installation

```bash
git clone https://github.com/your-username/image-encryption-tool.git
cd image-encryption-tool
pip install pillow numpy
```

## Usage

Encrypt:
```bash
python image_encryption_tool.py encrypt input.jpg encrypted.png --key 42 --seed 2025
```

Decrypt:
```bash
python image_encryption_tool.py decrypt encrypted.png output.jpg --key 42 --seed 2025
```

## Features

- **XOR Cipher**: Byte-wise reversible XOR on RGB channels
- **Pixel Shuffle**: Seed-based, deterministic pixel reordering
- **Lossless**: Original image recovered by reversing steps

---

© 2025 Jebin

