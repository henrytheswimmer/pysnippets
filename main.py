from snippet import Snippet, CODE_SNIPPETS

def format_snippet(idx, title, snippet, desc, tags):
    return f"""
{idx + 1}:
Title: {title}
Snippet: {snippet}
Description: {desc}
Tags: {tags}
    """

def add_snippet():
    title = input("What's the title of your code snippet? ")
    snippet = input("What's your code snippet? ")
    desc = input("What's your description of this code snippet? ")
    tags = input("What are the tags of your code snippet? ").split()
    CODE_SNIPPETS.append(Snippet(title, snippet, desc, tags))
    print(f"Successfully added snippet, '{title}'. ")

def view_snippets():
    print("Here are all of your code snippets: ")
    for idx, snippet in enumerate(CODE_SNIPPETS):
        print(format_snippet(idx + 1, snippet.title, snippet.snippet, snippet.desc, snippet.tags))

def search_snippets():
    tag = input("What tag would you like to search your code snippets by? ")
    searched_snippets = []

    for idx, snippet in enumerate(CODE_SNIPPETS):
        for snippet_tag in snippet.tags:
            if tag == snippet_tag:
                searched_snippets.append(idx)

    for idx in searched_snippets:
        print(format_snippet(idx, CODE_SNIPPETS[idx].title, CODE_SNIPPETS[idx].snippet, CODE_SNIPPETS[idx].desc, CODE_SNIPPETS[idx].tags))

def edit_snippet():
    pass

def delete_snippet():
    pass

if __name__ == "__main__":
    while True:
        choice = int(input("Welcome to pysnippets, where you can store your code snippets. Would you like to: 1) add a snippet, \
                    2) view your snippets, 3) search for a snippet or 4) exit? "))
        
        if choice == 1:
            add_snippet()
        elif choice == 2:
            view_snippets()
        elif choice == 3:
            search_snippets()
        else:
            print("Thank you for using pysnippets.")
            break
