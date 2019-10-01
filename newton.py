

#def jacobian(f, x):
    #     h = 1.0e-4
     #    n = len(x)
      #   Jac = zeros([n,n])
       #  f0 = X
        # for i in arange(0,n,1):
         #         tt = x[i]
          #        x[i] = tt + h
           #       f1= X
            #      x[i] = tt
             #     Jac [:,i] = (f1 - f0)/h
         #return Jac, f0
#def newton(f, x, tol=1.0e-9):
 #        iterMax = 50
  #       for i in range(iterMax):
   #               Jac, fO = jacobian(f, x)
    #              if sqrt(dot(fO, fO) / len(x)) < tol:
     #                      return x, i                 
      #            dx = linalg.solve(Jac, fO)
       #           x = x - dx
        # print ("Too many iterations for the Newton method")
#x, iter = newton(f, X)
#e = 0.0000001
#xx = 0
#while 1:
 #   if X.all()!=0:
  #      X = X - X_new / diff(X)
   # else:
    #    print("Error")
     #   break
    #if abs(X-xx) < e:
     #   print ('x=%10.6f'%X)
      #  break
    #xx = X