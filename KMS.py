# Importing Modules =======================================================================================================================================================================================================================

from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
from subprocess import run
from tkinter import filedialog
import datetime as dt
import sqlite3
import webbrowser
import tempfile
import os



# Login Window =======================================================================================================================================================================================================================

class Login():


	def __init__(self, master):

		# Login Window Configurations

		self.master = master
		self.master.geometry('1350x690+0+0')
		self.master.title('KITS MANAGEMENT SOFTWARE')
		self.master.iconbitmap('kits.ico')
		self.master.configure(background = '#ffffff')


		# Login Variables

		global username
		global password


		# Login Window Widgets

		self.logo = ImageTk.PhotoImage(Image.open("kits.png"))
		self.branding = Label(self.master, image = self.logo, bg = "#ffffff")
		self.branding.grid(row = 0, column = 1, padx = 0, pady = 50)

		self.title = Label(self.master, text = "PERSONNEL AUTHENTICATION", bg = '#ffffff' , font = ('Helvetica', 18, 'bold'))
		self.title.grid(row = 2, column = 1)

		self.loginFrame = Frame(self.master, padx = 30, pady = 30, bd = 1, relief = "ridge")
		self.loginFrame.grid(row = 3, column = 1, padx = 500, pady = 20)

		username = Entry(self.loginFrame, font =('Helvetica', 12))
		username.grid(row = 0, column = 1, padx = 10)
		password = Entry(self.loginFrame, show = "*", font =('Helvetica', 12))
		password.grid(row = 1, column = 1, pady = (10, 0))
		usernameLabel = Label(self.loginFrame, text = "Username", font = ("Helvetica", 12, "bold")).grid(row = 0, column = 0)
		passwordLabel = Label(self.loginFrame, text = "Password", font = ("Helvetica", 12, "bold")).grid(row = 1, column = 0, pady = (10, 0))
		loginButton = Button(self.loginFrame, text = "SIGN IN", width = 22, command = self.gotoWorkspace, bg = "#09383d", fg = "#ffffff", font = ("Helvetica", 10, "bold")).grid(row=2, column = 1, pady = 20)


# Users Authentication Function =======================================================================================================================================================================================================================

	def gotoWorkspace(self):

		# Authentication Variables

		global user
		global passwd
		global secret_word

		user = ['mkamande', 'pom', 'receptionist', 'accountant', 'hr']
		passwd = ['k1ts2020.admin', 'k1ts2020.', 'r3ce7t10n', 'acc0unt1n8', '4_hR']
		secret_word = ['tiempo', 'kaluna', 'bambistone', 'kerida', 'xiyun']


		# Checking Credentials and Assigning Rights

		if username.get() == user[0] and password.get() == passwd[0]:
			self.master.withdraw()
			dashboard = Toplevel(self.master)
			workspaceGUI = Workspace(dashboard)

		elif username.get() == user[1] and password.get() == passwd[1]:
			self.master.withdraw()
			dashboard = Toplevel(self.master)
			workspaceGUI = Workspace(dashboard)

			maintenanceBtn.configure(state = DISABLED)

		elif username.get() == user[2] and password.get() == passwd[2]:
			self.master.withdraw()
			dashboard = Toplevel(self.master)
			workspaceGUI = Workspace(dashboard)

			financesBtn.configure(state = DISABLED)
			personnelBtn.configure(state = DISABLED)
			maintenanceBtn.configure(state = DISABLED)

		elif username.get() == user[3] and password.get() == passwd[3]:
			self.master.withdraw()
			dashboard = Toplevel(self.master)
			workspaceGUI = Workspace(dashboard)

			personnelBtn.configure(state = DISABLED)
			maintenanceBtn.configure(state = DISABLED)

		elif username.get() == user[4] and password.get() == passwd[4]:
			self.master.withdraw()
			dashboard = Toplevel(self.master)
			workspaceGUI = Workspace(dashboard)

			projectsBtn.configure(state = DISABLED)
			productsBtn.configure(state = DISABLED)
			studentsBtn.configure(state = DISABLED)
			financesBtn.configure(state = DISABLED)
			documentsBtn.configure(state = DISABLED)
			maintenanceBtn.configure(state = DISABLED)
			
		else:
			self.warning = Label(self.loginFrame, text = "Incorrect Username or Password !", fg = "red").grid(row = 3, column = 1)


		# Clearing Fields

		username.delete(0, END)
		password.delete(0, END)


# Workspace Window =======================================================================================================================================================================================================================

class Workspace():

	# Workspace Window Configurations

	def __init__(self, master):

		self.master = master
		self.master.geometry('620x690+0+0')
		self.master.title('KITS MANAGEMENT SOFTWARE - Workspace')
		self.master.iconbitmap('kits.ico')
		self.master.configure(background = '#ffffff')


		# Workspace Variables

		global projectsBtn
		global productsBtn
		global studentsBtn
		global financesBtn
		global documentsBtn
		global personnelBtn
		global connectedUser
		global maintenanceBtn

		now = dt.datetime.now()


		# Workspace Widgets

		self.avatar = ImageTk.PhotoImage(Image.open("avatar.png"))
		self.showAvatar = Label(self.master, image = self.avatar, bg = "#ffffff")
		self.showAvatar.grid(row = 0, column = 0, pady = 15, rowspan = 2)
		self.leftPanel = Frame(self.master, bd = 1, padx = 10, pady = 50, bg = "#ffffff", relief = 'ridge')
		self.leftPanel.grid(row = 2, column = 0, padx = 20, pady = 20)
		self.currentUser = Frame(self.master, bd = 1, padx = 1, pady = 2, bg = "#ffffff", relief = 'ridge')
		self.currentUser.grid(row = 0, rowspan = 2, column = 1, padx = 10, pady = 20, sticky = E)
		self.rightPanel = Frame(self.master, bd = 1, padx = 20, pady = 20, bg = "#ffffff", relief = 'flat')
		self.rightPanel.grid(row = 2, column = 1, columnspan = 2, padx = 20, pady = 20)
		self.bottomPanel = Frame(self.master, bd = 1, bg = "#ffffff", relief = 'flat')
		self.bottomPanel.grid(row = 3, column = 1, columnspan = 2, padx = 20, pady = 20)


		connectedUser = Label(self.currentUser, text = str(username.get()), font = ('Helvetica', 12, 'bold'), bg = '#ffffff', fg = '#09383d').grid(row = 0, column = 0, sticky = E)
		loggedInAt = Label(self.master, text = "Logged in on " + str(now), font = ('Helvetica', 8), bg = '#ffffff').grid(row = 1, column = 1, sticky = E)
		self.logoutBtn = Button(self.master, text = "Log out", command = self.signout, width = 7, fg = "#ffffff", bg = "#09383d", bd = 1, relief = "ridge" , font = ('Helvetica', 9, 'bold'))
		self.logoutBtn.grid(row = 0, rowspan = 2, column = 2, pady = 10)

		kms = Label(self.bottomPanel, text = "KMS v1.0", font = ('Helvetica', 11, 'bold'), bg = '#ffffff', fg = '#09383d').grid(row = 0, column = 0, sticky = E)
		space = Label(self.bottomPanel, text = " ", font = ('Helvetica', 12, 'bold'), bg = '#ffffff').grid(row = 1, column = 0, sticky = E)
		
		copyrightBtn = Button(self.master, text = "Powered by KITS SARL " + u"\u00A9" + " 2020 All Rights Reserved.", command = self.gotoWebsite, font = ('Helvetica', 9), bg = '#ffffff', bd = 0).grid(row = 3, column = 0, padx = 20, sticky = "sw")
		
		maintenanceBtn = Button(self.bottomPanel, text = "Maintenance", command = self.gotoMaintenance, width = 15, bd = 1, relief = "ridge" , font = ('Helvetica', 10, 'bold'))
		maintenanceBtn.grid(row = 2, column = 0, sticky = "se")


		# Menu Buttons

		projectsBtn = Button(self.leftPanel, text = "PROJECTS", command = self.gotoProjects, width = 20, fg = "#ffffff", bg = "#09383d", font = ('Helvetica', 14, 'bold'))
		projectsBtn.grid(row = 2, column = 0)
		productsBtn = Button(self.leftPanel, text = "PRODUCTS", command = self.gotoProducts, width = 20, fg = "#ffffff", bg = "#09383d",font = ('Helvetica', 14, 'bold'))
		productsBtn.grid(row = 3, column = 0)
		studentsBtn = Button(self.leftPanel, text = "STUDENTS", command = self.gotoStudents, width = 20, fg = "#ffffff", bg = "#09383d", font = ('Helvetica', 14, 'bold'))
		studentsBtn.grid(row = 4, column = 0)
		financesBtn = Button(self.leftPanel, text = "FINANCES", command = self.gotoFinances, width = 20, fg = "#ffffff", bg = "#09383d", font = ('Helvetica', 14, 'bold'))
		financesBtn.grid(row = 6, column = 0)
		personnelBtn = Button(self.leftPanel, text = "PERSONNEL", command = self.gotoPersonnel, width = 20, fg = "#ffffff", bg = "#09383d", font = ('Helvetica', 14, 'bold'))
		personnelBtn.grid(row = 7, column = 0)
		documentsBtn = Button(self.leftPanel, text = "INVOICES", command = self.gotoDocuments, width = 20, fg = "#ffffff", bg = "#09383d", font = ('Helvetica', 14, 'bold'))
		documentsBtn.grid(row = 5, column = 0)
		self.entertainBtn = Button(self.leftPanel, text = "Game - Space invaders", command = self.gotoEntertain, width = 20, bd = 0, relief = SUNKEN, bg = "#ffffff", fg = "#09383d", font = ('Helvetica', 14, 'bold'))
		self.entertainBtn.grid(row = 8, column = 0, pady = 10)


	# Workspace Buttons Functions

	def gotoProjects(self):
		projects = Toplevel(self.master)
		gui = Projects(projects)

	def gotoProducts(self):
		products = Toplevel(self.master)
		gui = Products(products)

	def gotoStudents(self):
		students = Toplevel(self.master)
		gui = Students(students)

	def gotoFinances(self):
		finances = Toplevel(self.master)
		gui = Finances(finances)

	def gotoPersonnel(self):
		personnel = Toplevel(self.master)
		gui = Personnel(personnel)

	def gotoDocuments(self):
		global invoice
		self.master.filename = filedialog.askopenfilename(initialdir = "D:/Invoice", title = "Select invoice", filetypes = (("Excel Files", "*.xlsx"), ("PDF Files", "*.pdf")))
		os.system("start " + self.master.filename)

	def signout(self):
		response = messagebox.askyesno("CONFIRM...", "Do you want to close the application?")
		if response == 1:
			self.master.quit()

	def gotoEntertain(self):
		run("python space_invaders.py")

	def gotoMaintenance(self):
		maintenance = Toplevel(self.master)
		gui = Maintenance(maintenance)

	def gotoWebsite(self):
		webbrowser.open('https://www.kamande.net')
		

# Projects Window =======================================================================================================================================================================================================================

