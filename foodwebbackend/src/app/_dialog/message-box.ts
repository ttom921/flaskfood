import { MatDialog } from '@angular/material/dialog';
import { SimpleDialogComponent } from './simple-dialog/simple-dialog.component';

export class MessageBox {
  static show(
    dialog: MatDialog,
    message,
    title = "Alert",
    information = "",
    button = 0,
    allow_outside_click = false,
    style = 0,
    width = "520px") {
    const dialogRef = dialog.open(SimpleDialogComponent, {
      data: {
        title: title || "Alert",
        message: message,
        information: information,
        button: button || 0,
        style: style || 0,
        allow_outside_click: allow_outside_click || false
      },
      width: width
    });
    return dialogRef.afterClosed();
  }
  /**
   * 讀取的畫面
   * @param dialog
   * @param timenum
   */
  static load(dialog: MatDialog, timenum: number = 3000) {
    const dialogRef = dialog.open(SimpleDialogComponent, {
      data: {
        title: "Info",
        message: "",
        information: "",
        button: 0,
        style: 2,
        allow_outside_click: false
      },
      width: "200px"
    });
    setTimeout(() => {
      dialogRef.close();
    }, timenum);
  }
}
