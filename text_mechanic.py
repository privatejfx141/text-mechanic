import re
import unicodedata


def add_affix_into_line(text, prefix="", suffix=""):
    """(str[, str[, str]]) -> str

    Insert a prefix and/or suffix into the content of each line.
    """
    lines = text.splitlines()
    lines = [prefix + line + suffix for line in lines]
    result = '\n'.join(lines)
    return result


def add_remove_line_breaks():
    pass


def count_chars_words_lines(text):
    lines = text.splitlines()
    num_sentences = len(re.findall(r'(\.|\!|\?)\s+', text))
    num_lines = len(lines)
    # count characters and words
    num_chars = num_words = 0
    for line in lines:
        num_chars += len(line)
        num_words += len(re.split(' |/|-', line))
    # compile and return results
    results = dict()
    results['characters'] = num_chars
    results['words'] = num_words
    results['sentences'] = num_sentences
    results['lines'] = num_lines
    return results


def delimited_column_extractor(text, col, delimiter):
    """(str, int, str) -> list of [str]

    Extract a specific column of delimited text from each line of your input text.
    """
    lines = text.splitlines()
    column = list()
    for line in lines:
        if not delimiter:
            delimited = list(line)
        else:
            delimited = line.split(delimiter)
        try:
            word = delimited[col - 1]
        except IndexError:
            word = ''
        column.append(word)
    return column


def extract_urls(text):
    """(str) -> list of [str]

    Extract URLs in web pages, data files, text and more.
    """
    urls = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', text)
    return urls


def find_and_replace_text(text, by_regex=False, global_match=True, case_sensitive=False):
    """(str[, bool[, bool[, bool]]]) -> str

    Find and replace text matching your search criteria.
    """
    pass


def letter_case_converter():
    pass


def remove_duplicate_lines(text, case_sensitive=False, empty_lines=False):
    pass


def remove_empty_lines(text, whitespace_only=True):
    """(str[, bool]) -> str

    Remove/delete all empty lines within your text/list.
    """
    lines = text.splitlines()
    regex = r'^\s*$' if whitespace_only else r'^$'
    filtered = filter(lambda x: not re.match(regex, x), lines)
    result = '\n'.join(filtered)
    return result


def remove_extra_spaces(text, trim_whitespace=True, remove_all_spaces=False):
    """(str[, bool[, bool]]) -> str

    Remove leading/trailing/extra/all whitespaces from your text.
    """
    if trim_whitespace:
        text = text.strip()
    pattern = re.compile(r'\s+')
    repl = '' if remove_all_spaces else ' '
    text = re.sub(pattern, repl, text)
    return text


def remove_letter_accents(text):
    """(str) -> str

    Remove common letter accents from your text. (e.g. à will convert into a).

    >>> remove_letter_accents("àéêöhello")
    'aeeohello'
    """
    try:
        text = unicode(text, 'utf-8')
    except NameError: # unicode is a default on python 3 
        pass
    text = unicodedata.normalize('NFD', text)
    text = text.encode('ascii', 'ignore').decode("utf-8")
    return str(text)


def remove_lines_containing():
    pass


def soft_text_lines():
    pass


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    s = '''Enter text to be counted here. Check "Instant" to enable counting as you type.
Check "Cursor position." to instantly count to your cursor's position. Results will display in the "Cursor position" field.
Check "Selected count." to instantly count Select/highlight text. Results will display in the "Selected count is" field.
Check "Custom count." to instantly count any text entered into the "Enter custom count item here." field.
Check "Native spell-check." checkbox to enable your browser's built-in, spell-checker for this text area.
Click "Word Frequency" button for word frequency analysis to open. Analysis will contain each word, it's count and frequency percentage.
Line break formatting \r and/or \n will not be counted as characters but can be counted as a space by checking "Count line breaks as spaces.
Privacy of Data: This tool is built-with and functions-in Client Side JavaScripting, so only your computer will see or process your data input/output.'''
    print(count_chars_words_lines(s))    