class Projects():

	# Database Creation or Connection With Table Configuration

	conn = sqlite3.connect('kits_data.db')
	c = conn.cursor()

	c.execute(""" CREATE TABLE IF NOT EXISTS projects(
		title text,
		type text,
		client text,
		contact text,
		cost int,
		paid int,
		remainder int,
		charge int,
		profit int,
		date_ text,
		status text
		)""")



	def __init__(self, master):

		# Projects Window Configuration

		self.master = master
		self.master.geometry('1350x690+0+0')
		self.master.title('KMS - Projects')
		self.master.iconbitmap('kits.ico')
		self.master.configure(background = '#ffffff')


		# Projects Window Widgets


		self.exitBtn = Button(self.master, text = "Close", width = 5, command = self.exit, bg = "#09383d", fg = "#ffffff", font = ('Helvetica', 16, 'bold'))
		self.exitBtn.grid(row = 0, column = 0, pady = 10, sticky = W)

		self.leftPanel = Frame(self.master, padx = 20, pady = 10)
		self.leftPanel.grid(row = 3, column = 0, columnspan = 3, padx = 20, pady = 50)

		self.rightPanel = Frame(self.master, padx = 20, pady = 20)
		self.rightPanel.grid(row = 3, column = 3, rowspan = 15 , columnspan = 6, padx = 20, pady = 30)

		self.clearBtn = Button(self.master, text = "Clear", width = 5, command = self.clear, bg = "#09383d", fg = "#ffffff", font = ('Helvetica', 12, 'bold'))
		self.clearBtn.grid(row = 4, column = 8, ipadx = 14, pady = 10)

		self.newProjectLabel = Label(self.leftPanel, text = "New Project", fg = "#09383d", font = ("Helvetica", 18, "bold"))
		self.newProjectLabel.grid(row = 0, column = 0, columnspan = 2, pady = 10, sticky = W)

		self.titleLabel = Label(self.leftPanel, text = "Title", font =('Helvetica', 12, 'bold')).grid(row = 2, column = 0, sticky = W)
		self.typeLabel = Label(self.leftPanel, text = "Type", font =('Helvetica', 12, 'bold')).grid(row = 3, column = 0, sticky = W)
		self.clientLabel = Label(self.leftPanel, text = "Client", font =('Helvetica', 12, 'bold')).grid(row = 4, column = 0, sticky = W)
		self.contactLabel = Label(self.leftPanel, text = "Contact", font =('Helvetica', 12, 'bold')).grid(row = 5, column = 0, sticky = W)
		self.costLabel = Label(self.leftPanel, text = "Cost", font =('Helvetica', 12, 'bold')).grid(row = 6, column = 0, sticky = W)
		self.paidLabel = Label(self.leftPanel, text = "Paid", font =('Helvetica', 12, 'bold')).grid(row = 7, column = 0, sticky = W)
		self.chargeLabel = Label(self.leftPanel, text = "Charge", font =('Helvetica', 12, 'bold')).grid(row = 9, column = 0, sticky = W)
		self.statusLabel = Label(self.leftPanel, text = "Status", font =('Helvetica', 12, 'bold')).grid(row = 12, column = 0, sticky = W)


		self.note = Label(self.leftPanel, text = "Note: Currency is US dollars ($)", font =('Helvetica', 10)).grid(row = 13, column = 1)
		
		self.typeSelect = StringVar()
		self.typeSelect.set("Select a type")

		self.statusSelect = StringVar()
		self.statusSelect.set("Select a status")

		self.title = Entry(self.leftPanel, width = 25, bd = 1, font = ('Helvetica', 10))
		self.title.grid(row = 2, column = 1)
		self.type = OptionMenu(self.leftPanel, self.typeSelect, "Select a type", "Desktop App", "Desktop App and Graphics", "Digital Marketing", "Graphics", "Infrastructure", "Mobile App" , "Other", "Web App", "Web App and Graphics", "Web App and Mobile App", "Website", "Website and Desktop App", "Website and Graphics", "Website and Mobile App", "Website, Mobile App and Graphics", "Web App, Mobile App and Graphics")
		self.type.grid(row = 3, column = 1)
		self.client = Entry(self.leftPanel, width = 25, bd = 1, font = ('Helvetica', 10))
		self.client.grid(row = 4, column = 1)
		self.contact = Entry(self.leftPanel, width = 25, bd = 1, font = ('Helvetica', 10))
		self.contact.grid(row = 5, column = 1)
		self.cost = Entry(self.leftPanel, width = 25, bd = 1, font = ('Helvetica', 10))
		self.cost.grid(row = 6, column = 1)
		self.paid = Entry(self.leftPanel, width = 25, bd = 1, font = ('Helvetica', 10))
		self.paid.grid(row = 7, column = 1)
		self.charge = Entry(self.leftPanel, width = 25, bd = 1, font = ('Helvetica', 10))
		self.charge.grid(row = 9, column = 1)
		self.status = OptionMenu(self.leftPanel, self.statusSelect, "Off", "In Progress", "Cancelled" ,"Completed")
		self.status.grid(row = 12, column = 1)

		self.saveBtn = Button(self.leftPanel, text = "Save", command = self.save , width = 17, font = ("Helvetica", 12, "bold"), bg = "#09383d", fg = "#ffffff")
		self.saveBtn.grid(row = 14, column = 1, pady = 10)


		# Navigation Buttons

		self.projects = Button(self.master, text = "Projects", command = self.query_all, width = 15, font = ("Helvetica", 12, "bold"), bg = "#09383d", fg = "#ffffff")
		self.projects.grid(row = 1, column = 3)
		self.completed = Button(self.master, text = "Completed", command = self.query_completed, width = 15, font = ("Helvetica", 12, "bold"), bg = "#09383d", fg = "#ffffff")
		self.completed.grid(row = 1, column = 4)
		self.inprogress = Button(self.master, text = "In Progress", command = self.query_inprogress, width = 15, font = ("Helvetica", 12, "bold"), bg = "#09383d", fg = "#ffffff")
		self.inprogress.grid(row = 1, column = 5)
		self.cancelled = Button(self.master, text = "Cancelled",  command = self.query_cancelled,width = 15, font = ("Helvetica", 12, "bold"), bg = "#09383d", fg = "#ffffff")
		self.cancelled.grid(row = 1, column = 6)
		self.update = Button(self.master, text = "Update", command = self.updateWin, width = 15, font = ("Helvetica", 12, "bold"), bg = "#09383d", fg = "#ffffff")
		self.update.grid(row = 1, column = 7)
		self.delete = Button(self.master, text = "Delete", command = self.delete , width = 15, font = ("Helvetica", 12, "bold"), bg = "#09383d", fg = "#ffffff")
		self.delete.grid(row = 1, column = 8)
		self.pendingPayment = Button(self.master, text = "Pending Payment", command = self.query_pendingPayment , width = 15, font = ("Helvetica", 12, "bold"), bg = "#fa1b27", fg = "#ffffff")
		self.pendingPayment.grid(row = 0, column = 3)


		self.searchClient = Button(self.master, text = "Search by Client", command = self.query_byclient, bg = '#ffffff' , font = ("Helvetica", 10))
		self.searchClient.grid(row = 0, column = 7)
		self.searchBox = Entry(self.master, bd = 1, bg = "#f8fafa", relief = SUNKEN)
		self.searchBox.grid(row = 0, column = 8)


		self.projectIDLabel = Label(self.master, text = "Project ID: ", bg = '#ffffff' , font = ("Helvetica", 10))
		self.projectIDLabel.grid(row = 2, column = 7, sticky = E)
		self.projectID = Entry(self.master)
		self.projectID.grid(row = 2, column = 8)


		# Display Area

		self.dataList = Listbox(self.rightPanel, font = ('Helvetica', 9, 'bold'), width = 120, height = 16, bg = "#ffffff")
		self.dataList.grid(row = 0, rowspan = 15, column = 0)

		scrollbarY = Scrollbar(self.rightPanel, command = self.dataList.yview)
		scrollbarY.grid(row = 0, rowspan = 15, column = 1, sticky = 'ns')
		scrollbarX = Scrollbar(self.rightPanel, orient = 'horizontal' , command = self.dataList.xview)
		scrollbarX.grid(row = 16, column = 0, sticky = 'we')
		self.dataList.configure(yscrollcommand = scrollbarY.set, xscrollcommand = scrollbarX.set)

		self.dataList.delete(0, END)


	# Projects Navigation Buttons Functions	

	def save(self):
		
		conn = sqlite3.connect('kits_data.db')
		c = conn.cursor()

		cost = self.cost.get()
		paid = self.paid.get()
		charge = self.charge.get()
		remainder = int(cost) - int(paid)
		profit = int(paid) - int(charge)
		now = dt.datetime.now()


		c.execute("INSERT INTO projects VALUES (:title, :type, :client, :contact, :cost, :paid, :remainder, :charge , :profit, :date_, :status )",
			{
			'title': self.title.get(),
			'type': self.typeSelect.get(),
			'client': self.client.get(),
			'contact': self.contact.get(),
			'cost': self.cost.get(),
			'paid': self.paid.get(),
			'remainder': remainder,
			'charge': self.charge.get(),
			'profit': profit,
			'date_': now,
			'status': self.statusSelect.get() 
			})

		conn.commit()
		conn.close()



		self.title.delete(0, END)
		self.client.delete(0, END)
		self.contact.delete(0, END)
		self.cost.delete(0, END)
		self.paid.delete(0, END)
		self.charge.delete(0, END)
		

		response = messagebox.showinfo('Saved project', 'New project saved successfully !')


	def query_all(self):

		conn = sqlite3.connect('kits_data.db')
		c = conn.cursor()

		c.execute("SELECT *, oid FROM projects")
		projects_records = c.fetchall()
		
		print_projects_records = ''

		self.dataList.delete(0, END)

		self.dataList.insert(END, "PROJECTS"  + "\n" + "\n")
		self.dataList.insert(END, "\n" + "\n")
		self.dataList.insert(END, "Id." + "    " + "Title" + "    " + "Type" + "    " + "Client" + "    " + "Contact" + "    " + "Cost" + "    " + "Paid" + "    "  + "Status" + "    " + "Date of subscription" + "    "  + "\n" + "\n")
		self.dataList.insert(END, "\n" + "\n")	

		for record in projects_records:
			self.dataList.insert(END, str(record[11])+ "    " + str(record[0]) + "    " + str(record[1]) + "    " + str(record[2]) + "    " + str(record[3]) + "    " + str(record[4]) + "    " + str(record[5]) + "    "  + str(record[10]) + "    " + str(record[9])+ "    "  + "\n")


		conn.commit()
		conn.close()


	def query_completed(self):

		conn = sqlite3.connect('kits_data.db')
		c = conn.cursor()

		c.execute("SELECT *, oid FROM projects WHERE status = 'Completed' ")
		projects_records = c.fetchall()
		
		print_projects_records = ''

		self.dataList.delete(0, END)

		self.dataList.insert(END, "PROJECTS  |  Completed")
		self.dataList.insert(END, "\n" + "\n")
		self.dataList.insert(END, "Id." + "    " + "Title" + "    " + "Type" + "    " + "Client" + "    " + "Contact" + "    " + "Cost" + "    " + "Paid" + "    "  + "Status")
		self.dataList.insert(END, "\n" + "\n")	

		for record in projects_records:
			self.dataList.insert(END, str(record[11])+ "    " + str(record[0]) + "    " + str(record[1]) + "    " + str(record[2]) + "    " + str(record[3]) + "    " + str(record[4]) + "    " + str(record[5]) + "    "  + str(record[10]) + "\n")


		conn.commit()
		conn.close()


	def query_inprogress(self):

		conn = sqlite3.connect('kits_data.db')
		c = conn.cursor()

		c.execute("SELECT *, oid FROM projects WHERE status = 'In Progress' ")
		projects_records = c.fetchall()
		
		print_projects_records = ''

		self.dataList.delete(0, END)

		self.dataList.insert(END, "PROJECTS  |  In Progress")
		self.dataList.insert(END, "\n" + "\n")
		self.dataList.insert(END, "Id." + "    " + "Title" + "    " + "Type" + "    " + "Client" + "    " + "Contact" + "    " + "Cost" + "    " + "Paid" + "    "  + "Status")
		self.dataList.insert(END, "\n" + "\n")	

		for record in projects_records:
			self.dataList.insert(END, str(record[11])+ "    " + str(record[0]) + "    " + str(record[1]) + "    " + str(record[2]) + "    " + str(record[3]) + "    " + str(record[4]) + "    " + str(record[5]) + "    "  + str(record[10]) + "    " + "\n")


		conn.commit()
		conn.close()


	def query_cancelled(self):

		conn = sqlite3.connect('kits_data.db')
		c = conn.cursor()

		c.execute("SELECT *, oid FROM projects WHERE status = 'Cancelled' ")
		projects_records = c.fetchall()
		
		print_projects_records = ''

		self.dataList.delete(0, END)

		self.dataList.insert(END, "PROJECTS  |  Cancelled")
		self.dataList.insert(END, "\n" + "\n")
		self.dataList.insert(END, "Id." + "    " + "Title" + "    " + "Type" + "    " + "Client" + "    " + "Contact" + "    " + "Cost" + "    " + "Paid" + "    "  + "Status")
		self.dataList.insert(END, "\n" + "\n")	

		for record in projects_records:
			self.dataList.insert(END, str(record[11])+ "    " + str(record[0]) + "    " + str(record[1]) + "    " + str(record[2]) + "    " + str(record[3]) + "    " + str(record[4]) + "    " + str(record[5]) + "    "  + str(record[10]) + "    " + "\n")


		conn.commit()
		conn.close()


	def query_byclient(self):

		conn = sqlite3.connect('kits_data.db')
		c = conn.cursor()

		search = self.searchBox.get()

		c.execute("SELECT *, oid FROM projects WHERE client = ?", (search,))
		projects_records = c.fetchall()
		
		print_projects_records = ''

		self.dataList.delete(0, END)

		self.dataList.insert(END, "PROJECTS")
		self.dataList.insert(END, "\n" + "\n")
		self.dataList.insert(END, "Id." + "    " + "Title" + "    " + "Type" + "    " + "Client" + "    " + "Contact" + "    " + "Cost" + "    " + "Paid" + "    "  + "Status" + "    " + "Date of subscription")
		self.dataList.insert(END, "\n" + "\n")	

		for record in projects_records:
			self.dataList.insert(END, str(record[11])+ "    " + str(record[0]) + "    " + str(record[1]) + "    " + str(record[2]) + "    " + str(record[3]) + "    " + str(record[4]) + "    " + str(record[5]) + "    "  + str(record[10]) + "    " + str(record[9])+ "    "  + "\n")


		conn.commit()
		conn.close()

		self.searchBox.delete(0, END)


	def query_pendingPayment(self):

		conn = sqlite3.connect('kits_data.db')
		c = conn.cursor()

		c.execute("SELECT *, oid FROM projects WHERE remainder > 0 ")
		projects_records = c.fetchall()
		
		print_projects_records = ''

		self.dataList.delete(0, END)

		self.dataList.insert(END, "PROJECTS  |  Pending payment")
		self.dataList.insert(END, "\n" + "\n")
		self.dataList.insert(END, "Id." + "    " + "Title" + "    " + "Type" + "    " + "Client" + "    " + "Contact" + "    " + "Cost" + "    " + "Paid" + "    "  + "Status")
		self.dataList.insert(END, "\n" + "\n")

		for record in projects_records:
			self.dataList.insert(END, str(record[11])+ "    " + str(record[0]) + "    " + str(record[1]) + "    " + str(record[2]) + "    " + str(record[3]) + "    " + str(record[4]) + "    " + str(record[5]) + "    "  + str(record[10]) + "    " + "\n")


		conn.commit()
		conn.close()

	
	def updateWin(self):

		global project_id

		editor = Toplevel(self.master)
		gui = Updateproject(editor)
		
		conn = sqlite3.connect('kits_data.db')
		c = conn.cursor()

		project_id = self.projectID.get()

		c.execute("SELECT * from projects WHERE oid = ?", (project_id,))

		records = c.fetchall()


		for record in records:
			titleEditor.insert(0, record[0])
			typeSelectEditor.set(record[1])
			clientEditor.insert(0, record[2])
			contactEditor.insert(0, record[3])
			costEditor.insert(0, record[4])
			paidEditor.insert(0, record[5])
			chargeEditor.insert(0, record[7])
			statusSelectEditor.set(record[10])
	

		conn.commit()
		conn.close()

		self.projectID.delete(0, END)
		

	def delete(self):

		response = messagebox.askyesno('Delete Record', 'Do you want to delete this record?')
		if response == 1:
			conn = sqlite3.connect('kits_data.db')
			c = conn.cursor()

			c.execute("DELETE from projects WHERE oid = " + self.projectID.get())

			self.projectID.delete(0, END)

			
			conn.commit()
			conn.close()
			response = messagebox.showinfo('Delete Record', 'Record deleted successfully!')


	def clear(self):

		self.dataList.delete(0, END)


	def exit(self):

		self.master.destroy()


	conn.commit()
	conn.close()


# Update Projects Window =======================================================================================================================================================================================================================

class Updateproject():


	def __init__(self, master):

		self.master = master
		self.master.geometry('290x300+500+300')
		self.master.title('KMS - Update Project')
		self.master.iconbitmap('kits.ico')

		global titleEditor
		global typeSelectEditor
		global clientEditor
		global contactEditor
		global costEditor
		global paidEditor
		global chargeEditor
		global statusSelectEditor


		def update():
			
			conn = sqlite3.connect('kits_data.db')
			c = conn.cursor()

			pid = project_id

			cost = costEditor.get()
			paid = paidEditor.get()
			charge = chargeEditor.get()
			remainder = int(cost) - int(paid)
			profit = int(paid) - int(charge)

			c.execute(""" UPDATE projects SET
				title = :title,
				type = :type,
				client = :client,
				contact = :contact,
				cost = :cost,
				paid = :paid,
				remainder = :remainder,
				charge = :charge,
				profit = :profit,
				status = :status,
				date_ = date_
				WHERE oid = :pid """,
				{
				'title': titleEditor.get(),
				'type': typeSelectEditor.get(),
				'client': clientEditor.get(),
				'contact': contactEditor.get(),
				'cost': costEditor.get(),
				'paid': paidEditor.get(),
				'remainder': remainder,
				'charge': chargeEditor.get(),
				'profit': profit,
				'status': statusSelectEditor.get(),
				'pid': pid
				})
	

			conn.commit()
			conn.close()

			self.master.destroy()
			updatemessage = messagebox.showinfo("Update a project", "Project updated successfully!")


		titleLabel = Label(self.master, text = "Title", font =('Helvetica', 12, 'bold')).grid(row = 2, column = 0, sticky = W)
		typeLabel = Label(self.master, text = "Type", font =('Helvetica', 12, 'bold')).grid(row = 3, column = 0, sticky = W)
		clientLabel = Label(self.master, text = "Client", font =('Helvetica', 12, 'bold')).grid(row = 4, column = 0, sticky = W)
		contactLabel = Label(self.master, text = "Contact", font =('Helvetica', 12, 'bold')).grid(row = 5, column = 0, sticky = W)
		costLabel = Label(self.master, text = "Cost", font =('Helvetica', 12, 'bold')).grid(row = 6, column = 0, sticky = W)
		paidLabel = Label(self.master, text = "Paid", font =('Helvetica', 12, 'bold')).grid(row = 7, column = 0, sticky = W)
		chargeLabel = Label(self.master, text = "Charge", font =('Helvetica', 12, 'bold')).grid(row = 9, column = 0, sticky = W)
		statusLabel = Label(self.master, text = "Status", font =('Helvetica', 12, 'bold')).grid(row = 12, column = 0, sticky = W)

		note = Label(self.master, text = "Note: Currency is US dollars ($)", font =('Helvetica', 10)).grid(row = 13, column = 1)
		
		typeSelectEditor = StringVar()
		typeSelectEditor.set("Select a type")

		statusSelectEditor = StringVar()
		statusSelectEditor.set("Select a status")

		titleEditor = Entry(self.master, width = 25, bd = 1, font = ('Helvetica', 10))
		titleEditor.grid(row = 2, column = 1)
		typeEditor = OptionMenu(self.master, typeSelectEditor, "Select a type", "Other", "Desktop App", "Desktop App and Graphics", "Digital Marketing", "Graphics", "Infrastructure", "Mobile App" , "Web App", "Web App and Graphics", "Web App and Mobile App", "Website", "Website and Desktop App", "Website and Graphics", "Website and Mobile App", "Website, Mobile App and Graphics", "Web App, Mobile App and Graphics")
		typeEditor.grid(row = 3, column = 1)
		clientEditor = Entry(self.master, width = 25, bd = 1, font = ('Helvetica', 10))
		clientEditor.grid(row = 4, column = 1)
		contactEditor = Entry(self.master, width = 25, bd = 1, font = ('Helvetica', 10))
		contactEditor.grid(row = 5, column = 1)
		costEditor = Entry(self.master, width = 25, bd = 1, font = ('Helvetica', 10))
		costEditor.grid(row = 6, column = 1)
		paidEditor = Entry(self.master, width = 25, bd = 1, font = ('Helvetica', 10))
		paidEditor.grid(row = 7, column = 1)
		chargeEditor = Entry(self.master, width = 25, bd = 1, font = ('Helvetica', 10))
		chargeEditor.grid(row = 9, column = 1)
		statusEditor = OptionMenu(self.master, statusSelectEditor, "Select a status", "In Progress", "Cancelled" ,"Completed")
		statusEditor.grid(row = 12, column = 1)

		updateBtn = Button(self.master, text = "Update", command = update , width = 17, font = ("Helvetica", 12, "bold"), bg = "#09383d", fg = "#ffffff")
		updateBtn.grid(row = 14, column = 1, pady = 10)



# Products Window =======================================================================================================================================================================================================================

