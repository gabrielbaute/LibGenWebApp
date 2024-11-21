from libgen_api import LibgenSearch

def search_title(title):
    s = LibgenSearch()
    results = s.search_title(title)
    return results

def search_author(author):
    s = LibgenSearch()
    results = s.search_title(author)
    return results

def search_title_filtered(title, title_filters, exact_match):
    tf = LibgenSearch()
    titles = tf.search_title_filtered(title, title_filters, exact_match)
    return titles

def search_author_filtered(author, author_filters, exact_match):
    tf = LibgenSearch()
    titles = tf.search_title_filtered(author, author_filters, exact_match)
    return titles
