css_code = """
/* أكواد CSS هنا */
body {
    background-color: white;
}

h1 {
    color: blue;
}

p {
    color: black;
}

h2 {
    color: blue;
}

h1 {
    font-size: 20px;
}
"""

unique_css = set(css_code.splitlines())
unique_css_code = "\n".join(unique_css)

with open("/x.css", "w") as file:
    file.write(unique_css_code)

