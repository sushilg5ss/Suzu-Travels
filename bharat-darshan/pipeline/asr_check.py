import sys, time
from faster_whisper import WhisperModel
m = WhisperModel(sys.argv[1] if len(sys.argv)>2 else "medium", device="cpu", compute_type="int8")
for f in sys.argv[2:]:
    t=time.time(); segs,_ = m.transcribe(f, language="hi", beam_size=5)
    print(f, round(time.time()-t,1), "|", " ".join(s.text.strip() for s in segs), flush=True)
