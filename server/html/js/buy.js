
function checkBtn(){
    var host = window.location.host;
    var usePhone = document.getElementById("cbb_usePhone").checked;
    var user_name = document.getElementById("user_name").value;
    var buyer_num = document.getElementById("buy_num").value;
    var cbb_recharge = document.getElementById("cbb_recharge").checked;
    var user_phone = "";
    if (usePhone){
        user_phone = user_name;
        user_name = "";
    }
    var xmlhttp = new XMLHttpRequest();
    var data={
        "user_name":user_name,
        "user_phone":user_phone,
        "buyer_num":buyer_num,
        "recharge":cbb_recharge
    }
    var stringData=JSON.stringify(data);
    xmlhttp.onreadystatechange=function(){
        if (xmlhttp.readyState==4 && xmlhttp.status==200){
            document.getElementById("log").innerHTML=xmlhttp.responseText;
        }
    }
    xmlhttp.open("POST","/api/order/create",true);
    xmlhttp.setRequestHeader("Content-type","application/json;charset=UTF-8");//可以发送json格式字符串
    xmlhttp.send(stringData);
}

function on_use_phone_click(){
    var usePhone = document.getElementById("cbb_usePhone").checked;
    if (usePhone){
        document.getElementById("user_name").placeholder = "请输入手机号";
    }else{
        document.getElementById("user_name").placeholder = "请输入账号名";
    }
}