"""Build the fictional Northwind Traders test document as DOCX, PDF and image-only PDF.

The content lives in module-level constants so that check_output.py can compare
the converted Markdown against the exact ground truth instead of eyeballing it.

Requires Windows with Microsoft Word (PDF export and footnotes via COM),
python-docx, pywin32 and PyMuPDF.
"""

from pathlib import Path

HERE = Path(__file__).resolve().parent
INPUT = HERE / "input"
DOCX = INPUT / "northwind-ki-regeln.docx"
PDF = INPUT / "northwind-ki-regeln.pdf"
SCAN_PDF = INPUT / "northwind-ki-regeln-scan.pdf"

TITLE = "Interne Regeln zum Einsatz von KI im Vertrieb"
SUBTITLE = "Northwind Traders GmbH, Richtlinie VT-07, gültig ab 1. Oktober 2026"
HEADER = "Northwind Traders | Richtlinie VT-07 | Nur für den internen Gebrauch"
FOOTER_PREFIX = "Seite"

H_SCOPE = "1 Zweck und Geltungsbereich"
SCOPE_TEXT = (
    "Diese Richtlinie regelt, wie Mitarbeitende im Vertrieb von Northwind Traders "
    "generative KI-Werkzeuge einsetzen dürfen."
)
# The footnote reference is attached to the word "KI-Werkzeuge" in SCOPE_TEXT.
FOOTNOTE_ANCHOR = "KI-Werkzeuge"
FOOTNOTE = (
    "Gemeint sind alle Systeme, die auf Basis statistischer Sprachmodelle Texte, "
    "Tabellen oder Bilder erzeugen, unabhängig davon, ob sie lokal oder als "
    "Clouddienst betrieben werden."
)
SCOPE_TEXT_2 = (
    "Sie gilt für den Innendienst, den Außendienst und das Key-Account-Management "
    "an allen Standorten. Abweichende Regelungen einzelner Abteilungen sind nur "
    "zulässig, wenn sie strenger sind als diese Richtlinie. Die Richtlinie wird "
    "jährlich überprüft und bei Bedarf früher angepasst, etwa wenn neue Werkzeuge "
    "freigegeben oder gesetzliche Vorgaben geändert werden."
)

H_PRINCIPLES = "2 Grundsätze"
PRINCIPLES = [
    "Kundendaten werden nur in freigegebene Werkzeuge eingegeben.",
    "Jedes KI-Ergebnis wird vor der Weitergabe von einem Menschen geprüft.",
    "Angebote und Preise entstehen nie ausschließlich durch ein KI-Werkzeug.",
    "Prompts mit vertraulichem Inhalt werden nicht in gemeinsamen Vorlagen gespeichert.",
    "Unklare Fälle werden vor der Nutzung an das Team Datenschutz gemeldet.",
]

H_TABLE = "3 Datenklassen und erlaubte Werkzeuge"
TABLE_INTRO = (
    "Die folgende Tabelle ordnet jeder Datenklasse die zulässigen Werkzeuge zu."
)
TABLE = [
    ["Datenklasse", "Beispiele", "Erlaubte Werkzeuge", "Freigabe durch"],
    [
        "Öffentlich",
        "Produktkatalog, Pressemitteilungen",
        "Alle freigegebenen Chatassistenten",
        "keine",
    ],
    [
        "Intern",
        "Vertriebshandbuch, Schulungsfolien",
        "Unternehmensassistent im EU-Rechenzentrum",
        "Teamleitung",
    ],
    [
        "Vertraulich",
        "Kundenlisten, Rabattstaffeln",
        "Lokales Modell auf dem Firmenlaptop",
        "Vertriebsleitung",
    ],
    [
        "Streng vertraulich",
        "Vertragsentwürfe, Gesundheitsdaten",
        "Kein KI-Werkzeug",
        "nicht zulässig",
    ],
]
TABLE_OUTRO = (
    "Fällt ein Dokument in mehrere Klassen, gilt immer die strengste. Wer unsicher "
    "ist, behandelt das Dokument als vertraulich."
)

