import os
class gitdownload:
    def __init__(self, url, project, app, gitpath, worktree):
        self.url = url
        self.app = app
        self.worktree = worktree
        self.gitpath = gitpath
        self.project = project
    def clone(self):
        try:
            #判斷目錄不存在
            if not os.path.exists('{}/{}'.format(self.gitpath, self.project)):
                #makedirs = mkdir -p
                os.makedirs('{}/{}'.format(self.gitpath, self.project))
            os.chdir('{}/{}'.format(self.gitpath, self.project))
            if not os.path.exists(self.app):
                os.system('/bin/git clone {} {}'.format(self.url, self.app))
            else:
                print('git already')
        except Exception:
            print('clone false')
            exit()
    def changepath(self):
        #判斷目錄不存在
        if not os.path.exists('{}/{}/{}'.format(self.worktree, self.project, self.app)):
            os.makedirs('{}/{}/{}'.format(self.worktree, self.project, self.app))
        #判斷目錄是否為空
        if os.listdir('{}/{}/{}/.git'.format(self.gitpath, self.project, self.app)):
            try:
                os.chdir('{}/{}'.format(self.gitpath, self.project))
                os.system('mv {app}/* {worktree}/{pro}/{app}'.format(pro=self.project, app=self.app, worktree=self.worktree))
                os.system('mv {i}/.git/* {i}'.format(i=self.app))
                os.system('git --git-dir={app} config core.worktree {worktree}/{pro}/{app}'.format(pro=self.project, app=self.app, worktree=self.worktree))
            except OSError as e:
                print(e)
        else:
            print('worktree already')
class WM:
    #project = list()
    #app = list()
    def __init__(self):
        self.project = str()
        self.app = list()
    def pro(self):
        a = str(input('project #w1/w3 \nEnter: '))
        self.project = '%s' % a
        return self.project
    def apps(self):
        while True:
            a = str(input('app name #api/a168 \nEnter: '))
            self.app.append(a)
            b = str(input('continue #yes/no \nEnter: '))
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
            f.write('tbonline\n')
            for i in self.app:
                f.write('%s\n' % i)
    def hosts(self):
        IP = str(input('Rsync hosts IP? :'))
        with open('{}/{}-host.txt'.format(self.conf_path, self.project), 'w') as f:
            f.write('%s' % IP)

if __name__ == '__main__':
    user = 'a168-rp'
    passwd = 'XapfHLP4'
    gitapp = 'a168'
    gitpro = 'w3'
    url = 'http://{u}:{p}@igofun.net:30000/{r}/{r}-{a}.git'.format(u=user, p=passwd, r=gitpro, a=gitapp)
    worktree = '/home/work/test'
    gitpath = '/home/work/test2'
    git = gitdownload(url=url, project=gitpro, app=gitapp, gitpath=gitpath, worktree=worktree)
    git.clone()
    git.changepath()

    
    
    