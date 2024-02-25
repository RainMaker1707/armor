# ARMOR
**ARMOR** - **A**nalytical **R**esource for **M**onitoring **O**nline **R**isks

This framework is made to manage cyber threats and mitigation techniques.
Its purposes is to provides organisations and entreprises a simple way to share ressources.

This framework will use python3 and json files.
It will need to be downloaded locally to run.

You are allowed to fork this code, or cntribute to this repository actively.

All this project is firstly made to help a cyber assistant, running on GPT4, to classify cyber threats and provide mitigation techniques based on the threat behavior the user encountered.


## Immutability
All objects created in the  framework  are immutable. You can add new object annd delete old one, but mutability insert a risk 
of error that is not acceptable in a CyberSecurity framework.
The only mutable field are:
- Mitigation techniques ID list

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