class Products():

	conn = sqlite3.connect('kits_data.db')
	c = conn.cursor()

	c.execute(""" CREATE TABLE IF NOT EXISTS products(
		product_name text,
		category text,
		stock int,
		price int,
		status text,
		created_on text,
		updated_on text
		)""")

	c.execute(""" CREATE TABLE IF NOT EXISTS sales(
		client text,
		mobile int,
		product text,
		quantity int,
		cost int,
		date_ text
		)""")


	def __init__(self, master):

		# Window Configuration

		self.master = master
		self.master.geometry('1350x690+0+0')
		self.master.title('KMS - Products')
		self.master.iconbitmap('kits.ico')
		self.master.configure(background = '#ffffff')


		# Products Window Widgets

		self.exitBtn = Button(self.master, text = "Close", width = 5, command = self.exit, bg = "#09383d", fg = "#ffffff", font = ('Helvetica', 16, 'bold'))
		self.exitBtn.grid(row = 0, column = 0, pady = 10, sticky = W)

		self.left = Frame(self.master)
		self.left.grid(row = 3, column = 0, columnspan = 2, padx = 20, pady = 20)

		self.leftPanel = Frame(self.left, padx = 5, pady = 10)
		self.leftPanel.grid(row = 3, column = 0, columnspan = 3, padx = 20)

		self.leftLower = Frame(self.left, padx = 5, pady = 10)
		self.leftLower.grid(row = 4, column = 0, columnspan = 3, padx = 20)

		self.rightPanel = Frame(self.master, padx = 20, pady = 20)
		self.rightPanel.grid(row = 3, column = 3, rowspan = 10 , columnspan = 6, padx = 20, pady = 10)

		self.clearBtn = Button(self.master, text = "Clear", width = 5, command = self.clear, bg = "#09383d", fg = "#ffffff", font = ('Helvetica', 12, 'bold'))
		self.clearBtn.grid(row = 5, column = 8, ipadx = 14)

		self.newSaleLabel = Label(self.leftPanel, text = "Sell a product", fg = "#09383d", font = ("Helvetica", 18, "bold"))
		self.newSaleLabel.grid(row = 0, column = 0, columnspan = 2, pady = 1, sticky = W)

		self.productsList = Listbox(self.leftPanel, selectmode = MULTIPLE , font = ('Helvetica', 10, 'bold'), width = 30, height = 5, bg = "#ffffff")
		self.productsList.grid(row = 4, column = 1, pady = 10)

		scrollproducts = Scrollbar(self.leftPanel, command = self.productsList.yview)
		scrollproducts.grid(row = 4, column = 2, sticky = 'ns')
		self.productsList.configure(yscrollcommand = scrollproducts.set)

		self.id_ofProductLabel = Label(self.leftPanel, text = "Id no.", font = ('Helvetica', 12, 'bold')).grid(row = 5, column = 0)
		self.id_ofProduct = Entry(self.leftPanel, width = 25, bd = 1, font = ('Helvetica', 10))
		self.id_ofProduct.grid(row = 5, column = 1)

		self.selectProductBtn = Button(self.leftPanel, text = "Select product", command = self.selectProduct , width = 17, font = ("Helvetica", 12, "bold"), bg = "#09383d", fg = "#ffffff")
		self.selectProductBtn.grid(row = 7, column = 1, pady = 10)


		# Retrieving products from Database and Displaying Them

		conn = sqlite3.connect('kits_data.db')
		c = conn.cursor()

		c.execute("SELECT *, oid FROM products")
		product_record = c.fetchall()

		self.productsList.insert(END, "Id." + "  " + "Product" + "  " + "Price($)" + "  " + "Stock" + "\n")
		self.productsList.insert(END, "\n")
		
		for product in product_record:
			self.productsList.insert(END, str(product[7]) + "  " + str(product[0]) + "  " + str(product[3]) + "      " + str(product[2]) + "\n")

		conn.commit()
		conn.close()


		self.addProductLabel = Label(self.leftLower, text = "Add a product", fg = "#09383d", font = ("Helvetica", 18, "bold"))
		self.addProductLabel.grid(row = 8, column = 0, columnspan = 2, pady = 7, sticky = W)

		self.product_nameLabel = Label(self.leftLower, text = "Name", font =('Helvetica', 12, 'bold')).grid(row = 9, column = 0, sticky = W)
		self.categoryLabel = Label(self.leftLower, text = "Category", font =('Helvetica', 12, 'bold')).grid(row = 10, column = 0, sticky = W)
		self.stockLabel = Label(self.leftLower, text = "Stock", font =('Helvetica', 12, 'bold')).grid(row = 11, column = 0, sticky = W)
		self.priceLabel = Label(self.leftLower, text = "Price ($)", font =('Helvetica', 12, 'bold')).grid(row = 12, column = 0, sticky = W)
		
		self.categorySelect = StringVar()
		self.categorySelect.set("Choose category")

		self.product_name = Entry(self.leftLower, width = 25, bd = 1, font = ('Helvetica', 10))
		self.product_name.grid(row = 9, column = 1)
		self.category = OptionMenu(self.leftLower, self.categorySelect, "Choose category", "Gadget", "Hardware", "Software", "Web Service", "Other")
		self.category.grid(row = 10, column = 1)
		self.stockbox = Entry(self.leftLower, width = 25, bd = 1, font = ('Helvetica', 10))
		self.stockbox.grid(row = 11, column = 1)
		self.price = Entry(self.leftLower, width = 25, bd = 1, font = ('Helvetica', 10))
		self.price.grid(row = 12, column = 1)
	
		self.addBtn = Button(self.leftLower, text = "Add", command = self.add, font = ("Helvetica", 12, "bold"), bg = "#09383d", fg = "#ffffff")
		self.addBtn.grid(row = 13, column = 1, pady = 10, sticky = E)


		# Products Window Navigation Buttons

		self.sales = Button(self.master, text = "Sales", command = self.query_sales, width = 15, font = ("Helvetica", 12, "bold"), fg = "#fa1b27", bg = "#ffffff", bd = 2, relief = RIDGE)
		self.sales.grid(row = 1, column = 3)
		self.products = Button(self.master, text = "Products", command = self.query_products, width = 15, font = ("Helvetica", 12, "bold"), bg = "#09383d", fg = "#ffffff")
		self.products.grid(row = 1, column = 4)
		self.stock = Button(self.master, text = "Stock", command = self.query_stock, width = 15, font = ("Helvetica", 12, "bold"), bg = "#09383d", fg = "#ffffff")
		self.stock.grid(row = 1, column = 5)
		self.category = Button(self.master, text = "Categories",  command = self.query_categories,width = 15, font = ("Helvetica", 12, "bold"), bg = "#09383d", fg = "#ffffff")
		self.category.grid(row = 1, column = 6)
		self.update = Button(self.master, text = "Update", command = self.updateWin, width = 15, font = ("Helvetica", 12, "bold"), bg = "#09383d", fg = "#ffffff")
		self.update.grid(row = 1, column = 7)
		self.delete = Button(self.master, text = "Delete", command = self.delete , width = 15, font = ("Helvetica", 12, "bold"), bg = "#09383d", fg = "#ffffff")
		self.delete.grid(row = 1, column = 8)


		self.search = Button(self.master, text = "Search", command = self.query, bg = '#ffffff' , font = ("Helvetica", 10))
		self.search.grid(row = 0, column = 7, sticky = E)
		self.searchBox = Entry(self.master, bd = 1, bg = "#f8fafa", relief = SUNKEN)
		self.searchBox.grid(row = 0, column = 8)

		self.productIDLabel = Label(self.master, text = "Product ID: ", bg = '#ffffff' , font = ("Helvetica", 10))
		self.productIDLabel.grid(row = 2, column = 7, sticky = E)
		self.productID = Entry(self.master)
		self.productID.grid(row = 2, column = 8)


		# Display Area

		self.dataList = Listbox(self.rightPanel, font = ('Helvetica', 9, 'bold'), width = 120, height = 16, bg = "#ffffff")
		self.dataList.grid(row = 0, rowspan = 10, column = 0)

		scrollbarY = Scrollbar(self.rightPanel, command = self.dataList.yview)
		scrollbarY.grid(row = 0, rowspan = 15, column = 1, sticky = 'ns')
		scrollbarX = Scrollbar(self.rightPanel, orient = 'horizontal' , command = self.dataList.xview)
		scrollbarX.grid(row = 16, column = 0, sticky = 'we')
		self.dataList.configure(yscrollcommand = scrollbarY.set, xscrollcommand = scrollbarX.set)

		self.dataList.delete(0, END)


	# Products Navigation Buttons Functions

	def selectProduct(self):

		global identifier

		editor = Toplevel(self.master)
		gui = Sellproduct(editor)
		
		conn = sqlite3.connect('kits_data.db')
		c = conn.cursor()

		identifier = self.id_ofProduct.get()

		c.execute("SELECT * from products WHERE oid = ?", (identifier,))

		records = c.fetchall()


		for record in records:
			product.insert(0, record[0])
			status.insert(0, record[4])
			stock.insert(0, record[2])
			cost.insert(0, record[3])

		conn.commit()
		conn.close()

		self.id_ofProduct.delete(0, END)


	def add(self):
		
		conn = sqlite3.connect('kits_data.db')
		c = conn.cursor()

		now = dt.datetime.now()

		stocklevel = self.stockbox.get()

		if int(stocklevel) > 0:
			status = "In Stock"
		else:
			status = "Out of Stock"


		c.execute("INSERT INTO products VALUES (:product_name, :category, :stock, :price, :status, :created_on, :updated_on)",
			{
			'product_name': self.product_name.get(),
			'category': self.categorySelect.get(),
			'stock': self.stockbox.get(),
			'price': self.price.get(),
			'status': status,
			'created_on': now,
			'updated_on': now
			})

		conn.commit()
		conn.close()

		self.product_name.delete(0, END)
		self.stockbox.delete(0, END)
		self.price.delete(0, END)
	

		response = messagebox.showinfo('Add product', 'Product added successfully !')


	def query_sales(self):

		conn = sqlite3.connect('kits_data.db')
		c = conn.cursor()

		c.execute("SELECT *, oid FROM sales")
		sales_records = c.fetchall()

		self.dataList.delete(0, END)

		self.dataList.insert(END, "SALES")
		self.dataList.insert(END, "\n" + "\n")
		self.dataList.insert(END, "Id." + "    " + "Client" + "    " + "Mobile" + "    " + "Product" + "    " + "Qty" + "    " + "Cost" + "    " + "Date and time")
		self.dataList.insert(END, "\n" + "\n")

		for sale in sales_records:
			self.dataList.insert(END, str(sale[6])+ "       " + str(sale[0]) + "       " + str(sale[1]) + "       " + str(sale[2]) + "       " + str(sale[3]) + "       " + str(sale[4]) + "       " + str(sale[5]) + "\n")

		conn.commit()
		conn.close()


	def query_products(self):

		conn = sqlite3.connect('kits_data.db')
		c = conn.cursor()

		c.execute("SELECT *, oid FROM products")
		products_records = c.fetchall()

		self.dataList.delete(0, END)

		self.dataList.insert(END, "PRODUCTS")
		self.dataList.insert(END, "\n" + "\n")
		self.dataList.insert(END, "Id." + "    " + "Product name" + "    " + "Category" + "    " + "Price" + "    " + "Stock" + "    " + "Status" + "    " + "Created On" + "    " + "Updated On")
		self.dataList.insert(END, "\n" + "\n")

		for product in products_records:
			self.dataList.insert(END, str(product[7])+ "       " + str(product[0]) + "       " + str(product[1]) + "       " + str(product[3]) + "       " + str(product[2]) + "       " + str(product[4]) + "       " + str(product[5]) + "        " + str(product[6]) + "\n")

		conn.commit()
		conn.close()


	def query_stock(self):

		conn = sqlite3.connect('kits_data.db')
		c = conn.cursor()

		c.execute("SELECT *, oid FROM products")
		products_records = c.fetchall()

		self.dataList.delete(0, END)

		self.dataList.insert(END, "PRODUCTS  |  Stock Review")
		self.dataList.insert(END, "\n" + "\n")
		self.dataList.insert(END, "Id." + "    " + "Product name" + "    " + "Stock" + "    " + "Status")
		self.dataList.insert(END, "\n" + "\n")

		for product in products_records:
			self.dataList.insert(END, str(product[7])+ "       " + str(product[0]) +  "       " + str(product[2]) + "       " + str(product[4]) + "\n")

		conn.commit()
		conn.close()


	def query_categories(self):

		conn = sqlite3.connect('kits_data.db')
		c = conn.cursor()

		c.execute("SELECT *, oid FROM products")
		products_records = c.fetchall()

		self.dataList.delete(0, END)

		self.dataList.insert(END, "PRODUCTS  |  Categories")
		self.dataList.insert(END, "\n" + "\n")
		self.dataList.insert(END, "Id." + "    " + "Product name" + "    " + "Category")
		self.dataList.insert(END, "\n" + "\n")

		for product in products_records:
			self.dataList.insert(END, str(product[7])+ "       " + str(product[0]) +  "       " + str(product[1]) + "\n")

		conn.commit()
		conn.close()


	def query(self):

		conn = sqlite3.connect('kits_data.db')
		c = conn.cursor()

		search = self.searchBox.get()

		if search == "In Stock" or search == "Out of Stock":
			c.execute("SELECT *, oid FROM products WHERE status = ?", (search,))
			product_records = c.fetchall()

			self.dataList.delete(0, END)

			self.dataList.insert(END, "PRODUCTS  |  Stock Status")
			self.dataList.insert(END, "\n" + "\n")
			self.dataList.insert(END, "Id." + "    " + "Product name" + "    " + "Stock" + "    " + "Status")
			self.dataList.insert(END, "\n" + "\n")

			for record in product_records:
				self.dataList.insert(END, str(record[7])+ "       " + str(record[0]) + "       " + str(record[2]) + "       " + str(record[4]) +  "\n")

		else:

			c.execute("SELECT *, oid FROM sales WHERE product = ?", (search,))
			product_records = c.fetchall()

			self.dataList.delete(0, END)

			self.dataList.insert(END, "PRODUCTS  |  Sold")
			self.dataList.insert(END, "\n" + "\n")
			self.dataList.insert(END, "Id." + "    " + "Client" + "    " + "Mobile" + "    " + "Product" + "    " + "Qty" + "    " + "Cost" + "    " + "Sol On")
			self.dataList.insert(END, "\n" + "\n")

			for record in product_records:
				self.dataList.insert(END, str(record[6])+ "       " + str(record[0]) + "       " + str(record[1]) + "       " + str(record[2]) + "       " + str(record[3]) + "       " + str(record[4]) + "       " + str(record[5]) + "\n")


		conn.commit()
		conn.close()

		self.searchBox.delete(0, END)

	
	def updateWin(self):

		global product_id

		editor = Toplevel(self.master)
		gui = Updateproduct(editor)
		
		conn = sqlite3.connect('kits_data.db')
		c = conn.cursor()

		product_id = self.productID.get()

		c.execute("SELECT * from products WHERE oid = ?", (product_id,))

		records = c.fetchall()


		for record in records:
			product_nameEditor.insert(0, record[0])
			categorySelectEditor.set(record[1])
			stockEditor.insert(0, record[2])
			priceEditor.insert(0, record[3])

		conn.commit()
		conn.close()

		self.productID.delete(0, END)
		

	def delete(self):

		response = messagebox.askyesno('Delete Record', 'Do you want to delete this record?')

		if response == 1:
			conn = sqlite3.connect('kits_data.db')
			c = conn.cursor()

			c.execute("DELETE from products WHERE oid = " + self.productID.get())

			self.productID.delete(0, END)
		
			conn.commit()
			conn.close()

			response = messagebox.showinfo('Delete Record', 'Record deleted successfully!')


	def clear(self):
		self.dataList.delete(0, END)

	def exit(self):
		self.master.destroy()


	conn.commit()
	conn.close()



# Update Product =========================================================================================================================================================================================================================================================================================================================================================

class Updateproduct():

	def __init__(self, master):

		self.master = master
		self.master.geometry('300x170+500+300')
		self.master.title('KMS - Update Product')
		self.master.iconbitmap('kits.ico')

		global product_nameEditor
		global categorySelectEditor
		global stockEditor
		global priceEditor
		global statusEditor


		def update():
			
			conn = sqlite3.connect('kits_data.db')
			c = conn.cursor()

			pid = product_id
			now = dt.datetime.now()

			stocklevel = stockEditor.get()

			if int(stocklevel) > 0:
				status = "In Stock"
			else:
				status = "Out of Stock"


			c.execute(""" UPDATE products SET
				product_name = :product_name,
				category = :category,
				stock = :stock,
				price = :price,
				status = :status,
				updated_on = :updated_on
				WHERE oid = :pid """,
				{
				'product_name': product_nameEditor.get(),
				'category': categorySelectEditor.get(),
				'stock': stockEditor.get(),
				'price': priceEditor.get(),
				'status': status,
				'updated_on': now,
				'pid': pid
				})
	

			conn.commit()
			conn.close()

			self.master.destroy()
			updatemessage = messagebox.showinfo("Updated", "Product updated successfully!")


		product_nameLabel = Label(self.master, text = "Product name", font =('Helvetica', 12, 'bold')).grid(row = 9, column = 0, sticky = W)
		categoryLabel = Label(self.master, text = "Category", font =('Helvetica', 12, 'bold')).grid(row = 10, column = 0, sticky = W)
		stockLabel = Label(self.master, text = "Stock", font =('Helvetica', 12, 'bold')).grid(row = 11, column = 0, sticky = W)
		priceLabel = Label(self.master, text = "Price ($)", font =('Helvetica', 12, 'bold')).grid(row = 12, column = 0, sticky = W)
		
		categorySelectEditor = StringVar()
		categorySelectEditor.set("Choose category")
		statusSelectEditor = StringVar()
		statusSelectEditor.set("In Stock")

		product_nameEditor = Entry(self.master, width = 25, bd = 1, font = ('Helvetica', 10))
		product_nameEditor.grid(row = 9, column = 1)
		categoryEditor = OptionMenu(self.master, categorySelectEditor, "Choose category", "Gadget", "Hardware", "Software", "Web Service", "Other")
		categoryEditor.grid(row = 10, column = 1)
		stockEditor = Entry(self.master, width = 25, bd = 1, font = ('Helvetica', 10))
		stockEditor.grid(row = 11, column = 1)
		priceEditor = Entry(self.master, width = 25, bd = 1, font = ('Helvetica', 10))
		priceEditor.grid(row = 12, column = 1)
	
		updateEditorBtn = Button(self.master, text = "Update", command = update , width = 17, font = ("Helvetica", 12, "bold"), bg = "#09383d", fg = "#ffffff")
		updateEditorBtn.grid(row = 13, column = 1, pady = 10)


# Sell Product Window =========================================================================================================================================================================================================================================================================================================================================================

