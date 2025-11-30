import tkinter as tk
from tkinter import messagebox
import math

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Máy Tính Cầm Tay")
        self.root.geometry("400x600")
        self.root.resizable(False, False)
        self.root.configure(bg="#1e1e1e")
        
        self.expression = ""
        self.result = ""
        
        self.create_widgets()
        
        self.root.bind('<Key>', self.key_press)
        
    def create_widgets(self):
        display_frame = tk.Frame(self.root, bg="#1e1e1e")
        display_frame.pack(pady=20, padx=20, fill="both")
        
        self.expression_label = tk.Label(
            display_frame,
            text="",
            font=("Arial", 16),
            bg="#2d2d2d",
            fg="#888888",
            anchor="e",
            padx=10,
            pady=5
        )
        self.expression_label.pack(fill="both")
        
        self.result_label = tk.Label(
            display_frame,
            text="0",
            font=("Arial", 32, "bold"),
            bg="#2d2d2d",
            fg="#ffffff",
            anchor="e",
            padx=10,
            pady=10
        )
        self.result_label.pack(fill="both")
        
        buttons_frame = tk.Frame(self.root, bg="#1e1e1e")
        buttons_frame.pack(pady=10, padx=20, fill="both", expand=True)
        
        buttons = [
            ('C', 0, 0, 1, '#ff6b6b'), ('⌫', 0, 1, 1, '#ff6b6b'), 
            ('%', 0, 2, 1, '#4ecdc4'), ('÷', 0, 3, 1, '#4ecdc4'),
            
            ('√', 1, 0, 1, '#4ecdc4'), ('x²', 1, 1, 1, '#4ecdc4'),
            ('1/x', 1, 2, 1, '#4ecdc4'), ('×', 1, 3, 1, '#4ecdc4'),
            
            ('7', 2, 0, 1, '#383838'), ('8', 2, 1, 1, '#383838'),
            ('9', 2, 2, 1, '#383838'), ('-', 2, 3, 1, '#4ecdc4'),
            
            ('4', 3, 0, 1, '#383838'), ('5', 3, 1, 1, '#383838'),
            ('6', 3, 2, 1, '#383838'), ('+', 3, 3, 1, '#4ecdc4'),
            
            ('1', 4, 0, 1, '#383838'), ('2', 4, 1, 1, '#383838'),
            ('3', 4, 2, 1, '#383838'), ('=', 4, 3, 2, '#00b894'),
            
            ('±', 5, 0, 1, '#383838'), ('0', 5, 1, 1, '#383838'),
            ('.', 5, 2, 1, '#383838'),
        ]
        
        for (text, row, col, rowspan, color) in buttons:
            btn = tk.Button(
                buttons_frame,
                text=text,
                font=("Arial", 18, "bold"),
                bg=color,
                fg="white",
                border=0,
                cursor="hand2",
                command=lambda t=text: self.on_button_click(t)
            )
            btn.grid(row=row, column=col, rowspan=rowspan, 
                    sticky="nsew", padx=3, pady=3)
            

            btn.bind("<Enter>", lambda e, b=btn: self.on_hover(b, True))
            btn.bind("<Leave>", lambda e, b=btn: self.on_hover(b, False))
        

        for i in range(6):
            buttons_frame.grid_rowconfigure(i, weight=1)
        for i in range(4):
            buttons_frame.grid_columnconfigure(i, weight=1)
    
    def lighten_color(self, color):
        color_map = {
            '#ff6b6b': '#ff8a8a',
            '#4ecdc4': '#6dddd4',
            '#00b894': '#00d9aa',
            '#383838': '#505050'
        }
        return color_map.get(color, color)
    
    def on_button_click(self, char):
        """Xử lý khi nhấn nút"""
        if char == 'C':
            self.clear()
        elif char == '⌫':
            self.backspace()
        elif char == '=':
            self.calculate()
        elif char == '√':
            self.square_root()
        elif char == 'x²':
            self.square()
        elif char == '1/x':
            self.reciprocal()
        elif char == '±':
            self.toggle_sign()
        elif char in ['÷', '×', '-', '+', '%']:
            self.add_operator(char)
        else:
            self.add_to_expression(char)
    
    def clear(self):
        """Xóa toàn bộ"""
        self.expression = ""
        self.result = ""
        self.update_display()
    
    def backspace(self):
        """Xóa ký tự cuối"""
        self.expression = self.expression[:-1]
        self.update_display()
    
    def add_to_expression(self, char):
        """Thêm số hoặc dấu chấm vào biểu thức"""
        self.expression += str(char)
        self.update_display()
    
    def add_operator(self, operator):
        """Thêm phép toán"""
        if self.expression and self.expression[-1] not in ['÷', '×', '-', '+', '%']:
            op_map = {'÷': '/', '×': '*', '-': '-', '+': '+', '%': '%'}
            self.expression += op_map[operator]
            self.update_display()
    
    def calculate(self):
        """Tính toán kết quả"""
        try:
            expr = self.expression.replace('÷', '/').replace('×', '*')
            result = eval(expr)
            self.result = str(result)
            self.expression = str(result)
            self.update_display()
        except ZeroDivisionError:
            messagebox.showerror("Lỗi", "Không thể chia cho 0!")
            self.clear()
        except:
            messagebox.showerror("Lỗi", "Biểu thức không hợp lệ!")
            self.clear()
    
    def square_root(self):
        """Tính căn bậc 2"""
        try:
            if self.expression:
                result = math.sqrt(float(self.expression))
                self.expression = str(result)
                self.update_display()
        except ValueError:
            messagebox.showerror("Lỗi", "Không thể tính căn của số âm!")
        except:
            messagebox.showerror("Lỗi", "Lỗi tính toán!")
    
    def square(self):
        """Tính bình phương"""
        try:
            if self.expression:
                result = float(self.expression) ** 2
                self.expression = str(result)
                self.update_display()
        except:
            messagebox.showerror("Lỗi", "Lỗi tính toán!")
    
    def reciprocal(self):
        try:
            if self.expression:
                result = 1 / float(self.expression)
                self.expression = str(result)
                self.update_display()
        except ZeroDivisionError:
            messagebox.showerror("Lỗi", "Không thể chia cho 0!")
        except:
            messagebox.showerror("Lỗi", "Lỗi tính toán!")
    
    def toggle_sign(self):
        try:
            if self.expression and self.expression != "0":
                if self.expression[0] == '-':
                    self.expression = self.expression[1:]
                else:
                    self.expression = '-' + self.expression
                self.update_display()
        except:
            pass
    
    def update_display(self):
        """Cập nhật màn hình """
        display_expr = self.expression.replace('*', '×').replace('/', '÷')
        self.expression_label.config(text=display_expr)
        
        if self.expression:
            last_num = self.expression.split('/')[-1].split('*')[-1].split('+')[-1].split('-')[-1]
            self.result_label.config(text=last_num if last_num else "0")
        else:
            self.result_label.config(text="0")
    
    def key_press(self, event):
        """Xử lý phím bàn phím"""
        key = event.char
        
        if key.isdigit() or key == '.':
            self.add_to_expression(key)
        elif key in ['+', '-', '*', '/', '%']:
            op_map = {'+': '+', '-': '-', '*': '×', '/': '÷', '%': '%'}
            self.add_operator(op_map[key])
        elif key == '\r' or key == '=':  # Enter
            self.calculate()
        elif event.keysym == 'BackSpace':
            self.backspace()
        elif event.keysym == 'Escape':
            self.clear()

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop() 