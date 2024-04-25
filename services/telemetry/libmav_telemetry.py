#!/usr/bin/python

import datetime
import libmav

if __name__ == "__main__":
    # Load Mavlink XML dialect
    message_set = libmav.MessageSet('mavlink/common.xml')

    # Specify a custom heartbeat
    heartbeat = message_set.create('HEARTBEAT').set_from_dict({
        'type': message_set.enum('MAV_TYPE_LOG'),
        'autopilot': message_set.enum('MAV_AUTOPILOT_INVALID'),
        'base_mode': 0,
        'custom_mode': 0,
        'system_status': message_set.enum('MAV_STATE_ACTIVE')
    })

    # Set up identifier with custom system and component ID
    system_id = 1
    mavlink_identifier = libmav.Identifier(
        system_id, message_set.enum('MAV_COMP_ID_USER1'))

    # Connect to a TCP server
    conn_physical = libmav.TCPClient("172.17.0.1", 5790)
    conn_runtime = libmav.NetworkRuntime(
        mavlink_identifier, message_set, heartbeat, conn_physical)
    connection = conn_runtime.await_connection(2000)

    while True:
        # Wait for battery telemetry
        try:
            received_message = connection.receive("BATTERY_STATUS", 2000)
            print(
                "{} Battery Voltage: {}V".format(
                    datetime.datetime.now(),
                    received_message['voltages'][0] /
                    1000.0))

        except RuntimeError:
            print(
                "{} Not receiving Battery measurements...",
                format(
                    datetime.datetime.now()))

        # Wait for global position
        try:
            received_message = connection.receive("GLOBAL_POSITION_INT", 1000)
            print(
                "{} Global Position: {}° latitude / {}° longitude".format(
                    datetime.datetime.now(),
                    received_message['lat'] / 1e7,
                    received_message['lon'] / 1e7))

        except RuntimeError:
            print(
                "{} Not receiving Global Position yet...",
                format(
                    datetime.datetime.now()))
