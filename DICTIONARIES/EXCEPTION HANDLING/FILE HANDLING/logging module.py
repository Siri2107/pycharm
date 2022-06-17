import logging
logging.basicConfig(filename="7pmlog.txt",level=logging.DEBUG)
# logging.critical("This is an critical msg")
# logging.error("this is an error mdg")
# logging.warning("this is an wraning msg")
# logging.info("this is an info msg")
# logging.debug("this is an debug msg")
# print("log file is created")




username=input("enter the username")
try:
    logging.info(username+"logged in succesfully")
    a=int(input("enter the number"))
    b=int(input("enter the number"))
    print(a//b)
    logging.info("dividion completed successfully")
except:
    print("error in the code")
    logging.error("user has given alphanumeric and zero values")
finally:
    print("code executed")
    logging.info(username+"logged out successfully") 