"""
Convert RPG module .txt files to .docx
Usage: python3 txt_to_docx.py <input.txt> [output.docx]
"""
import sys
import re
from docx import Document
from docx.shared import Pt, RGBColor, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH

def convert(input_path, output_path):
    with open(input_path, "r") as f:
        lines = f.readlines()

    doc = Document()

    # Page margins
    for section in doc.sections:
        section.top_margin    = Inches(1)
        section.bottom_margin = Inches(1)
        section.left_margin   = Inches(1.2)
        section.right_margin  = Inches(1.2)

    def add_rule(doc):
        p = doc.add_paragraph()
        p.add_run("─" * 72)
        p.runs[0].font.color.rgb = RGBColor(0xAA, 0xAA, 0xAA)
        p.runs[0].font.size = Pt(8)

    i = 0
    while i < len(lines):
        line = lines[i].rstrip("\n")

        # ===...=== banner lines → H1 title block
        if re.match(r"^={10,}", line):
            i += 1
            continue

        # --- section divider → thin rule
        if re.match(r"^-{3,}$", line.strip()):
            add_rule(doc)
            i += 1
            continue

        # Blank line
        if line.strip() == "":
            i += 1
            continue

        # "--- N. TITLE ---" location headers
        m = re.match(r"^---\s+(\d+\.\s+.+?)\s+---$", line)
        if m:
            p = doc.add_heading(m.group(1), level=2)
            i += 1
            continue

        # ALL-CAPS section headers (THE HOOK, LOCATIONS, etc.)
        if re.match(r"^[A-Z][A-Z /&'()0-9\-]{3,}$", line.strip()) and not line.startswith(" "):
            p = doc.add_heading(line.strip(), level=1)
            i += 1
            continue

        # "WORD WORD:" label lines (BOLD / SENSORY / ACTION, GM NOTE, etc.)
        if re.match(r"^[A-Z][A-Z /&'()0-9\-]+:$", line.strip()):
            p = doc.add_paragraph()
            run = p.add_run(line.strip())
            run.bold = True
            run.font.size = Pt(10)
            i += 1
            continue

        # Indented bullet lines (start with 2+ spaces or a dash)
        if re.match(r"^  +- ", line) or re.match(r"^  +[A-Z]", line):
            # strip leading spaces, treat as body indent
            p = doc.add_paragraph(style="List Bullet")
            p.paragraph_format.left_indent = Inches(0.3)
            _add_inline(p, line.strip())
            i += 1
            continue

        # Dialogue lines  DALE: "..." or FENN: "..."
        if re.match(r"^[A-Z]+:\s+\"", line.strip()):
            p = doc.add_paragraph()
            p.paragraph_format.left_indent = Inches(0.4)
            run = p.add_run(line.strip())
            run.italic = True
            run.font.size = Pt(10)
            i += 1
            continue

        # Default: body paragraph
        p = doc.add_paragraph()
        _add_inline(p, line.strip())
        i += 1

    doc.save(output_path)
    print(f"Saved: {output_path}")


def _add_inline(paragraph, text):
    """Handle **bold** or plain text within a paragraph."""
    parts = re.split(r"(\*\*[^*]+\*\*)", text)
    for part in parts:
        if part.startswith("**") and part.endswith("**"):
            run = paragraph.add_run(part[2:-2])
            run.bold = True
        else:
            paragraph.add_run(part)
    for run in paragraph.runs:
        run.font.size = Pt(11)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 txt_to_docx.py <input.txt> [output.docx]")
        sys.exit(1)
    inp = sys.argv[1]
    out = sys.argv[2] if len(sys.argv) > 2 else inp.replace(".txt", ".docx")
    convert(inp, out)
