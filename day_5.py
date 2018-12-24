import string

with open('input_5.txt') as input_file:
  mutate = True
  polymer = input_file.read()
  polymer = polymer.strip()
  polymer = list(polymer)
  best_tally = float('Inf')
  letters = list(string.ascii_lowercase)
  for letter in letters:
    without_letter = [l for l in polymer if l.lower() != letter]

    while mutate:
      mutate = False
      for i in range(len(without_letter) - 1):
        if not without_letter[i]:
          continue
        if without_letter[i] != without_letter[i + 1] and without_letter[i].upper() == without_letter[i + 1].upper():
          without_letter[i], without_letter[i + 1] = None, None
          mutate = True
      without_letter = [l for l in without_letter if l]
    run_tally = len(without_letter)
    mutate = True
    if run_tally < best_tally:
      best_tally = run_tally
  print(best_tally)
        
