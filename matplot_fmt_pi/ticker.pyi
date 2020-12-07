from matplotlib.ticker import FuncFormatter, MultipleLocator


class MultiplePi:
    denominator: int
    base: float
    symbol: str
    original_num: float

    def __init__(
        self,
        denominator: int,
        base: float = ...,
        symbol: str = ...) -> None: ...

    def formatter(self) -> FuncFormatter: ...
    def locator(self) -> MultipleLocator: ...
