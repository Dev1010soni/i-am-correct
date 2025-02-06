import markdown
import os

def markdown_to_html(markdown_text):
    """
    Converts a Markdown string to HTML.
    :param markdown_text: str, Markdown formatted text
    :return: str, HTML formatted text
    """
    html = markdown.markdown(markdown_text)
    return html

def main():
    md_text = """
    # Heading 1
    
    **Bold Text**
    
    *Italic Text*
    
    - List item 1
    - List item 2
    """
    
    html_output = markdown_to_html(md_text)
    os.makedirs("dist", exist_ok=True)
    with open("dist/output.html", "w") as file:
        file.write(html_output)
    print("HTML file created: dist/output.html")

if __name__ == "__main__":
    main()
