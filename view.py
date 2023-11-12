import text

key_1 = "title"
key_2 = "body"
key_3 = "date"

def main_menu():
    for i, item in enumerate(text.menu):
        if i == 0:
            print(item)
        else:
            print(f'\t{i}. {item}')
    while True:
        choice = input(text.input_menu)
        if choice.isdigit() and 0 < int(choice) < len(text.menu):
            return int(choice)
        else:
            print(text.input_menu_error)

def print_message(msg: str):
    print('\n' + '=' * len(msg))
    print(msg)
    print('=' * len(msg) + '\n')

def show_notes(notes: dict[str, dict[str, str]], msg: str):
    global key_1, key_3
    if notes:
        print('\n' + '*' * 57)
        for i, note in notes.items():
            print(f'{i:>3}. {note[key_1]:<30} {note[key_3]:<20}')
            print(f"        {note[key_2]:<45}")
        print ('*' * 57 + '\n')
    else:
        print_message(msg)

def input_note(msg: str) -> list[str]:
    note = []
    for input_text in msg:
        note.append(input(input_text))
    return note

def input_request(msg: str) -> str:
    return input(msg)