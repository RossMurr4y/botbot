from textual.widgets import Static
from textual.app import ComposeResult
from quandary.ui.widgets.DebugPanel import DebugPanel

class DebugTab(Static):
    """the debug tab of the main navigation window"""
    
    def compose(self) -> ComposeResult:
        yield DebugPanel()