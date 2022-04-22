> A (semi-commercial) web app written in Flask to create QR-Codes. 

# Project Organization
## Structure  
├───run.sh # 👈🏻 `sh run.sh`
├───app.py
├───requirements.txt
├───migrations # folder created for migrations by calling
├───project # main project folder, sub-components will be in separate folders
│   │   data.sqlite
│   │   models.py
│   │   __init__.py
│   │
│   ├───qrcode
│   │   │   forms.py
│   │   │   views.py
│   │   │
│   │   ├───templates
│   │      └───qrcode
│   │             basicqr.html
│   │             imageqr.html
│   │
│   ├───userdata
│   │   │   forms.py
│   │   │   views.py
│   │   │
│   │   ├───templates
│   │   │   └───userdata
│   │   │           qr.html
│   │   │           create-form.html
│   │   │           get-data.html
│   │
│   ├───static # CSS, JS, Images, Fonts, etc...
│   ├───templates
│          base.html
│          index.html

## Branching Strategy  
... is `GitHub flow`  
## Commit Messages  
- 👨‍💻 = feat (a new feature)  
- 📜 = docs (changes a documentation)  
- 👷‍♀️ = refactor (refactoring production code)  
- 🎬 = test (adding tests, refactoring test, no production code change)  
- 💄 = style (formatting, missing semi colons, etc; no code changes)  
- 🔧 = chore (updating build tasks, package manager configs; no production code change)  