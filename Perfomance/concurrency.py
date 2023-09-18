# import time
#
#
# # This is a prototype of a network IO type function
# def network_request(number):
#     time.sleep(3.0)
#     return {"success": True, "result": number ** 2}
#
#
# def fetch_square(number):
#     response = network_request(number)
#     if response["success"]:
#         print("Result is: \
#         {}".format(response["result"]))
#
# fetch_square(3)
# fetch_square(6)

################################################
# Implementing threading via callback

import threading


def network_request(number):
    def callback():
        print({"success": True, "result": number ** 2})

    timer = threading.Timer(3.0, callback)
    timer.start()


network_request(3)
network_request(6)
print("After submission")

################################################
# Implementing threading via Futures

