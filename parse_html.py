import argparse
import requests

def get_arguments():
    parser = argparse.ArgumentParser(description="path")
    parser.add_argument("--url-file", type=str, default='',
                        help="url file path",
                        required=True)
    parser.add_argument("--output-dir", type=str, default='',
                        help="output file path",
                        required=True)

def get_source(url):
    headers={'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
    response = requests.get(url,headers = headers)
    return (response.content).decode('utf-8')


def main():
    i=0
    args = get_arguments()
    f=open(args.url_file,'r')
    for url in f.readlines():
        i+=1
        html=get_source(url)
        w=open(args.output_dir+'/'+str(i)+'.html','w')
        w.write(html)
        w.close()
    f.close()
    
    