class Sellproduct():

	def __init__(self, master):

		self.master = master
		self.master.geometry('260x290+500+200')
		self.master.title('KMS - Sell Product')
		self.master.iconbitmap('kits.ico')

		global product
		global status
		global stock
		global cost


		def sell():
			
			conn = sqlite3.connect('kits_data.db')
			c = conn.cursor()

			pid = identifier
			now = dt.datetime.now()

			totalCost = int(cost.get()) * int(quantity.get())

			c.execute("INSERT INTO sales VALUES (:client, :mobile, :product, :quantity, :cost, :date_)",
					{
					'client': client.get(),
					'mobile': mobile.get(),
					'product': product.get(),
					'quantity': quantity.get(),
					'cost': totalCost,
					'date_': now
					})

			stocklevel = int(stock.get()) - int(quantity.get())
			stockvalue = StringVar()

			if int(stocklevel) > 0:
				stockvalue = "In Stock"
			else:
				stockvalue = "Out of Stock"


			c.execute(""" UPDATE products SET
				stock = :stock,
				status = :status
				WHERE oid = :pid """,
				{
				'stock': stocklevel,
				'status': stockvalue,
				'pid': pid
				})
		
			conn.commit()
			conn.close()


			invoice = tempfile.mktemp('Invoice.txt')
			open(invoice, 'w').write('\n\nKITS SARL | Invoice \n\n' + 'DT	:	' + str(now) + '\n\n' + 'Client	:	' + str(client.get()) + '\n' + 'Mobile	:	' + str(mobile.get()) + '\n' + 'Product	:	' + str(product.get()) + '\n' + 'Qty	:	' + str(quantity.get()) + '\n' + 'Cost	:	' + str(totalCost) + ' $\n\n\n' + 'Thank you for visiting us!' + '\n\n' + 'Tel : +243 81 583 60 68 \nAdresse: 19, Comité urbain, Gombe, Kinshasa, RDC')
			os.startfile(invoice, 'print')

			soldmessage = messagebox.showinfo("Sell a product", "Product sold successfully!")

			self.master.destroy()

		productLabel = Label(self.master, text = "Product", font =('Helvetica', 12, 'bold')).grid(row = 9, column = 0, sticky = W)
		statusLabel = Label(self.master, text = "Status", font =('Helvetica', 12, 'bold')).grid(row = 10, column = 0, sticky = W)
		stockLabel = Label(self.master, text = "Stock", font =('Helvetica', 12, 'bold')).grid(row = 11, column = 0, sticky = W)
		costLabel = Label(self.master, text = "Cost ($)", font =('Helvetica', 12, 'bold')).grid(row = 12, column = 0, sticky = W)
		quantityLabel = Label(self.master, text = "Qty", font =('Helvetica', 12, 'bold')).grid(row = 13, column = 0, sticky = W)
		spaceLabel = Label(self.master, text = "  ", font =('Helvetica', 12, 'bold')).grid(row = 14, column = 0, sticky = W)
		clientLabel = Label(self.master, text = "Client", font =('Helvetica', 12, 'bold')).grid(row = 16, column = 0, sticky = W)
		mobileLabel = Label(self.master, text = "Mobile", font =('Helvetica', 12, 'bold')).grid(row = 17, column = 0, sticky = W)

		product = Entry(self.master, width = 25, bd = 1, font = ('Helvetica', 10))
		product.grid(row = 9, column = 1)
		status = Entry(self.master, width = 25, bd = 1, font = ('Helvetica', 10))
		status.grid(row = 10, column = 1)
		cost = Entry(self.master, width = 25, bd = 1, font = ('Helvetica', 10))
		cost.grid(row = 12, column = 1)
		quantity = Entry(self.master, width = 25, bd = 1, font = ('Helvetica', 10))
		quantity.grid(row = 13, column = 1)
		stock = Entry(self.master, width = 25, bd = 1, font = ('Helvetica', 10))
		stock.grid(row = 11, column = 1)

		client = Entry(self.master, width = 25, bd = 1, font = ('Helvetica', 10))
		client.grid(row = 16, column = 1)
		mobile = Entry(self.master, width = 25, bd = 1, font = ('Helvetica', 10))
		mobile.grid(row = 17, column = 1)
	
		sellBtn = Button(self.master, text = "Sell", command = sell , width = 17, font = ("Helvetica", 12, "bold"), bg = "#09383d", fg = "#ffffff")
		sellBtn.grid(row = 18, column = 1, pady = 10)


# Students Window =========================================================================================================================================================================================================================================================================================================================================================

class Students():

	# Database Connection With Tables Creation

	conn = sqlite3.connect('kits_data.db')
	c = conn.cursor()

	c.execute(""" CREATE TABLE IF NOT EXISTS students(
		name text,
		gender text,
		email text,
		mobile int,
		course text,
		length text,
		fees int,
		paid int,
		remainder int,
		date_ text,
		status text,
		certnumber text
		)""")


	def __init__(self, master):

		# Students Window Configuration 

		self.master = master
		self.master.geometry('1350x690+0+0')
		self.master.title('KMS - Students')
		self.master.iconbitmap('kits.ico')
		self.master.configure(background = '#ffffff')


		# Students Window Widgets

		self.exitBtn = Button(self.master, text = "Close", width = 5, command = self.exit, bg = "#09383d", fg = "#ffffff", font = ('Helvetica', 16, 'bold'))
		self.exitBtn.grid(row = 0, column = 0, pady = 10, sticky = W)

		self.leftPanel = Frame(self.master, padx = 20, pady = 20)
		self.leftPanel.grid(row = 3, column = 0, columnspan = 3, padx = 20, pady = 50)

		self.rightPanel = Frame(self.master, padx = 20, pady = 20)
		self.rightPanel.grid(row = 3, column = 3, rowspan = 15 , columnspan = 6, padx = 20, pady = 10)

		self.clearBtn = Button(self.master, text = "Clear", width = 5, command = self.clear, bg = "#09383d", fg = "#ffffff", font = ('Helvetica', 12, 'bold'))
		self.clearBtn.grid(row = 4, column = 8, ipadx = 14)

		self.enrolmentLabel = Label(self.leftPanel, text = "Student Enrolment", fg = "#09383d", font = ("Helvetica", 18, "bold"))
		self.enrolmentLabel.grid(row = 0, column = 0, columnspan = 2, pady = 7, sticky = W)

		self.nameLabel = Label(self.leftPanel, text = "Name", font =('Helvetica', 12, 'bold')).grid(row = 2, column = 0, sticky = W)
		self.genderLabel = Label(self.leftPanel, text = "Gender", font =('Helvetica', 12, 'bold')).grid(row = 3, column = 0, sticky = W)
		self.emailLabel = Label(self.leftPanel, text = "E-mail", font =('Helvetica', 12, 'bold')).grid(row = 4, column = 0, sticky = W)
		self.mobileLabel = Label(self.leftPanel, text = "Mobile", font =('Helvetica', 12, 'bold')).grid(row = 5, column = 0, sticky = W)
		self.courseLabel = Label(self.leftPanel, text = "Course", font =('Helvetica', 12, 'bold')).grid(row = 6, column = 0, sticky = W)
		self.lengthLabel = Label(self.leftPanel, text = "Length", font =('Helvetica', 12, 'bold')).grid(row = 7, column = 0, sticky = W)
		self.feesLabel = Label(self.leftPanel, text = "Fees", font =('Helvetica', 12, 'bold')).grid(row = 8, column = 0, sticky = W)
		self.paidLabel = Label(self.leftPanel, text = "paid", font =('Helvetica', 12, 'bold')).grid(row = 9, column = 0, sticky = W)
		self.statusLabel = Label(self.leftPanel, text = "Status", font =('Helvetica', 12, 'bold')).grid(row = 12, column = 0, sticky = W)

		self.note = Label(self.leftPanel, text = "Note: Currency is US dollars ($)", font =('Helvetica', 10)).grid(row = 14, column = 1)
		
		self.genderSelect = StringVar()
		self.genderSelect.set("Select a gender")

		self.courseSelect = StringVar()
		self.courseSelect.set("Select a course")

		self.statusSelect = StringVar()
		self.statusSelect.set("Select a status")

		self.name = Entry(self.leftPanel, width = 25, bd = 1, font = ('Helvetica', 10))
		self.name.grid(row = 2, column = 1)
		self.gender = OptionMenu(self.leftPanel, self.genderSelect, "Select a gender", "Male", "Female")
		self.gender.grid(row = 3, column = 1)
		self.email = Entry(self.leftPanel, width = 25, bd = 1, font = ('Helvetica', 10))
		self.email.grid(row = 4, column = 1)
		self.mobile = Entry(self.leftPanel, width = 25, bd = 1, font = ('Helvetica', 10))
		self.mobile.grid(row = 5, column = 1)
		self.course = OptionMenu(self.leftPanel, self.courseSelect, "Select a course", "Cisco CCNA RS", "Cisco CCNP", "Cisco Voice", "Cyber Security", "Database Administrator", "Ethical Hacking", "Exchange Server", "Java Developer", "Linux Essentials", "Linux SYSADMIN", "Mobile App Developer", "Oracle Database", "Penetration Testing", "PostgreSQL", "Python", "Software Developer", "SQL Server", "Web Developer", "Webmaster", "Windows Server")
		self.course.grid(row = 6, column = 1)
		self.length = Entry(self.leftPanel, width = 25, bd = 1, font = ('Helvetica', 10))
		self.length.grid(row = 7, column = 1)
		self.fees = Entry(self.leftPanel, width = 25, bd = 1, font = ('Helvetica', 10))
		self.fees.grid(row = 8, column = 1)
		self.paid = Entry(self.leftPanel, width = 25, bd = 1, font = ('Helvetica', 10))
		self.paid.grid(row = 9, column = 1)
		self.status = OptionMenu(self.leftPanel, self.statusSelect, "Select a status", "In Progress", "Cancelled" ,"Completed")
		self.status.grid(row = 12, column = 1)
		
		self.enrollBtn = Button(self.leftPanel, text = "Enroll", command = self.enroll , width = 17, font = ("Helvetica", 12, "bold"), bg = "#09383d", fg = "#ffffff")
		self.enrollBtn.grid(row = 15, column = 1, pady = 10)


		# Students Window Navigation Buttons

		self.students = Button(self.master, text = "Students", command = self.query_all, width = 15, font = ("Helvetica", 12, "bold"), bg = "#09383d", fg = "#ffffff")
		self.students.grid(row = 1, column = 3)
		self.completed = Button(self.master, text = "Completed", command = self.query_completed, width = 15, font = ("Helvetica", 12, "bold"), bg = "#09383d", fg = "#ffffff")
		self.completed.grid(row = 1, column = 4)
		self.inprogress = Button(self.master, text = "In Progress", command = self.query_inprogress, width = 15, font = ("Helvetica", 12, "bold"), bg = "#09383d", fg = "#ffffff")
		self.inprogress.grid(row = 1, column = 5)
		self.cancelled = Button(self.master, text = "Cancelled",  command = self.query_cancelled,width = 15, font = ("Helvetica", 12, "bold"), bg = "#09383d", fg = "#ffffff")
		self.cancelled.grid(row = 1, column = 6)
		self.update = Button(self.master, text = "Update", command = self.updateWin, width = 15, font = ("Helvetica", 12, "bold"), bg = "#09383d", fg = "#ffffff")
		self.update.grid(row = 1, column = 7)
		self.delete = Button(self.master, text = "Delete", command = self.delete , width = 15, font = ("Helvetica", 12, "bold"), bg = "#09383d", fg = "#ffffff")
		self.delete.grid(row = 1, column = 8)
		self.pendingPayment = Button(self.master, text = "Pending Payment", command = self.query_pendingPayment , width = 15, font = ("Helvetica", 12, "bold"), bg = "#fa1b27", fg = "#ffffff")
		self.pendingPayment.grid(row = 0, column = 3)

		self.searchstudent = Button(self.master, text = "Search Student", command = self.query_student, bg = '#ffffff' , font = ("Helvetica", 10))
		self.searchstudent.grid(row = 0, column = 7)
		self.searchBox = Entry(self.master, bd = 1, bg = "#f8fafa", relief = SUNKEN)
		self.searchBox.grid(row = 0, column = 8)

		self.studentIDLabel = Label(self.master, text = "Student ID: ", bg = '#ffffff' , font = ("Helvetica", 10))
		self.studentIDLabel.grid(row = 2, column = 7, sticky = E)
		self.studentID = Entry(self.master)
		self.studentID.grid(row = 2, column = 8)

		# Display Area

		self.dataList = Listbox(self.rightPanel, font = ('Helvetica', 9, 'bold'), width = 120, height = 16, bg = "#ffffff")
		self.dataList.grid(row = 0, rowspan = 15, column = 0)

		scrollbarY = Scrollbar(self.rightPanel, command = self.dataList.yview)
		scrollbarY.grid(row = 0, rowspan = 15, column = 1, sticky = 'ns')
		scrollbarX = Scrollbar(self.rightPanel, orient = 'horizontal' , command = self.dataList.xview)
		scrollbarX.grid(row = 16, column = 0, sticky = 'we')
		self.dataList.configure(yscrollcommand = scrollbarY.set, xscrollcommand = scrollbarX.set)

		self.dataList.delete(0, END)


	def enroll(self):

		global trainingIncome

		conn = sqlite3.connect('kits_data.db')
		c = conn.cursor()

		fees = self.fees.get()
		trainingIncome = self.paid.get()
		remainder = int(fees) - int(trainingIncome)
		now = dt.datetime.now()

		c.execute("INSERT INTO students VALUES (:name, :gender, :email, :mobile, :course, :length, :fees, :paid , :remainder, :date_, :status, :certnumber )",
			{
			'name': self.name.get(),
			'gender': self.genderSelect.get(),
			'email': self.email.get(),
			'mobile': self.mobile.get(),
			'course': self.courseSelect.get(),
			'length': self.length.get(),
			'fees': self.fees.get(),
			'paid': self.paid.get(),
			'remainder': remainder,
			'date_': now,
			'status': self.statusSelect.get(),
			'certnumber': self.certnumber.get() 
			})

		conn.commit()
		conn.close()


		self.name.delete(0, END)
		self.email.delete(0, END)
		self.mobile.delete(0, END)
		self.length.delete(0, END)
		self.fees.delete(0, END)
		self.paid.delete(0, END)
		self.certnumber.delete(0, END)	

		response = messagebox.showinfo('Enrolment', 'Student enrolled successfully !')


	def query_all(self):

		conn = sqlite3.connect('kits_data.db')
		c = conn.cursor()

		c.execute("SELECT *, oid FROM students")
		students_records = c.fetchall()
		

		self.dataList.delete(0, END)

		self.dataList.insert(END, "STUDENTS")
		self.dataList.insert(END, "\n" + "\n")
		self.dataList.insert(END, "Id." + "    " + "Full name" + "    " + "Gender" + "    " + "E-mail" + "    " + "Mobile" + "    " + "Course" + "    " + "Length" + "    " + "Fees" + "    " + "Paid" + "    " + "Remainder" + "    " + "Status" + "    " + "Cert no." + "    " + "Date of enrolment" )
		self.dataList.insert(END, "\n" + "\n")

		for record in students_records:
			self.dataList.insert(END, str(record[12])+ "    " + str(record[0]) + "    " + str(record[1]) + "    " + str(record[2]) + "    " + str(record[3]) + "    " + str(record[4]) + "    "  + str(record[5]) + "    " + str(record[6]) + "    " + str(record[7]) + "    "  + str(record[8]) + "    "  + str(record[10]) + "    "  + str(record[11]) + "    " + str(record[9]) + "\n")

		conn.commit()
		conn.close()


	def query_completed(self):

		conn = sqlite3.connect('kits_data.db')
		c = conn.cursor()

		c.execute("SELECT *, oid FROM students WHERE status = 'Completed' ")
		projects_records = c.fetchall()
		
		self.dataList.delete(0, END)

		self.dataList.insert(END, "STUDENTS  |  Alumni")
		self.dataList.insert(END, "\n" + "\n")
		self.dataList.insert(END, "Id." + "    " + "Full name" + "    " + "Gender" + "    " + "E-mail" + "    " + "Mobile" + "    " + "Course" + "    " + "Status" + "    " + "Cert no.")
		self.dataList.insert(END, "\n" + "\n")

		for record in projects_records:
			self.dataList.insert(END, str(record[12])+ "     " + str(record[0]) + "     " + str(record[1]) + "     " + str(record[2]) + "     " + str(record[3]) + "     " + str(record[4]) + "     "  + str(record[10]) + "     "  + str(record[11]) + "\n")

		conn.commit()
		conn.close()


	def query_inprogress(self):

		conn = sqlite3.connect('kits_data.db')
		c = conn.cursor()

		c.execute("SELECT *, oid FROM students WHERE status = 'In Progress' ")
		projects_records = c.fetchall()
		
		self.dataList.delete(0, END)

		self.dataList.insert(END, "STUDENTS  |  Trainings In Progress")
		self.dataList.insert(END, "\n" + "\n")
		self.dataList.insert(END, "Id." + "    " + "Full name" + "    " + "Gender" + "    " + "E-mail" + "    " + "Mobile" + "    " + "Course" + "    " + "Fees" + "    " + "Paid" + "    " + "Remainder"    + "    " + "Status" + "    " + "Date of enrolment")
		self.dataList.insert(END, "\n" + "\n")

		for record in projects_records:
			self.dataList.insert(END, str(record[12])+ "     " + str(record[0]) + "     " + str(record[1]) + "     " + str(record[2]) + "     " + str(record[3]) + "     " + str(record[4]) + "     " + str(record[6]) + "     " + str(record[7]) + "     "  + str(record[8]) + "     "  + str(record[10])  + "     " + str(record[9]) + "\n")


		conn.commit()
		conn.close()


	def query_cancelled(self):

		conn = sqlite3.connect('kits_data.db')
		c = conn.cursor()

		c.execute("SELECT *, oid FROM students WHERE status = 'Cancelled' ")
		projects_records = c.fetchall()
		
		self.dataList.delete(0, END)

		self.dataList.insert(END, "STUDENTS  |  Cancelled Trainings")
		self.dataList.insert(END, "\n" + "\n")
		self.dataList.insert(END, "Id." + "    " + "Full name" + "    " + "Gender" + "    " + "E-mail" + "    " + "Mobile" + "    " + "Course" + "    " + "Fees" + "    " + "Paid" + "    " + "Remainder"    + "    " + "Status")
		self.dataList.insert(END, "\n" + "\n")

		for record in projects_records:
			self.dataList.insert(END, str(record[12])+ "     " + str(record[0]) + "     " + str(record[1]) + "     " + str(record[2]) + "     " + str(record[3]) + "     " + str(record[4]) +  "     " + str(record[6]) + "     " + str(record[7]) + "     "  + str(record[8]) + "     "  + str(record[10]) + "\n")

		conn.commit()
		conn.close()


	def query_student(self):

		conn = sqlite3.connect('kits_data.db')
		c = conn.cursor()

		search = self.searchBox.get()

		c.execute("SELECT *, oid FROM students WHERE name = ?", (search,))
		projects_records = c.fetchall()
		
		self.dataList.delete(0, END)

		self.dataList.insert(END, "STUDENTS  |  Searched")
		self.dataList.insert(END, "\n" + "\n")
		self.dataList.insert(END, "Id." + "    " + "Full name" + "    " + "Gender" + "    " + "E-mail" + "    " + "Mobile" + "    " + "Course" + "    " + "Fees" + "    " + "Paid" + "    " + "Remainder"    + "    " + "Status" + "    " + "Cert no." + "    " + "Date of enrolment")
		self.dataList.insert(END, "\n" + "\n")

		for record in projects_records:
			self.dataList.insert(END, str(record[12])+ "   " + str(record[0]) + "   " + str(record[1]) + "   " + str(record[2]) + "   " + str(record[3]) + "   " + str(record[4]) + "   "  + str(record[5]) + "   " + str(record[6]) + "   " + str(record[7]) + "   "  + str(record[8]) + "   "  + str(record[10]) + "   "  + str(record[11]) + "   " + str(record[9]) + "\n")

		conn.commit()
		conn.close()

		self.searchBox.delete(0, END)


	def query_pendingPayment(self):

		conn = sqlite3.connect('kits_data.db')
		c = conn.cursor()

		c.execute("SELECT *, oid FROM students WHERE remainder > 0 ")
		projects_records = c.fetchall()
		
		self.dataList.delete(0, END)

		self.dataList.insert(END, "STUDENTS  |  Pending payment")
		self.dataList.insert(END, "\n" + "\n")
		self.dataList.insert(END, "Id." + "    " + "Full name" + "    " + "Mobile" + "    " + "Course" + "    " + "Fees" + "    " + "Paid" + "    " + "Remainder"    + "    " + "Status")
		self.dataList.insert(END, "\n" + "\n")

		for record in projects_records:
			self.dataList.insert(END, str(record[12])+ "     " + str(record[0]) + "     " +  str(record[3]) + "     " + str(record[4]) + "     " + str(record[6]) + "     " + str(record[7]) + "     "  + str(record[8]) + "     "  + str(record[10]) + "\n")

		conn.commit()
		conn.close()

	
	def updateWin(self):

		global student_id

		editor = Toplevel(self.master)
		gui = Updatestudent(editor)
		
		conn = sqlite3.connect('kits_data.db')
		c = conn.cursor()

		student_id = self.studentID.get()

		c.execute("SELECT * from students WHERE oid = ?", (student_id,))

		records = c.fetchall()

		for record in records:
			nameEditor.insert(0, record[0])
			genderSelectEditor.set(record[1])
			emailEditor.insert(0, record[2])
			mobileEditor.insert(0, record[3])
			courseSelectEditor.set(record[4])
			lengthEditor.insert(0, record[5])
			feesEditor.insert(0, record[6])
			paidEditor.insert(0, record[7])
			statusSelectEditor.set(record[10])
			certnumberEditor.insert(0, record[11])
	

		conn.commit()
		conn.close()

		self.studentID.delete(0, END)
		

	def delete(self):

		response = messagebox.askyesno('Delete Record', 'Do you want to delete this student?')

		if response == 1:
			conn = sqlite3.connect('kits_data.db')
			c = conn.cursor()

			c.execute("DELETE from students WHERE oid = " + self.studentID.get())

			self.studentID.delete(0, END)
		
			conn.commit()
			conn.close()

			response = messagebox.showinfo('Delete Record', 'Record deleted successfully!')


	def clear(self):
		self.dataList.delete(0, END)

	def exit(self):
		self.master.destroy()

	conn.commit()
	conn.close()


