# django-projects
Initial two Django projects learned from YouTube

********************************************************************************************************************************
關於studybud 

(12/8/2023)

複製 theme 或 user 到  C:\Users\customer\ 之下時 運行 `(env) C:\Users\customer\dev\studybud>python manage.py migrate`

出現 錯誤
`OSError: [WinError 123] The filename, directory name, or volume label syntax is incorrect: '<frozen importlib._bootstrap>' `
但，所以提供的解決方式：執行 `python manage.py migrate`
參考 [sol1](https://stackoverflow.com/questions/56166319/oserror-winerror-123-the-filename-directory-name-or-volume-label-syntax-is)

出現另一錯誤 `ModuleNotFoundError: No module named 'rest_framework'`<br>
解決方式 `(env) C:\Users\customer\dev\studybud>pip install djangorestframework`
參考 [sol2](https://stackoverflow.com/questions/33308781/django-rest-framework-no-module-named-rest-framework)

再次執行 `python manage.py migrate`

又出現另一錯誤 `ModuleNotFoundError: No module named 'corsheaders'`<br>
解決方式 `(env) C:\Users\customer\dev\studybud>pip install django-cors-headers`
參考 [sol3](https://stackoverflow.com/questions/26072426/import-error-django-corsheaders)

又再次執行 <br>
`(env) C:\Users\customer\dev\studybud>python manage.py migrate` 成功 <br>
`(env) C:\Users\customer\dev\studybud>python manage.py makemigrations` 成功 <br>
此時並沒有如參考**sol1**再執行一次 `python manage.py migrate`

最後執行 <br>
`(env) C:\Users\customer\dev\studybud>python manage.py runserver` 成功

(12/8/2023)

複製  資料夾user 到  `C:\Users\customer\dev>` 之下後，運行 `(env) C:\Users\customer\dev\studybud>python manage.py migrate` <br>
出現錯誤 <br>
`django.core.management.base.SystemCheckError: SystemCheckError: System check identified some issues:`<br>
`ERRORS:`<br>
`base.User.avatar: (fields.E210) Cannot use ImageField because Pillow is not installed.`<br>
 `      HINT: Get Pillow at https://pypi.org/project/Pillow/ or run command "python -m pip install Pillow".`<br>
`System check identified 1 issue (0 silenced).`<br>

發現Pillow沒安裝，需要安裝，解決方式 `(env) C:\Users\customer\dev\studybud>python -m pip install Pillow`
