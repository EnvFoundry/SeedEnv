"""European call and put under an illustrative Black-Scholes process."""
import json
import QuantLib as ql

date = ql.Date(1, 1, 2025)
ql.Settings.instance().evaluationDate = date
expiry = date + 365
day_count = ql.Actual365Fixed()
spot = 100.0
rate = 0.05
volatility = 0.2
risk_free = ql.YieldTermStructureHandle(ql.FlatForward(date, rate, day_count))
dividend = ql.YieldTermStructureHandle(ql.FlatForward(date, 0.0, day_count))
vol = ql.BlackVolTermStructureHandle(ql.BlackConstantVol(date, ql.NullCalendar(), volatility, day_count))
process = ql.BlackScholesMertonProcess(ql.QuoteHandle(ql.SimpleQuote(spot)), dividend, risk_free, vol)
engine = ql.AnalyticEuropeanEngine(process)
values = []
for kind in (ql.Option.Call, ql.Option.Put):
    option = ql.VanillaOption(ql.PlainVanillaPayoff(kind, 100.0), ql.EuropeanExercise(expiry))
    option.setPricingEngine(engine)
    values.append(option.NPV())
parity_error = values[0] - values[1] - (spot - 100 * risk_free.discount(expiry))
print(json.dumps({'inputs':'synthetic', 'call':values[0], 'put':values[1], 'put_call_parity_error':parity_error}))
assert abs(parity_error) < 1e-10
