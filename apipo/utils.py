import requests
import yaml


class RequestUtils:
    session = requests.session ()

    def send_request(self, method, url, **kwargs):      #  **kwargs 是采用键值对的形式取出任意数量的关键字
        return RequestUtils.session.request ( method, url, **kwargs )

    def hanle_yaml(self, caseinfo: dict):  # caseinfo: dict  给一个字典的类型可以调用字典的方法
        keys = caseinfo.keys ()
        # 判断关键词是否在keys中
        if "base_url" in keys and "request" in keys and "assert_data" in keys:
            base_url = caseinfo["base_url"]
            request = caseinfo["request"]
            print ( request )
            request_keys = request.keys ()
            if "url" in request_keys and "method" in request_keys:
                if "pre_url" in request_keys:
                    pre_url = base_url + request["pre_url"]
                    # 要执行pre_url必须通过'GET'方法
                    self.send_request ( "GET", pre_url )
                    del request["pre_url"]
                url = base_url + request["url"]
                del request["url"]
                method = request["method"]
                del request["method"]
                print ( request )
                if request:
                    r = self.send_request ( method, url, **request )
                else:
                    r = self.send_request ( method, url )

                if caseinfo["assert_data"]:

                    '''
                    也可以这样做
                    code=caseinfo["assert_data"]     键值对: 关键字"caseinfo["assert_data"]["status_code"]的值
                    assert code["status_code"] == r.status_code 
                    '''

                    assert caseinfo["assert_data"]["status_code"] == r.status_code

                    # 这时还剩两个关键字
                    keys = caseinfo["assert_data"].keys ()  #dict_keys
                    # key = keys[1]     # TypeError: 'dict_keys' object is not subscriptable

                    # 将keys转化成list格式
                    keys = list ( keys )
                    key = keys[1]  # keys[1]=='msg'  准确的说key是一个字符串

                    # json格式响应[key],即是响应msg的信息
                    msg = r.json ()[key]  #  r.json是将返回的json数据转为字典,即是这个字典中返回关键字['msg']的值
                    ast_msg = caseinfo["assert_data"][key]

                    print ( msg )
                    print ( ast_msg )
                    # key = keys[1]  由于测试数据的时候关键字的值不总是文字也有可能是数字,所以要分开来断言
                    if str ( ast_msg ).isdigit ():   # 如果msg是数字的
                        assert msg == ast_msg      # 是数字这样断言
                    else:
                        assert ast_msg in msg     #不是数字这样断言


            else:
                print ( "取消必要参数" )
        else:
            print ( "缺少必要参数" )


def read_testcase_yaml(yaml_path):
    with open ( yaml_path, "r", encoding="utf8" ) as f:
        yaml_obj = yaml.load ( f, Loader=yaml.FullLoader )
        return yaml_obj


if __name__ == '__main__':
    res = read_testcase_yaml ( "data/login.yml" )
    print ( res[0] )
    RequestUtils ().hanle_yaml ( res[2] )  #   "RequestUtils ()" ,必须是实例变量才能调用
