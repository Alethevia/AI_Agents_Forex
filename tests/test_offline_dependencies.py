import pytest
from src.data import mt5_connector
from src.execution import mt5_executor

def test_missing_terminal_dependency_is_explicit():
    if mt5_connector.mt5 is None:
        with pytest.raises(RuntimeError, match='MetaTrader5'):
            mt5_connector.MT5Connector().connect()
    if mt5_executor.mt5 is None:
        with pytest.raises(RuntimeError, match='MT5'):
            mt5_executor.MT5OrderExecutor()
