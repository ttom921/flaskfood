import { Injectable } from '@angular/core';
import { MatDialog } from '@angular/material/dialog';
import { Router } from '@angular/router';
import { MessageBox } from 'src/app/_dialog/message-box';
import { MessageBoxButton, MessageBoxStyle, RespCode } from 'src/app/_dialog/message-enums';

@Injectable({
  providedIn: 'root'
})
export class MessageboxService {

  constructor(
    private dialog: MatDialog,
    private router: Router,
  ) { }
  ResponseErrorMsg(error, message = 'Please login again.') {
    //console.log("ResponseErrorMsg->" + error.status);
    switch (error.status) {
      // case RespCode.ARGS_ERROR:// = 912,//# 上傳參數錯誤
      //   message = "912 Parameter error";
      //   MessageBox.show(this.dialog, message);
      //   break;
      case RespCode.UNDEFINERROR:// = 999 //# 未定義的錯誤
        message = "999 Undefine error";
        MessageBox.show(this.dialog, message);
        break;
      default:
        message = `${error.status} ${error.statusText}`;
        MessageBox.show(this.dialog, message);
        break;
    }
  }
  /**
     * 服務器回傳成功訊息顯示
     */
  SuccessDialog() {
    let message = "success";
    let title = "Info";
    let information = "";
    let button = MessageBoxButton.Ok;
    let allow_outside_click = false;
    let style = MessageBoxStyle.Full;
    let width = "450px";
    MessageBox.show(this.dialog, message, title, information, button, allow_outside_click, style, width);
  }
}
