import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._listBox1 = System.Windows.Forms.ListBox()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# listBox1
		# 
		self._listBox1.FormattingEnabled = True
		self._listBox1.Location = System.Drawing.Point(13, 13)
		self._listBox1.Name = "listBox1"
		self._listBox1.Size = System.Drawing.Size(259, 160)
		self._listBox1.TabIndex = 0
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(13, 179)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(75, 70)
		self._button1.TabIndex = 1
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Location = System.Drawing.Point(105, 179)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(75, 70)
		self._button2.TabIndex = 2
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.Location = System.Drawing.Point(197, 179)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(75, 70)
		self._button3.TabIndex = 3
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = True
		self._button3.Click += self.Button3Click
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(284, 261)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._listBox1)
		self.Name = "MainForm"
		self.Text = "Prog166e"
		self.ResumeLayout(False)


	def Button1Click(self, sender, e):
		self._listBox.Items.Clear()
		num = 1
		den = 2
		while den <= 15:
			while num < den:
				frac = float(num)/ den
				fstr = str(num) + "/" + str(den)
				self._listBox1.Items.Add(fstr + " = " + str(round(frac, 5)))
				num += 1
			num = 1
			den += 1

	def Button2Click(self, sender, e):
		self._listBox.Items.Clear()

	def Button3Click(self, sender, e):
		Application.Exit()