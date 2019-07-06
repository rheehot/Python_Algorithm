def solution(arr1,arr2):
    if len(arr1)!=7 or len(arr2)!=7:
      return "길이를 확인하세요."  
    if arr_check(arr1)!= True or arr_check(arr2) != True:
      return "원소의 값을 확인하세요."
    arr1.sort()
    arr2.sort()
    count_arr1 = list()
    set_arr1 = set(arr1)
    count_arr2 = list()
    set_arr2 = set(arr2)
    for i in set_arr1:
      if arr1.count(i)==1:
        pass
      else:
        count_arr1.append([i,arr1.count(i)])
    for i in set_arr2:
      if arr2.count(i)<=1:
        pass
      else:
        count_arr2.append([i,arr2.count(i)])
    if len(count_arr1) == 0 and len(count_arr2) == 0:
      return 0
    elif len(count_arr1) > len(count_arr2):
      return 1
    elif len(count_arr1) < len(count_arr2):
      return 2
    else:
      if count_arr1[-1][0] == count_arr2[-1][0]:
        return 0
      elif count_arr1[-1][0] > count_arr2[-1][0]:
        return 1
      else:
        return 2    


def arr_check(arr):
  for i in arr:
    if i < 1 or i > 13:
      return False
  return True


print(solution([1,5,7,2,9,13,10],[2,3,9,10,4,8,11]))
print(solution([1,4,1,3,5,6,10],[9,2,3,1,3,4,10]))