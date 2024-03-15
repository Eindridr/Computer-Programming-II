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
		self._label1 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(12, 60)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(60, 23)
		self._button1.TabIndex = 1
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Location = System.Drawing.Point(79, 60)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(61, 23)
		self._button2.TabIndex = 2
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.Location = System.Drawing.Point(146, 60)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(60, 23)
		self._button3.TabIndex = 3
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = True
		self._button3.Click += self.Button3Click
		# 
		# label1
		# 
		self._label1.Location = System.Drawing.Point(13, 27)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(193, 30)
		self._label1.TabIndex = 4
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(13, 4)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(193, 20)
		self._textBox1.TabIndex = 5
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(218, 84)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "pg272"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		x = int(self._textBox1.Text)
		a = .07
		b = .12
		c = .05
		self._label1.Text = "Day:" + str(a*x) + "\t" + "Afternoon:" + str(b*x) + "\t" + "Midnight" + str(c*x)

	def Button2Click(self, sender, e):
		self._label1.Text = ""

	def Button3Click(self, sender, e):
		Application.Exit()