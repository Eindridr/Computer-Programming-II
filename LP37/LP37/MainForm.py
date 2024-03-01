import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._textBox1 = System.Windows.Forms.TextBox()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._label1 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# textBox1
		# 
		self._textBox1.BackColor = System.Drawing.Color.DarkViolet
		self._textBox1.Font = System.Drawing.Font("Comic Sans MS", 11.25, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.Location = System.Drawing.Point(176, 69)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 28)
		self._textBox1.TabIndex = 0
		# 
		# button1
		# 
		self._button1.Font = System.Drawing.Font("Comic Sans MS", 11.25, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(13, 25)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(75, 23)
		self._button1.TabIndex = 1
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Font = System.Drawing.Font("Comic Sans MS", 11.25, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(81, 87)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(75, 23)
		self._button2.TabIndex = 2
		self._button2.Text = "Exit"
		self._button2.UseVisualStyleBackColor = True
		# 
		# button3
		# 
		self._button3.Font = System.Drawing.Font("Comic Sans MS", 11.25, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(66, 37)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(75, 23)
		self._button3.TabIndex = 3
		self._button3.Text = "Clear"
		self._button3.UseVisualStyleBackColor = True
		# 
		# textBox2
		# 
		self._textBox2.BackColor = System.Drawing.Color.DarkViolet
		self._textBox2.Font = System.Drawing.Font("Comic Sans MS", 11.25, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox2.Location = System.Drawing.Point(118, 43)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(100, 28)
		self._textBox2.TabIndex = 4
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.Yellow
		self._label1.Font = System.Drawing.Font("Comic Sans MS", 11.25, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(66, 102)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(218, 95)
		self._label1.TabIndex = 5
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.DarkGoldenrod
		self.ClientSize = System.Drawing.Size(260, 189)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._textBox1)
		self.Name = "MainForm"
		self.Text = "LP37"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		num1 = int(self._textBox1.Text)
		num2 = int(self._textBox2.Text)
		from ClLP37 import *
		obj1 = ClLP37(num1, num2)
		obj2 = ClLP37(num2, num1)
		obj1.calc()
		obj2.calc()
		div1 = obj1.getDiv()
		mod1 = obj1.getMod()
		div2, mod2 = obj2.getDivMod()
		self._label1.Text = str(num1) + "/" + str(num2) + "=" + str(div1) + "\n"
		self._label1.Text += str(num1) + "%" + str(num2) + "=" + str(mod1) + "\n"
		self._label1.Text += str(num2) + "/" + str(num1) + "=" + str(div2) + "\n"
		self._label1.Text += str(num2) + "%" + str(num1) + "=" + str(mod2) + "\n"