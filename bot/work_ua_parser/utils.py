def save_html(filename: str, html) -> None:
    with open(filename, "w") as file:
        file.write(html)
        

def read_html(filename: str) -> str:
    with open(filename, "r") as file:
        html_content = file.read()
    return html_content