a = 2
b = 3
#Z/pZ
p = 5

class Points:

    def __init__(self, x, y):
        self.x = x
        self.y = y

class InfinityPoint:

    def __init__(self):
        pass

def inverseNonZeroElement(nonZeroElement):
    if nonZeroElement == 0:
        print("No inverse")
        raise ValueError("No inverse")
    return pow(nonZeroElement,-1,p)

def pointIsOnCurve(pointToTest):
    if ((pointToTest.y) ** 2)%p == ((pointToTest.x)**3 + a * pointToTest.x + b) % p:
        return True
    else:
        return False

def mapPto2P(pointP):
    #our tangent equation is 3X^2 + a = 2Y and we search the point on the line
    if pointP.y == 0:
        print("point to infinity")
        return InfinityPoint()

    invPoint = inverseNonZeroElement((2*pointP.y) % p)
    if isinstance(invPoint, InfinityPoint):
        return InfinityPoint()
    s = ((3 * (pointP.x**2) + a)*invPoint)
    newx = (s**2 - 2 * pointP.x) % p
    newy = ( s*( pointP.x - newx) - pointP.y ) % p
    return Points(newx, newy)

def addition(pointP, pointQ):
    if isinstance(pointP, InfinityPoint):
        return pointQ
    if isinstance(pointQ, InfinityPoint):
        return pointP
    if pointP.x == pointQ.x:
        if pointP.y == pointQ.y:
            return mapPto2P(pointP)
        else: 
            return InfinityPoint()
    #our tangent equation is 3X^2 + a = 2Y and we search the point on the line
    inv = inverseNonZeroElement((pointQ.x - pointP.x)%p)
    delta = ((pointQ.y - pointP.y) * inv)%p
    newx = (delta**2 - pointP.x - pointQ.x )%p
    newy = (delta * (pointP.x - newx) - pointP.y)%p
    return Points(newx, newy)

def multiplicationByAdd(pointP, d):
    if d == 1:
        return pointP
    elif d == 2:
        return addition(pointP, pointP)
    elif d == 0:
        return 0
    else : 
        return addition(multiplicationByAdd(pointP, d-1), pointP)

def multiplication(pointP, d):
    if d == 0:
        return 0
    elif d == 1 :
        return pointP
    elif d % 2 == 1:
        return addition(pointP, multiplication(pointP, d-1) )
    else:
        return multiplication(mapPto2P(pointP), d/2)


def diffieHellman(commonPoint, AchoosenNumber, BchoosenNumber):
    ApointToB = multiplication(commonPoint, AchoosenNumber)
    BpointToA = multiplication(commonPoint, BchoosenNumber)

    AKey = multiplication(BpointToA, AchoosenNumber)
    BKey = multiplication(ApointToB, BchoosenNumber)
    print("Key of A : ")
    if isinstance(AKey, InfinityPoint):
        print("Infinity point")
    else : 
        print(AKey.x)
        print(AKey.y)
    
    print("Key of B : ")
    if isinstance(BKey, InfinityPoint):
        print("Infinity point")
    else : 
        print(BKey.x)
        print(BKey.y)

if __name__ == "__main__":
    print("-------------------------------")
    print("Point on curve : ")
    for i in range(0, p):
        for j in range(0,p):
            if pointIsOnCurve(Points(i,j)):
                print("(" + str(i) +" , " + str(j) + ")")
    print("-------------------------------")

    assert( isinstance(mapPto2P(Points(1,0)), InfinityPoint))

    point = multiplication(Points(1,1), 11)

    print("-------------------------------")
    print("Addition  Multiplication")
    for i in range(1,12):
        string_to_print = ""
        curr_point_addition = multiplicationByAdd(Points(1,1), i)
        curr_point_multiplication = multiplication(Points(1,1), i)
        if isinstance(curr_point_addition, InfinityPoint):
            string_to_print += "InfinityPoint"
        else:
            string_to_print += "(" + str(curr_point_addition.x) +" , " + str(curr_point_addition.y) + ")"
        if isinstance(curr_point_multiplication, InfinityPoint):
            string_to_print += "  " +  "InfinityPoint"
        else:
            string_to_print += "  " + "(" + str(curr_point_multiplication.x) +" , " + str(curr_point_multiplication.y) + ")"
        print(string_to_print)
    print("-------------------------------")
    print("Multiplication")
    if isinstance(point, InfinityPoint):
        print("Infinity point")
    else : 
        print(point.x)
        print(point.y)
    print("\n\nDiffie Hellman \n")
    diffieHellman(Points(3,4),  4, 2)


    a = 0
    b = 7
    #Z/pZ
    p = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F
    y = 0x483ADA7726A3C4655DA4FBFC0E1108A8FD17B448A68554199C47D08FFB10D4B8
    x = 0x79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798
    o = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141

    #Question 7 
    print("-------------------------------------------------")
    print("Question 7 : \nx : {}\ny : {}\np : {}".format(x,y,p))
    print("Test if x, y belongs to E(F) : {}".format(pointIsOnCurve(Points(x,y))))

    #Question 8
    print("-------------------------------------------------")
    print("Question 8 : \no : {}\np : {}".format(o,p))
    result = multiplication(Points(x,y), o)
    string_to_print = ""
    if isinstance(result, InfinityPoint):
        string_to_print += "InfinityPoint"
    else:
        string_to_print += "(" + str(result.x) +" , " + str(result.y) + ")"
    print("Compute oP {}".format(string_to_print))