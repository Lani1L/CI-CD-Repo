import os

def generate_html():
    os.makedirs("../site", exist_ok=True)
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>My Python GitHub Pages Site</title>
    </head>
    <body>
        <h1>Hello from Python CI/CD!</h1>
        <p>This page is generated automatically by Python and deployed via GitHub Actions.</p>
    </body>
    </html>
    """
    with open("../site/index.html", "w") as f:
        f.write(html_content)
    return True

if __name__ == "__main__":
    if generate_html():
        print("HTML page generated successfully!")
