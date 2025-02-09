"""rice_ball_shopモジュールを使ったドキュメンテーション文字列の例
"""

class Rice_ball:
    """おにぎりを表すクラス
    """

    def __init__(self, id: int, name: str, price: int):
        """Rice_ballクラスの__init__メソッド
        """
        self.id = id
        self.name = name
        self.price = price
    
    def raise_price(self, markup: int=10) -> int:
        """価格を値上げする。
        """
        self.price += markup
        return self.price
    
print(Rice_ball.__doc__)
print(Rice_ball.__init__.__doc__)
print(Rice_ball.__init__.__annotations__)
print(Rice_ball.raise_price.__doc__)
print(Rice_ball.raise_price.__annotations__)