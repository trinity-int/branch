# Branch

## Setup

```
#Install Git
https://git-scm.com/downloads

#Install Python with custom installation 
https://www.python.org/downloads/

#fork the repo
In the top right of your page, click on the fork button. 
If you don't know what forking means read this: 
https://help.github.com/en/articles/fork-a-repo

#clone the repo
On the the page of your forked repo click on the green button that says "Clone or download". 
Copy the link in the menu that pops up.
Open up your terminal and go to the folder you want to clone this project.
Run the command:
git clone https://github.com/trinity-int/branch.git
This link is the link you copied from the "Clone or download" button

In your terminal: 

#Go into the project folder you just cloned
cd branch

#Create a remote of the repo you forked from
git remote add upstream https://github.com/trinity-int/branch.git
```

## Pushing/Pulling 
```

```

## Start
```
In your terminal: 

#Set environments
Windows PowerShell:
$env:FLASK_APP = "flaskr"
$env:FLASK_ENV = "development"

Mac Terminal/Linux: 
export FLASK_APP=flaskr
export FLASK_ENV=development

# Start the project
flask run
```
