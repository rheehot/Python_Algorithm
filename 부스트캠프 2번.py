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
        count_1 = 4 if arr1.count(i) > 4 else arr1.count(i)
        count_arr1.append([i,count_1])
    for i in set_arr2:
      if arr2.count(i)<=1:
        pass
      else:
        count_2 = 4 if arr2.count(i) > 4 else arr2.count(i)
        count_arr2.append([i,count_2])
    if len(count_arr1) == 0 and len(count_arr2) == 0:
      return 0
    else:
      max_value1 = count_arr1[0][0]
      max_count1 = count_arr1[0][1]
      max_value2 = count_arr2[0][0]
      max_count2 = count_arr2[0][1]
      for i in range(1,len(count_arr1)):
        if count_arr1[i-1][1] < count_arr1[i][1]:
          max_value1 = count_arr1[i][0]
          max_count1 = count_arr1[i][1]
        elif count_arr1[i-1][1] == count_arr1[i][1]:
          max_value1 = count_arr1[i][0]
          max_count1 = count_arr1[i][1]
        else:
          max_value1 = count_arr1[i-1][0]
          max_count1 = count_arr1[i-1][1]
      for i in range(1,len(count_arr2)):
        if count_arr2[i-1][1] < count_arr2[i][1]:
          max_value2 = count_arr2[i][0]
          max_count2 = count_arr2[i][1]
        elif count_arr2[i-1][1] == count_arr2[i][1]:
          max_value2 = count_arr2[i][0]
          max_count2 = count_arr2[i][1]
        else:
          max_value2=count_arr2[i-1][0]
          max_count2 = count_arr2[i-1][1]

      if max_count1 == max_count2:
        if max_value1 > max_value2:
          return 1
        elif max_value1 < max_value2:
          return 2
        else:
          return 0
      elif max_count1 > max_count2:
        return 1
      else:
        return 2

def arr_check(arr):
  for i in arr:
    if i < 1 or i > 13:
      return False
  return True

# 갯수에 대한 비교도 필요
print(solution([1,5,7,2,9,13,10],[2,3,9,10,4,8,11]))
print(solution([1,4,1,3,5,6,10],[9,2,3,1,3,4,10]))
print(solution([1,1,9,4,1,3,11],[2,3,3,13,12,9,9]))
print(solution([1,4,9,4,1,10,13],[11,13,9,3,1,9,1]))
print(solution([1,4,4,4,1,10,4],[11,13,11,3,11,9,1]))
print(solution([1,2,2,3,2,2,2],[4,5,4,5,4,5,4]))