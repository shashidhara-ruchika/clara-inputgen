def l3n(num1, num2, num3):
        #num1, num2, num3 = list(map(int, input().split()))
        if(num1 > num2):
                if(num1 > num3):
                        #print(num1)
                        return num1
                else:
                        #print(num3)
                        return num3
        else:
                if(num2 > num3):
                        #print(num2)
                        return num2
                else:
                        #print(num3)
                        return num3
                        



