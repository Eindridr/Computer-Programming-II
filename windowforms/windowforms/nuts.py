



import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class nuts(Form):
	def __init__(self, parent, msg):
		self.InitializeComponent()
		self.myparent = parent
		self.msg = msg
	
	def InitializeComponent(self):
		self._label1 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.Location = System.Drawing.Point(108, 55)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(100, 23)
		self._label1.TabIndex = 0
		self._label1.Text = "label1"
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(108, 82)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(100, 62)
		self._button1.TabIndex = 1
		self._button1.Text = "Show Home Form"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# nuts
		# 
		self.ClientSize = System.Drawing.Size(284, 261)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label1)
		self.Name = "nuts"
		self.Text = "nuts"
		self.FormClosing += self.NutsFormClosing
		self.Load += self.NutsLoad
		self.ResumeLayout(False)


	def Button1Click(self, sender, e):
		self.Close()
		self.myparent.Show()

	def NutsLoad(self, sender, e):
		self._label1.Text = self.msg

	def NutsFormClosing(self, sender, e):
		self.myparent.Show()