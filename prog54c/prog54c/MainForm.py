import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._label1 = System.Windows.Forms.Label()
		self._webBrowser1 = System.Windows.Forms.WebBrowser()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(12, 89)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(75, 23)
		self._button1.TabIndex = 0
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Location = System.Drawing.Point(93, 89)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(75, 23)
		self._button2.TabIndex = 1
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.Location = System.Drawing.Point(175, 89)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(75, 23)
		self._button3.TabIndex = 2
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = True
		self._button3.Click += self.Button3Click
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(79, 12)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 20)
		self._textBox1.TabIndex = 3
		# 
		# label1
		# 
		self._label1.Location = System.Drawing.Point(12, 35)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(238, 51)
		self._label1.TabIndex = 4
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# webBrowser1
		# 
		self._webBrowser1.Location = System.Drawing.Point(79, 118)
		self._webBrowser1.MinimumSize = System.Drawing.Size(20, 20)
		self._webBrowser1.Name = "webBrowser1"
		self._webBrowser1.Size = System.Drawing.Size(250, 250)
		self._webBrowser1.TabIndex = 5
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(393, 371)
		self.Controls.Add(self._webBrowser1)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "prog54c"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		rad = int(self._textBox1.Text)
		pi = 3.14159
		di = rad * 2
		area = rad**2 * pi
		area = round(area, 2)
		self._label1.Text = ("The radius is:" + str(rad) + "\t" + "The diameter is:" + str(di) + "\t" + "The area is:" + str(area))

	def Button2Click(self, sender, e):
		self._label1.Text = ""
		self._textBox1.Text = ""

	def Button3Click(self, sender, e):
		Application.Exit()