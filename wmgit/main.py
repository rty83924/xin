import git
from config import config

if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    user = config.user
    passwd = config.passwd
    domain = config.domain
    worktree = config.worktree
    gitpath = config.gitpath
    conf_path = config.conf_path
    while True:
        pro = '%s' % git.WM().pro()
        app = git.WM().apps()
        #url = list()
        for j in app:
            if j == 'tbonline':
                url = ('http://{u}:{p}@{d}/a168/{a}.git'.format(u=user, p=passwd, a=j, d=domain))
            else:
                url = ('http://{u}:{p}@{d}/{r}/{r}-{a}.git'.format(u=user, p=passwd, r=pro, a=j, d=domain))
            gitdownload = git.gitdownload(url=url, project=pro, app=j, gitpath=gitpath, worktree=worktree)
            gitdownload.clone()
            gitdownload.changepath()
                #print(url)
        rsync_conf = git.rsync_conf(conf_path=conf_path, app=app, project=pro)
        rsync_conf.folder()
        rsync_conf.hosts()
        while True:
            b = str(input('continue #yes/no \nEnter: '))
            if b == 'yes':
                break
            elif b == 'no':
                exit()
            else:
                print("Enter either yes/no")

