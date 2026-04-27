import sys

def caesar_cipher(message, shift):
  encoded = []
  for char in message:
    if char.isalpha():
      upper = char.upper()
      shifted = chr((ord(upper) - ord('A') + shift) % 26 + ord('A'))
      encoded.append(shifted)
  return encoded

def main():
  if len(sys.argv) < 2:
    print("Usage: python caesar.py <shift>")
    sys.exit(1)

  shift = int(sys.argv[1])
  encoded_chars = []

  for line in sys.stdin:
    encoded_chars.extend(caesar_cipher(line, shift))

  block_size = 5
  blocks_per_line = 10
  
  blocks = []
  for i in range