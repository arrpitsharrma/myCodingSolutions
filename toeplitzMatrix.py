def isToeplitz(arr):
  for j in range(len(arr[0])):
    if helper(0, j, arr, arr[0][j]): continue
    else: return False
    
  for i in range(len(arr)):
    if helper(i, 0, arr, arr[i][0]): continue
    else: return False
    
  return True 
    
def helper(i, j, arr, val):
  if i > len(arr)-1: return True
  if j > len(arr[0])-1: return True
  if val != arr[i][j]: return False
  
  return helper(i+1, j+1, arr, val)
￼
