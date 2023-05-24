"""
File : rewrite_replace.py
Date : 03/08/2023
"""

def conv_to_list(string):
   list1 = []
   for i in range(len(string)):
      list1.append(string[i])
   return list1

def to_string(list1):
   str1 = ""
   str1 = str1.join(list1)
   return str1

def rewrite_replace(the_string, look_for, replace_with):
   base = conv_to_list(the_string)
   target = conv_to_list(look_for)
   replacement = conv_to_list(replace_with)
   size_target = len(target)
   size_replacement = len(replacement)
   k = 0
   i = 0
   while i < len(base):
      j = 0
      if base[i] == target[j]:
         k = i
         while j < size_target and k < len(base) and base[k] == target[j] :
            if j == size_target - 1:
               rem_index = i
               for l in range(size_replacement):
                  base.insert(rem_index, replacement[l])
                  rem_index += 1
               for m in range(rem_index,size_target+rem_index):
                  base.pop(rem_index)
            j += 1
            k += 1
      i += 1
   return to_string(base)


if __name__ == '__main__':
   total = input("What is the total string? ")
   to_be_replaced = input("What to look for? ")
   replacement = input("What should we replace that string with? ")
   str1 = rewrite_replace(total,to_be_replaced,replacement)
   print(str1)
