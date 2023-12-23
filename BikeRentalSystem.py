class BikeShop():
    def __init__(self,stock):
        self.stock=stock
    def DisplayBikes (self):
        print("Total Bike",self.stock)
    def Rentforbike(self,q):
        if q<=0:
            print("Enter the positive value or should be greater than zero")
        elif q>self.stock:
            print("Enter the value less than stock")
        else:
            self.stock=self.stock-q
            print("Total Price",q*150)
            print("Total Bikes",self.stock)

while True:
 obj=BikeShop(200)
 uc=int(input('''
1 Dispaly Bikes
2 Rent a Bike
3 Exit
             '''          ))
 if uc==1:
    obj.DisplayBikes()
 elif uc==2:
    n=int(input("Enter the QTY:----"))
    obj.Rentforbike(n)
 else:
    break


