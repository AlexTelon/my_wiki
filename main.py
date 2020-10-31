import markdown
import glob
from pathlib import Path
from markdown.extensions.wikilinks import WikiLinkExtension
from markdown.extensions.codehilite import CodeHiliteExtension

OUTPUT_DIR = 'output'

def markdown_to_html(file):
    with open(file) as f:
        page = f.read()

    return markdown.markdown(page, extensions=[
        WikiLinkExtension(base_url='/', end_url='.html'),
        CodeHiliteExtension()
    ])

HEADER = """
<!DOCTYPE html>
<html lang="en">

<head>
<meta charset="utf-8">
<link rel="stylesheet" type="text/css" href="codehilite.css">
</head>

<body>
"""

FOOTER = """
</body>
</html>
"""

for file in glob.glob('pages/*.md'):
    html = markdown_to_html(file)

    file_name = Path(file).stem

    output_file = Path(OUTPUT_DIR) / (file_name + '.html')
    with open(output_file, 'w') as f:
        f.write(HEADER + html + FOOTER)