H_PROCESS = "4 Freigabeprozess für neue Werkzeuge"
# Set in two columns. Each paragraph opens with a distinct lead word so that the
# reading order can be checked by position in the Markdown.
PROCESS = [
    "Antrag. Ein neues KI-Werkzeug beantragt die Teamleitung schriftlich. Der Antrag "
    "beschreibt den Zweck, die betroffenen Datenklassen, den Anbieter und den Ort, an "
    "dem die Daten verarbeitet werden. Ohne diese Angaben wird der Antrag nicht bearbeitet.",
    "Datenflussprüfung. Das Team Datenschutz prüft, welche Daten das Werkzeug verlässt, "
    "wer sie speichert und wie lange. Werkzeuge, die Eingaben zum Training eigener Modelle "
    "verwenden, werden für interne und vertrauliche Daten grundsätzlich abgelehnt.",
    "Pilotphase. Nach positiver Prüfung testet eine kleine Gruppe das Werkzeug vier Wochen "
    "lang mit öffentlichen Daten. Die Gruppe dokumentiert Fehler, auffällige Ergebnisse und "
    "den tatsächlichen Zeitgewinn in einem gemeinsamen Protokoll.",
    "Bewertung. Die Vertriebsleitung bewertet das Protokoll gemeinsam mit dem Team "
    "Datenschutz. Maßgeblich sind die Qualität der Ergebnisse, der Aufwand für die "
    "menschliche Prüfung und die Frage, ob ein bereits freigegebenes Werkzeug denselben "
    "Zweck erfüllt.",
    "Freigabe. Wird das Werkzeug freigegeben, trägt das Team Datenschutz es mit der "
    "höchsten zulässigen Datenklasse in die Werkzeugliste im Intranet ein. Erst ab diesem "
    "Eintrag darf das Werkzeug im Tagesgeschäft verwendet werden.",
    "Wiedervorlage. Jede Freigabe gilt zwölf Monate. Danach wird das Werkzeug erneut "
    "geprüft, weil sich Nutzungsbedingungen und Datenverarbeitung der Anbieter häufig ändern.",
]

H_VIOLATIONS = "5 Verstöße und Ansprechpartner"
VIOLATIONS_TEXT = (
    "Verstöße gegen diese Richtlinie meldet man der Teamleitung oder direkt dem Team "
    "Datenschutz. Fragen zur Einordnung einzelner Dokumente beantwortet das Team "
    "Datenschutz unter der internen Durchwahl 4711."
)

HEADINGS = [TITLE, H_SCOPE, H_PRINCIPLES, H_TABLE, H_PROCESS, H_VIOLATIONS]

# Page that is rasterised for the OCR test (0-based); chosen after inspecting the
# layout so that it carries the list and the table.
SCAN_PAGE = 0
SCAN_DPI = 150


def _add_field(paragraph, instr: str) -> None:
    from docx.oxml import OxmlElement
    from docx.oxml.ns import qn

    fld = OxmlElement("w:fldSimple")
    fld.set(qn("w:instr"), instr)
    run = OxmlElement("w:r")
    text = OxmlElement("w:t")
    text.text = "1"
    run.append(text)
    fld.append(run)
    paragraph._p.append(fld)


def _set_columns(section, count: int) -> None:
    from docx.oxml import OxmlElement
    from docx.oxml.ns import qn

    sect_pr = section._sectPr
    cols = sect_pr.find(qn("w:cols"))
    if cols is None:
        cols = OxmlElement("w:cols")
        sect_pr.append(cols)
    cols.set(qn("w:num"), str(count))
    cols.set(qn("w:space"), "567")


