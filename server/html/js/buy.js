
function checkBtn(){

    var usePhone = document.getElementById("cbb_usePhone").checked;
    var name = document.getElementById("user_name").value;
    if (usePhone){
        alert(name);
    }
}

function on_use_phone_click(){
    var usePhone = document.getElementById("cbb_usePhone").checked;
    if (usePhone){
        document.getElementById("user_name").placeholder = "请输入手机号";
    }else{
        document.getElementById("user_name").placeholder = "请输入账号名";
    }
}