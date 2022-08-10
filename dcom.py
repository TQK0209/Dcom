from pywinauto import Application
path_dcom = "C:/Program Files (x86)/Kcell/Kcell Connect.exe"
app = Application(backend="uia").start(path_dcom)
app.window(ti)