########################################
#///////////////////////////////////////
# 
# The stracture of plc in opc ua is looklike of tree
# first connect to plc and get node then get_childrens()
# for better UI in first use , use opcua_client to find
# your path in plc and get right node Here in code just 
# find and get the right path of variable in plc
# 
#       youtube link : https://www.youtube.com/watch?v=o-mXEqElVXY
#       git hub : https://github.com/FreeOpcUa
#
#
#///////////////////////////////////////
########################################

# This is a sample of get a Variabble


from opcua import Client, ua    
import threading
import time



client=Client("opc.tcp://192.168.0.1:4840")          # plc IP and Port
client.connect()


name_spaces=client.get_namespace_array()                         # get base details op plc   check connection
print('name_spaces',name_spaces)

objects = client.get_objects_node()
print(objects)


tempsens=objects.get_children()[2]
print(tempsens)

tempsens=tempsens.get_children()
print(tempsens)

tempsens=tempsens[0].get_children()
print(tempsens)

tempsens=tempsens[8]

def set_value():
    import time
    i=0
    while True: 
        if i%2==0:
            value_=True
        else:
            value_=False
        value = ua.DataValue(ua.Variant(value_,ua.VariantType.Boolean))
        tempsens.set_value(value)
        i+=1

        #print('asd')

        time.sleep(1)


def get_values_plc():
    import time
    while True:
        print(tempsens.get_value())
        time.sleep(1)
get_values_plc()

# threading.Thread(target=set_value(),args=None)
#threading.Thread(target=get_values_plc(),args=None)