import { Component, ElementRef, OnInit, ViewChild } from '@angular/core';
import { ChatService } from './_service/chat.service';

@Component({
  selector: 'muc-nick',
  templateUrl: './muc-nick.component.html',
  styleUrls: ['./muc-nick.component.scss']
})
export class MucNickComponent implements OnInit {

  @ViewChild('nickname', { static: true }) nickname: ElementRef;
  @ViewChild('msg', { static: true }) msg: ElementRef;
  messagelist = [];
  constructor(private chatService: ChatService) {

  }

  ngOnInit(): void {
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
    sendmsg.author = this.nickname.nativeElement.value;
    sendmsg.message = this.msg.nativeElement.value;
    this.chatService.messages.next(sendmsg);

  }

}
