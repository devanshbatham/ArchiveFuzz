# ArchiveFuzz : hunt the archives

![ArchiveFuzz](https://raw.githubusercontent.com/Grumpy-developer/ArchiveFuzz/master/static/banner.PNG)
# What the heck is this thing ? 

ArchiveFuzz hunts down the archived data(subdomains/emails/API keys) of domains. **Web archiving** is the process of collecting portions of the [World Wide Web](https://en.wikipedia.org/wiki/World_Wide_Web "World Wide Web") to ensure the information is [preserved](https://en.wikipedia.org/wiki/Digital_preservation "Digital preservation") in an [archive](https://en.wikipedia.org/wiki/Archive "Archive") for future researchers, historians, and the public.

This tool uses webarchive's cdx to enumerate Emails/Subdomains/IPs/API tokens .

# But why ?
I initially made ArchiveFuzz for my personal use , Now making it public . This really helped me a lot , Good luck finding potential assets with this <3 

# Example

Lets scan mail.ru for archived secrets :

`python archivehunter.py mail.ru`


![example](https://github.com/Grumpy-developer/ArchiveFuzz/blob/master/static/mailru-example.PNG)

# Compatibility
**It works on anything that has python installed** 

# Installation
`note : it only works with python3.+`

`mkdir Archive-Fuzz`

`cd Archive-Fuzz`

`git clone https://github.com/devanshbatham/ArchiveFuzz`

`virtualenv env `

`source env/bin/activate`

`cd ArchiveFuzz`

`pip install -r requirements.txt`

`python archivefuzz.py example.com`

# TODO
Implementing checks for more API keys that are passed in GET requests.

# Wanna show support for the tool ?

**I will be more than happy if you will show some love for Animals by donating to [Animal Aid Unlimited](https://animalaidunlimited.org/)** **,Animal Aid Unlimited saves animals through street animal rescue, spay/neuter and education. Their mission is dedicated to the day when all living beings are treated with compassion and love.** ✨
