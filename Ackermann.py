# josé Fredes 


def A(m,n):
    if m==0:
      return n + 1
    elif m > 0 and n == 0:
      print ("A(",m-1,",",1,")")
      return A(m-1,1)
    else:
      if m>0 and n > 0:
        print("A(",m-1,",","A(",m,",",n-1,")",")")
        return A(m-1,A(m,n-1))

print(A(3,2))