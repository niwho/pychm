# coding: utf-8
import re
from ctypes import *
CAF = WINFUNCTYPE(c_bool,c_char_p)
def callback_t(info):
    print '编译：\t',info
    return True
def callback_t2(info):
    print '进度：\t',info
    return True
class myFile(object):
    def __init__(self):
        self.p0= re.compile(r'\[[\w(),\s"]+\]\s*(HRESULT\s(\w+))\(')
        self.p1=re.compile(r'\[(?:in)?,?(?:out)?,?(?:retval)?\]\s*(\w+\*?\s*(\w+))')
        
        pass
    def compile_t(self,hhpfile):
        ole32=windll.LoadLibrary('ole32.dll')
        ole32. CoInitialize (0)
        hha=windll.LoadLibrary('E:/eclipse_workspace/CHMaker/HHA.DLL')
        print hha
        print 'compile file:',hhpfile
        print hha. HHA_CompileHHP(hhpfile,CAF(callback_t),CAF(callback_t2),0)
        print 'success'
        
    def open_hhp(self,filename):
        self.fin= open(filename,'r')
        
        for lin in self.fin:
            
            matfun=self.p0.search(lin)
            if matfun:
                str_main ='''﻿<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN">
<HTML><HEAD><TITLE>NP_LIVE_PlaybackControl</TITLE>
<META content="text/html; charset=UTF-8" http-equiv=Content-Type>
<META name=GENERATOR content="MSHTML 8.00.7601.17514"><LINK rel=stylesheet 
href="_template.css"></HEAD>''' + '\n<BODY>\
                    \r\n<DIV id=nsbanner>\
                    \r\n<DIV id=bannerrow1>\
                    \r\n<TABLE class=bannerparthead>\
                      \r\n<TBODY>\
                      \r\n<TR id=hdr>\
                    \r\n<TD class=runninghead noWrap>PVG6.7客户端PIXLiveSDK使用手册 </TD></TR></TBODY></TABLE></DIV></DIV>\
                    \r\n<DIV id=titlerow>\
                    \r\n<H1 class=dtH1>'+matfun.group(2)+'</H1></DIV>\
                    \r\n<DIV id=nstext>\
                    \r\n<P>\
                    \r\n<UL>\
                    \r\n<P>desaa</P></P><PRE class=syntax><B>'
                str_main+=matfun.group(1)+'('
                matparas= self.p1.findall(lin)
                flag= False
                str_ss = '<DL>\r\n'
                for para in matparas:
                    if flag:
                        str_main+=','
                    else: 
                        flag=True
                    str_main+='<BR>    '+para[0]
                    str_ss+='<DT>%s</DT>\r\n<DD>des</DD>\r\n'%(para[1],)
                str_ss+='</DL>'
                str_main+='<BR>    );</B></PRE>\r\n<H4>Parameters</H4>\r\n'+ str_ss +'\r\n<H4>Return Values</H4> \
  \r\n<P>成功返回NPSDK_OK，失败返回错误码。 </P>\
  \r\n<H4>Remarks</H4>\
  \r\n<P>&nbsp;</P>\
  \r\n<H4>See Also</H4>\
  \r\n<P><STRONG><A href=" ">&nbsp;</A></STRONG></P></UL>\
  \r\n<DIV class=footer>\
  \r\n<HR>\
  \r\n</DIV></BODY></HTML>'
                fout_t=open(matfun.group(2)+'.htm','w')
                fout_t.write(str_main)
                fout_t.close()
                #print str
                
        
        self.fin.close()
    
        
if __name__ == '__main__':
    ob= myFile()
    ob.open_hhp('./tt.txt')
    #ob.open_hhp('./t.txt')
    #ob.compile_t('./test.hhp')