from copy import deepcopy
import json
from datetime import datetime

PATH = 'Приложение заметки\\notes.json'
notes = {}
original_notes = {}
key_1 = "title"
key_2 = "body"
key_3 = "date"

def find_max_id():
    global notes
    max_id = 0
    for key in notes:
        if (int(key) > max_id):
            max_id = int(key)
    if (max_id == 0):
        return 1
    else:
        return max_id+1

def open_file():
    global notes, original_notes, PATH
    with open(PATH, "r", encoding="utf-8") as file:
        notes = json.load(file)
    original_notes = deepcopy(notes)

def save_file():
    global notes, original_notes, PATH
    with open(PATH, "w", encoding="utf-8") as file:
        file.write(json.dumps(notes, ensure_ascii=False))
    original_notes = deepcopy(notes)

def add_note(new_note_val: list[str]):
    global notes, key_1, key_2, key_3
    max_id = find_max_id()
    date = datetime.now()
    date_format = date.strftime("%Y-%m-%d %H:%M:%S")

    new_note = {key_1 : new_note_val[0],
                key_2 : new_note_val[1],
                key_3 : date_format}

    notes[max_id] = new_note

def find_notes(word: str) -> dict[str, dict[str, str]]:
    global notes
    result = {}
    for n_id, note in notes.items():
        if (n_id == word):
            result[n_id] = note
            continue
        for nn_id, field in note.items():
            if word.lower() in field.lower():
                result[n_id] = note
                break
    return result

def edit_note(n_id: str, new_note: list[str]):
    global notes, key_1, key_2, key_3
    current_note = notes.get(n_id)
    note = {}
    date = datetime.now()
    date_format = date.strftime("%Y-%m-%d %H:%M:%S")

    if new_note[0]:
        note[key_1] = new_note[0]
    else:
        note[key_1] = current_note[key_1]
    
    if new_note[1]:
        note[key_2] = new_note[1]
    else:
        note[key_2] = current_note[key_2]
    if (new_note[0] or new_note[1]):
        note[key_3] = date_format
        notes[n_id] = note

    return note[key_1]

def delete_note(c_id: int) -> str:
    global notes
    return notes.pop(c_id)[key_1]