CODE_SNIPPETS = []

class Snippet:
    def __init__(self, title, snippet, desc, tags):
        self.title = title
        self.snippet = snippet
        self.desc = desc
        self.tags = tags

        self.validate()

    def validate(self):
        if not self.title:
            raise ValueError("Title cannot be empty.")
        
        # make sure the snippet is valid python code
        try:
            compile(self.snippet, "<string>", "exec")
        except SyntaxError as _:
            raise ValueError(f"Invalid code snippet: {_}") from _
        
        if not self.desc:
            raise ValueError("Description cannot be empty.")
        
        if not self.tags:
            raise ValueError("Tags cannot be empty.")
        
    def edit(self, new_title, new_snippet, new_desc, new_tags):
        self.title = new_title
        self.snippet = new_snippet
        self.desc = new_desc
        self.tags = new_tags

    def delete(self):
        CODE_SNIPPETS.remove(self)

class SnippetNotFoundError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)

    def __str__(self) -> str:
        return f"Snippet not found: {self.message}"