# Update Student =========================================================================================================================================================================================================================================================================================================================================================	


class Updatestudent():

	def __init__(self, master):

		self.master = master
		self.master.geometry('290x350+500+250')
		self.master.iconbitmap('kits.ico')
		self.master.title('KMS - Update Student')

		global nameEditor
		global genderSelectEditor
		global emailEditor
		global mobileEditor
		global courseSelectEditor
		global lengthEditor
		global feesEditor
		global paidEditor
		global certnumberEditor
		global statusSelectEditor


		def update():
			
			conn = sqlite3.connect('kits_data.db')
			c = conn.cursor()

			sid = student_id

			fees = feesEditor.get()
			trainingIncome = paidEditor.get()
			remainder = int(fees) - int(trainingIncome)
			now = dt.datetime.now()

			c.execute(""" UPDATE students SET
				name = :name,
				gender = :gender,
				email = :email,
				mobile = :mobile,
				course = :course,
				length = :length,
				fees = :fees,
				paid = :paid,
				remainder = :remainder,
				date_ = date_,
				status = :status,
				certnumber = :certnumber
				WHERE oid = :sid """,
				{
				'name': nameEditor.get(),
				'gender': genderSelectEditor.get(),
				'email': emailEditor.get(),
				'mobile': mobileEditor.get(),
				'course': courseSelectEditor.get(),
				'length': lengthEditor.get(),
				'fees': feesEditor.get(),
				'paid': paidEditor.get(),
				'remainder': remainder,
				'status': statusSelectEditor.get(),
				'certnumber': certnumberEditor.get(),
				'sid': sid
				})
	

			conn.commit()
			conn.close()

			self.master.destroy()
			updatemessage = messagebox.showinfo("Updated", "Student updated successfully!")

		nameLabel = Label(self.master, text = "Name", font =('Helvetica', 12, 'bold')).grid(row = 2, column = 0, sticky = W)
		genderLabel = Label(self.master, text = "Gender", font =('Helvetica', 12, 'bold')).grid(row = 3, column = 0, sticky = W)
		emailLabel = Label(self.master, text = "E-mail", font =('Helvetica', 12, 'bold')).grid(row = 4, column = 0, sticky = W)
		mobileLabel = Label(self.master, text = "Mobile", font =('Helvetica', 12, 'bold')).grid(row = 5, column = 0, sticky = W)
		courseLabel = Label(self.master, text = "Course", font =('Helvetica', 12, 'bold')).grid(row = 6, column = 0, sticky = W)
		lengthLabel = Label(self.master, text = "Length", font =('Helvetica', 12, 'bold')).grid(row = 7, column = 0, sticky = W)
		feesLabel = Label(self.master, text = "Fees", font =('Helvetica', 12, 'bold')).grid(row = 8, column = 0, sticky = W)
		paidLabel = Label(self.master, text = "Paid", font =('Helvetica', 12, 'bold')).grid(row = 9, column = 0, sticky = W)
		statusLabel = Label(self.master, text = "Status", font =('Helvetica', 12, 'bold')).grid(row = 12, column = 0, sticky = W)
		certnumberLabel = Label(self.master, text = "Cert no.", font =('Helvetica', 12, 'bold')).grid(row = 13, column = 0, sticky = W)
		
		note = Label(self.master, text = "Note: Currency is US dollars ($)", font =('Helvetica', 10)).grid(row = 14, column = 1)
		
		genderSelectEditor = StringVar()
		genderSelectEditor.set("Select a gender")

		courseSelectEditor = StringVar()
		courseSelectEditor.set("Select a course")

		statusSelectEditor = StringVar()
		statusSelectEditor.set("Select a status")

		nameEditor = Entry(self.master, width = 25, bd = 1, font = ('Helvetica', 10))
		nameEditor.grid(row = 2, column = 1)
		genderEditor = OptionMenu(self.master, genderSelectEditor, "Select a gender", "Male", "Female")
		genderEditor.grid(row = 3, column = 1)
		emailEditor = Entry(self.master, width = 25, bd = 1, font = ('Helvetica', 10))
		emailEditor.grid(row = 4, column = 1)
		mobileEditor = Entry(self.master, width = 25, bd = 1, font = ('Helvetica', 10))
		mobileEditor.grid(row = 5, column = 1)
		courseEditor = OptionMenu(self.master, courseSelectEditor, "Select a course", "Cisco CCNA RS", "Cisco CCNP", "Cisco Voice", "Cyber Security", "Database Administrator", "Ethical Hacking", "Exchange Server", "Java Developer", "Linux Essentials", "Linux Networking and Administration", "Mobile App Developer", "Oracle Database", "Penetration Testing", "PostgreSQL", "Python", "Software Developer", "SQL Server", "Web Developer", "Webmaster", "Windows Server")
		courseEditor.grid(row = 6, column = 1)
		lengthEditor = Entry(self.master, width = 25, bd = 1, font = ('Helvetica', 10))
		lengthEditor.grid(row = 7, column = 1)
		feesEditor = Entry(self.master, width = 25, bd = 1, font = ('Helvetica', 10))
		feesEditor.grid(row = 8, column = 1)
		paidEditor = Entry(self.master, width = 25, bd = 1, font = ('Helvetica', 10))
		paidEditor.grid(row = 9, column = 1)
		statusEditor = OptionMenu(self.master, statusSelectEditor, "Select a status", "In Progress", "Cancelled" ,"Completed")
		statusEditor.grid(row = 12, column = 1)
		certnumberEditor = Entry(self.master, width = 25, bd = 1, font = ('Helvetica', 10))
		certnumberEditor.grid(row = 13, column = 1)
		
		updateBtn = Button(self.master, text = "Update", command = update , width = 17, font = ("Helvetica", 12, "bold"), bg = "#09383d", fg = "#ffffff")
		updateBtn.grid(row = 15, column = 1, pady = 10)
	

# Finances Window =========================================================================================================================================================================================================================================================================================================================================================

