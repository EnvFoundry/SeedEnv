"""Exchange an explicitly synthetic frame using python-can's virtual backend."""
import json
import uuid
import can

channel = 'seedenv-' + uuid.uuid4().hex
with can.Bus(interface='virtual', channel=channel) as sender, \
        can.Bus(interface='virtual', channel=channel) as receiver:
    sent = can.Message(arbitration_id=0x123, data=[0x09, 0xC4], is_extended_id=False)
    sender.send(sent, timeout=1)
    received = receiver.recv(timeout=1)
    if received is None or received.data != sent.data or received.arbitration_id != sent.arbitration_id:
        raise RuntimeError('The virtual bus did not return the frame')
    # The example protocol declares unsigned big-endian hundredths of a kelvin.
    print(json.dumps({'mode': 'virtual', 'id': received.arbitration_id,
                      'raw': list(received.data), 'synthetic_temperature_K':
                      int.from_bytes(received.data, 'big') / 100}))
