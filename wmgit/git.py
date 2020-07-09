import os
class gitdownload:
    def __init__(self, url, project, app, gitpath, worktree):
        self.url = url
        self.app = app
        self.project = project
        if self.app == 'tbonline':
            self.worktree = worktree
            self.gitpath = gitpath
        else:
            self.worktree = '{}/{}'.format(worktree, project)
            self.gitpath = '{}/{}'.format(gitpath, project)
    def clone(self):
        try:
            #判斷目錄不存在
            if not os.path.exists('{}'.format(self.gitpath)):
                #makedirs = mkdir -p
                os.makedirs('{}'.format(self.gitpath))
            os.chdir('{}'.format(self.gitpath))
            if not os.path.exists(self.app):
                os.system('/bin/git clone {} {}'.format(self.url, self.app))
            else:
                print('git already')
        except Exception:
            print('clone false')
            exit()
    def changepath(self):
        #判斷目錄不存在
        if not os.path.exists('{}/{}'.format(self.worktree, self.app)):
            os.makedirs('{}/{}'.format(self.worktree, self.app))
        #判斷目錄是否為空
        try:
            if os.listdir('{}/{}/.git'.format(self.gitpath, self.app)):
                os.chdir('{}'.format(self.gitpath))
                os.system('mv {app}/* {worktree}/{app}'.format(app=self.app, worktree=self.worktree))
                os.system('mv {i}/.git/* {i}'.format(i=self.app))
                os.system('git --git-dir={app} config core.worktree {worktree}/{app}'.format(app=self.app, worktree=self.worktree))
            else:
                print('worktree already')
        except OSError as e:
                print(e)
class WM:
    #project = list()
    #app = list()
    def __init__(self):
        self.project = str()
        self.app = list()
    def pro(self):
        a = str(input('專案名稱 如 #w1/w3 \nEnter: '))
        self.project = '%s' % a
        return self.project
    def apps(self):
        print('-----第一個APP請輸入tbonline!!!----')
        while True:
            a = str(input('請輸入app 名稱如 #api/a168 \nEnter: '))
            self.app.append(a)
            b = str(input('是否繼續 #yes/no \nEnter: '))
            if b == 'no':
                break
        return self.app
class rsync_conf:
    def __init__(self, conf_path, app, project):
        self.app = app 
        self.project = project
        self.conf_path = conf_path
        if not os.path.exists('{}'.format(self.conf_path)):
            os.makedirs('{}'.format(self.conf_path))
    def folder(self):
        with open('{}/{}-folder.txt'.format(self.conf_path, self.project), 'w') as f:
            #f.write('tbonline\n')
            for i in self.app:
                f.write('%s\n' % i)
    def hosts(self):
        IP = str(input('Rsync hosts IP? :'))
        with open('{}/{}-host.txt'.format(self.conf_path, self.project), 'w') as f:
            f.write('%s' % IP)

if __name__ == '__main__':
    user = 'a168-rp'
    passwd = 'XapfHLP4'
    gitapp = 'tbonline'
    gitpro = 'w3'
    url = 'http://{u}:{p}@igofun.net:30000/a168/{a}.git'.format(u=user, p=passwd, r=gitpro, a=gitapp)
    worktree = '/home/work/test'
    gitpath = '/home/work/test2'
    git = gitdownload(url=url, project=gitpro, app=gitapp, gitpath=gitpath, worktree=worktree)
    git.clone()
    git.changepath()

    
    
    