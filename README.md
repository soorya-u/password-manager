# **Password Manager**

## About Project

**Description**: The password manager is a Python project that securely stores and manages user passwords. It allows users to store their passwords for various accounts, generate strong passwords, and retrieve passwords when needed.

**Scope**: The scope of this project involves implementing encryption algorithms to secure password storage, designing a user interface to input and retrieve passwords, and developing functions to generate strong passwords and store/retrieve them from a database.

**Concepts Used**: The Concepts of *Hashing* and *Encryption* has been used along with the implementation of a *Basic Database* and a *Graphical User Interface*. The Detailed Description of the Project has been given below.

## Modules Used

### Cryptography

`cryptography`[^doc_cryptography] is a package which provides cryptographic recipes and primitives in Python. It is used to Encrypt and Decrypt User Passwords using a Unique Key.

### Database

`sqlite3`[^doc_sqlite3] is a C-language library that implements a small, fast, self-contained, high-reliability, full-featured, SQL database engine. It is used to store and maintain datas recieved from the user.

### Graphical User Interface

`Tkinter`[^doc_Tkinter] is the standard GUI library for a fast and easy way to create GUI applications. It is used to create a Simple Graphical User Interface for the Application.

### Hashing

`hashlib`[^doc_hashlib] implements a common interface to many different secure hash and message digest algorithms. It is used to hash the Password of our Application and use it for Verification.

### Regular Expression

`re`[^doc_re]  provides regular expression matching operations. It is used to set Rules for Username and Password.

### Other Modules

- `os`[^doc_os]
- `sys`[^doc_sys]
- `PIL`[^doc_PIL]
- `enum`[^doc_enum]
- `random`[^doc_random]
- `wonderwords`[^doc_wonderwords]
- `pyglet`[^doc_pyglet]

## Objectives

### Cryptography Tasks

- [x] Generating Unique Key
- [x] Getting Unique Key
- [x] Destroying Unique Key
- [x] Encryption of Data
- [x] Decryption of Data

### Hashing Tasks

- [x] Creating a Hash
- [x] Verifying a Hash
- [x] Generating a Strong Password

### Database Tasks

- [x] Creating a Default Path of Database inside AppData
- [x] Creation and Initialization of Database
- [ ] Altering Read-Write Permissions of Database
- [x] Establishing Database Connection
- [x] Insertion of User Data
- [x] Insertion of Account Details
- [ ] Adding Characteristics to Table Datas
- [x] Read User Hashed Password
- [x] Read User Unique Key
- [x] Read User First Name
- [x] Read Account Table
- [ ] Delete Account Details
- [ ] Update Account Details

### Regular Expression Tasks

- [x] Setting Master Username Rules
- [x] Setting Master Password Rules

### Graphical User Interface Tasks

- [x] Adding Custom Fonts
- [x] Setting Dimensions for Each Window
- [x] Initialization of Images For Login and Register Window
- [x] Initialization of Images For Account Form Window and Dropdown Subwindow
- [x] Clearing Images
- [x] SignIn Window
- [x] SignUp Window
- [x] Successfull Message
- [x] Unsuccessfull Message
- [ ] Display All Errors done by Users
- [x] Welcome Message
- [x] Account Form Window
- [x] Table Subwindow
- [ ] Dropdown Subwindow

### Others

- [x] Login to Register Shifter
- [x] Register to Login Shifter
- [x] SignIn Backend Function
- [x] SignUp Backend Function
- [x] Login and Register Main Function
- [x] Account Form Function
- [x] Account List Function

[^doc_cryptography]: [*cryptography*](https://cryptography.io/en/latest/)
[^doc_sqlite3]: [*sqlite3*](https://docs.python.org/3/library/sqlite3.html)
[^doc_Tkinter]: [*Tkinter*](https://docs.python.org/3/library/tkinter.html)
[^doc_hashlib]: [*hashlib*](https://docs.python.org/3/library/hashlib.html#)
[^doc_re]: [*re*](https://docs.python.org/3/library/re.html)
[^doc_os]: [*os*](https://docs.python.org/3/library/os.html)
[^doc_sys]: [*sys*](https://docs.python.org/3/library/sys.html)
[^doc_PIL]: [*PIL*](https://pypi.org/project/Pillow/)
[^doc_enum]: [*enum*](https://docs.python.org/3/library/enum.html)
[^doc_random]: [*random*](https://docs.python.org/3/library/random.html)
[^doc_wonderwords]: [*wonderwords*](https://pypi.org/project/wonderwords/)
[^doc_pyglet]: [*pyglet*](https://pyglet.org/)
