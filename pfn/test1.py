import sys


def main(lines: list[str]):
  x = lines[0]
  n = len(x)
  result = sorted(x)

  # 先頭が0にならないようにする
  if result[0] == '0':
    for i in range(1, n):
      if result[i] != '0':
        result[0], result[i] = result[i], result[0]
        break
  print(int(''.join(result)))


if __name__ == '__main__':
  lines = []
  for l in sys.stdin:
    lines.append(l.rstrip('\r\n'))
  main(lines)
