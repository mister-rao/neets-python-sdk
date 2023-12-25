

chat 

```bash
neets chat -p "Describe the size of a large elephant"
neets chat --prompt "Describe the size of a large elephant"
neets chat -p "Describe the size of a large elephant" -m "mistralai/Mixtral-8X7B-Instruct-v0.1" 
neets chat -p "Describe the size of a large elephant" --model "mistralai/Mixtral-8X7B-Instruct-v0.1" 
neets chat -p "Describe the size of a large elephant" -m "mistralai/Mixtral-8X7B-Instruct-v0.1" -quiet
neets chat -p "Describe the size of a large elephant" -q
neets chat -p "Describe the size of a large elephant" --max-tokens 400 
neets chat -p "Describe the size of a large elephant" -mt 600 
neets chat -p "Describe the size of a large elephant" -mt 600  -m "mistralai/Mixtral-8X7B-Instruct-v0.1" -q
```

tts
```bash
neets tts --voice "tucker-carlson"  --text "Why do they want to demonize zyn?"
neets tts -v "tucker-carlson"  -t "Why do they want to demonize zyn?"
neets tts -v "tucker-carlson"  -t "Why do they want to demonize zyn?" --output-file "tucker-carlson.mp3"
neets tts -v "tucker-carlson"  -t "Why do they want to demonize zyn?" --output-file "tucker-carlson.wav"
neets tts -v "tucker-carlson"  -t "Why do they want to demonize zyn?" --output-fmt "mp3" 
neets tts -v "tucker-carlson"  -t "Why do they want to demonize zyn?" --output-fmt "wav" 
```