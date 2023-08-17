from textual.app import ComposeResult
from textual.widgets import Static, Markdown

class ResponsePanel(Static):
    """the output panel of the response tab of the main navigation window"""

    content = ""

    def compose(self) -> ComposeResult:
        yield Markdown(self.content)

    def clear(self) -> None:
        """clears content from the response panel"""
        self.query_one(Markdown).update("")
                                        
    def update(self, content) -> None:
        """updates the response panel with new markdown content"""
        self.query_one(Markdown).update(content)

    def append_on_new_line(self, content) -> None:
        """appends to the existing markdown content after two new lines."""
        md = self.query_one(Markdown)
        self.content = self.content + "\n\n" + content
        self.update(self.content)

    def append_line_rule(self) -> None:
        """appends a line rule to existing markdown content."""
        md = self.query_one(Markdown)
        self.content = self.content + "\n --- \n"