class Finances():

	# Database Connection and Tables Creation

	conn = sqlite3.connect('kits_data.db')
	c = conn.cursor()

	c.execute(""" CREATE TABLE IF NOT EXISTS expenses(
		amount int,
		beneficiary text,
		reason text,
		date_ text,
		updated_on text
		)""")

	c.execute(""" CREATE TABLE IF NOT EXISTS investments(
		amount int,
		description text,
		investor text,
		mobile int,
		email text,
		date_ text
		)""")


	def __init__(self, master):

		# Window Configuration

		self.master = master
		self.master.geometry('1350x690+0+0')
		self.master.title('KMS - Finances')
		self.master.iconbitmap('kits.ico')
		self.master.configure(background = '#ffffff')


		# Finances Variables

		global income_fromProjects
		global income_fromSales
		global income_fromStudents
		global fromExpenses
		global fromInvestments

		self.exitBtn = Button(self.master, text = "Close", width = 5, command = self.exit, bg = "#09383d", fg = "#ffffff", font = ('Helvetica', 16, 'bold'))
		self.exitBtn.grid(row = 0, column = 0, pady = 10, sticky = W)

		self.left = Frame(self.master, padx = 20)
		self.left.grid(row = 3, column = 0, padx = 20, pady = 50)

		self.leftupper = Frame(self.left)
		self.leftupper.grid(row = 0, column = 0, pady = 5)

		self.leftlower = Frame(self.left)
		self.leftlower.grid(row = 1, column = 0, pady = 5)

		self.rightPanel = Frame(self.master, padx = 20, pady = 20)
		self.rightPanel.grid(row = 3, column = 3, rowspan = 10 , columnspan = 6, padx = 20, pady = 10)

		self.clearBtn = Button(self.master, text = "Clear", width = 5, command = self.clear, bg = "#09383d", fg = "#ffffff", font = ('Helvetica', 12, 'bold'))
		self.clearBtn.grid(row = 5, column = 8, ipadx = 14)

		self.expensesLabel = Label(self.leftupper, text = "Add expense", fg = "#09383d", font = ("Helvetica", 18, "bold"))
		self.expensesLabel.grid(row = 0, column = 0, columnspan = 2, pady = 1, sticky = W)
	
		self.amountLabel = Label(self.leftupper, text = "Amount ($)", font =('Helvetica', 12, 'bold')).grid(row = 1, column = 0, sticky = W)
		self.beneficiaryLabel = Label(self.leftupper, text = "Beneficiary", font =('Helvetica', 12, 'bold')).grid(row = 2, column = 0, sticky = W)
		self.reasonLabel = Label(self.leftupper, text = "Reason", font =('Helvetica', 12, 'bold')).grid(row = 3, column = 0, sticky = W)
		
		self.amount = Entry(self.leftupper, width = 25, bd = 1, font = ('Helvetica', 10))
		self.amount.grid(row = 1, column = 1)
		self.beneficiary = Entry(self.leftupper, width = 25, bd = 1, font = ('Helvetica', 10))
		self.beneficiary.grid(row = 2, column = 1)
		self.reason = Entry(self.leftupper, width = 25, bd = 1, font = ('Helvetica', 10))
		self.reason.grid(row = 3, column = 1)

		self.addexpenseBtn = Button(self.leftupper, text = "Add", command = self.addExpense, width = 5, font = ("Helvetica", 10, "bold"), bg = "#09383d", fg = "#ffffff")
		self.addexpenseBtn.grid(row = 4, column = 1, pady = 10, sticky = E)


		self.investmentLabel = Label(self.leftlower, text = "Make an investment", fg = "#09383d", font = ("Helvetica", 18, "bold"))
		self.investmentLabel.grid(row = 0, column = 0, columnspan = 2, pady = 1, sticky = W)

		self.investedAmountLabel = Label(self.leftlower, text = "Amount ($)", font =('Helvetica', 12, 'bold')).grid(row = 1, column = 0, sticky = W)
		self.descriptionLabel = Label(self.leftlower, text = "Description", font =('Helvetica', 12, 'bold')).grid(row = 2, column = 0, sticky = W)
		self.investorLabel = Label(self.leftlower, text = "Investor", font =('Helvetica', 12, 'bold')).grid(row = 3, column = 0, sticky = W)
		self.mobileLabel = Label(self.leftlower, text = "Mobile", font =('Helvetica', 12, 'bold')).grid(row = 4, column = 0, sticky = W)
		self.emailLabel = Label(self.leftlower, text = "E-mail", font =('Helvetica', 12, 'bold')).grid(row = 5, column = 0, sticky = W)
		

		self.investedAmount = Entry(self.leftlower, width = 25, bd = 1, font = ('Helvetica', 10))
		self.investedAmount.grid(row = 1, column = 1)
		self.description = Entry(self.leftlower, width = 25, bd = 1, font = ('Helvetica', 10))
		self.description.grid(row = 2, column = 1)
		self.investor = Entry(self.leftlower, width = 25, bd = 1, font = ('Helvetica', 10))
		self.investor.grid(row = 3, column = 1)
		self.mobile = Entry(self.leftlower, width = 25, bd = 1, font = ('Helvetica', 10))
		self.mobile.grid(row = 4, column = 1)
		self.email = Entry(self.leftlower, width = 25, bd = 1, font = ('Helvetica', 10))
		self.email.grid(row = 5, column = 1)
	
		self.investBtn = Button(self.leftlower, text = "Invest", command = self.invest, width = 10, font = ("Helvetica", 10, "bold"), bg = "#09383d", fg = "#ffffff")
		self.investBtn.grid(row = 6, column = 1, pady = 10, sticky = E)

		# Finances Navigation Buttons

		self.account = Button(self.master, text = "Accounting", command = self.accounting, width = 15, font = ("Helvetica", 12, "bold"), fg = "#fa1b27", bg = "#ffffff", bd = 2, relief = RIDGE)
		self.account.grid(row = 1, column = 3)
		self.exp = Button(self.master, text = "Expenses", command = self.query_expenses, width = 15, font = ("Helvetica", 12, "bold"), bg = "#09383d", fg = "#ffffff")
		self.exp.grid(row = 1, column = 4)
		self.invests = Button(self.master, text = "Investments", command = self.query_investments, width = 15, font = ("Helvetica", 12, "bold"), bg = "#09383d", fg = "#ffffff")
		self.invests.grid(row = 1, column = 5)
		self.investors = Button(self.master, text = "Investors",  command = self.query_investors,width = 15, font = ("Helvetica", 12, "bold"), bg = "#09383d", fg = "#ffffff")
		self.investors.grid(row = 1, column = 6)
		self.update = Button(self.master, text = "Update", command = self.updateWin, width = 15, font = ("Helvetica", 12, "bold"), bg = "#09383d", fg = "#ffffff")
		self.update.grid(row = 1, column = 7)
		self.delete = Button(self.master, text = "Delete", command = self.delete , width = 15, font = ("Helvetica", 12, "bold"), bg = "#09383d", fg = "#ffffff")
		self.delete.grid(row = 1, column = 8)


		self.search = Button(self.master, text = "Search beneficiary", command = self.query_beneficiary, bg = '#ffffff' , font = ("Helvetica", 10))
		self.search.grid(row = 0, column = 7, sticky = E)
		self.searchBox = Entry(self.master, bd = 1, bg = "#f8fafa", relief = SUNKEN)
		self.searchBox.grid(row = 0, column = 8)

		self.expenseIDLabel = Label(self.master, text = "Expense ID: ", bg = '#ffffff' , font = ("Helvetica", 10))
		self.expenseIDLabel.grid(row = 2, column = 7, sticky = E)
		self.expenseID = Entry(self.master)
		self.expenseID.grid(row = 2, column = 8)


		# Display Area

		self.dataList = Listbox(self.rightPanel, font = ('Helvetica', 9, 'bold'), width = 120, height = 16, bg = "#ffffff")
		self.dataList.grid(row = 0, rowspan = 10, column = 0)

		scrollbarY = Scrollbar(self.rightPanel, command = self.dataList.yview)
		scrollbarY.grid(row = 0, rowspan = 15, column = 1, sticky = 'ns')
		scrollbarX = Scrollbar(self.rightPanel, orient = 'horizontal' , command = self.dataList.xview)
		scrollbarX.grid(row = 16, column = 0, sticky = 'we')
		self.dataList.configure(yscrollcommand = scrollbarY.set, xscrollcommand = scrollbarX.set)

		self.dataList.delete(0, END)


	# Finances Button Functions

	def addExpense(self):
		
		conn = sqlite3.connect('kits_data.db')
		c = conn.cursor()

		now = dt.datetime.now()

		c.execute("INSERT INTO expenses VALUES (:amount, :beneficiary, :reason, :date_, :updated_on)",
			{
			'amount': self.amount.get(),
			'beneficiary': self.beneficiary.get(),
			'reason': self.reason.get(),
			'date_': now,
			'updated_on': now
			})

		conn.commit()
		conn.close()

		self.amount.delete(0, END)
		self.beneficiary.delete(0, END)
		self.reason.delete(0, END)
	
		response = messagebox.showinfo('Add expense', 'Expense added successfully !')


	def invest(self):
		
		conn = sqlite3.connect('kits_data.db')
		c = conn.cursor()

		now = dt.datetime.now()

		c.execute("INSERT INTO investments VALUES (:amount, :description, :investor, :mobile, :email, :date_)",
			{
			'amount': self.investedAmount.get(),
			'description': self.description.get(),
			'investor': self.investor.get(),
			'mobile': self.mobile.get(),
			'email': self.email.get(),
			'date_': now
			})

		conn.commit()
		conn.close()

		self.investedAmount.delete(0, END)
		self.description.delete(0, END)
		self.investor.delete(0, END)
		self.mobile.delete(0, END)
		self.email.delete(0, END)
	
		response = messagebox.showinfo('Make an investment', 'Investment made successfully !')


	def query_expenses(self):

		conn = sqlite3.connect('kits_data.db')
		c = conn.cursor()

		c.execute("SELECT *, oid FROM expenses")
		expenses_records = c.fetchall()

		self.dataList.delete(0, END)

		self.dataList.insert(END, "EXPENSES")
		self.dataList.insert(END, "\n" + "\n")
		self.dataList.insert(END, "Id." + "    " + "Amount ($)" + "    " + "Beneficiary" + "    " + "Reason" + "    " + "Date and time")
		self.dataList.insert(END, "\n" + "\n")

		for expense in expenses_records:
			self.dataList.insert(END, str(expense[5])+ "       " + str(expense[0]) + "       " + str(expense[1]) + "       " + str(expense[2]) + "       " + str(expense[3]) + "       " + str(expense[4]) + "\n")

		conn.commit()
		conn.close()


	def query_beneficiaries(self):

		conn = sqlite3.connect('kits_data.db')
		c = conn.cursor()

		c.execute("SELECT *, oid FROM expenses")
		expenses_records = c.fetchall()

		self.dataList.delete(0, END)

		self.dataList.insert(END, "EXPENSES  |  Beneficiaries")
		self.dataList.insert(END, "\n" + "\n")
		self.dataList.insert(END, "Id." + "    " + "Beneficiary" + "    " + "Amount ($)" + "    " + "Date and time")
		self.dataList.insert(END, "\n" + "\n")

		for expense in expenses_records:
			self.dataList.insert(END, str(expense[4])+ "       " + str(expense[1]) + "       " + str(expense[0]) + "\n")

		conn.commit()
		conn.close()


	def query_investments(self):

		conn = sqlite3.connect('kits_data.db')
		c = conn.cursor()

		c.execute("SELECT *, oid FROM investments")
		investments_records = c.fetchall()

		self.dataList.delete(0, END)

		self.dataList.insert(END, "INVESTMENTS")
		self.dataList.insert(END, "\n" + "\n")
		self.dataList.insert(END, "Id." + "    " + "Amount ($)" + "    " + "Description" + "    " + "Investor" + "    " + "Mobile" + "    " + "E-mail" + "    " + "Date")
		self.dataList.insert(END, "\n" + "\n")

		for investment in investments_records:
			self.dataList.insert(END, str(investment[6])+ "       " + str(investment[0]) +  "       " + str(investment[1]) + "       " + str(investment[2]) + "       " + str(investment[3]) + "       " + str(investment[4]) + "       " + str(investment[5]) + "\n")

		conn.commit()
		conn.close()


	def query_investors(self):

		conn = sqlite3.connect('kits_data.db')
		c = conn.cursor()

		c.execute("SELECT *, oid FROM investments")
		investments_records = c.fetchall()

		self.dataList.delete(0, END)

		self.dataList.insert(END, "INVESTMENTS  |  Investors")
		self.dataList.insert(END, "\n" + "\n")
		self.dataList.insert(END, "Id." + "    " + "Investor" + "    " + "Amount ($)" + "    " + "Date")
		self.dataList.insert(END, "\n" + "\n")

		for investment in investments_records:
			self.dataList.insert(END, str(investment[6])+ "       " + str(investment[2]) +  "       " + str(investment[0]) + "       " + str(investment[5]) + "\n")

		conn.commit()
		conn.close()


	def query_beneficiary(self):

		conn = sqlite3.connect('kits_data.db')
		c = conn.cursor()

		search = self.searchBox.get()

		c.execute("SELECT *, oid FROM expenses WHERE beneficiary = ?", (search,))
		expenses_records = c.fetchall()

		self.dataList.delete(0, END)

		self.dataList.insert(END, "BENEFICIARY  |  " + search)
		self.dataList.insert(END, "\n" + "\n")
		self.dataList.insert(END, "Id." + "    " + "Beneficiary" + "    " + "Amount ($)" + "    " + "Date and time")
		self.dataList.insert(END, "\n" + "\n")

		for expense in expenses_records:
			self.dataList.insert(END, str(expense[4])+ "       " + str(expense[1]) + "       " + str(expense[0]) + "\n")

		conn.commit()
		conn.close()

		self.searchBox.delete(0, END)


	def accounting(self):

		financialStatement = Toplevel(self.master)
		financialStatement.geometry('849x520+200+90')
		financialStatement.title('KMS - Accounting')
		financialStatement.iconbitmap('kits.ico')
		financialStatement.configure(background = '#ffffff')

		global total_income
		global total_profit
		global total_loss
		global balance

		Label(financialStatement, text = "Below figures are in dollars ($)", bg = "#ffffff", font = ('Helvetica', 12)).grid(row = 8, column = 0, columnspan = 5, pady = 40)

		self.income_fromProjectsLabel = Label(financialStatement, text = "Projects", bg = "white", fg = "#023136", font =('Helvetica', 15, 'bold')).grid(row = 9, column = 0, sticky = W)
		self.income_fromSalesLabel = Label(financialStatement, text = "Sales", bg = "white", fg = "#023136", font =('Helvetica', 15, 'bold')).grid(row = 9, column = 1, sticky = W)
		self.income_fromFeesLabel = Label(financialStatement, text = "Fees", bg = "white", fg = "#023136", font =('Helvetica', 15, 'bold')).grid(row = 9, column = 2, sticky = W)
		self.expensesLabel = Label(financialStatement, text = "Expenses", bg = "white", fg = "#023136", font =('Helvetica', 15, 'bold')).grid(row = 9, column = 3, sticky = W)
		self.investmentsLabel = Label(financialStatement, text = "Investments", bg = "white", fg = "#023136", font =('Helvetica', 15, 'bold')).grid(row = 9, column = 4, sticky = W)

		income_fromProjects = Entry(financialStatement, width = 15, bd = 1, fg = "white", bg = "#023136", font = ('Helvetica', 15, 'bold'))
		income_fromProjects.grid(row = 10, column = 0)
		income_fromSales = Entry(financialStatement, width = 15, bd = 1, fg = "white", bg = "#023136", font = ('Helvetica', 15, 'bold'))
		income_fromSales.grid(row = 10, column = 1)
		income_fromStudents = Entry(financialStatement, width = 15, bd = 1, fg = "white", bg = "#023136", font = ('Helvetica', 15, 'bold'))
		income_fromStudents.grid(row = 10, column = 2)
		fromExpenses = Entry(financialStatement, width = 15, bd = 1, fg = "white", bg = "#023136", font = ('Helvetica', 15, 'bold'))
		fromExpenses.grid(row = 10, column = 3)
		fromInvestments = Entry(financialStatement, width = 15, bd = 1, fg = "white", bg = "#023136", font = ('Helvetica', 15, 'bold'))
		fromInvestments.grid(row = 10, column = 4)


		conn = sqlite3.connect('kits_data.db')
		c = conn.cursor()

		c.execute("SELECT SUM(profit) from projects")
		records = c.fetchall()

		for record in records:
			income_fromProjects.insert(0, record[0])

		c.execute("SELECT SUM(cost) from sales")
		records = c.fetchall()

		for record in records:
			income_fromSales.insert(0, record[0])

		c.execute("SELECT SUM(paid) from students")
		records = c.fetchall()

		for record in records:
			income_fromStudents.insert(0, record[0])

		c.execute("SELECT SUM(amount) from expenses")
		records = c.fetchall()

		for record in records:
			fromExpenses.insert(0, record[0])

		c.execute("SELECT SUM(amount) from investments")
		records = c.fetchall()

		for record in records:
			fromInvestments.insert(0, record[0])
			

		conn.commit()
		conn.close()


		total_income = int(income_fromProjects.get()) + int(income_fromSales.get()) + int(income_fromStudents.get())
		total_profit = int(total_income) - int(fromInvestments.get())
		total_loss = int(fromInvestments.get()) - int(total_income)
		balance = (int(total_income) + int(fromInvestments.get()) - int(fromExpenses.get()))

		startupLabel = Label(financialStatement, text = "Startup cost", font = ('Helvetica', 13, 'bold'), bg = "#ffffff")
		startupLabel.grid(row = 0, column = 0, sticky = E)
		startup = Label(financialStatement, text = "$ 200", bg = "#ffffff", font = ('Helvetica', 13, 'bold'))
		startup.grid(row = 0, column = 1, sticky = W)
		capitalLabel = Label(financialStatement, text = "Capital", fg = "black", bg = "yellow", font = ('Helvetica', 13, 'bold'))
		capitalLabel.grid(row = 1, column = 0, sticky = E)
		capital = Label(financialStatement, text = "$ 2000", bg = "black", fg = "yellow", font = ('Helvetica', 13, 'bold'))
		capital.grid(row = 1, column = 1, sticky = W)
		incomeLabel = Label(financialStatement, text = "Income", bg = "white", fg = "#0398a8", font = ('Helvetica', 18, 'bold'))
		incomeLabel.grid(row = 3, column = 1)
		income = Label(financialStatement, text = "$ " + str(total_income), bg = "white", fg = "#0398a8", font = ('Helvetica', 18, 'bold'))
		income.grid(row = 4, column = 1)
		profitLabel = Label(financialStatement, text = "Profit", bg = "white", fg = "#069cda", font = ('Helvetica', 18, 'bold'))
		profitLabel.grid(row = 3, column = 2)
		profit = Label(financialStatement, text = "$ " + str(total_profit), bg = "white", fg = "#069cda", font = ('Helvetica', 18, 'bold'))
		profit.grid(row = 4, column = 2)
		lossLabel = Label(financialStatement, text = "Loss", bg = "white", fg = "gray", font = ('Helvetica', 18, 'bold'))
		lossLabel.grid(row = 3, column = 3)
		loss = Label(financialStatement, text = "$ " + str(total_loss), bg = "white", fg = "gray", font = ('Helvetica', 18, 'bold'))
		loss.grid(row = 4, column = 3)

		Label(financialStatement, text = " ", font = ('Helvetica', 15), bg = "#ffffff").grid(row = 5, column = 0, pady = 10)
		Label(financialStatement, text = " ", font = ('Helvetica', 15), bg = "#ffffff").grid(row = 2, column = 0, pady = 10)


		balanceLabel = Label(financialStatement, text = "Balance", bg = "#ffffff", fg = "red", font = ('Helvetica', 25, 'bold'))
		balanceLabel.grid(row = 6, column = 0, columnspan = 5)
		balanceDisplay = Label(financialStatement, text = "$ " + str(balance), bg = "red", fg = "#fafafa", font = ('Helvetica', 25, 'bold'))
		balanceDisplay.grid(row = 7, column = 0, columnspan = 5)


	def updateWin(self):

		global expense_id

		editor = Toplevel(self.master)
		gui = Updateexpense(editor)
		
		conn = sqlite3.connect('kits_data.db')
		c = conn.cursor()

		expense_id = self.expenseID.get()

		c.execute("SELECT * from expenses WHERE oid = ?", (expense_id,))

		records = c.fetchall()


		for record in records:
			amountEditor.insert(0, record[0])
			beneficiaryEditor.insert(0, record[1])
			reasonEditor.insert(0, record[2])

		conn.commit()
		conn.close()

		self.expenseID.delete(0, END)
		

	def delete(self):

		response = messagebox.askyesno('Delete Record', 'Do you want to delete this record?')

		if response == 1:
			conn = sqlite3.connect('kits_data.db')
			c = conn.cursor()

			c.execute("DELETE from expenses WHERE oid = " + self.expenseID.get())

			self.expenseID.delete(0, END)

			
			conn.commit()
			conn.close()
			response = messagebox.showinfo('Delete Record', 'Record deleted successfully!')

	def clear(self):
		self.dataList.delete(0, END)

	def exit(self):
		self.master.destroy()


	conn.commit()
	conn.close()


# Update Finances =========================================================================================================================================================================================================================================================================================================================================================

class Updateexpense():

	def __init__(self, master):

		self.master = master
		self.master.geometry('300x150+500+300')
		self.master.title('KMS - Update Expense')
		self.master.iconbitmap('kits.ico')

		global amountEditor
		global beneficiaryEditor
		global reasonEditor


		def update():
			
			conn = sqlite3.connect('kits_data.db')
			c = conn.cursor()

			eid = expense_id
			now = dt.datetime.now()

			c.execute(""" UPDATE expenses SET
				amount = :amount,
				beneficiary = :beneficiary,
				reason = :reason,
				updated_on = :updated_on
				WHERE oid = :eid """,
				{
				'amount': amountEditor.get(),
				'beneficiary': beneficiaryEditor.get(),
				'reason': reasonEditor.get(),
				'updated_on': now,
				'eid': eid
				})
	

			conn.commit()
			conn.close()

			self.master.destroy()
			updatemessage = messagebox.showinfo("Updated", "Expense updated successfully!")


		amountLabel = Label(self.master, text = "Amount ($)", font =('Helvetica', 12, 'bold')).grid(row = 9, column = 0, sticky = W)
		beneficiaryLabel = Label(self.master, text = "Beneficiary", font =('Helvetica', 12, 'bold')).grid(row = 10, column = 0, sticky = W)
		reasonLabel = Label(self.master, text = "Reason", font =('Helvetica', 12, 'bold')).grid(row = 11, column = 0, sticky = W)

		amountEditor = Entry(self.master, width = 25, bd = 1, font = ('Helvetica', 10))
		amountEditor.grid(row = 9, column = 1)
		beneficiaryEditor = Entry(self.master, width = 25, bd = 1, font = ('Helvetica', 10))
		beneficiaryEditor.grid(row = 11, column = 1)
		reasonEditor = Entry(self.master, width = 25, bd = 1, font = ('Helvetica', 10))
		reasonEditor.grid(row = 12, column = 1)
		
		updateEditorBtn = Button(self.master, text = "Update", command = update , width = 17, font = ("Helvetica", 12, "bold"), bg = "#09383d", fg = "#ffffff")
		updateEditorBtn.grid(row = 13, column = 1, pady = 10)


# Personnel Window =========================================================================================================================================================================================================================================================================================================================================================

