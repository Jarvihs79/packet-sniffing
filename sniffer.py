from scapy.all import sniff
from flask import Flask, jsonify
from flask_cors import CORS
import threading

app = Flask(__name__)
CORS(app)  # Allow frontend to fetch data

packet_data = []  # Store packets

# Function to process packets
def process_packet(packet):
    packet_info = {
        "protocol": packet.summary().split()[0],  # Extract protocol (TCP/UDP/ICMP)
        "size": len(packet),  # Packet size
    }
    packet_data.append(packet_info)
    print(packet_info)  # Debugging

# Start packet sniffing in a separate thread
def start_sniffing():
    sniff(prn=process_packet, store=False)

@app.route('/packets', methods=['GET'])
def get_packets():
    return jsonify(packet_data[-20:])  # Send last 20 packets

if __name__ == '__main__':
    sniff_thread = threading.Thread(target=start_sniffing, daemon=True)
    sniff_thread.start()
    app.run(host="0.0.0.0", port=5000)
