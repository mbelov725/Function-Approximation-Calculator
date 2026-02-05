from getters import get_API_KEY
import os

def create_html():
    YOUR_API_KEY = get_API_KEY()

    BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    WEB_DIR = os.path.join(BASE_DIR, "web")

    template_path = os.path.join(WEB_DIR, "desmos_template.html")
    output_path = os.path.join(WEB_DIR, "desmos.html")

    with open(template_path) as f:
        html = f.read()

    with open(output_path, "w") as f:
        html = html.replace("YOUR_API_KEY", YOUR_API_KEY)
        f.write(html)

    print("web/desmos.html created with API key.")