import webbrowser

def web_search(query):
    webbrowser.open(f"https://www.google.com/search?q={query}")

def yt_search(query):
    webbrowser.open(f"https://www.youtube.com/results?search_query={query}")