class Personnel():

	# Database Connection and Tables Creation

	conn = sqlite3.connect('kits_data.db')
	c = conn.cursor()

	c.execute(""" CREATE TABLE IF NOT EXISTS personnel(
		fullname text,
		gender text,
		dob text,
		marital_status text,
		children int,
		mobile int,
		email text,
		address text,
		department text,
		position text,
		salary int,
		contract_type text,
		start_date text,
		end_date text,
		renewed int,
		status text
		)""")


	def __init__(self, master):

		# Personnel Window Configuration

		self.master = master
		self.master.geometry('1350x690+0+0')
		self.master.title('KMS - Human Ressources')
		self.master.iconbitmap('kits.ico')
		self.master.configure(background = '#ffffff')


		# Personnel Window Widgets

		self.exitBtn = Button(self.master, text = "Close", width = 5, command = self.exit, bg = "#09383d", fg = "#ffffff", font = ('Helvetica', 16, 'bold'))
		self.exitBtn.grid(row = 0, column = 0, pady = 10, sticky = W)

		self.leftPanel = Frame(self.master, padx = 10, pady = 10)
		self.leftPanel.grid(row = 3, rowspan = 17 , column = 0, columnspan = 3, padx = 10, pady = 10)

		self.rightPanel = Frame(self.master, padx = 20, pady = 20)
		self.rightPanel.grid(row = 1, column = 3, rowspan = 15 , columnspan = 6, padx = 20, pady = 50)

		self.clearBtn = Button(self.master, text = "Clear", width = 5, command = self.clear, bg = "#09383d", fg = "#ffffff", font = ('Helvetica', 12, 'bold'))
		self.clearBtn.grid(row = 14, rowspan = 15, column = 8, ipadx = 14, pady = 10)

		self.addemployeeLabel = Label(self.leftPanel, text = "Add Employee", fg = "#09383d", font = ("Helvetica", 18, "bold"))
		self.addemployeeLabel.grid(row = 0, column = 0, columnspan = 2, pady = 7, sticky = W)

		self.fullnameLabel = Label(self.leftPanel, text = "Full name", font =('Helvetica', 12, 'bold')).grid(row = 2, column = 0, sticky = W)
		self.genderLabel = Label(self.leftPanel, text = "Gender", font =('Helvetica', 12, 'bold')).grid(row = 3, column = 0, sticky = W)
		self.dobLabel = Label(self.leftPanel, text = "Date of birth", font =('Helvetica', 12, 'bold')).grid(row = 4, column = 0, sticky = W)
		self.marital_statusLabel = Label(self.leftPanel, text = "Marital status", font =('Helvetica', 12, 'bold')).grid(row = 5, column = 0, sticky = W)
		self.childrenLabel = Label(self.leftPanel, text = "No. of Children", font =('Helvetica', 12, 'bold')).grid(row = 6, column = 0, sticky = W)
		self.mobileLabel = Label(self.leftPanel, text = "Mobile no.", font =('Helvetica', 12, 'bold')).grid(row = 7, column = 0, sticky = W)
		self.emailLabel = Label(self.leftPanel, text = "E-mail", font =('Helvetica', 12, 'bold')).grid(row = 8, column = 0, sticky = W)
		self.addressLabel = Label(self.leftPanel, text = "Address", font =('Helvetica', 12, 'bold')).grid(row = 9, column = 0, sticky = W)
		self.departmentLabel = Label(self.leftPanel, text = "Department", font =('Helvetica', 12, 'bold')).grid(row = 10, column = 0, sticky = W)
		self.positionLabel = Label(self.leftPanel, text = "Position", font =('Helvetica', 12, 'bold')).grid(row = 11, column = 0, sticky = W)
		self.salaryLabel = Label(self.leftPanel, text = "Salary ($)", font =('Helvetica', 12, 'bold')).grid(row = 12, column = 0, sticky = W)
		self.contract_typeLabel = Label(self.leftPanel, text = "Contract type", font =('Helvetica', 12, 'bold')).grid(row = 13, column = 0, sticky = W)
		self.startLabel = Label(self.leftPanel, text = "Start date", font =('Helvetica', 12, 'bold')).grid(row = 14, column = 0, sticky = W)
		self.statusLabel = Label(self.leftPanel, text = "Status", font =('Helvetica', 12, 'bold')).grid(row = 17, column = 0, sticky = W)


		self.genderSelect = StringVar()
		self.genderSelect.set("Select a gender")

		self.marital_statusSelect = StringVar()
		self.marital_statusSelect.set("Select a status")

		self.departmentSelect = StringVar()
		self.departmentSelect.set("Select a dept")

		self.contract_typeSelect = StringVar()
		self.contract_typeSelect.set("Select a type")

		self.statusSelect = StringVar()
		self.statusSelect.set("Select a status")

		self.fullname = Entry(self.leftPanel, width = 25, bd = 1, font = ('Helvetica', 10))
		self.fullname.grid(row = 2, column = 1)
		self.gender = OptionMenu(self.leftPanel, self.genderSelect, "Select a gender", "Male", "Female")
		self.gender.grid(row = 3, column = 1)
		self.dob = Entry(self.leftPanel, width = 25, bd = 1, font = ('Helvetica', 10))
		self.dob.grid(row = 4, column = 1)
		self.marital_status = OptionMenu(self.leftPanel, self.marital_statusSelect, "Select a status", "Single", "Married", "Divorced")
		self.marital_status.grid(row = 5, column = 1)
		self.children = Entry(self.leftPanel, width = 25, bd = 1, font = ('Helvetica', 10))
		self.children.grid(row = 6, column = 1)
		self.mobile = Entry(self.leftPanel, width = 25, bd = 1, font = ('Helvetica', 10))
		self.mobile.grid(row = 7, column = 1)
		self.email = Entry(self.leftPanel, width = 25, bd = 1, font = ('Helvetica', 10))
		self.email.grid(row = 8, column = 1)
		self.address = Entry(self.leftPanel, width = 25, bd = 1, font = ('Helvetica', 10))
		self.address.grid(row = 9, column = 1)
		self.departement = OptionMenu(self.leftPanel, self.departmentSelect, "Select a dept", "Accounts and Finance", "Administration", "Human Ressources", "Sales and Marketing", "Information and Technology", "Product Development", "Reseach and Development", "Logistics and Transport")
		self.departement.grid(row = 10, column = 1)
		self.position = Entry(self.leftPanel, width = 25, bd = 1, font = ('Helvetica', 10))
		self.position.grid(row = 11, column = 1)
		self.salary = Entry(self.leftPanel, width = 25, bd = 1, font = ('Helvetica', 10))
		self.salary.grid(row = 12, column = 1)
		self.contract_type = OptionMenu(self.leftPanel, self.contract_typeSelect, "Select a type", "Internship", "Temporary", "Permanent")
		self.contract_type.grid(row = 13, column = 1)
		self.start_date = Entry(self.leftPanel, width = 25, bd = 1, font = ('Helvetica', 10))
		self.start_date.grid(row = 14, column = 1)
		self.status = OptionMenu(self.leftPanel, self.statusSelect, "Select a status", "Hired", "Fired" ,"Left", "Deceased")
		self.status.grid(row = 17, column = 1)

		self.addBtn = Button(self.leftPanel, text = "Add", command = self.add , width = 17, font = ("Helvetica", 12, "bold"), bg = "#09383d", fg = "#ffffff")
		self.addBtn.grid(row = 18, column = 1, pady = 10)


		# Personnel Window Navigation Buttons

		self.summary = Button(self.master, text = "Summary", command = self.query_sum, width = 15, font = ("Helvetica", 12, "bold"), bg = "#09383d", fg = "#ffffff")
		self.summary.grid(row = 1, column = 3)
		self.employees = Button(self.master, text = "Employees", command = self.query_all, width = 15, font = ("Helvetica", 12, "bold"), bg = "#09383d", fg = "#ffffff")
		self.employees.grid(row = 1, column = 4)
		self.salaries = Button(self.master, text = "Salaries", command = self.query_salaries, width = 15, font = ("Helvetica", 12, "bold"), bg = "#09383d", fg = "#ffffff")
		self.salaries.grid(row = 1, column = 5)
		self.contracts = Button(self.master, text = "Contracts",  command = self.query_contracts, width = 15, font = ("Helvetica", 12, "bold"), bg = "#09383d", fg = "#ffffff")
		self.contracts.grid(row = 1, column = 6)
		self.update = Button(self.master, text = "Update", command = self.updateWin, width = 15, font = ("Helvetica", 12, "bold"), bg = "#09383d", fg = "#ffffff")
		self.update.grid(row = 1, column = 7)
		self.delete = Button(self.master, text = "Delete", command = self.delete , width = 15, font = ("Helvetica", 12, "bold"), bg = "#09383d", fg = "#ffffff")
		self.delete.grid(row = 1, column = 8)
		self.personaldetails = Button(self.master, text = "Personal Details", command = self.query_personalDetails , width = 15, font = ("Helvetica", 12, "bold"), bg = "#fa1b27", fg = "#ffffff")
		self.personaldetails.grid(row = 0, column = 3)

		self.searchBtn = Button(self.master, text = "Search", command = self.query, bg = '#ffffff' , font = ("Helvetica", 10))
		self.searchBtn.grid(row = 0, column = 7, sticky = E)
		self.searchBox = Entry(self.master, bd = 1, bg = "#f8fafa", relief = SUNKEN)
		self.searchBox.grid(row = 0, column = 8)

		self.empIDLabel = Label(self.master, text = "Emp ID: ", bg = '#ffffff' , font = ("Helvetica", 10))
		self.empIDLabel.grid(row = 2, column = 7, sticky = E)
		self.empID = Entry(self.master)
		self.empID.grid(row = 2, column = 8)

		# Display Area

		self.dataList = Listbox(self.rightPanel, font = ('Helvetica', 9, 'bold'), width = 120, height = 16, bg = "#ffffff")
		self.dataList.grid(row = 0, rowspan = 15, column = 0)

		scrollbarY = Scrollbar(self.rightPanel, command = self.dataList.yview)
		scrollbarY.grid(row = 0, rowspan = 15, column = 1, sticky = 'ns')
		scrollbarX = Scrollbar(self.rightPanel, orient = 'horizontal' , command = self.dataList.xview)
		scrollbarX.grid(row = 16, column = 0, sticky = 'we')
		self.dataList.configure(yscrollcommand = scrollbarY.set, xscrollcommand = scrollbarX.set)

		self.dataList.delete(0, END)


	# Personnel Window Buttons Functions

	def add(self):
		
		conn = sqlite3.connect('kits_data.db')
		c = conn.cursor()

		c.execute("INSERT INTO personnel VALUES (:fullname, :gender, :dob, :marital_status, :children, :mobile, :email, :address , :department, :position, :salary, :contract_type, :start_date, :end_date, :renewed, :status )",
			{
			'fullname': self.fullname.get(),
			'gender': self.genderSelect.get(),
			'dob': self.dob.get(),
			'marital_status': self.marital_statusSelect.get(),
			'children': self.children.get(),
			'mobile': self.mobile.get(),
			'email': self.email.get(),
			'address': self.address.get(),
			'department': self.departmentSelect.get(),
			'position': self.position.get(),
			'salary': self.salary.get(),
			'contract_type': self.contract_typeSelect.get(),
			'start_date': self.start_date.get(),
			'end_date': self.end_date.get(),
			'renewed': self.renewed.get(),
			'status': self.statusSelect.get() 
			})

		conn.commit()
		conn.close()

		self.fullname.delete(0, END)
		self.dob.delete(0, END)
		self.children.delete(0, END)
		self.mobile.delete(0, END)
		self.email.delete(0, END)
		self.address.delete(0, END)
		self.position.delete(0, END)
		self.salary.delete(0, END)
		self.start_date.delete(0, END)
		self.end_date.delete(0, END)
		self.renewed.delete(0, END)
		
		response = messagebox.showinfo('Add employee', 'New employee added successfully !')


	def query_sum(self):

		conn = sqlite3.connect('kits_data.db')
		c = conn.cursor()

		c.execute("SELECT *, oid FROM personnel")
		personnel_records = c.fetchall()
		
		self.dataList.delete(0, END)

		self.dataList.insert(END, "PERSONNEL  |  Summary")
		self.dataList.insert(END, "\n" + "\n")
		self.dataList.insert(END, "Id." + "    " + "Full name" + "    " + "Mobile" + "    " + "E-mail" + "    " + "Department" + "    " + "Position" + "    " + "Salary" + "    " + "Contract type" + "    " + "Status")
		self.dataList.insert(END, "\n" + "\n")

		for record in personnel_records:
			self.dataList.insert(END, str(record[16])+ "    " + str(record[0]) + "    " + str(record[5]) + "    " + str(record[6]) + "    "  + str(record[8]) + "    " + str(record[9]) + "    " + str(record[10])+ "    " + str(record[11]) + "     " + str(record[15]) + "\n")

		conn.commit()
		conn.close()


	def query_all(self):

		conn = sqlite3.connect('kits_data.db')
		c = conn.cursor()

		c.execute("SELECT *, oid FROM personnel")
		personnel_records = c.fetchall()
		
		self.dataList.delete(0, END)

		self.dataList.insert(END, "PERSONNEL")
		self.dataList.insert(END, "\n" + "\n")
		self.dataList.insert(END, "Id." + "    " + "Full name" + "    " + "Gender" + "    " + "Date of birth" + "    " + "Marital status" + "    " + "No. of Children" + "    " + "Mobile" + "    " + "E-mail" + "    " + "Address"    + "    " + "Department" + "    " + "Position" + "    " + "Salary" + "    " + "Contract type" + "    " + "Start date" + "    " + "End date" + "    " + "Renewal" + "    " + "Status")
		self.dataList.insert(END, "\n" + "\n")

		for record in personnel_records:
			self.dataList.insert(END, str(record[16])+ " " + str(record[0]) + " " + str(record[1]) + " " + str(record[2]) + " " + str(record[3]) + " " + str(record[4]) + " " + str(record[5]) + " "  + str(record[6]) + " " + str(record[7])+ " "  + str(record[8]) + " " + str(record[9]) + " " + str(record[10]) + " " + str(record[11]) + " " + str(record[12]) + " " + str(record[13]) + " " + str(record[14]) + " " + str(record[15]) +"\n")

		conn.commit()
		conn.close()


	def query_salaries(self):

		conn = sqlite3.connect('kits_data.db')
		c = conn.cursor()

		c.execute("SELECT *, oid FROM personnel")
		personnel_records = c.fetchall()
		

		self.dataList.delete(0, END)

		self.dataList.insert(END, "PERSONNEL  |  Salaries")
		self.dataList.insert(END, "\n" + "\n")
		self.dataList.insert(END, "Id." + "    " + "Full name" + "    " + "Gender" + "    " + "Marital status" + "    " + "No. of Children" + "    " + "Position" + "    " + "Salary" + "    " + "Status")
		self.dataList.insert(END, "\n" + "\n")


		for record in personnel_records:
			self.dataList.insert(END, str(record[16])+ "      " + str(record[0]) + "      " + str(record[1]) + "      " + str(record[3]) + "      " + str(record[4]) + "      " + str(record[9]) + "      " + str(record[10]) + "      "  + str(record[15]) + "\n")

		conn.commit()
		conn.close()


	def query_contracts(self):

		conn = sqlite3.connect('kits_data.db')
		c = conn.cursor()

		c.execute("SELECT *, oid FROM personnel")
		personnel_records = c.fetchall()
		

		self.dataList.delete(0, END)

		self.dataList.insert(END, "PERSONNEL  |  Contracts")
		self.dataList.insert(END, "\n" + "\n")
		self.dataList.insert(END, "Id." + "    " + "Full name" + "    " + "Position" + "    " + "Salary" + "    " + "Contract type" + "    " + "Start date" + "    " + "End date" + "    " + "Status")
		self.dataList.insert(END, "\n" + "\n")

		for record in personnel_records:
			self.dataList.insert(END, str(record[16])+ "      " + str(record[0]) + "      " + str(record[9]) + "      " + str(record[10]) + "      " + str(record[11]) + "      " + str(record[12]) + "      " + str(record[13]) + "      "  + str(record[14]) + "      " + str(record[15]) + "\n")

		conn.commit()
		conn.close()


	def query(self):

		conn = sqlite3.connect('kits_data.db')
		c = conn.cursor()

		search = self.searchBox.get()

		if search == "Male" or search == "Female":
			c.execute("SELECT *, oid FROM personnel WHERE gender = ?", (search,))
			personnel_records = c.fetchall()
			self.dataList.delete(0, END)

			self.dataList.insert(END, "PERSONNEL  |  Gender")
			self.dataList.insert(END, "\n" + "\n")
			self.dataList.insert(END, "Id." + "    " + "Full name" + "    " + "Gender" + "    " + "Department" + "    " + "Position" + "    " + "Salary" + "    " + "Contract type" + "    " + "Status")
			self.dataList.insert(END, "\n" + "\n")

			for record in personnel_records:
				self.dataList.insert(END, str(record[16])+ "    " + str(record[0]) + "    " + str(record[1]) + "    " + str(record[8]) + "    " + str(record[9]) + "    " + str(record[10])+ "    " + str(record[11]) + "     " + str(record[15]) + "\n")


			conn.commit()
			conn.close()

			self.searchBox.delete(0, END)


		elif search == "Single" or search == "Married" or search == "Divorced":
			c.execute("SELECT *, oid FROM personnel WHERE marital_status = ?", (search,))
			personnel_records = c.fetchall()
			self.dataList.delete(0, END)

			self.dataList.insert(END, "PERSONNEL  |  Marital Status")
			self.dataList.insert(END, "\n" + "\n")
			self.dataList.insert(END, "Id." + "    " + "Full name" + "    " + "Marital Status" + "    " + "No. of Children" + "    " + "Department" + "    " + "Position" + "    " + "Salary" + "    " + "Contract type" + "    " + "Status")
			self.dataList.insert(END, "\n" + "\n")

			for record in personnel_records:
				self.dataList.insert(END, str(record[16])+ "    " + str(record[0]) + "    " + str(record[3]) + "    " + str(record[4]) + "    " + str(record[8]) + "    " + str(record[9]) + "    " + str(record[10])+ "    " + str(record[11]) + "     " + str(record[15]) + "\n")


			conn.commit()
			conn.close()

			self.searchBox.delete(0, END)

		elif search == "Children":
			c.execute("SELECT *, oid FROM personnel WHERE children > 0")
			personnel_records = c.fetchall()
			self.dataList.delete(0, END)

			self.dataList.insert(END, "PERSONNEL  |  With Children")
			self.dataList.insert(END, "\n" + "\n")
			self.dataList.insert(END, "Id." + "    " + "Full name" + "    " + "Marital Status" + "    " + "No. of Children" + "    " + "Department" + "    " + "Position" + "    " + "Salary" + "    " + "Contract type" + "    " + "Status")
			self.dataList.insert(END, "\n" + "\n")

			for record in personnel_records:
				self.dataList.insert(END, str(record[16])+ "    " + str(record[0]) + "    " + str(record[3]) + "    " + str(record[4]) + "    " + str(record[8]) + "    " + str(record[9]) + "    " + str(record[10])+ "    " + str(record[11]) + "     " + str(record[15]) + "\n")


			conn.commit()
			conn.close()

			self.searchBox.delete(0, END)

		elif search == "Accounts and Finance" or search == "Administration" or search == "Human Ressources" or search == "Sales and Marketing" or search == "Information and Technology" or search == "Product Development" or search == "Reseach and Development" or search == "Logistics and Transport":
			c.execute("SELECT *, oid FROM personnel WHERE department = ?", (search,))
			personnel_records = c.fetchall()
			self.dataList.delete(0, END)

			self.dataList.insert(END, "PERSONNEL  |  by Department")
			self.dataList.insert(END, "\n" + "\n")
			self.dataList.insert(END, "Id." + "    " + "Full name" + "    " + "Gender" + "    " + "Department" + "    " + "Position" + "    " + "Salary" + "    " + "Status")
			self.dataList.insert(END, "\n" + "\n")

			for record in personnel_records:
				self.dataList.insert(END, str(record[16])+ "    " + str(record[0]) + "    " + str(record[1]) + "    " + str(record[8]) + "    " + str(record[9]) + "    " + str(record[10])+ "    " + str(record[15]) + "\n")


			conn.commit()
			conn.close()

			self.searchBox.delete(0, END)

		elif search == "Internship" or search == "Temporary" or search == "Permanent":
			c.execute("SELECT *, oid FROM personnel WHERE contract_type = ?", (search,))
			personnel_records = c.fetchall()
			self.dataList.delete(0, END)

			self.dataList.insert(END, "PERSONNEL  |  Contract type")
			self.dataList.insert(END, "\n" + "\n")
			self.dataList.insert(END, "Id." + "    " + "Full name" + "    " + "Department" + "    " + "Position" + "    " + "Salary" + "    " + "Contract type" + "    " + "Status")
			self.dataList.insert(END, "\n" + "\n")

			for record in personnel_records:
				self.dataList.insert(END, str(record[16])+ "    " + str(record[0]) + "    " + str(record[8]) + "    " + str(record[9]) + "    " + str(record[10])+ "    " + str(record[11]) + "     " + str(record[15]) + "\n")


			conn.commit()
			conn.close()

			self.searchBox.delete(0, END)
			
		elif search == "Hired" or search == "Fired" or search == "Deceased" or search == "Left":
			c.execute("SELECT *, oid FROM personnel WHERE status = ?", (search,))
			personnel_records = c.fetchall()
			self.dataList.delete(0, END)

			self.dataList.insert(END, "PERSONNEL  |  Status")
			self.dataList.insert(END, "\n" + "\n")
			self.dataList.insert(END, "Id." + "    " + "Full name" + "    " + "Department" + "    " + "Position" + "    " + "Salary" + "    " + "Contract type" + "    " + "Status")
			self.dataList.insert(END, "\n" + "\n")

			for record in personnel_records:
				self.dataList.insert(END, str(record[16])+ "    " + str(record[0]) + "    " + str(record[8]) + "    " + str(record[9]) + "    " + str(record[10])+ "    " + str(record[11]) + "     " + str(record[15]) + "\n")


			conn.commit()
			conn.close()

			self.searchBox.delete(0, END)
			

		else : 

			c.execute("SELECT *, oid FROM personnel WHERE fullname = ?", (search,))
			personnel_records = c.fetchall()
		

			self.dataList.delete(0, END)

			self.dataList.insert(END, "PERSONNEL  |  Searched")
			self.dataList.insert(END, "\n" + "\n")
			self.dataList.insert(END, "Id." + "    " + "Full name" + "    " + "Mobile" + "    " + "E-mail" + "    " + "Department" + "    " + "Position" + "    " + "Salary" + "    " + "Contract type" + "    " + "Status")
			self.dataList.insert(END, "\n" + "\n")

			for record in personnel_records:
				self.dataList.insert(END, str(record[16])+ "    " + str(record[0]) + "    " + str(record[1]) + "    " + str(record[3]) + "    " + str(record[4]) + "    " + str(record[5]) + "    " + str(record[6]) + "    "  + str(record[8]) + "    " + str(record[9]) + "    " + str(record[10])+ "    " + str(record[11]) + "     " + str(record[15]) + "\n")


			conn.commit()
			conn.close()

			self.searchBox.delete(0, END)



	def query_personalDetails(self):

		conn = sqlite3.connect('kits_data.db')
		c = conn.cursor()

		c.execute("SELECT *, oid FROM personnel")
		personnel_records = c.fetchall()
		

		self.dataList.delete(0, END)

		self.dataList.insert(END, "PERSONNEL  |  Personal details")
		self.dataList.insert(END, "\n" + "\n")
		self.dataList.insert(END, "Id." + "    " + "Full name" + "    " + "Gender" + "    " + "Date of birth" + "    " + "Marital status" + "    " + "No. of Children" + "    " + "Address" + "    " + "Position" + "    " + "Status")
		self.dataList.insert(END, "\n" + "\n")

		for record in personnel_records:
			self.dataList.insert(END, str(record[16])+ "    " + str(record[0]) + "    " + str(record[1]) + "    " + str(record[2]) + "    " + str(record[3]) + "    " + str(record[4]) + "    " + str(record[7])+ "    "  + str(record[9])+ "    " + str(record[15]) + "\n")


		conn.commit()
		conn.close()

	
	def updateWin(self):

		global employee_id

		editor = Toplevel(self.master)
		gui = Updateemployee(editor)
		
		conn = sqlite3.connect('kits_data.db')
		c = conn.cursor()

		employee_id = self.empID.get()

		c.execute("SELECT * from personnel WHERE oid = ?", (employee_id,))

		records = c.fetchall()


		for record in records:
			fullnameEditor.insert(0, record[0])
			genderSelectEditor.set(record[1])
			dobEditor.insert(0, record[2])
			marital_statusSelectEditor.set(record[3])
			childrenEditor.insert(0, record[4])
			mobileEditor.insert(0, record[5])
			emailEditor.insert(0, record[6])
			addressEditor.insert(0, record[7])
			departmentSelectEditor.set(record[8])
			positionEditor.insert(0, record[9])
			salaryEditor.insert(0, record[10])
			contract_typeSelectEditor.set(record[11])
			start_dateEditor.insert(0, record[12])
			end_dateEditor.insert(0, record[13])
			statusSelectEditor.set(record[15])
	

		conn.commit()
		conn.close()

		self.empID.delete(0, END)
		

	def delete(self):

		response = messagebox.askyesno('Delete Record', 'Do you want to delete this record?')

		if response == 1:
			conn = sqlite3.connect('kits_data.db')
			c = conn.cursor()

			c.execute("DELETE from personnel WHERE oid = " + self.empID.get())

			self.empID.delete(0, END)

			
			conn.commit()
			conn.close()
			response = messagebox.showinfo('Delete Record', 'Record deleted successfully!')

	def clear(self):
		self.dataList.delete(0, END)

	def exit(self):
		self.master.destroy()

	conn.commit()
	conn.close()


