#My Solution
def combine_lists(list1, list2):
  # Generate a new list containing the elements of list2
  # Followed by the elements of list1 in reverse order
  sorted_list = []
  i = len(list1)-1

  for student in list2:
    sorted_list.append(student)

  while i>=0:
    sorted_list.append(list1[i])
    i-=1
  return sorted_list

#Option 1
# def combine_lists(list1, list2):
#   # Generate a new list containing the elements of list2
#   # Followed by the elements of list1 in reverse order
#   return list2 + list1[::-1]

#Option 2
# def combine_lists(list1, list2):

#   list1.reverse()
#   list2.extend(list1)
#   return list2

Jamies_list = ["Alice", "Cindy", "Bobby", "Jan", "Peter"]
Drews_list = ["Mike", "Carol", "Greg", "Marcia"]

print(combine_lists(Jamies_list, Drews_list))
