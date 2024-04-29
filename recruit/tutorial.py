import sys

def main(lines):
  text = lines[0]
  print(f"Hello {text}!")

if __name__ == '__main__':
  lines = []
  for l in sys.stdin:
    lines.append(l.rstrip('\r\n'))
  main(lines)

