def numbers(a,b): 
        len_max=max(len(a), len(b)) 
        carry_no=0
        result_of_no=' '
        a=a.zfill(len_max) 
        b=b.zfill(len_max) 
        for j in range(len_max -1, -1, -1): 
            z=carry_no 
            z=z+(1 if a[j]=='1' else 0)
            z=z+(1 if b[j]=='1' else 0)
            result_of_no=(('1' if z % 2 == 1 else '0')+result_of_no)
            carry_no=(0 if z < 2 else 1)
        if(carry_no !=0):
            result_of_no = '1'+result_of_no
  
        return result_of_no.zfill(len_max) 
a = '11'
b = '1'
print(numbers(a,b)) 
