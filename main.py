import markdown
import glob

def markdown_to_html(file):
    with open(file) as f:
        page = f.read()
    return markdown.markdown(page)

for file in glob.glob('pages/*.md'):
    html = markdown_to_html(file)
    print(html)
    print()