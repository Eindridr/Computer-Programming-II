import System.Drawing
import System.Windows.Forms
import ClLP32

from ClLP32 import *
from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._label1 = System.Windows.Forms.Label()
		self._button3 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button1 = System.Windows.Forms.Button()
		self._textBox1 = System.Windows.Forms.TextBox()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.Yellow
		self._label1.Font = System.Drawing.Font("Comic Sans MS", 11.25, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.ForeColor = System.Drawing.SystemColors.ControlLightLight
		self._label1.Location = System.Drawing.Point(91, 190)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(218, 95)
		self._label1.TabIndex = 11
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.Yellow
		self._button3.Font = System.Drawing.Font("Comic Sans MS", 11.25, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.ForeColor = System.Drawing.SystemColors.ControlLightLight
		self._button3.Location = System.Drawing.Point(152, 132)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(75, 23)
		self._button3.TabIndex = 9
		self._button3.Text = "Clear"
		self._button3.UseVisualStyleBackColor = False
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.Yellow
		self._button2.Font = System.Drawing.Font("Comic Sans MS", 11.25, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.ForeColor = System.Drawing.SystemColors.ControlLightLight
		self._button2.Location = System.Drawing.Point(173, 167)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(75, 23)
		self._button2.TabIndex = 8
		self._button2.Text = "Exit"
		self._button2.UseVisualStyleBackColor = False
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.Yellow
		self._button1.Font = System.Drawing.Font("Comic Sans MS", 11.25, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.ForeColor = System.Drawing.SystemColors.ControlLightLight
		self._button1.Location = System.Drawing.Point(159, 103)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(75, 23)
		self._button1.TabIndex = 7
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# textBox1
		# 
		self._textBox1.BackColor = System.Drawing.Color.Yellow
		self._textBox1.Font = System.Drawing.Font("Comic Sans MS", 11.25, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.ForeColor = System.Drawing.SystemColors.ControlLightLight
		self._textBox1.Location = System.Drawing.Point(138, 69)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(82, 28)
		self._textBox1.TabIndex = 6
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.FromArgb(244, 51, 255)
		self.ClientSize = System.Drawing.Size(278, 310)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._textBox1)
		self.Name = "MainForm"
		self.Text = "LP32"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		num1 = float(self._textBox1.Text)
		price = calc(num1)
		self._label1.Text = "The price is:" + str(price)