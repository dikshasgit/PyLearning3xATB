#Main function
def this_is_my_main_fu():
    print("main function")

if __name__ =='__main__':# this will give pyth interpreter that below is the main mention given
    this_is_my_main_fu()


    def f1():
        print("f1")


    def f2():
        print("f2")


    def f3():
        print("f3")


    def main():  # main method
        print("main from 163")


    # python allows to have unlimited main function, multiple main method,/function
    # import the function also allowed
    if __name__ == "__main__":
        main()
        f1()
        f2()
        f3()