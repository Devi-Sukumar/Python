# Pythagorean triplets

def pytriples(n):
    c=0
    y=2

    if n>=6:
        #Calculate triples
        print("Pythagorean triples are:")
        while c<n:
            for x in range(1,y+1):
                a= y*y - x*x
                b= 2*x*y
                c= x*x + y*y

                if c>n:
                    break
                elif (a==0 or b==0 or c==0):
                    break
                else:
                    print (a,b,c)
            y+=1
    else:
        #print("No \"Pythagorean triples\" exists which is lesser than ", n)
        print("No \"Pythagorean triples\" exists which is lesser than {}".format(n))