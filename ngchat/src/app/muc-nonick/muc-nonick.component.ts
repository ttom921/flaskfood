import { ChatService } from './_service/chat.service';
import { Component, ElementRef, OnInit, ViewChild } from '@angular/core';

@Component({
  selector: 'muc-nonick',
  templateUrl: './muc-nonick.component.html',
  styleUrls: ['./muc-nonick.component.scss']
})
export class MUCNonickComponent implements OnInit {
  @ViewChild('msg', { static: true }) msg: ElementRef;
  messagelist = [];
  constructor(private chatService: ChatService) {

  }

  ngOnInit(): void {
    //console.log(this.msg);
    this.chatService.messages.subscribe(msg => {
      //console.log("Response from websocket: " + msg);
      this.messagelist.push(msg);
    });

  }
  send() {
    let sendmsg = {
      author: 'tutorialedge',
      message: 'this is a test message'
    }
    //console.log(this.msg.nativeElement.value);
    sendmsg.message = this.msg.nativeElement.value;
    this.chatService.messages.next(sendmsg);

  }
}
