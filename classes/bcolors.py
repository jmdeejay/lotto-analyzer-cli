class bcolors:
    ENDC          = "\033[0m";
    BOLD          = "\033[1m";
    UNDERLINE     = "\033[4m";
    BLACK         = "\033[30m";
    RED           = "\033[31m";
    GREEN         = "\033[32m";
    YELLOW        = "\033[33m";
    BLUE          = "\033[34m";
    PURPLE        = "\033[35m";
    CYAN          = "\033[36m";
    LIGHT_GRAY    = "\033[37m";
    DARK_GRAY     = "\033[90m";
    LIGHT_RED     = "\033[91m";
    LIGHT_GREEN   = "\033[92m";
    LIGHT_YELLOW  = "\033[93m";
    LIGHT_BLUE    = "\033[94m";
    LIGHT_PURPLE  = "\033[95m";
    LIGHT_CYAN    = "\033[96m";
    WHITE         = "\033[97m";

    def output(string, color):
        return color + str(string) + bcolors.ENDC;

    def testColors():
        print(bcolors.BOLD + "BOLD" + bcolors.ENDC);
        print(bcolors.UNDERLINE + "UNDERLINE" + bcolors.ENDC);
        print(bcolors.BLACK + "BLACK" + bcolors.ENDC);
        print(bcolors.RED + "RED" + bcolors.ENDC);
        print(bcolors.GREEN + "GREEN" + bcolors.ENDC);
        print(bcolors.YELLOW + "YELLOW" + bcolors.ENDC);
        print(bcolors.BLUE + "BLUE" + bcolors.ENDC);
        print(bcolors.PURPLE + "PURPLE" + bcolors.ENDC);
        print(bcolors.CYAN + "CYAN" + bcolors.ENDC);
        print(bcolors.LIGHT_GRAY + "LIGHT_GRAY" + bcolors.ENDC);
        print(bcolors.DARK_GRAY + "DARK_GRAY" + bcolors.ENDC);
        print(bcolors.LIGHT_RED + "LIGHT_RED" + bcolors.ENDC);
        print(bcolors.LIGHT_GREEN + "LIGHT_GREEN" + bcolors.ENDC);
        print(bcolors.LIGHT_YELLOW + "LIGHT_YELLOW" + bcolors.ENDC);
        print(bcolors.LIGHT_BLUE + "LIGHT_BLUE" + bcolors.ENDC);
        print(bcolors.LIGHT_PURPLE + "LIGHT_PURPLE" + bcolors.ENDC);
        print(bcolors.LIGHT_CYAN + "LIGHT_CYAN" + bcolors.ENDC);
        print(bcolors.WHITE + "WHITE" + bcolors.ENDC);
