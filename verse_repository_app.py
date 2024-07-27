from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, DirectoryTree, TextArea, Button, Checkbox
from textual.containers import Horizontal, Vertical
import pyperclip
import os

class VerseRepositoryApp(App):
    CSS = """
    #file_tree {
        width: 30%;
        height: 100%;
    }
    #editor_container {
        width: 70%;
        height: 100%;
    }
    #editor {
        height: 90%;
    }
    #copy_button {
        dock: bottom;
        width: 100%;
    }
    #wrap_checkbox {
        margin: 1 1;
    }
    #controls {
        height: 3;
        dock: top;
    }
    """

    BINDINGS = [
        ("q", "quit", "Quit"),
        ("c", "copy", "Copy"),
    ]

    def __init__(self):
        super().__init__()
        self.current_file = None

    def compose(self) -> ComposeResult:
        yield Header()
        yield Horizontal(
            DirectoryTree("./verse", id="file_tree"),
            Vertical(
                Horizontal(
                    Checkbox("Word Wrap", id="wrap_checkbox"),
                    id="controls"
                ),
                TextArea(id="editor"),
                Button("Copy to Clipboard", id="copy_button", variant="primary"),
                id="editor_container"
            )
        )
        yield Footer()

    def on_mount(self):
        self.query_one(DirectoryTree).focus()
        self.query_one(TextArea).focus()

    def on_directory_tree_file_selected(self, event: DirectoryTree.FileSelected):
        self.current_file = event.path
        with open(self.current_file, "r") as file:
            content = file.read()
        self.query_one(TextArea).load_text(content)

    def on_button_pressed(self, event: Button.Pressed):
        self.copy_to_clipboard()

    def action_copy(self):
        self.copy_to_clipboard()

    def copy_to_clipboard(self):
        content = self.query_one(TextArea).text
        pyperclip.copy(content)
        self.notify("Content copied to clipboard!")

    def on_checkbox_changed(self, event: Checkbox.Changed):
        text_area = self.query_one(TextArea)
        text_area.wrap = event.value

    def action_quit(self):
        self.exit()

if __name__ == "__main__":
    app = VerseRepositoryApp()
    app.run()