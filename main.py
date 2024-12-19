from game.factory import GameComponentFactory

def main():
    # Creating game elements using fabric pattern
    manager = GameComponentFactory.create_manager()
    controller = GameComponentFactory.create_controller(manager)
    ui = GameComponentFactory.create_ui(controller)

    # Running user interface
    ui.run()

if __name__ == "__main__":
    main()