def build_docx() -> None:
    from docx import Document
    from docx.enum.section import WD_SECTION
    from docx.shared import Pt

    doc = Document()
    doc.styles["Normal"].font.name = "Calibri"
    doc.styles["Normal"].font.size = Pt(11)

    first = doc.sections[0]
    first.header.paragraphs[0].text = HEADER
    footer = first.footer.paragraphs[0]
    footer.add_run(f"{FOOTER_PREFIX} ")
    _add_field(footer, "PAGE")
    footer.add_run(" von ")
    _add_field(footer, "NUMPAGES")

    doc.add_heading(TITLE, level=0)
    doc.add_paragraph(SUBTITLE)

    doc.add_heading(H_SCOPE, level=1)
    doc.add_paragraph(SCOPE_TEXT)
    doc.add_paragraph(SCOPE_TEXT_2)

    doc.add_heading(H_PRINCIPLES, level=1)
    for item in PRINCIPLES:
        doc.add_paragraph(item, style="List Number")

    doc.add_heading(H_TABLE, level=1)
    doc.add_paragraph(TABLE_INTRO)
    table = doc.add_table(rows=len(TABLE), cols=len(TABLE[0]))
    table.style = "Table Grid"
    for r, row in enumerate(TABLE):
        for c, value in enumerate(row):
            cell = table.cell(r, c)
            cell.text = value
            if r == 0:
                cell.paragraphs[0].runs[0].bold = True
    doc.add_paragraph(TABLE_OUTRO)

    # The two-column part starts on a fresh page so that both columns are full.
    # page_break_before instead of a break paragraph, which would spill onto an
    # empty page when page 1 is already full.
    doc.add_heading(H_PROCESS, level=1).paragraph_format.page_break_before = True
    two_col = doc.add_section(WD_SECTION.CONTINUOUS)
    _set_columns(two_col, 2)
    for text in PROCESS:
        lead, rest = text.split(". ", 1)
        p = doc.add_paragraph()
        p.add_run(lead + ". ").bold = True
        p.add_run(rest)

    one_col = doc.add_section(WD_SECTION.CONTINUOUS)
    _set_columns(one_col, 1)
    doc.add_heading(H_VIOLATIONS, level=1)
    doc.add_paragraph(VIOLATIONS_TEXT)

    INPUT.mkdir(exist_ok=True)
    doc.save(DOCX)


def export_pdf_with_word() -> None:
    """Add the footnote and export to PDF; python-docx cannot create footnotes."""
    import win32com.client

    word = win32com.client.DispatchEx("Word.Application")
    word.Visible = False
    word.DisplayAlerts = 0
    try:
        doc = word.Documents.Open(str(DOCX))
        rng = doc.Content
        find = rng.Find
        if not find.Execute(FOOTNOTE_ANCHOR):
            raise RuntimeError("footnote anchor not found")
        rng.Collapse(0)  # wdCollapseEnd: reference mark goes after the anchor word
        # The Text argument of Footnotes.Add is ignored under late binding,
        # so the footnote body is set on the returned object.
        note = doc.Footnotes.Add(Range=rng)
        note.Range.Text = FOOTNOTE
        doc.Fields.Update()
        doc.Save()
        doc.ExportAsFixedFormat(str(PDF), 17)  # wdExportFormatPDF
        doc.Close(False)
    finally:
        word.Quit()


def build_scan_pdf() -> None:
    """Rasterise one page into an image-only PDF so Docling must fall back to OCR."""
    import fitz

    src = fitz.open(PDF)
    pix = src[SCAN_PAGE].get_pixmap(dpi=SCAN_DPI, colorspace=fitz.csGRAY)
    out = fitz.open()
    page = out.new_page(
        width=src[SCAN_PAGE].rect.width, height=src[SCAN_PAGE].rect.height
    )
    page.insert_image(page.rect, stream=pix.tobytes("png"))
    out.save(SCAN_PDF)
    if out[0].get_text().strip():
        raise RuntimeError("scan PDF unexpectedly carries a text layer")


if __name__ == "__main__":
    build_docx()
    export_pdf_with_word()
    build_scan_pdf()
    print(f"written: {DOCX.name}, {PDF.name}, {SCAN_PDF.name}")
