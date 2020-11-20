qsort = lambda L: [] if L==[] else qsort([x for x in L[1:] if x< L[0]]) + L[0:1] + qsort([x for x in L[1:] if x>=L[0]])

isprime = lambda n: [i for i in range(1 ,n) if n % i == 0] == [1]

euclidian_distance = lambda w, v: (sum((wi - vi)**2 for wi,vi in zip(w,v)))**.5 


