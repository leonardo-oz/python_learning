
data=[1,3,7,8,12,16,22,34,69]


def find_pivot(start_s,end_s):
  if (end_s-start_s+1)%2==1:
    p_i=start_s+round((end_s-start_s)/2)
  else:
    p_i=start_s+round((end_s-start_s)/2)
  # end if 
  return p_i
# end method find pivot



def binary_search(data,qry_nbr):
  start_idx=0
  end_idx=len(data)-1
  s=end_idx-start_idx
  if s==0: # check if there is only one charecter in the data
    if data[0]==qry_nbr: 
      return True,0 # check if it equals qry_nbr
    else:
      return False,-1 
    # end if
  # end if
  pivot= find_pivot(start_idx,end_idx)# find the first medium also know as pivot
  if qry_nbr==data[pivot]:# check if it equals the qry_nbr
    return True,pivot
  # end if
  while qry_nbr!=data[pivot] and s>1:
    if qry_nbr>data[pivot]:
      start_idx=pivot+1 # then set serch boundary in upper range
    else:
      end_idx=pivot # set bundary in lower range
    # end if
    pivot= find_pivot(start_idx,end_idx) # get the new pivot after new boundarys
    s=end_idx-start_idx+1 # update S so there is no infinite loop
    # end if
  # end while
  if qry_nbr==data[pivot]: 
    return True,pivot
  # end if
  if s==1:
    if data[start_idx]==qry_nbr:
      return True,0
    else:
      return False,-1
    # end if
  # end if
# end method binary_search

def main():
  data=[1,3,7,8,12,16,22,34,69]
  qry_nbr=34
  result,result_idx=binary_search(data,qry_nbr)
  print(result,result_idx)
# end method main








main()


