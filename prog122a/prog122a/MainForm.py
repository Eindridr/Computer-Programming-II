import math
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._button3 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button1 = System.Windows.Forms.Button()
		self._listBox1 = System.Windows.Forms.ListBox()
		self.SuspendLayout()
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.LightCoral
		self._button3.Font = System.Drawing.Font("Comic Sans MS", 8.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(526, 290)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(249, 75)
		self._button3.TabIndex = 7
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.LightCoral
		self._button2.Font = System.Drawing.Font("Comic Sans MS", 8.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(249, 290)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(279, 75)
		self._button2.TabIndex = 6
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.LightCoral
		self._button1.Font = System.Drawing.Font("Comic Sans MS", 8.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(1, 290)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(250, 75)
		self._button1.TabIndex = 5
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# listBox1
		# 
		self._listBox1.BackColor = System.Drawing.Color.LightCoral
		self._listBox1.Font = System.Drawing.Font("Comic Sans MS", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._listBox1.FormattingEnabled = True
		self._listBox1.ItemHeight = 40
		self._listBox1.Location = System.Drawing.Point(1, 3)
		self._listBox1.Name = "listBox1"
		self._listBox1.Size = System.Drawing.Size(774, 284)
		self._listBox1.TabIndex = 4
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(776, 365)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._listBox1)
		self.Name = "MainForm"
		self.Text = "prog122a"
		self.ResumeLayout(False)


	def Button1Click(self, sender, e):
		heading = "Number\t\tSquare\t\tSquare Root"
		self._listBox1.Items.Add(heading)
		for num in range(1, 50+1):
			nsqrd = num**2
			nsqrt = math.sqrt(num)
			msg = str(num) + "\t\t" + str(nsqrd) + "\t\t" + str(round(nsqrt, 4))
			self._listBox1.Items.Add(msg)

	def Button2Click(self, sender, e):
		self._listBox1.Items.Clear()

	def Button3Click(self, sender, e):
		Application.Exit()