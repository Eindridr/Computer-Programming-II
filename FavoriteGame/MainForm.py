import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		resources = System.Resources.ResourceManager("FavoriteGame.MainForm", System.Reflection.Assembly.GetEntryAssembly())
		self._button3 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button1 = System.Windows.Forms.Button()
		self._label2 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# button3
		# 
		self._button3.Location = System.Drawing.Point(191, 194)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(86, 60)
		self._button3.TabIndex = 8
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = True
		self._button3.Click += self.Button3Click
		# 
		# button2
		# 
		self._button2.Location = System.Drawing.Point(101, 194)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(84, 60)
		self._button2.TabIndex = 7
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(8, 194)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(87, 60)
		self._button1.TabIndex = 6
		self._button1.Text = "Show"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# label2
		# 
		self._label2.Font = System.Drawing.Font("Comic Sans MS", 26.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Image = resources.GetObject("label2.Image")
		self._label2.Location = System.Drawing.Point(27, 7)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(231, 147)
		self._label2.TabIndex = 5
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		self._label2.Click += self.Label2Click
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(284, 261)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label2)
		self.Name = "MainForm"
		self.Text = "FavoriteGame"
		self.ResumeLayout(False)


	def Button1Click(self, sender, e):
		self._label2.Text = "My favorite game is, Lethal Company!"

	def Button2Click(self, sender, e):
		self._label2.Text = ""

	def Button3Click(self, sender, e):
		Application.Exit()