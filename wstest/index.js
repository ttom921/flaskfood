//使用 WebSocket 的網址向 Server 開啟連結
//let ws = new WebSocket('ws://192.168.83.128:5000/echo')
let ws = new WebSocket('ws://192.168.83.128:5000/v0.0/ws/echo')

//開啟後執行的動作，指定一個 function 會在連結 WebSocket 後執行
ws.onopen = () => {
    console.log('open connection')
}

//關閉後執行的動作，指定一個 function 會在連結中斷後執行
ws.onclose = (event) => {
    console.log(`Closed connect=${event.code}`)
}

//接收 Server 發送的訊息
ws.onmessage = event => {
    console.log(event)
    console.log(event.data)
}

// send message from the form
document.forms.publish.onsubmit = function () {
    let outgoingMessage = this.message.value;

    ws.send(outgoingMessage);
    return false;
};