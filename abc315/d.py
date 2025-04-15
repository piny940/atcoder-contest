h, w = list(map(int, input().split()))
css = []
for i in range(h):
  cs = list(input())
  css.append(cs)

rest_rows = [i for i in range(h)]
rest_cols = [j for j in range(w)]
to_continue = True
row_maps = []
col_maps = []

for row in range(h):
  row_map = {}
  for c in css[row]:
    if c not in row_map:
      row_map[c] = 1
    else:
      row_map[c] += 1
  row_maps.append(row_map)

for col in range(w):
  col_map = {}
  for row in range(h):
    c = css[row][col]
    if c not in col_map:
      col_map[c] = 1
    else:
      col_map[c] += 1
  col_maps.append(col_map)


def to_remove_from_map(m):
  single = True
  one = False
  count = 0
  for k in m:
    if m[k] <= 0:
      continue
    if one:
      single = False
    else:
      one = True
    count += m[k]
  return count >= 2 and single


while to_continue:
  to_continue = False
  to_remove_rows = []
  to_remove_row_colors = {}
  if len(rest_cols) >= 2:
    for row in rest_rows:
      color = css[row][rest_cols[0]]
      if to_remove_from_map(row_maps[row]):
        to_remove_rows.append(row)
        to_continue = True
        if color not in to_remove_row_colors:
          to_remove_row_colors[color] = 1
        else:
          to_remove_row_colors[color] += 1

  to_remove_cols = []
  to_remove_col_colors = {}
  if len(rest_rows) >= 2:
    for col in rest_cols:
      color = css[rest_rows[0]][col]
      if to_remove_from_map(col_maps[col]):
        to_remove_cols.append(col)
        to_continue = True
        if color not in to_remove_col_colors:
          to_remove_col_colors[color] = 1
        else:
          to_remove_col_colors[color] += 1

  for row in to_remove_rows:
    rest_rows.remove(row)
  for col in to_remove_cols:
    rest_cols.remove(col)
  for row in rest_rows:
    for color in to_remove_col_colors:
      row_maps[row][color] -= to_remove_col_colors[color]
  for col in rest_cols:
    for color in to_remove_row_colors:
      col_maps[col][color] -= to_remove_row_colors[color]

print(len(rest_rows) * len(rest_cols))
