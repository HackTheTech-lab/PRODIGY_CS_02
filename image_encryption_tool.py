from PIL import Image
import numpy as np
import argparse


def xor_cipher(data: np.ndarray, key: int) -> np.ndarray:
    """
    Apply XOR cipher to the image data with a single-byte key.
    """
    return data ^ key


def swap_pixels(data: np.ndarray, seed: int) -> np.ndarray:
    """
    Swap pixels in a deterministic way using a seed.
    """
    rng = np.random.default_rng(seed)
    flat = data.reshape(-1, data.shape[-1])
    indices = np.arange(flat.shape[0])
    rng.shuffle(indices)
    shuffled = flat[indices]
    return shuffled.reshape(data.shape)


def encrypt_image(input_path: str, output_path: str, key: int, seed: int):
    img = Image.open(input_path)
    data = np.array(img)

    # Step 1: XOR cipher
    xored = xor_cipher(data, key)
    # Step 2: Pixel swapping
    encrypted = swap_pixels(xored, seed)

    enc_img = Image.fromarray(encrypted.astype('uint8'))
    enc_img.save(output_path)
    print(f"Encrypted image saved to {output_path}")


def decrypt_image(input_path: str, output_path: str, key: int, seed: int):
    img = Image.open(input_path)
    data = np.array(img)

    # Reverse pixel swapping
    rng = np.random.default_rng(seed)
    flat = data.reshape(-1, data.shape[-1])
    indices = np.arange(flat.shape[0])
    rng.shuffle(indices)
    # To invert, we need the inverse permutation
    inverse_idx = np.argsort(indices)
    unshuffled = flat[inverse_idx]
    unshuffled = unshuffled.reshape(data.shape)

    # Reverse XOR
    decrypted = xor_cipher(unshuffled, key)

    dec_img = Image.fromarray(decrypted.astype('uint8'))
    dec_img.save(output_path)
    print(f"Decrypted image saved to {output_path}")


def main():
    parser = argparse.ArgumentParser(description="Simple Image Encryption/Decryption Tool")
    parser.add_argument('mode', choices=['encrypt', 'decrypt'], help="Mode: encrypt or decrypt")
    parser.add_argument('input', help="Path to input image file")
    parser.add_argument('output', help="Path to output image file")
    parser.add_argument('--key', type=int, default=123, help="Single-byte key for XOR (0-255)")
    parser.add_argument('--seed', type=int, default=42, help="Seed for pixel swapping")

    args = parser.parse_args()

    if args.mode == 'encrypt':
        encrypt_image(args.input, args.output, args.key, args.seed)
    else:
        decrypt_image(args.input, args.output, args.key, args.seed)


if __name__ == '__main__':
    main()
