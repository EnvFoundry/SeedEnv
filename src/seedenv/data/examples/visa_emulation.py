"""A PyVISA transaction against the upstream simulator, without hardware."""
import json
import pyvisa

manager = pyvisa.ResourceManager('@sim')
try:
    with manager.open_resource('ASRL1::INSTR', read_termination='\n',
                               write_termination='\r\n', timeout=1000) as instrument:
        identity = instrument.query('?IDN')
        if not identity.strip():
            raise RuntimeError('The simulated instrument returned no identity')
        print(json.dumps({'mode': 'simulated', 'resource': instrument.resource_name,
                          'identity': identity}))
finally:
    manager.close()
