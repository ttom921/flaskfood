import { WebsocketService } from './../../_service/websocket.service';
import { Injectable } from '@angular/core';
import { Subject } from 'rxjs';
import { map } from 'rxjs/operators';

const CHAT_URL = 'ws://192.168.83.128:5000/v0.0/ws/echo';

export interface Message {
  author: string,
  message: string
}


@Injectable({
  providedIn: 'root'
})
export class ChatService {
  public messages: Subject<Message>;
  constructor(websocketService: WebsocketService) {
    this.messages = <Subject<Message>>websocketService
      .connect(CHAT_URL)
      .pipe(map((response: MessageEvent): Message => {
        let data = JSON.parse(response.data);
        return {
          author: data.author,
          message: data.message
        }
      }));
  }
}
