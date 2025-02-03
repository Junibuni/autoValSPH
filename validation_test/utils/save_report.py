import os
import atexit
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.pagesizes import A4 
from datetime import datetime

class Document:
    def __init__(self, save_pth, name, git):
        self.cnt = 1
        self.lh = 0
        self.save_pth = os.path.join(save_pth, "report.pdf")
        atexit.register(self.save)
        
        current_date = datetime.now().strftime("%Y/%m/%d")

        pdfmetrics.registerFont(TTFont("맑은고딕", "malgun.ttf"))
        pdfmetrics.registerFont(TTFont("맑은고딕_볼드", "malgunbd.ttf"))
        self.pdf = canvas.Canvas(f"{self.save_pth}", pagesize=A4)
        self.width, self.height = A4
        self.pdf.setFont("맑은고딕", 16)
        title = "NFLOW SDK Validation Report"
        str_width = self.pdf.stringWidth(title)
        self.pdf.drawString((self.width // 2) - (str_width // 2), 800, title)

        self.pdf.setFont("맑은고딕", 9)
        date_text = current_date
        date_text_width = self.pdf.stringWidth(date_text)
        self.pdf.drawString(580 - date_text_width, 779, date_text)

        self.pdf.setLineWidth(0.3)
        self.pdf.line(30, 770, 580, 770)
        self.pdf.line(30, 773, 580, 773)

        author_text = f"작성자: {name}"
        author_text_width = self.pdf.stringWidth(author_text)
        self.pdf.drawString(580 - author_text_width, 755, author_text)
        git_text = f"Git: {git}"
        git_text_width = self.pdf.stringWidth(git_text)
        self.pdf.drawString(580 - git_text_width, 740, git_text)

        self.lh = 740
        
    def write_section(self, title, save_log_pth, elapsed_time, error):
        if self.cnt >= 3 and self.cnt % 2 == 1:
            self.pdf.showPage() # newpage
            self.lh = 740
            
        self.pdf.setFont("맑은고딕_볼드", 12)
        subtitle_text = f"{self.cnt}. {title}"
        self.lh -= 40
        self.pdf.drawString(30, self.lh, subtitle_text)
        
        self.pdf.setFont("맑은고딕", 9)
        text = f"• 해석 시간: {elapsed_time:.5f}초"
        self.lh -= 15        
        self.pdf.drawString(30, self.lh, text)
        self.lh -= 15
        if error:
            error_text = f"• 오차율: {error:.3f}%"
            self.pdf.drawString(30, self.lh, error_text)

        if "dambreak" in title.replace("_", "").lower():
            self.lh -= 200
            self.pdf.drawImage(os.path.join(save_log_pth, "graph_p1.png"), (self.width // 2)-260, self.lh, width=240, height=180)
            self.pdf.drawImage(os.path.join(save_log_pth, "graph_p3.png"), (self.width // 2)+20, self.lh, width=240, height=180)
            self.pdf.setFont("맑은고딕_볼드", 9)
            self.lh -= 15
            self.pdf.drawString((self.width // 2)-260+120-self.pdf.stringWidth('P1'), self.lh, 'P1')
            self.pdf.drawString((self.width // 2)+20+120-self.pdf.stringWidth('P3'), self.lh, 'P3')
        else:
            self.lh -= 200
            self.pdf.drawImage(os.path.join(save_log_pth, "graph.png"), (self.width // 2)-120, self.lh, width=240, height=180)
        
        self.cnt += 1
        
    def save(self):
        self.pdf.save()