# Update Personnel =========================================================================================================================================================================================================================================================================================================================================================

class Updateemployee():

	def __init__(self, master):

		self.master = master
		self.master.geometry('340x500+500+50')
		self.master.title('KMS - Update Employee')
		self.master.iconbitmap('kits.ico')

		global fullnameEditor
		global genderSelectEditor
		global dobEditor
		global marital_statusSelectEditor
		global childrenEditor
		global mobileEditor
		global emailEditor
		global addressEditor
		global departmentSelectEditor
		global positionEditor
		global salaryEditor
		global contract_typeSelectEditor
		global start_dateEditor
		global end_dateEditor
		global renewedEditor
		global statusSelectEditor


		def update():
			
			conn = sqlite3.connect('kits_data.db')
			c = conn.cursor()

			empid = employee_id


			c.execute(""" UPDATE personnel SET
				fullname = :fullname,
				gender = :gender,
				dob = :dob,
				marital_status = :marital_status,
				children = :children,
				mobile = :mobile,
				email = :email,
				address = :address,
				department = :department,
				position = :position,
				salary = salary,
				contract_type = :contract_type,
				start_date = start_date,
				end_date = :end_date,
				renewed = :renewed,
				status = :status
				WHERE oid = :empid """,
				{
				'fullname': fullnameEditor.get(),
				'gender': genderSelectEditor.get(),
				'dob': dobEditor.get(),
				'marital_status': marital_statusSelectEditor.get(),
				'children': childrenEditor.get(),
				'mobile': mobileEditor.get(),
				'email': emailEditor.get(),
				'address': addressEditor.get(),
				'department': departmentSelectEditor.get(),
				'position': positionEditor.get(),
				'salary': salaryEditor.get(),
				'contract_type': contract_typeSelectEditor.get(),
				'start_date': start_dateEditor.get(),
				'end_date':end_dateEditor.get(),
				'renewed': renewedEditor.get(),
				'status': statusSelectEditor.get(),
				'empid': empid
				})
	

			conn.commit()
			conn.close()

			self.master.destroy()
			updatemessage = messagebox.showinfo("Updated", "Employee updated successfully!")


		fullnameLabel = Label(self.master, text = "Full name", font =('Helvetica', 12, 'bold')).grid(row = 2, column = 0, sticky = W)
		genderLabel = Label(self.master, text = "Gender", font =('Helvetica', 12, 'bold')).grid(row = 3, column = 0, sticky = W)
		dobLabel = Label(self.master, text = "Date of birth", font =('Helvetica', 12, 'bold')).grid(row = 4, column = 0, sticky = W)
		marital_statusLabel = Label(self.master, text = "Marital status", font =('Helvetica', 12, 'bold')).grid(row = 5, column = 0, sticky = W)
		childrenLabel = Label(self.master, text = "No. of Children", font =('Helvetica', 12, 'bold')).grid(row = 6, column = 0, sticky = W)
		mobileLabel = Label(self.master, text = "Mobile no.", font =('Helvetica', 12, 'bold')).grid(row = 7, column = 0, sticky = W)
		emailLabel = Label(self.master, text = "E-mail", font =('Helvetica', 12, 'bold')).grid(row = 8, column = 0, sticky = W)
		addressLabel = Label(self.master, text = "Address", font =('Helvetica', 12, 'bold')).grid(row = 9, column = 0, sticky = W)
		departmentLabel = Label(self.master, text = "Department", font =('Helvetica', 12, 'bold')).grid(row = 10, column = 0, sticky = W)
		positionLabel = Label(self.master, text = "Position", font =('Helvetica', 12, 'bold')).grid(row = 11, column = 0, sticky = W)
		salaryLabel = Label(self.master, text = "Salary ($)", font =('Helvetica', 12, 'bold')).grid(row = 12, column = 0, sticky = W)
		contract_typeLabel = Label(self.master, text = "Contract type", font =('Helvetica', 12, 'bold')).grid(row = 13, column = 0, sticky = W)
		startLabel = Label(self.master, text = "Start date", font =('Helvetica', 12, 'bold')).grid(row = 14, column = 0, sticky = W)
		endLabel = Label(self.master, text = "End date", font =('Helvetica', 12, 'bold')).grid(row = 15, column = 0, sticky = W)
		renewedLabel = Label(self.master, text = "Contract renewal", font =('Helvetica', 12, 'bold')).grid(row = 16, column = 0, sticky = W)
		statusLabel = Label(self.master, text = "Status", font =('Helvetica', 12, 'bold')).grid(row = 17, column = 0, sticky = W)


		genderSelectEditor = StringVar()
		genderSelectEditor.set("Male")

		marital_statusSelectEditor = StringVar()
		marital_statusSelectEditor.set("Single")

		departmentSelectEditor = StringVar()
		departmentSelectEditor.set("None")

		contract_typeSelectEditor = StringVar()
		contract_typeSelectEditor.set("None")

		statusSelectEditor = StringVar()
		statusSelectEditor.set("Off")

		fullnameEditor = Entry(self.master, width = 25, bd = 1, font = ('Helvetica', 10))
		fullnameEditor.grid(row = 2, column = 1)
		genderEditor = OptionMenu(self.master, genderSelectEditor, "Male", "Female")
		genderEditor.grid(row = 3, column = 1)
		dobEditor = Entry(self.master, width = 25, bd = 1, font = ('Helvetica', 10))
		dobEditor.grid(row = 4, column = 1)
		marital_statusEditor = OptionMenu(self.master, marital_statusSelectEditor, "Single", "Married", "Divorced")
		marital_statusEditor.grid(row = 5, column = 1)
		childrenEditor = Entry(self.master, width = 25, bd = 1, font = ('Helvetica', 10))
		childrenEditor.grid(row = 6, column = 1)
		mobileEditor = Entry(self.master, width = 25, bd = 1, font = ('Helvetica', 10))
		mobileEditor.grid(row = 7, column = 1)
		emailEditor = Entry(self.master, width = 25, bd = 1, font = ('Helvetica', 10))
		emailEditor.grid(row = 8, column = 1)
		addressEditor = Entry(self.master, width = 25, bd = 1, font = ('Helvetica', 10))
		addressEditor.grid(row = 9, column = 1)
		departementEditor = OptionMenu(self.master, departmentSelectEditor, "None", "Accounts and Finance", "Administration", "Human Ressources", "Sales and Marketing", "Information and Technology", "Product Development", "Reseach and Development", "Logistics and Transport")
		departementEditor.grid(row = 10, column = 1)
		positionEditor = Entry(self.master, width = 25, bd = 1, font = ('Helvetica', 10))
		positionEditor.grid(row = 11, column = 1)
		salaryEditor = Entry(self.master, width = 25, bd = 1, font = ('Helvetica', 10))
		salaryEditor.grid(row = 12, column = 1)
		contract_typeEditor = OptionMenu(self.master, contract_typeSelectEditor, "None", "Internship", "Temporary", "Permanent")
		contract_typeEditor.grid(row = 13, column = 1)
		start_dateEditor = Entry(self.master, width = 25, bd = 1, font = ('Helvetica', 10))
		start_dateEditor.grid(row = 14, column = 1)
		end_dateEditor = Entry(self.master, width = 25, bd = 1, font = ('Helvetica', 10))
		end_dateEditor.grid(row = 15, column = 1)
		renewedEditor = Entry(self.master, width = 25, bd = 1, font = ('Helvetica', 10))
		renewedEditor.grid(row = 16, column = 1)
		statusEditor = OptionMenu(self.master, statusSelectEditor, "Off", "Hired", "Fired" ,"Left", "Deceased")
		statusEditor.grid(row = 17, column = 1)

		addBtnEditor = Button(self.master, text = "Update", command = update , width = 17, font = ("Helvetica", 12, "bold"), bg = "#09383d", fg = "#ffffff")
		addBtnEditor.grid(row = 18, column = 1, pady = 10)


# Maintenance Window =========================================================================================================================================================================================================================================================================================================================================================

class Maintenance():

	def __init__(self, master):

		self.master = master
		self.master.geometry('250x100+31+545')
		self.master.title('KMS - Maintenance')
		self.master.iconbitmap('kits.ico')

		def backup():
			run('git init')
			run('git remote add origin https://github.com/michaelkamande/db.git')
			run('git add .gitignore')
			run('git add kits_data.db')
			run('git commit -m "Database backup"')
			run('git push origin master')
			run('cp kits_data.db ./db')

		def restore():
			run('git init')
			run('git remote add origin https://github.com/michaelkamande/db.git')
			run('git pull origin master')

		self.backupBtn = Button(self.master, text = "Back up", command = backup, width = 10, font = ('Helvetica', 10, 'bold'), bg = "#09383d", fg = "#ffffff")
		self.backupBtn.grid(row = 0, column = 0, pady = 25, padx = 20)
		self.restoreBtn = Button(self.master, text = "Restore", command = restore, width = 10, font = ('Helvetica', 10, 'bold'), bg = "#b1030d", fg = "#ffffff")
		self.restoreBtn.grid(row = 0, column = 1)


def main():
	root = Tk()
	loginGUI = Login(root)
	root.mainloop()


if __name__ == '__main__':
	main()