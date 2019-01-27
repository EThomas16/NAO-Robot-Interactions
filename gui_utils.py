import webbrowser as wb

def load_webpage(url):
    wb.open_new(url)

def toggle_checkbox_state(checkbox, toggle_text):
    if checkbox.text() == toggle_text[0]:
        checkbox.setText(toggle_text[1])
    elif checkbox.text() == toggle_text[1]:
        checkbox.setText(toggle_text[0])