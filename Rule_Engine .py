
import datetime
import re
######Different ValueTypes the Signal will take #######
Integer = ['Integer']
MaxIntSignal = 240.00
DateTime = ['Datetime']
String = ['String']
StringValue = ['HIGH', 'LOW']
SignalSeparator = '},'


DataStream = input()

###Reading the date and time of a system #####

LocalTime = datetime.datetime.now()
TempStream = DataStream.replace(SignalSeparator,'}')
Signals = TempStream.split("}")
InValidSignals = []
for Signal in Signals:
    try:
      Elements = Signal.split(',')
      Temp1 = Elements[1].split(':')
      Temp2 = Elements[2].split('":')
      ValueType = Temp1[1].replace('"','').strip()
      Value = Temp2[1].replace('"','').strip()
      InvalidSignal=""
      if (ValueType in Integer) and ((float(Value)) > MaxIntSignal):
         InvalidSignal = Signal+SignalSeparator
      if ((ValueType in DateTime) and (str(LocalTime) < Value)):
        InvalidSignal = Signal + SignalSeparator
      if ValueType in String and (Value not in StringValue):
        InvalidSignal = Signal + SignalSeparator
      if(InvalidSignal != ""):
        InValidSignals.append(InvalidSignal)
    except:
        continue

f= open("InvalidSignals.txt","a+")
f.writelines(["%s\n" % InvalidSignal  for InvalidSignal in InValidSignals])
f.close()




