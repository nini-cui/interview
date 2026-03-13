import unittest
from batcher.batch_processor import BatcherProcessor
from unittest.mock import Mock, MagicMock
import time


class TestBatchProcessor(unittest.TestCase):
    def test_trigger_on_batch_size(self):
        mock = Mock()
        batcher = BatcherProcessor(
            batch_processor=mock
        )
        
        batcher.add_items(1)
        batcher.add_items(2)
        batcher.add_items(3)
        assert mock.call_count == 1

    def test_trigger_on_timeout(self):
        batcher = BatcherProcessor(
            batch_processor=mock
        )
        batcher.add_items(1)
        batcher.add_items(2)
        batcher.add_items(3)
        # call once 
        time.sleep(2)
        batcher.add_items(4)
        time.sleep(1.5)
        # assert mock.call_count == 2
        print(mock.method_calls)

    def test_inputs(self):
        mock = Mock()
        with self.assertRaises(ValueError):
            batcher = BatcherProcessor(
            batch_size=-1,
            batch_processor=mock
        )
            
        self.assertEqual(str(re.exception), "batch size cannot be less than 0")

if __name__ == "__main__":
    unittest.main()