#Linear search
def linear_search(search_list, target_value):
  for idx in range(len(search_list)):
    print(search_list[idx])
    if search_list[idx] == target_value:
      return idx
  raise ValueError("{0} not in list".format(target_value))
  
  
#Finding duplicates
def linear_search(search_list, target_value):
  matches = []
  for idx in range(len(search_list)):
    if search_list[idx] == target_value:
      matches.append(idx)
  if matches:
    return matches
  else:
    raise ValueError("{0} not in list".format(target_value))
    

#Finding maximum value
def linear_search(search_list):
  maximum_score_index = None
  for idx in range(len(search_list)):
    if not maximum_score_index or search_list[idx] > search_list[maximum_score_index]:
      maximum_score_index = idx
  return maximum_score_index
