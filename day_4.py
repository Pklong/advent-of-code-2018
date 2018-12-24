with open('input_4.txt') as input_file:
  file_contents = input_file.read()
  content_list = file_contents.split('\n')
  content_list.sort()
  
  guard_schedule = {}
  current_guard = None
  current_sleep = None
  for line in content_list:
    if line == '':
      continue
    time, activity = line.split(']')
    day, hour = time[1:].split(' ')
    hour = hour.split(':')[1]
    if "#" in activity:
      guard_id = activity.split(' ')[2]
      current_guard = guard_id
      if not guard_schedule.get(current_guard, False):
        guard_schedule[current_guard] = [0 for i in range(60)]
    elif 'wakes' in activity:
      print(current_guard, "slept for ", int(hour) - int(current_sleep))
      print(sum(guard_schedule[current_guard]))
      for i in range(int(current_sleep), int(hour)):
        guard_schedule[current_guard][i] += 1
      print(sum(guard_schedule[current_guard]))        
    else:
      current_sleep = hour      

  lazy_guard = None
  max_sleep = None
  for guard, sleep_schedule in guard_schedule.items():
    time_asleep = sum(sleep_schedule)
    if not max_sleep or time_asleep > max_sleep:
      lazy_guard = guard
      max_sleep = time_asleep
  lazy_sleep = guard_schedule[lazy_guard]
  most_minutes = max(lazy_sleep)
  minute = lazy_sleep.index(most_minutes)
  # star one
  print(int(lazy_guard[1:]) * minute)

  # start two
  lazy_guard = None
  max_sleep = None
  for guard, sleep_schedule in guard_schedule.items():
    time_asleep = max(sleep_schedule)
    if not max_sleep or time_asleep > max_sleep:
      lazy_guard = guard
      max_sleep = time_asleep
  lazy_sleep = guard_schedule[lazy_guard]
  most_minutes = max(lazy_sleep)
  minute = lazy_sleep.index(most_minutes)
  print(int(lazy_guard[1:]) * minute)


