#!usr/bin/python
# -*- coding: utf-8 -*

import requests
import yaml
import os


class QueryByContion(object):




    def load_file_yaml(self,ymlpath):


        with open(ymlpath, 'r', encoding='utf-8') as stream:
            dict_content = yaml.load(stream, Loader=yaml.FullLoader)
            return dict_content

    def read_file_yaml(self,ymlpath):
        dict_condent = self.load_file_yaml(ymlpath)
        #print(dict_condent)
        self.url = dict_condent['QueryByCondition_interface']['base_url']
        self.headers = dict_condent['QueryByCondition_interface']['Request Headers']
        return self.url,self.headers


    def request_queryinfo(self,ymlpath):

        self.url,self.headers = self.read_file_yaml(ymlpath)
        r = requests.get(self.url, self.headers)
        return r





