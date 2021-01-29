from alipay import AliPay
from app import config

def get_pay_url():
    with open("应用私钥2048.txt",'r',encoding='utf-8') as f:
        private_key = f.read()
    with open("应用公钥2048.txt",'r',encoding='utf-8') as f:
        public_key = f.read()
    alipay = AliPay(
                appid=config.get_config_dc()["appid"],
                app_notify_url="",  # 默认回调url
                app_private_key_string=private_key,
                # app_private_key_string="www.fuakorm.com_公钥.txt",
                alipay_public_key_string=public_key,
                # alipay_public_key_string="www.fuakorm.com_私钥.txt",
                sign_type="RSA2",
                debug=False,  # 上线则改为False , 沙箱True
            )

    order_string = alipay.api_alipay_trade_page_pay(
            out_trade_no="95befc40-1312-40ec-8fdc-08d05ac02fee",
            total_amount="88.88",
            subject='支付订单:20150320010101',
            return_url=None,
            notify_url=config.get_config_dc()["pay_call_back"],
        )
    pay_url = 'https://openapi.alipay.com/gateway.do?' + order_string
    print(pay_url)