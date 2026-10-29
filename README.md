# AI Agents Forex — experimental forex tools

**The one-click script uses artificial prices. It does not run a five-year historical forex backtest.** No real-market profitability is established.

## Offline use

Python 3.11+:

```bash
python -m pip install -r requirements.txt
python -m pytest tests -q
python 一键回测.py --years 0.03
```

The short run checks the synthetic pipeline. It does not require API credentials, install packages at runtime, or place broker orders. Reports explicitly identify synthetic provenance. Lengthening the simulation does not turn it into historical evidence.

## Optional MT5 integration

On Windows, install `requirements-mt5.txt` and configure a local MetaTrader 5 terminal. On other systems, importing offline code remains possible; attempting MT5 connection/execution fails with an explicit dependency message. The offline pair catalogue does not certify broker symbol availability. No live order or terminal integration was tested during this repair.

`src/` contains indicator, agent, simulation and connector experiments. Agent confidence values are heuristic scores, not calibrated probabilities. See [AUDIT.md](AUDIT.md).
