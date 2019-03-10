# flask_pywebview_pyinstaller
### Just seeing if I can compile a simple flask app run via pywebview into a single file exe using pyinstaller

## Clone the GIT repository

```powershell
git clone https://github.com/miahnelson/flask_pywebview_pyinstaller
```
![alt text](./img/git_clone.jpg?style=centerme)

## Setup and activate the virtual enviroment
This will setup the virtual environment and install all the dependencies. 
```powershell
pipenv install
pipenv shell
```
![alt text](./img/pipenv_install.jpg?style=centerme)


## Run pyinstaller with the included spec file to compile the app
```powershell
pyinstaller test.spec
```
![alt text](./img/pyinstaller_test.jpg?style=centerme)

## test.exe will be built in the ./dist folder

![alt text](./img/Built.jpg?style=centerme)

## Run the app to see the output

![alt text](./img/App.jpg?style=centerme)

# Issues
### In order to compile correctly, I had to add the following highlighted entries to the spec file prior to running 'pyinstaller test.spec'

![alt text](./img/specfile_additions.jpg?style=centerme)

