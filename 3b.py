def b3b1 (a,i):
  while (i < len(a)):
    if (a[i] % 2 == 0):
      i = i+1;
    else:
      a.pop(i);
  print (a);

def b3b2 (a,i):
  if (i == len(a)):
    return (a);
  if (a[i] % 2 == 0):
    i = i+1;
  else:
    a.pop(i);
  return b3b2 (a,i);

aa = [-1,1,2,3,4,5,6,7,8,9,10,11,7,7,7,7,7,7,7,8,8,8,8,8,8,8,8];
ii = 0;
b3b1 (aa,ii);
print(b3b2 (aa,ii));
