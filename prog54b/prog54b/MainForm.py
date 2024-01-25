import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._label1 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._textBox3 = System.Windows.Forms.TextBox()
		self._textBox4 = System.Windows.Forms.TextBox()
		self._label2 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.DarkKhaki
		self._label1.Location = System.Drawing.Point(63, 28)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(89, 33)
		self._label1.TabIndex = 0
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.DarkKhaki
		self._button1.Location = System.Drawing.Point(2, 12)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(10, 10)
		self._button1.TabIndex = 1
		self._button1.Text = "button1"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.DarkKhaki
		self._button2.Location = System.Drawing.Point(18, 12)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(10, 10)
		self._button2.TabIndex = 2
		self._button2.Text = "button2"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.DarkKhaki
		self._button3.Location = System.Drawing.Point(34, 12)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(10, 10)
		self._button3.TabIndex = 3
		self._button3.Text = "button3"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# textBox1
		# 
		self._textBox1.BackColor = System.Drawing.Color.DarkKhaki
		self._textBox1.Location = System.Drawing.Point(2, 28)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(42, 20)
		self._textBox1.TabIndex = 4
		# 
		# textBox2
		# 
		self._textBox2.BackColor = System.Drawing.Color.DarkKhaki
		self._textBox2.Location = System.Drawing.Point(2, 104)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(42, 20)
		self._textBox2.TabIndex = 5
		# 
		# textBox3
		# 
		self._textBox3.BackColor = System.Drawing.Color.DarkKhaki
		self._textBox3.Location = System.Drawing.Point(2, 54)
		self._textBox3.Name = "textBox3"
		self._textBox3.Size = System.Drawing.Size(42, 20)
		self._textBox3.TabIndex = 6
		# 
		# textBox4
		# 
		self._textBox4.BackColor = System.Drawing.Color.DarkKhaki
		self._textBox4.Location = System.Drawing.Point(2, 78)
		self._textBox4.Name = "textBox4"
		self._textBox4.Size = System.Drawing.Size(42, 20)
		self._textBox4.TabIndex = 7
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.DarkKhaki
		self._label2.Location = System.Drawing.Point(63, 78)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(89, 33)
		self._label2.TabIndex = 8
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.Indigo
		self.ClientSize = System.Drawing.Size(163, 144)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._textBox4)
		self.Controls.Add(self._textBox3)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "prog54b"
		self.ResumeLayout(False)
		self.PerformLayout()
                                        

	def Button1Click(self, sender, e):
		num1 = int(self._textBox1.Text)
		num2 = int(self._textBox2.Text)
		num3 = int(self._textBox3.Text)
		num4 = int(self._textBox4.Text)
		sum = num1 + num2 + num3 + num4
		avg = sum/4
		self._label1.Text = str(sum)
		self._label2.Text = str(avg)

	def Button2Click(self, sender, e):
		self._textBox1.Text = ""
		self._textBox2.Text = ""
		self._textBox4.Text = ""
		self._textBox3.Text = ""
		self._label2.Text = ""
		self._label1.Text = ""

	def Button3Click(self, sender, e):
		Application.Exit()