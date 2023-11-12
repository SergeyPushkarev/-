import view
import model
import text

def search_note():
    word = view.input_request(text.input_search_word)
    result = model.find_notes(word)
    view.show_notes(result, text.not_find(word))
    if result:
        return True
    
def start():
    while True:
        choice = view.main_menu()
        match choice:
            case 1:
                model.open_file()
                view.print_message(text.load_successful)
            case 2:
                model.save_file()
                view.print_message(text.save_successful)
            case 3:
                view.show_notes(model.notes, text.empty_notes_error)
            case 4:
                new_note = view.input_note(text.input_note)
                model.add_note(new_note)
                view.print_message(text.note_action(new_note[0], text.operation[0]))
            case 5:
                if search_note():
                    n_id = str(view.input_request(text.input_edit_note_id))
                    new_contact = view.input_note(text.input_edit_note)
                    name = model.edit_note(n_id, new_contact)
                    view.print_message(text.note_action(name, text.operation[1]))
            case 6:
                if search_note():
                    n_id = str(view.input_request(text.input_del_note_id))
                    name = model.delete_note(n_id)
                    view.print_message(text.note_action(name, text.operation[2]))
            case 7:
                search_note()
            case 8:
                if model.original_notes != model.notes:
                    if view.input_request(text.confirm_changes).lower() == 'y':
                        model.save_file()
                        view.print_message(text.save_successful)
                view.print_message(text.exit_program)
                break