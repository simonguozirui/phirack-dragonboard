import requests
import mraa
print (mraa.getVersion())


ledGreen = mraa.Gpio(27)
ledGreen.dir(mraa.DIR_OUT)
ledGreen.write(0)

ledRed = mraa.Gpio(29)
ledRed.dir(mraa.DIR_OUT)
ledRed.write(0)

buzzer = mraa.Gpio(31)
buzzer.dir(mraa.DIR_OUT)
buzzer.write(0)

while True:
    r = requests.get('https://phiracks-d85c6.firebaseio.com/status.json')
    status = r.json()
    print status
    if status == '1':
        print "status = 1"
        ledGreen.write(1)
        ledRed.write(0)
        buzzer.write(0)
    elif status == '2':
        print "status = 2"
        ledRed.write(1)
        ledGreen.write(0)
        buzzer.write(1)
    elif status == '0':
       print "status = 0"
