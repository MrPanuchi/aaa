def sortp (a,b):
  a.sort();
  b.sort();
  if (a == b):
    print ('анаграмма');
  else:
    print ('не анаграмма');

def slop (a,b):
  la = {};
  lb = {};
  for i in range (0,len(a)):
    if (a[i] in la):
      la.update({a[i]:la.get(a[i])+1});
    else:
      la.update({a[i]:0});
  for i in range (0,len(b)):
    if (b[i] in lb):
      lb.update({b[i]:lb.get(b[i])+1});
    else:
      lb.update({b[i]:0});
  if (la == lb):
    print ('анаграмма');
  else:
    print ('не анаграмма');

aa = list(input('Введите слово: '));
bb = list(input('Введите второе слово: '));
sortp (aa,bb);
slop (aa,bb);
