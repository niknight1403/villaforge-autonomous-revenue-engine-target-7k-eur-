from pptx import Presentation
from pptx.util import Inches

prs = Presentation()
slide_layout = prs.slide_layouts[5]  # Blank layout
slide = prs.slides.add_slide(slide_layout)

# Title
left = Inches(1)
top = Inches(1)
width = Inches(6)
height = Inches(1)
title = slide.shapes.add_textbox(left, top, width, height)
text_frame = title.text_frame
text_frame.text = 'Autonomous Revenue Engine'
text_frame.paragraphs[0].font.bold = True
text_frame.paragraphs[0].font.size = Inches(0.5)

# Content
content_slide_layout = prs.slide_layouts[1]  # Title and Content layout
content_slide = prs.slides.add_slide(content_slide_layout)

left = Inches(1)
top = Inches(2)
width = Inches(6)
height = Inches(2)
content_title = content_slide.shapes.add_textbox(left, top, width, height)
text_frame = content_title.text_frame
text_frame.text = 'Project Overview'
text_frame.paragraphs[0].font.bold = True
text_frame.paragraphs[0].font.size = Inches(0.4)

content_text = content_slide.shapes.add_textbox(left, Inches(4), width, Inches(4))
text_frame = content_text.text_frame
text_frame.text = 'This deck provides an overview of the Autonomous Revenue Engine project, including its goals, progress, and key milestones.'
text_frame.paragraphs[0].font.size = Inches(0.3)

prs.save('/opt/villaforge/server/data/workspace/autonomate-revenue-engine/deck.pptx')