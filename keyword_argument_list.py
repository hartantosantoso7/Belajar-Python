# def create_html(tag, text, href=""):
#     html = f"<{tag} href='{href}'>{text}</{tag}>"
#     return html


def create_html(tag, text, **attributes):
    html = f"<{tag}"

    for key, value in attributes.items():
        html = html + f" {key}='{value}'"

    html = html + f">{text}</{tag}>"
    print(attributes)
    return html

html = create_html("p", "Hello Python", style="paragraf")
print(html)
html = create_html("p", "ini link", href="www.google.com")
print(html)