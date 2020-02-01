from time import sleep


def out_red(text):
    print("\033[31m {}".format(text))


def out_yellow(text):
    print("\033[33m {}".format(text))


def out_green(text):
    print("\033[32m {}".format(text))


class TrafficLight:
    # атрибуты класса
    __light_color = 0

    # методы класса

    def running(self):
        while True:
            out_red("КРАСНЫЙ")
            sleep(7)
            out_yellow("ЖЕЛТЫЙ")
            sleep(2)
            out_green("ЗЕЛЕННЫЙ")
            sleep(7)
            out_yellow("ЖЕЛТЫЙ")
            sleep(2)


obj_traffic = TrafficLight()
obj_traffic.running()
