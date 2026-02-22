"""Tests for Incident ticket auto-classifier."""
import pytest, sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from ticketClassifier import TicketClassifier
from keywordMatcher import KeywordMatcher

class TestMain:
    def test_basic(self):
        obj = TicketClassifier()
        assert obj.process({"key": "val"}) is not None
    def test_empty(self):
        obj = TicketClassifier()
        assert obj.process(None) is None
    def test_stats(self):
        obj = TicketClassifier()
        obj.process({"x": 1})
        assert obj.get_stats()["processed"] == 1

class TestSupport:
    def test_basic(self):
        obj = KeywordMatcher()
        assert obj.process({"key": "val"}) is not None

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
