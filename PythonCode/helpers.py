from colorama import Fore
# colorama 打印颜色


def display(message, is_warning=False):
    if is_warning:
        print(Fore.RED + message)
    else:
        print(Fore.BLUE + message)
