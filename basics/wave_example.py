import wave

obj = wave.open("./Sports.wav", "rb") #read binary
print("Number of channels", obj.getnchannels())
print("Sample width", obj.getsampwidth())
print("Frame rate", obj.getframerate())
print("Number of channels", obj.getnchannels())
print("Parameters", obj.getparams())

with wave.open("./Sports.wav", "rb") as audio_file:
    num_channels = audio_file.getnchannels()
    print("Number of channels:", num_channels)

    sample_width =  audio_file.getsampwidth()
    print("Sample width (bytes):", sample_width)

    frame_rate = audio_file.getframerate()
    print("Frame rate:", frame_rate)
    
    num_frames = audio_file.getnframes()
    print("Number of frames:", num_frames)

    params = audio_file.getparams()
    print("Parameters:", params )

    t_audio = audio_file.getnframes() / audio_file.getframerate()
    print(t_audio)

    frames = audio_file.readframes(-1)
    print(type(frames), type(frames[0]))
    print(len(frames) / 2)

obj_new = wave.open("./Sports_new.wav", "wb") # write back
obj_new.setnchannels(1)
obj_new.setsampwidth(2)
obj_new.setframerate(48000)
obj_new.writeframes(frames)
obj_new.close()