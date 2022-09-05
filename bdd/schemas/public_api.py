from pydantic import BaseModel


class ServerTimeResultSchema(BaseModel):
    unixtime: int
    rfc1123: str


class ServerTimeResponseSchema(BaseModel):
    result: ServerTimeResultSchema
    error: list[str]


FeeSchema = tuple[int, float]


class AssetPairSchema(BaseModel):
    altname: str
    wsname: str
    aclass_base: str
    base: str
    aclass_quote: str
    quote: str
    lot: str
    pair_decimals: int
    lot_decimals: int
    lot_multiplier: int
    leverage_buy: list[int]
    leverage_sell: list[int]
    fees: list[FeeSchema]
    fees_maker: list[FeeSchema]
    fee_volume_currency: str
    margin_call: int
    margin_stop: int
    ordermin: str


class TradingPairResultSchema(BaseModel):
    XXBTZUSD: AssetPairSchema


class TradingPairResponseSchema(BaseModel):
    result: TradingPairResultSchema
    error: list[str]
