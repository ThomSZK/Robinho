# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
import webrepl
import network
webrepl.start()
sta_if = network.WLAN(network.STA_IF); sta_if.active(True)
sta_if.connect("It hurts when IP 2.4","SzK$45%63@")


#test test