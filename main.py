from snippet import Snippet, CODE_SNIPPETS, SnippetNotFoundError

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
    tags = input("What are the tags of your code snippet? (separated by spaces) ").split()
    CODE_SNIPPETS.append(Snippet(title, snippet, desc, tags))
    print(f"Successfully added snippet, '{title}'. ")

def view_snippets():
    print("Here are all of your code snippets: ")
    for idx, snippet in enumerate(CODE_SNIPPETS):
        print(format_snippet(idx, snippet.title, snippet.snippet, snippet.desc, snippet.tags))

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
    title = input("What's the title of the code snippet you would like to edit? ")
    for snippet in CODE_SNIPPETS:
        if snippet.title == title:
            new_title = input("Enter the new title: ") or snippet.title
            new_snippet = input("Enter the new code snippet: ") or snippet.snippet
            new_desc = input("Enter the new description: ") or snippet.desc
            new_tags = input("Enter the new tags (separated by spaces): ").split() or snippet.tags

            snippet.edit(new_title, new_snippet, new_desc, new_tags)
            print("Snippet edited successfully.")
            break
    else:
        raise SnippetNotFoundError(f"No such code snippet with title '{title}'.")

def delete_snippet():
    title = input("What's the title of the code snippet you would like to delete? ")
    for snippet in CODE_SNIPPETS:
        if snippet.title == title:
            snippet.delete()
            print("Snippet deleted successfully.")
            break
    else:
        raise SnippetNotFoundError(f"No such code snippet with title '{title}'.")

    

if __name__ == "__main__":
    while True:
        try:
            choice = int(input("Welcome to pysnippets, where you can store your code snippets. Enter a number: \n \
                        1) add a snippet \n \
                        2) view your snippets \n \
                        3) search for a snippet \n \
                        4) edit a snippet \n \
                        5) delete a snippet \n \
                        4) exit? "))
        except ValueError as _:
            continue
        
        if choice == 1:
            add_snippet()
        elif choice == 2:
            view_snippets()
        elif choice == 3:
            search_snippets()
        elif choice == 4:
            edit_snippet()
        elif choice == 5:
            delete_snippet()
        else:
            print("Thank you for using pysnippets.")
            break
