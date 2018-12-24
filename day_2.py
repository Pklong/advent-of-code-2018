test = [
  'abcdef',
  'bababc',
  'abbcde',
  'abcccd',
  'aabcdd',
  'abcdee ',
  'ababab '
]

with open('input_2.py') as input_file:
  two_count = 0
  three_count = 0
  box_ids = []
  for line in input_file:
    alphabet = [0 for i in range(26)]
    for letter in line.strip():
      alphabet[ord(letter) - 97] += 1
    two_counted = False
    three_counted = False
    for idx, count in enumerate(alphabet):
      if count == 2 and not two_counted:
        two_count += 1
        two_counted = True
      elif count == 3 and not three_counted:
        three_count += 1
        three_counted = True
    if two_counted or three_counted:
      box_ids.append(line.strip())
  print(two_count * three_count)
  for i in range(len(box_ids)):

    for j in range(i + 1, len(box_ids)):
      hamming_diff = 0
      og = box_ids[i]
      comp = box_ids[j]
      result = ''
      for k in range(len(og)):
        if og[k] != comp[k]:
          hamming_diff += 1
        else:
          result += og[k]
      if hamming_diff == 1:
        print(result)
        break
        

