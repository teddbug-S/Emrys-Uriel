import re
from colored import bg, fg, attr


# asking for file
file = input(r"Enter file path: ")

try:  # try opening and reading file
    with open(file, 'r') as f:
        contents = f.read()
except FileNotFoundError:
    print('File not found')

# defining a search pattern for names
names_pattern = re.compile(r'(Mr|Miss).+?\w+', re.I)
# using the search pattern on contents of the file
name_matches = names_pattern.finditer(contents)
# gathering results
names = [name.group() for name in name_matches]
# finally printing them
if names:
    print('\nNames:')
    for name in names:
        print(f"-- {name}")

# same process for telephone numbers
telephone_pattern = re.compile(r'\+\d+.+?\d+.+?\d{3}.+?(\d{4}|\d{3})', re.I)
telephone_matches = telephone_pattern.finditer(contents)
telephones = [numbers.group() for numbers in telephone_matches]
if telephones:
    print('\nTelephone Numbers:')
    for number in telephones:
        print(f"-- {number}")

# same process for emails
emails_pattern = re.compile(r'\w+.?@\w+\.(com|net|org|mail)', re.I)
email_matches = emails_pattern.finditer(contents)
email_addresses = [email.group() for email in email_matches]
if email_addresses:
    print('\nEmail Addresses:')
    for address in email_addresses:
        print(f"-- {address}")

# for web addresses
url_patterns = re.compile(r'http(s)?://(w{3})?\.?\w+\.(com|net|org|mail)', re.I)
url_matches = url_patterns.finditer(contents)
urls = [url.group() for url in url_matches]
if urls:
    print('\nWeb Addresses:')
    for url in urls:
        print(f"-- {url}")


# now defining a function to all user to do a custom search
def do_search(query):
    # parsing the query entered by user into a regex pattern
    search_pattern = re.compile(fr"{query}", re.I)
    # for confirming matches
    found = False
    # splitting contents from file into individual lines
    con = contents.split('\n')
    # if user searches for a line
    if query in con:
        position = con.index(query) + 1
        print(f'{query} found at line {position}.')
    else:
        for line in con:
            search_matches = search_pattern.search(line)
            if search_matches:
                start_pos = search_matches.start()
                end_pos = search_matches.end()
                line_pos = con.index(line)
                print(f"\nWord found at {start_pos+1} in line {line_pos}.")
                print(line[:start_pos]+f"%s%s{line[start_pos:end_pos]}%s" % (fg(232), bg(226), attr('reset'))+line[end_pos:])
                found = True
    if not found:
        print('No matches found')


while True:
    user_query = input("\nSearch word or line: ")
    do_search(user_query)
