# From Li_xin
* wmgit
```py
工作目錄下新增config.py
class config:
    user = '${user}'
    passwd = '${password}'
    domain = '${git_domain}'
    worktree = '${path}'
    gitpath = '${git_path}'
    conf_path = '${shell_config_path}'
```
* git path
```
git init
git config core.sparseCheckout true
echo 'wmgit/*' > .git/info/sparse-checkout 
git remote add origin https://github.com/rty83924/xin.git
git pull origin master
```
