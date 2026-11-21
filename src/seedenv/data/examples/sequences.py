"""Read a small sequence and preserve its identifier."""
import io
import json
from Bio import SeqIO
from Bio.SeqUtils import gc_fraction

record=SeqIO.read(io.StringIO(">example\nATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG\n"), "fasta")
print(json.dumps({"id":record.id, "length":len(record), "gc_fraction":gc_fraction(record.seq),
                  "protein":str(record.seq.translate())}))
