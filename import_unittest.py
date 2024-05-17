import unittest
from unittest.mock import patch, MagicMock
import pandas as pd
from stock import api_key, symbol, output_size, ts, data, meta_data, df

class TestStockAnalysis(unittest.TestCase):
    @patch('stock.TimeSeries')
    def setUp(self, mock_ts):
        # Mock the TimeSeries.get_daily method
        self.mock_get_daily = MagicMock(return_value=(pd.DataFrame({'4. close': [100, 200, 300]}), None))
        mock_ts.return_value.get_daily = self.mock_get_daily

        # Mock matplotlib.pyplot
        self.plt_patcher = patch('stock.plt')
        self.mock_plt = self.plt_patcher.start()

    def tearDown(self):
        self.plt_patcher.stop()

    def test_api_key_set(self):
        self.assertNotEqual(api_key, 'YOUR_API_KEY', "API key is not set.")

    def test_symbol_set(self):
        self.assertEqual(symbol, 'TSLA', "Stock symbol is not set correctly.")

    def test_output_size_set(self):
        self.assertEqual(output_size, 'full', "Output size is not set correctly.")

    def test_time_series_initialization(self):
        ts.get_daily(symbol='TSLA')
        self.mock_get_daily.assert_called_once()

    def test_get_daily_data(self):
        ts.get_daily(symbol=symbol, outputsize=output_size)
        self.mock_get_daily.assert_called_with(symbol=symbol, outputsize=output_size)

    def test_data_frame_creation(self):
        self.assertIsInstance(df, pd.DataFrame, "Data is not a pandas DataFrame.")

    def test_plotting(self):
        self.mock_plt.plot.assert_called()
        self.mock_plt.xlabel.assert_called_with('Date')
        self.mock_plt.ylabel.assert_called_with('Closing Price')
        self.mock_plt.title.assert_called_with('Tesla Stock Price')
        self.mock_plt.xticks.assert_called()
        self.mock_plt.show.assert_called()

if __name__ == '__main__':
    unittest.main()