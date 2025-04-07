import re

# Mapping of header paths to replacements (handles both <> and "")
header_replacements = {
    r'#include\s+[<"]cJSON.h[>"]': '#include <cjson/CJSON.h>',
    r'#include\s+[<"]paho-mqtt/MQTTClient.h[>"]': '#include <MQTTClient.h>',
    r'#include\s+[<"]rabbitmq-c/amqp.h[>"]': '#include <amqp.h>',
    r'#include\s+[<"]libjpeg/jpeglib.h[>"]': '#include <jpeglib.h>',
    r'#include\s+[<"]paho-mqtt3c/MQTTClient.h[>"]': '#include <paho-mqtt/MQTTClient.h>',
    r'#include\s+[<"]paho-mqtt3a/MQTTClient.h[>"]': '#include <paho-mqtt/MQTTClient.h>',
}
def replace_headers_in_output(output):
    """Replace headers that are problematic"""
    #output = entry.get("output", "")
    for pattern, replacement in header_replacements.items():
        matches = re.findall(pattern, output)
        if matches:
            output = re.sub(pattern, replacement, output)
    #entry["output"] = output
    return output