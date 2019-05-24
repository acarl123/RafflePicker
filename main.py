from wx import App
from maincontroller import Controller

def main():
    app = App()
    controller = Controller()
    controller.show()
    app.MainLoop()

if __name__ == "__main__":
    main()