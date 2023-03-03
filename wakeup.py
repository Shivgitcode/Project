import pvporcupine
from pvrecorder import PvRecorder

for keyword in pvporcupine.KEYWORDS:
    print(keyword)



try:
    recoder.start()
    keyword_index = porcupine.process(recoder.read())
    if keyword_index >= 0:
        print(f"hello world")

except KeyboardInterrupt:
    recoder.stop()
finally:
    porcupine.delete()
    recoder.delete()
