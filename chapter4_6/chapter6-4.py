class Rice_ball:

    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price
    
    def __str__(self):
        return f"{self.id} {self.name}の価格は{self.price}です"
    
    def raise_price(self, markup=10):
        self.price += markup

rice_ball = Rice_ball(1, "sake", 110)
print(rice_ball)

rice_ball.raise_price()
print(rice_ball)

rice_ball.raise_price(40)
print(rice_ball)

rice_ball2 = Rice_ball(2, "ume", 200)
print(rice_ball2)