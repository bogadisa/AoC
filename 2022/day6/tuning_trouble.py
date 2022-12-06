filename = "datastream.txt"  

with open(filename, "r") as f:
    line = f.readline().strip()
    
    packet_marker = line[:4]
    packet_marker_found = False
    message_marker = line[:14]
    for i, char in enumerate(line):
        if not(packet_marker_found):
            if char in packet_marker:
                packet_marker = packet_marker[1:] + char
            else:
                done = True
                packet_marker = packet_marker[1:] + char
                for packet_marker_char in packet_marker:
                    if packet_marker.count(packet_marker_char) > 1:
                        done = False
                        break
                if done:
                    packet_marker_i = i + 1
                    packet_marker_found = True

        if char in message_marker:
            message_marker = message_marker[1:] + char
        else:
            done = True
            message_marker = message_marker[1:] + char
            for message_marker_char in message_marker:
                if message_marker.count(message_marker_char) > 1:
                    done = False
                    break
            if done:
                message_marker_i = i +1
                break

    print(packet_marker, packet_marker_i)
    print(message_marker, message_marker_i)
