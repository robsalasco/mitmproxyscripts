import os,re

def request(context, flow):
  if(re.search(".*--.*\\.googlevideo\\.com", flow.request.get_host())):
        url="%s%s" % (flow.request.get_host(), flow.request.path)
        os.system("echo \"https://%s\"|pbcopy" % url)
