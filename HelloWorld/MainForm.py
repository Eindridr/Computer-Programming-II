import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		resources = System.Resources.ResourceManager("HelloWorld.MainForm", System.Reflection.Assembly.GetEntryAssembly())
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.Location = System.Drawing.Point(0, 0)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(100, 23)
		self._label1.TabIndex = 0
		# 
		# label2
		# 
		self._label2.Font = System.Drawing.Font("Comic Sans MS", 26.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Image = resources.GetObject("label2.Image")
		self._label2.Location = System.Drawing.Point(22, 9)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(231, 147)
		self._label2.TabIndex = 1
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		self._label2.Click += self.Label2Click
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(3, 196)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(87, 60)
		self._button1.TabIndex = 2
		self._button1.Text = "Show"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Location = System.Drawing.Point(96, 196)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(84, 60)
		self._button2.TabIndex = 3
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.Location = System.Drawing.Point(186, 196)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(86, 60)
		self._button3.TabIndex = 4
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = True
		self._button3.Click += self.Button3Click
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(274, 261)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label2)
		self.Name = "MainForm"
		self.Text = "HelloWorld"
		self.ResumeLayout(False)


	def Label2Click(self, sender, e):
		pass

	def Button1Click(self, sender, e):
		self._label2.Text = "Hello, World!"

	def Button2Click(self, sender, e):
		self._label2.Text = ""

	def Button3Click(self, sender, e):
		Application.Exit()