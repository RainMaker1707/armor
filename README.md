# ARMOR
**ARMOR** - **A**nalytical **R**esource for **M**onitoring **O**nline **R**isks

This framework is made to manage cyber threats and mitigation techniques.
Its purposes is to provides organisations and entreprises a simple way to share ressources.

This framework will use python3 and json files.
It will need to be downloaded locally to run.

You are allowed to fork this code, or cntribute to this repository actively.

All this project is firstly made to help a cyber assistant, running on GPT4, 
to classify cyber threats and provide mitigation techniques based on the 
threat behavior the user encountered.

## Forewords
As the syntax of STIX2 is pretty heavy ARMOR aims to simplify it.\
ARMOR will use the simplest syntax and object creation to save the 
important parameters of a threat,

Threat and  Mitigation techniques are load from JSON files. Each of these has its own file.\
It is pretty simple to add a threat or a mitigation technique by adding a file in the data directory.
The main  will automaticaly load it.
When the software runs, it is impossible to modify a loaded file.\
It is possile to modify JSON or XML files and then ojects loaded will change in the next run.\


## Immutability
All objects created in the  framework  are immutable. You can add new object 
and delete old one, but mutability evolves risks.
of error that is not acceptable in a CyberSecurity framework.
The only mutable field are:
- Mitigation techniques ID list
- Last modified date

## New objects
Threat and Mitigation  object can be load from three functions:\
`from_scratch`: You will provide all the necessary component from python code\
`from_json`: You will provide a well formatted JSON with all the necessary fields.\
`from_xml`: You will provide a well formatted XML with all the necessary fields.\

**__Examples:__**
```python
threat = Threat()
threat.from_scratch(name="test", behavior="test", ...)
# OR
threat.from_json("JSON/file/path")
# OR
threat.from_xml("XML/file/path")
```

**JSON files format** can be found in `data/JSON/templatet.json`


## Threats

## Mitigation techniques

## Add new file at RunTime 

## Website
### Search for a threat
### Search  for a mitigation technniques
### Add a threat
### Add a mitigation technique

## ChatBot
Explain the behavior of your threat to the chatbot.\
You do not need to startt by "Hello" or something polish as it is a AI that don't care about social interaction.\
The ChatBot will reply with a list of suspected CyberThreatand appropriate mitigation techniques.
The ChatBot Need GPT4 to be used. 
[GPT4 ChatBot URL](https://chat.openai.com/g/g-hMkR7B3Rx-cyberthreat-assistant)
